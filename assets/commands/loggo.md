# TAGLINE

用于结构化 JSON 日志流式查看的终端应用

# TLDR

**从文件流式查看日志**

```loggo stream -f [path/to/logfile]```

**从管道输入流式查看日志**

```cat [logfile] | loggo stream```

**流式查看 Kubernetes 日志**

```kubectl logs -f [pod_name] | loggo stream```

# SYNOPSIS

**loggo** _command_ [_options_]

# DESCRIPTION

**loggo** 是一个功能丰富的终端 UI，用于处理基于 JSON 的结构化日志流。它可以流式解析来自持久化文件和管道输入的日志，还提供创建日志模板的工具。

它可用于本地运行的应用、Kubernetes 集群、GCP Stack Driver（Google Logs）以及许多其他来源。TUI 基于 tview 和 tcell 构建，支持交互式日志浏览和过滤。

# CAVEATS

专为 JSON 格式的日志设计。非 JSON 日志格式可能无法正确解析。

# HISTORY

**loggo** 由 **aurc** 创建，采用 **Go** 编写。

# INSTALL

```aur: yay -S loggo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [lnav](/man/lnav)(1)
