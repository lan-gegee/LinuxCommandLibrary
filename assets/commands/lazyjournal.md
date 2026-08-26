# TAGLINE

查看 journald、Docker 和 Kubernetes 日志的 TUI

# TLDR

**启动交互式日志查看器**

```lazyjournal```

通过管道传入日志并用模糊搜索过滤

```cat [/var/log/syslog] | lazyjournal -f "[error]"```

通过管道传入日志并用正则表达式过滤

```cat [/var/log/syslog] | lazyjournal -r "[error|fatal]"```

通过 SSH 连接远程系统

```lazyjournal --ssh "[user@host -p 2222]"```

# SYNOPSIS

**lazyjournal** [_options_]

# PARAMETERS

**-f**
> 启用模糊搜索过滤模式（不区分大小写的近似匹配，类似 fzf）。

**-r**
> 启用正则表达式过滤模式。

**-c**
> 在命令行模式下启用输出高亮。

**-l**, **--logging**
> 将执行过的命令写入日志文件以便调试。

**-m**
> 禁用鼠标控制。

**-t**, **--timezone-filter** _offset_
> 为日期/时间范围过滤设置 UTC 偏移量（默认：`+00:00`）。

**--ssh** _args_
> 通过 SSH 连接远程系统。接受标准的 SSH 参数，须作为一个整体加引号传入。

# DESCRIPTION

**lazyjournal** 是一个 TUI 工具，可以从多种来源读取日志，包括 journald、auditd、文件系统、Docker 和 Podman 容器、Compose 编排栈以及 Kubernetes Pod。它支持日志高亮和多种过滤模式。

过滤能力包括区分大小写的精确匹配、模糊搜索（类似 fzf）、正则表达式模式，以及基于时间戳的日期/时间范围选择。它可以列出所有 systemd 服务及其当前状态，并像 **tail** 一样实时输出新事件。

# CAVEATS

日志来源是否可用取决于主机系统。Docker 和 Kubernetes 日志来源要求各自的运行时已安装且正在运行。

# HISTORY

**lazyjournal** 由 **Lifailon** 创建，使用 **Go** 编写。它的灵感来自 lazydocker 和 lazygit，支持 Linux、macOS、BSD 和 Windows。

# INSTALL

```brew: brew install lazyjournal```

```nix: nix profile install nixpkgs#lazyjournal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[journalctl](/man/journalctl)(1), [lazydocker](/man/lazydocker)(1), [lazygit](/man/lazygit)(1), [tail](/man/tail)(1)
