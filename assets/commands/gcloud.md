# TAGLINE

Google Cloud Platform 命令行界面

# TLDR

**初始化 gcloud** 并完成配置

```gcloud init```

**登录 Google** Cloud

```gcloud auth login```

**设置当前项目**

```gcloud config set project [project-id]```

**列出所有项目**

```gcloud projects list```

**创建 Compute Engine VM** 实例

```gcloud compute instances create [name] --zone=[zone]```

**列出运行中的 VM** 实例

```gcloud compute instances list```

**获取用于本地开发的 application-default** 凭据

```gcloud auth application-default login```

**将输出格式化为 JSON** 以便脚本处理

```gcloud compute instances list --format=json```

# SYNOPSIS

**gcloud** _group_ [_command_] [_options_]

# PARAMETERS

_GROUP_
> 服务组：compute、container、iam、sql、storage、functions、run 等。

**auth**
> 身份验证与凭据相关命令。

**config**
> 配置管理。

**compute**
> Compute Engine 命令。

**container**
> Kubernetes Engine 命令。

**projects**
> 项目管理。

**--project** _ID_
> 为本次命令覆盖默认项目。

**--format** _FORMAT_
> 输出格式：json、yaml、csv、table、text、value 等。

**--filter** _EXPRESSION_
> 过滤结果（例如 'name~prod'）。

**--quiet**, **-q**
> 禁用交互式提示并使用默认值。

**--verbosity** _LEVEL_
> 日志详细程度：debug、info、warning、error、critical、none。

**--account** _ACCOUNT_
> 为本次命令覆盖默认账户。

**--region** _REGION_
> 为本次命令覆盖默认区域（region）。

**--zone** _ZONE_
> 为本次命令覆盖默认可用区（zone）。

**--configuration** _NAME_
> 使用指定的命名配置而非当前活动配置。

**--flags-file** _FILE_
> 从 YAML 或 JSON 文件读取标志。

**--flatten** _KEY_
> 展平嵌套的列表或映射输出。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.config/gcloud/configurations/config_default**
> 默认配置属性，包括项目、区域、可用区和账户设置。

**~/.config/gcloud/credentials.db**
> 已认证账户的加密凭据数据库。

**~/.config/gcloud/application_default_credentials.json**
> 用于本地开发的 application default 凭据。

# DESCRIPTION

**gcloud** 是用于管理云资源的 Google Cloud Platform CLI。它为所有 GCP 服务提供命令，包括 Compute Engine、Kubernetes Engine、Cloud SQL、Cloud Run、Cloud Functions 等。

该工具负责身份验证、配置和资源管理。命令按服务组组织，每个操作对应相应的子命令。所有命令都支持 **--format** 和 **--filter** 标志，便于脚本化和自动化。输出格式包括 json、yaml、csv、table、text、value 等多种。

可以通过 **gcloud config configurations** 管理多个命名配置，以便在不同项目和账户之间切换。

# CAVEATS

需要 GCP 账户和项目。某些操作可能产生费用。部分命令需要特定的 IAM 权限。**gcloud** CLI 是 Google Cloud SDK 的一部分，而后者在大多数软件包管理器中需要单独安装。

# HISTORY

**gcloud** 是 **Google Cloud SDK** 的组成部分，于 **2013 年**首次发布，作为 Google Cloud Platform 管理与自动化的主要 CLI。它现已覆盖数百个 GCP 服务，并持续更新新功能。

# SEE ALSO

[gsutil](/man/gsutil)(1), [kubectl](/man/kubectl)(1), [bq](/man/bq)(1), [aws](/man/aws)(1), [az](/man/az)(1), [terraform](/man/terraform)(1)
