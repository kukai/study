terraform {
  backend "s3" {
    bucket = "kukai-noise-web-terraform-state-bucket"
    key    = "terraform.tfstate"
    region = "ap-northeast-1"
  }
}
