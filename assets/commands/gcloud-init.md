# TAGLINE

初始化 Google Cloud SDK 配置

# TLDR

**初始化 gcloud**

```gcloud init```

**不启动浏览器进行初始化**

```gcloud init --console-only```

**使用新配置重新初始化**

```gcloud init --skip-diagnostics```

# SYNOPSIS

**gcloud** **init** [_options_]

# PARAMETERS

**--console-only**
> 登录时不启动浏览器。

**--skip-diagnostics**
> 跳过网络诊断。

**--configuration** _name_
> 使用指定的配置。

# DESCRIPTION

**gcloud init** 是一个交互式向导，引导你完成 Google Cloud SDK 的初始设置。它通过启动浏览器进行 OAuth 登录来完成身份验证，然后帮助你从账户可用的项目中选择一个默认项目。

初始化过程还会提示设置默认的 Compute Engine 区域（region）和可用区（zone），从而免去在后续命令中反复指定这些值的麻烦，让命令执行更顺畅。该命令会创建或更新一个包含这些偏好设置的配置档案。

gcloud init 可以多次运行，以创建不同的命名配置，便于处理多个项目或账户。它是安装 Google Cloud SDK 后推荐的第一步，也是在不同的 GCP 环境之间切换的最简单方式。

# SEE ALSO

[gcloud](/man/gcloud)(1)
