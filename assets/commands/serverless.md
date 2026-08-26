# TAGLINE

将无服务器函数部署到云服务商

# TLDR

**创建新服务**

```serverless create --template [aws-nodejs] --name [my-service]```

**部署服务**

```serverless deploy```

**部署单个函数**

```serverless deploy function -f [functionName]```

**调用函数**

```serverless invoke -f [functionName]```

**查看日志**

```serverless logs -f [functionName]```

**移除服务**

```serverless remove```

**本地运行**

```serverless invoke local -f [functionName]```

**打印配置**

```serverless print```

# SYNOPSIS

**serverless** [_create_] [_deploy_] [_invoke_] [_logs_] [_remove_] [_options_]

# PARAMETERS

**create**
> 创建新服务。

**deploy**
> 部署服务。

**deploy function**
> 部署单个函数。

**invoke** **-f** _FUNC_
> 调用函数。

**invoke local**
> 本地调用。

**logs** **-f** _FUNC_
> 查看函数日志。

**remove**
> 移除服务。

**package**
> 仅打包而不部署。

**print**
> 打印配置。

**--template**, **-t** _TPL_
> 项目模板。

**--name**, **-n** _NAME_
> 服务名称。

**--stage**, **-s** _STAGE_
> 部署阶段。

**--region**, **-r** _REGION_
> AWS 区域。

**--config**, **-c** _FILE_
> 配置文件。

# DESCRIPTION

**serverless**（sls）是一个构建无服务器应用的框架。它可将函数部署到 AWS Lambda、Azure Functions、Google Cloud Functions 等平台。

serverless.yml 中的服务配置定义函数、事件和资源。事件通过 HTTP、队列、定时计划等来源触发函数。

部署过程会打包代码并预置基础设施。CloudFormation（AWS）或等价服务负责资源创建。

本地调用无需部署即可测试函数，加快开发迭代速度。

日志从云服务商流式传输函数输出，展示调用情况、错误和执行细节。

插件可扩展功能：自定义域名、监控、优化以及框架集成。

# CONFIGURATION

**serverless.yml**
> 主服务配置文件，定义函数、事件、资源、插件和服务商设置。

**~/.serverlessrc**
> 用户级配置，用于跟踪与遥测偏好。

**AWS_ACCESS_KEY_ID** / **AWS_SECRET_ACCESS_KEY**
> 用于部署的 AWS 凭证（或通过 AWS CLI 配置文件配置）。

# CAVEATS

需要云服务商凭证。部署会创建大量资源。冷启动会影响延迟。需考虑服务商锁定问题。

# HISTORY

**Serverless Framework** 由 **Austen Collins** 于 **2015** 年创建，最初名为 JAWS。它开创了无服务器部署工具的先河，并成为最流行的 Lambda 开发框架。

# INSTALL

```brew: brew install serverless```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [sam](/man/sam)(1), [terraform](/man/terraform)(1), [pulumi](/man/pulumi)(1)
