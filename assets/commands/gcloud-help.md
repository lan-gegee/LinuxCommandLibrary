# TAGLINE

gcloud 命令的集成文档

# TLDR

**通用帮助**

```gcloud help```

**某个命令的帮助**

```gcloud help [compute instances create]```

**列出所有命令**

```gcloud help --all```

**搜索帮助**

```gcloud help -- [keyword]```

# SYNOPSIS

**gcloud help** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 要查看帮助的命令。

**--all**
> 列出所有可用命令。

**--** _KEYWORD_
> 在帮助中搜索关键词。

# DESCRIPTION

**gcloud help** 提供对 Google Cloud SDK 内置文档系统的完整访问。每个 gcloud 命令和命令组都有详细的帮助文本，涵盖语法、可用选项和常见用法示例。

指定完整路径即可查看任意命令的帮助，例如 "gcloud help compute instances create" 可查看实例创建的详细文档。--all 标志列出 SDK 中所有可用命令，有助于发现鲜为人知的命令。

搜索功能（通过 -- 加关键词）让你在想实现某个目标但不知道确切命令名时找到相关命令。考虑到 gcloud 庞大的命令面——横跨数十个服务组和数百条命令——这一点尤为有用。帮助系统始终与你安装的 SDK 版本保持同步，确保针对你已有的组件给出准确信息。

# CAVEATS

帮助内容可能较为冗长。在线文档可能有更多示例。某些选项仅在特定上下文中可用。

# HISTORY

gcloud help 是 **Google Cloud SDK** 的集成文档系统，在 CLI 内提供完整的命令参考。

# SEE ALSO

[gcloud](/man/gcloud)(1), [man](/man/man)(1)

# RESOURCES

```[Documentation](https://cloud.google.com/sdk/gcloud/reference/help)```

<!-- verified: 2026-07-15 -->
