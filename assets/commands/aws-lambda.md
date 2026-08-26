# TAGLINE

管理无服务器函数和事件驱动计算。

# TLDR

**从 ZIP 文件创建函数**

```aws lambda create-function --function-name [my-function] --runtime python3.11 --role [arn:aws:iam::account:role/lambda-role] --handler [index.handler] --zip-file fileb://[function.zip]```

**调用函数并获取响应**

```aws lambda invoke --function-name [my-function] --cli-binary-format raw-in-base64-out --payload '{"key": "value"}' response.json```

**列出账户中的所有函数**

```aws lambda list-functions```

**获取函数详情和配置**

```aws lambda get-function --function-name [my-function]```

**从 ZIP 文件更新函数代码**

```aws lambda update-function-code --function-name [my-function] --zip-file fileb://[function.zip]```

**更新函数配置**（内存、超时）

```aws lambda update-function-configuration --function-name [my-function] --memory-size 512 --timeout 30```

**创建来自 SQS 的事件源映射**

```aws lambda create-event-source-mapping --function-name [my-function] --event-source-arn [arn:aws:sqs:region:account:queue-name]```

**发布新版本**

```aws lambda publish-version --function-name [my-function]```

# SYNOPSIS

**aws lambda** _command_ [_options_]

# DESCRIPTION

**aws lambda** 是 AWS Lambda 的 AWS CLI 接口。Lambda 是一项无服务器计算服务，无需预置或管理服务器即可运行代码来响应事件；它会自动扩缩并处理高可用性。

Lambda 支持多种运行时，包括 Python、Node.js、Java、Go、Ruby、.NET 以及自定义运行时。函数可由 AWS 服务触发、通过 API Gateway 接收 HTTP 请求触发，或被直接调用。

# COMMANDS

**create-function**
> 创建新的 Lambda 函数

**delete-function**
> 删除函数

**invoke**
> 同步执行函数

**list-functions**
> 列出所有函数

**get-function**
> 获取函数配置和代码位置

**update-function-code**
> 部署新的函数代码

**update-function-configuration**
> 更改函数设置

**publish-version**
> 创建不可变的版本快照

**create-alias**
> 创建指向某个函数版本的别名

**create-event-source-mapping**
> 将函数连接到事件源

**publish-layer-version**
> 创建可复用的代码层

**add-permission**
> 向其他服务授予调用权限

# CAVEATS

函数的最大超时时间为 15 分钟。部署包大小限制为压缩后 50 MB（解压后 250 MB）。冷启动会增加首次调用的延迟。并发执行数量受账户和区域级上限约束。连接 VPC 的函数冷启动时间可能更长。

# HISTORY

AWS Lambda 于 **2014 年 11 月** 推出，是首个主流无服务器计算服务，最初仅支持 Node.js。Python 支持于 **2015 年** 加入，自定义运行时于 **2018 年** 加入。面向 CloudFront 的 Lambda@Edge、容器镜像支持和 Lambda URL 显著拓展了其使用场景。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-apigateway](/man/aws-apigateway)(1), [aws-events](/man/aws-events)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/lambda/index.html)```

<!-- verified: 2026-06-18 -->
