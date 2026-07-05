provider "aws" {
  region = "ap-northeast-1"
}

# CloudFrontで使うACM証明書はリージョンに関わらずus-east-1で発行する必要がある
provider "aws" {
  alias  = "us_east_1"
  region = "us-east-1"
}

resource "aws_s3_bucket" "noise_web" {
  bucket = "kukai-noise-web-bucket"
}

# CloudFront（OAI）経由のみで読ませるため、バケット自体は非公開にする
resource "aws_s3_bucket_public_access_block" "noise_web_public_access_block" {
  bucket                  = aws_s3_bucket.noise_web.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_policy" "noise_web_policy" {
  bucket = aws_s3_bucket.noise_web.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          AWS = aws_cloudfront_origin_access_identity.oai.iam_arn
        },
        Action   = "s3:GetObject",
        Resource = "${aws_s3_bucket.noise_web.arn}/*"
      }
    ]
  })

  depends_on = [
    aws_s3_bucket_public_access_block.noise_web_public_access_block,
  ]
}

locals {
  assets = fileset("assets/", "*")

  content_types = {
    "html" = "text/html"
    "css"  = "text/css"
    "js"   = "application/javascript"
    "png"  = "image/png"
    "jpg"  = "image/jpeg"
    // 他のファイルタイプに対するContent-Typeもここに追加できます
  }
}

resource "aws_s3_object" "asset_files" {
  for_each = { for asset in local.assets : asset => asset }

  bucket       = aws_s3_bucket.noise_web.bucket
  key          = each.value
  source       = "assets/${each.value}"
  content_type = lookup(local.content_types, try(element(regex("\\.([^\\.]+)$", each.value), 0), "default"), "binary/octet-stream")
  etag         = filemd5("assets/${each.value}")
}


// DNS TLS
resource "aws_acm_certificate" "cert" {
  provider          = aws.us_east_1
  domain_name       = "noise.kukai.dev"
  validation_method = "DNS"

  lifecycle {
    create_before_destroy = true
  }
}

# DNS検証はCloudflare側（infra/cloudflare/dns.tf）で手動追加するため、
# 検証用CNAMEの名前・値はoutputで確認して反映する。
resource "aws_acm_certificate_validation" "cert" {
  provider        = aws.us_east_1
  certificate_arn = aws_acm_certificate.cert.arn
}

resource "aws_cloudfront_origin_access_identity" "oai" {
  comment = "OAI for S3 bucket"
}

resource "aws_cloudfront_distribution" "s3_distribution" {
  origin {
    domain_name = aws_s3_bucket.noise_web.bucket_regional_domain_name
    origin_id   = "S3Origin"

    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.oai.cloudfront_access_identity_path
    }
  }

  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"
  aliases             = ["noise.kukai.dev"]

  viewer_certificate {
    acm_certificate_arn      = aws_acm_certificate_validation.cert.certificate_arn
    ssl_support_method       = "sni-only"
    minimum_protocol_version = "TLSv1.2_2018"
  }

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3Origin"

    forwarded_values {
      query_string = false

      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 3600
    max_ttl                = 86400
  }

  # S3のwebsite hosting機能を使わなくなった代わりに、エラー時はerror.htmlを返す
  custom_error_response {
    error_code         = 403
    response_code      = 404
    response_page_path = "/error.html"
  }

  custom_error_response {
    error_code         = 404
    response_code      = 404
    response_page_path = "/error.html"
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }
}

output "cloudfront_domain_name" {
  description = "CloudflareのDNSレコード（noise）に設定するCNAME転送先"
  value       = aws_cloudfront_distribution.s3_distribution.domain_name
}

output "acm_validation_records" {
  description = "Cloudflareに追加するACM検証用CNAME（name/value）"
  value = [
    for o in aws_acm_certificate.cert.domain_validation_options : {
      name  = o.resource_record_name
      value = o.resource_record_value
      type  = o.resource_record_type
    }
  ]
}
