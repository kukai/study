# study_ecs
ecs pipeline cfn

## CFn + docker compose

ECS上のシンプルなアプリ(on ECS) を CFn と docker compose で展開できるようにする

- cfn-vpc.yml まずVPCを作る
- cfn-fargate.yml ECS Cluster + ECR
- ??? CodePipeline ???

### VPC

```shell
export AWS_PROFILE=xxxx
aws cloudformation create-stack --template-body file://cfn-vpc.yml --stack-name kukai-vpc
unset AWS_PROFILE
```

### ECS fargate cluster

```shell
export AWS_PROFILE=xxxx
aws cloudformation create-stack --template-body file://cfn-fargate.yml --stack-name kukai-fargate
unset AWS_PROFILE
```

## TODO 手動でECS task service

## TODO CodePipeline + ECR を CFn で構築する

