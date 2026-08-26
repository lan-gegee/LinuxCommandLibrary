# TAGLINE

管理 authentik 身份提供商

# TLDR

**启动服务器**

```ak server```

**执行数据库迁移**

```ak migrate```

**创建超级用户**

```ak createsuperuser```

**导出配置**

```ak export_blueprint```

**导入蓝图**

```ak import_blueprint [blueprint.yaml]```

**生成有效期为若干分钟的恢复链接**

```ak create_recovery_key [minutes] [username]```

**显示版本**

```ak version```

**运行 worker 进程**

```ak worker```

# SYNOPSIS

**ak** _command_ [_options_]

# COMMANDS

**server**
> 启动 authentik Web 服务器。

**worker**
> 启动后台 worker 进程。

**migrate**
> 应用数据库迁移。

**createsuperuser**
> 交互式创建管理员用户。

**create_recovery_key** _minutes_ _user_
> 生成一个在给定分钟数内有效的账户恢复链接。

**dump_config**
> 以 YAML 格式打印完整生效配置。

**export_blueprint**
> 将当前配置导出为 blueprint YAML。

**import_blueprint** _file_
> 从 blueprint 文件导入配置。

**version**
> 显示版本信息。

**repair**
> 运行诊断和修复例程。

**shell**
> 打开带 authentik 上下文的交互式 Python shell。

**dbshell**
> 打开数据库 shell。

# PARAMETERS

**--bind** _address_
> 服务器的监听地址。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ak** 是 authentik 的命令行界面。authentik 是一个开源身份提供商。ak 负责管理 authentik 服务器、worker、数据库操作以及配置的导入导出。

**server** 命令启动 Web 界面和 API 服务器。邮件发送和 LDAP 同步等后台任务需要单独运行 **worker** 进程。

蓝图（blueprint）提供声明式的配置管理。使用 **export_blueprint** 导出配置以便版本控制或迁移，再用 **import_blueprint** 应用它们。

当用户被锁定时，可用 **create_recovery_key** 生成有时效限制的恢复 URL 来找回账户。第一个参数是有效期（分钟），第二个参数是用户名。这需要在服务器命令行上操作。

authentik 支持多种认证协议，包括 SAML、OAuth2/OIDC、LDAP、SCIM，以及为原生不支持 SSO 的应用提供的代理认证。

# CONFIGURATION

**/etc/authentik/config.yml**
> authentik 主配置文件，包含数据库、密钥、邮件和日志设置。

**blueprints/**
> 存放声明式 YAML 蓝图的目录，实现配置即代码。

# CAVEATS

需要已安装 authentik 的 Python 环境。数据库必须完成配置且可访问。大多数管理任务通过 Web 界面完成；CLI 主要用于服务器操作和紧急恢复。

# HISTORY

authentik 由 **Jens Langhammer** 创建，于 **2020** 年首次发布，是较老身份提供商的现代替代品。它基于 Django 构建，为容器化部署设计，提供全面的身份管理功能。该项目作为商业身份提供商的自托管替代品而广受欢迎，提供应用代理、多因素认证和广泛的协议支持。

# SEE ALSO

[authelia](/man/authelia)(1), [keycloak](/man/keycloak)(1), [vault](/man/vault)(1)

# RESOURCES

```[Source code](https://github.com/goauthentik/authentik)```

```[Homepage](https://goauthentik.io/)```

```[Documentation](https://docs.goauthentik.io/)```

<!-- verified: 2026-06-11 -->
