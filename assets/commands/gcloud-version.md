# TAGLINE

显示 SDK 版本信息

# TLDR

**显示 gcloud 版本**

```gcloud version```

**以 JSON 格式显示版本**

```gcloud version --format=json```

**简短版本输出（顶层标志）**

```gcloud --version```

**以 YAML 格式显示版本**

```gcloud version --format=yaml```

# SYNOPSIS

**gcloud version** [_options_]

# PARAMETERS

**--format** _FORMAT_
> 输出格式：text、json、yaml。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud version** 显示 Google Cloud SDK 及已安装组件的版本。它会列出 gcloud、bq、gsutil 以及其他 SDK 工具的版本号。

该命令有助于确认安装的 SDK 版本，并判断是否有可用更新。组件版本信息有助于故障排查和兼容性检查。

gcloud version 可用于记录环境细节并确保环境一致性。

# CAVEATS

版本可能不是最新可用版本。各组件版本独立更新。

# HISTORY

gcloud version 是 **Google Cloud SDK** 诊断命令的一部分，提供所有已安装组件的版本信息。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-components](/man/gcloud-components)(1)
