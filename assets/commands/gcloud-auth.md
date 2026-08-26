# TAGLINE

Google Cloud 身份验证管理

# TLDR

**交互式登录**

```gcloud auth login```

**激活服务账号**

```gcloud auth activate-service-account --key-file=[key.json]```

**列出账号**

```gcloud auth list```

**打印访问令牌**

```gcloud auth print-access-token```

**撤销凭据**

```gcloud auth revoke [account]```

# SYNOPSIS

**gcloud auth** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：login、list、revoke 等。

**login**
> 使用用户账号进行身份验证。

**activate-service-account**
> 使用服务账号进行身份验证。

**list**
> 列出已认证的账号。

**print-access-token**
> 输出当前的访问令牌。

**revoke** _ACCOUNT_
> 撤销凭据。

**--key-file** _FILE_
> 服务账号密钥文件。

**application-default**
> 管理用于本地开发和客户端库的默认应用凭据（ADC）。

**configure-docker**
> 将 gcloud 注册为 Docker 凭据助手，用于推送/拉取 Artifact Registry 和 Container Registry 镜像。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud auth** 管理 Google Cloud Platform 访问的身份验证与授权。所有 gcloud 操作都需要有效凭据，这些凭据由该命令组提供和维护。

交互式场景下，login 命令会发起基于浏览器的 OAuth 流程，用你的 Google 账号完成认证。自动化和服务器环境则可使用 JSON 密钥文件激活服务账号，提供适合 CI/CD 流水线的非交互式身份验证。

该命令支持多个并发认证账号，让你可以在不同 Google 账号之间、或在用户账号与服务账号之间切换。同一时刻只有一个账号处于活动状态，但切换很快且保留所有凭据。访问令牌可以打印出来，供需要向 Google Cloud API 认证的外部工具使用。

# CAVEATS

用户登录需要浏览器。服务账号密钥是敏感信息。令牌过期后需要重新认证。

# HISTORY

gcloud auth 属于 **Google Cloud SDK**，为所有 gcloud 命令及 GCP API 访问提供统一的身份验证管理。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-config](/man/gcloud-config)(1)
