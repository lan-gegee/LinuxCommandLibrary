# TAGLINE

显示 gcloud 安装与配置详情

# TLDR

**显示 SDK 信息**

```gcloud info```

**显示安装路径**

```gcloud info --format='value(installation.sdk_root)'```

**显示账号信息**

```gcloud info --format='value(config.account)'```

**以 YAML 输出**

```gcloud info --format=yaml```

# SYNOPSIS

**gcloud info** [_options_]

# PARAMETERS

**--format** _FORMAT_
> 输出格式：yaml、json、value。

**--run-diagnostics**
> 检查连接性和权限。

**--anonymize**
> 省略个人信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud info** 提供 Google Cloud SDK 安装及运行环境的完整快照。输出包括 SDK 版本、安装目录、Python 解释器位置和版本、已配置的账号与项目以及活动配置名称。

当 gcloud 命令行为异常或需要求助时，这些信息对排查问题极有价值，因为它揭示了可能影响命令执行的环境因素。--run-diagnostics 标志更进一步，会对 Google Cloud 服务执行主动连接测试，帮助定位网络或防火墙问题。

--format 选项允许以编程方式提取特定值，适合需要确定安装路径或活动配置设置的脚本。--anonymize 标志会从输出中移除个人可识别信息，使其可以安全地包含在缺陷报告或支持请求中而不泄露账号详情。

# CAVEATS

可能包含敏感账号信息。诊断测试需要网络访问。

# HISTORY

gcloud info 属于 **Google Cloud SDK** 诊断工具，用于查看 CLI 配置和环境。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-config](/man/gcloud-config)(1)

# RESOURCES

```[Documentation](https://cloud.google.com/sdk/gcloud/reference/info)```

<!-- verified: 2026-07-15 -->
