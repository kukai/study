provider "aws" {
  region = "ap-northeast-1"
}

resource "aws_s3_bucket" "noise_web" {
  bucket = "kukai-noise-web-bucket"
}

resource "aws_s3_bucket_public_access_block" "noise_web_public_access_block" {
  bucket                  = aws_s3_bucket.noise_web.id
  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_bucket_policy" "noise_web_policy" {
  bucket = aws_s3_bucket.noise_web.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Principal = "*",
        Action   = "s3:GetObject",
        Resource = "${aws_s3_bucket.noise_web.arn}/*"
      }
    ]
  })

  depends_on = [
    aws_s3_bucket_public_access_block.noise_web_public_access_block,
  ]
}

resource "aws_s3_bucket_website_configuration" "noise_web_config" {
  bucket = aws_s3_bucket.noise_web.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
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

  bucket = aws_s3_bucket.noise_web.bucket
  key    = each.value
  source = "assets/${each.value}"
  content_type = lookup(local.content_types, try(element(regex("\\.([^\\.]+)$", each.value), 0), "default"), "binary/octet-stream")
  etag = filemd5("assets/${each.value}")
}


// DNS TLS
resource "aws_acm_certificate" "cert" {
  domain_name       = "noise.kukai.dev"
  validation_method = "DNS"
}

resource "aws_cloudfront_distribution" "s3_distribution" {
  origin {
    domain_name = aws_s3_bucket.your_bucket.bucket_regional_domain_name
    origin_id   = "S3Origin"

    s3_origin_config {
      origin_access_identity = aws_cloudfront_origin_access_identity.oai.cloudfront_access_identity_path
    }
  }

  enabled             = true
  is_ipv6_enabled     = true
  default_root_object = "index.html"

  viewer_certificate {
    acm_certificate_arn      = aws_acm_certificate.cert.arn
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
}

resource "aws_cloudfront_origin_access_identity" "oai" {
  comment = "OAI for S3 bucket"
}
