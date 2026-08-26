# TAGLINE

管理 Chainguard 容器镜像和资源

# TLDR

**向 Chainguard 认证**

```chainctl auth login```

**列出可用的容器镜像**

```chainctl images list```

**列出镜像标签**

```chainctl images tags list [image_name]```

**获取镜像详情**

```chainctl images describe [image_name]```

**列出组织**

```chainctl iam organizations list```

**配置 chainctl 设置**

```chainctl config set [key] [value]```

# SYNOPSIS

**chainctl** [**--api** _url_] [**--config** _file_] [**-o** _format_] [**--log-level** _level_] _command_ [_subcommand_] [_arguments..._]

# DESCRIPTION

**chainctl**（Chainguard Control）是管理 Chainguard 资源的命令行界面，包括安全加固的容器镜像、身份管理和平台配置。

该 CLI 采用 **context noun verb**（上下文 名词 动词）的交互风格，让用户可以发现可用镜像、分析安全元数据、管理组织以及控制对 Chainguard 资源的访问。

# PARAMETERS

**--api** _url_
> Chainguard 平台 API URL（默认：https://console-api.enforce.dev）

**--config** _file_
> chainctl 配置文件路径（或设置 CHAINCTL_CONFIG）

**-o, --output** _format_
> 输出格式：csv、json、table、tree、wide、markdown、yaml 或 go-template

**--log-level** _level_
> 日志级别：debug、info（默认：ERROR）

**--force-color**
> 强制彩色输出

**Main commands:**

**auth** - 认证相关命令（login、logout、token）
**images** - 管理容器镜像（list、describe、tags）
**iam** - 身份与访问管理
**packages** - 与 Chainguard 软件包交互
**config** - 管理 chainctl 配置

# CONFIGURATION

**CHAINCTL_CONFIG**
> 指定备用配置文件位置的环境变量。

# CAVEATS

需要 Chainguard 账户进行认证。某些命令需要你所在组织内的相应 IAM 权限。

# HISTORY

**chainctl** 由 **Chainguard** 开发，是其安全软件供应链平台的一部分。Chainguard 专注于提供攻击面更小、可持续安全更新的最小化加固容器镜像。

# SEE ALSO

[docker](/man/docker)(1), [cosign](/man/cosign)(1)

# RESOURCES

```[Documentation](https://edu.chainguard.dev/chainguard/chainctl/)```

<!-- verified: 2026-06-22 -->
