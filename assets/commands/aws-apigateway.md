# TAGLINE

为应用创建和管理 REST API

# TLDR

**列出所有 REST API**

```aws apigateway get-rest-apis```

**创建新的 REST API**

```aws apigateway create-rest-api --name "[MyAPI]" --description "[API description]"```

**创建区域性 API** 端点

```aws apigateway create-rest-api --name "[MyAPI]" --endpoint-configuration types=REGIONAL```

按 ID **获取 API 详情**

```aws apigateway get-rest-api --rest-api-id [api-id]```

在 API 中**创建资源**（路径）

```aws apigateway create-resource --rest-api-id [api-id] --parent-id [parent-id] --path-part "[users]"```

为资源**添加 HTTP 方法**

```aws apigateway put-method --rest-api-id [api-id] --resource-id [resource-id] --http-method [GET] --authorization-type NONE```

将 API **部署到阶段**

```aws apigateway create-deployment --rest-api-id [api-id] --stage-name [prod]```

从 OpenAPI 定义**导入 API**

```aws apigateway import-rest-api --body fileb://[api.json]```

**删除 REST API**

```aws apigateway delete-rest-api --rest-api-id [api-id]```

# SYNOPSIS

**aws apigateway** _command_ [_options_]

# PARAMETERS

**create-rest-api**
> 创建新的 REST API

**get-rest-apis**
> 列出账户中的所有 REST API

**get-rest-api**
> 获取特定 REST API 的详情

**delete-rest-api**
> 删除一个 REST API

**create-resource**
> 在 API 中创建资源（URL 路径段）

**get-resources**
> 列出 API 中的资源

**put-method**
> 为资源添加 HTTP 方法

**put-integration**
> 为方法配置后端集成

**create-deployment**
> 将 API 部署到阶段

**create-stage**
> 从一次部署创建部署阶段

**import-rest-api**
> 根据 OpenAPI/Swagger 定义创建 API

**put-rest-api**
> 根据 OpenAPI/Swagger 定义更新现有 API

**get-stages**
> 列出部署阶段

**get-api-keys**
> 列出 API 密钥

**create-api-key**
> 创建新的 API 密钥

**--rest-api-id** _id_
> REST API 的标识符

**--name** _name_
> API 或资源的名称

**--description** _text_
> API 的描述

**--endpoint-configuration** _config_
> 端点类型：EDGE、REGIONAL 或 PRIVATE

**--stage-name** _name_
> 部署阶段名称（dev、staging、prod）

# DESCRIPTION

**aws apigateway** 通过 AWS CLI 管理 Amazon API Gateway 的 REST API。它创建和配置的 API 是应用访问后端服务、Lambda 函数或其他 AWS 服务的前门。

典型工作流包括：用 **create-rest-api** 创建 API，用 **create-resource** 定义资源（URL 路径），用 **put-method** 添加 HTTP 方法，用 **put-integration** 配置后端集成，最后用 **create-deployment** 部署到阶段。

端点类型决定 API 的访问方式：**EDGE** 用于 CloudFront 分发（全球）、**REGIONAL** 用于同区域访问、**PRIVATE** 用于仅限 VPC 内访问。

API 密钥和使用计划提供访问控制与限流。阶段代表不同的环境（dev、staging、prod），各自拥有独立的配置。

# CAVEATS

需要通过 **aws configure** 或环境变量配置好 AWS 凭证。REST API 的变更需要重新部署才能生效。API Gateway 对资源数量、方法数量和请求速率设有配额。私有 API 需要 VPC 端点配置。

# HISTORY

**Amazon API Gateway** 于 **2015 年 7 月**推出，是一项用于创建、发布和管理 API 的完全托管服务。AWS CLI 命令提供了对 API Gateway 功能的程序化访问。REST API 是最初的产品形态，之后加入了 HTTP API（更简单、成本更低）和 WebSocket API。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-lambda](/man/aws-lambda)(1), [aws-iam](/man/aws-iam)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/apigateway/)```

<!-- verified: 2026-06-17 -->
