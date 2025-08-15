# noise web

## deploy

```
aws s3api create-bucket --bucket kukai-noise-web-terraform-state-bucket --create-bucket-configuration LocationConstraint=ap-northeast-1
```

```
terraform init
```

```
terraform apply
```
