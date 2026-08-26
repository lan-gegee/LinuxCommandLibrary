# TAGLINE

打开 Google Cloud CLI 的反馈表单

# TLDR

在浏览器中**打开反馈表单**

```gcloud feedback```

**附上日志文件**

```gcloud feedback --log-file [path/to/gcloud.log]```

# SYNOPSIS

**gcloud feedback** [**--log-file=**_LOG_FILE_] [_GCLOUD_WIDE_FLAGS_...]

# PARAMETERS

**--log-file** _FILE_
> 要附上的 `gcloud` 日志文件路径（通常位于 `~/.config/gcloud/logs/`）。提供该选项时，gcloud 会读取日志并将指向它的链接连同追踪信息一起粘贴到新建 issue 的 URL 中，便于 CLI 团队复现问题。

**gcloud wide flags**
> 所有全局标志均适用：`--help`、`--quiet`、`--verbosity`、`--configuration`、`--user-output-enabled`、`--log-http` 等。

# DESCRIPTION

**gcloud feedback** 会在默认浏览器中打开 Google Cloud CLI 的官方 issue 跟踪器，并预填系统信息（gcloud 版本、平台、Python 版本），避免报告从空白开始。这是向 CLI 本身报告缺陷或请求功能的推荐方式；若要反馈具体的 Google Cloud 产品，请使用其控制台内的"发送反馈"组件。

配合 `--log-file` 使用时，gcloud 会打开日志、剔除敏感头部信息，方便把最近的失败轨迹随报告一起分享。

# CAVEATS

需要浏览器——在无头（headless）机器上会把 URL 打印到 stdout。日志可能包含资源名称和项目 ID；粘贴到公开 issue 前请先检查。安全漏洞请通过私密的安全联系方式报告，不要使用公开的 issue 跟踪器。

# SEE ALSO

[gcloud](/man/gcloud)(1), [gcloud-help](/man/gcloud-help)(1), [gcloud-version](/man/gcloud-version)(1)
