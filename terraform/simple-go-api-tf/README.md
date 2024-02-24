# simple-go-api-tf

TerraformでAWS LambdaにデプロイするGo製のAPIサーバー

## TODO (Push時に消すパート)

- [ ] tf.stateのS3バケットでの管理、複数の場所でterraform appplyしたい

## 使うツール

1. go
2. terraform

## デプロイ方法

```
terraform plan
```

```
terraform apply
```

```
curl https://xxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/test/example_pahty
```

## Lambdaをローカルデバッグする

VSCode(AWS Toolkit)とSAMを使ったリモートデバッグ方法を検討したがVSCodeから上手くデバッガに接続できないためローカルデバッグは諦める
