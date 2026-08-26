# TAGLINE

AWS Serverless Application Model CLI

# TLDR

**初始化**无服务器应用

```sam init```

以指定的**运行时**初始化

```sam init --runtime [python3.12]```

**构建** Lambda 函数代码

```sam build```

在**本地**运行无服务器应用

```sam local start-api```

在本地**调用** Lambda 函数

```sam local invoke [FunctionName]```

通过引导式提示**部署**

```sam deploy --guided```

**校验** SAM 模板

```sam validate```

# SYNOPSIS

**sam** _command_ [_options_]

# PARAMETERS

**init**
> 初始化新的无服务器应用

**build**
> 构建 Lambda 函数代码

**deploy**
> 将应用部署到 AWS

**delete**
> 删除已部署的应用及其资源

**validate**
> 校验 SAM 模板

**sync**
> 将本地更改同步到已部署的应用

**logs**
> 获取并显示 Lambda 函数日志

**local invoke**
> 在本地调用 Lambda 函数

**local start-api**
> 在本地运行 API Gateway

**local start-lambda**
> 启动本地 Lambda 端点

**local generate-event**
> 生成用于测试的示例事件负载

# DESCRIPTION

**sam** 是 AWS Serverless Application Model 的 CLI。它提供使用 AWS Lambda、API Gateway 及其他 AWS 服务构建、测试和部署无服务器应用的工具。

该 CLI 支持在云端部署之前进行本地开发和测试。

# CAVEATS

需要配置 AWS 凭据。本地测试需要 Docker。部署会创建可能产生费用的 AWS 资源。

# HISTORY

由 **AWS** 开发，旨在通过基础设施即代码简化无服务器应用的开发与部署。

# INSTALL

```aur: yay -S sam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [docker](/man/docker)(1)
