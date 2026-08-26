# TAGLINE

带时间线直方图的快速远程优先多主机 TUI 日志查看器

# TLDR

**查看远程主机的日志**

```nerdlog [user]@[host]```

**查看多台主机的日志**

```nerdlog [user]@[host1] [user]@[host2]```

# SYNOPSIS

**nerdlog** [_options_] [_hosts_...]

# DESCRIPTION

**nerdlog** 是一款快速的远程优先多主机 TUI 日志查看器，带有交互式时间线直方图，灵感来自 Graylog 和 Kibana，但没有它们的臃肿。它通过 SSH 同时查询多台远程机器上的日志，按时间范围和模式过滤，并绘制可视化时间线。

该工具读取 /var/log/messages、/var/log/syslog 或 journalctl 中的系统日志，并在远端使用标准 GNU 工具（bash、awk）进行过滤和生成直方图。无需中央服务器或安装代理程序。

# CAVEATS

需要对目标主机的 SSH 访问权限。远程主机上必须可用 bash 和 awk。

# HISTORY

**nerdlog** 由 **dimonomid** 创建，使用 **Go** 语言和 tview 库编写。支持 Linux、FreeBSD、macOS 和 Windows（仅客户端）。

# INSTALL

```apk: sudo apk add nerdlog```

```brew: brew install nerdlog```

```nix: nix profile install nixpkgs#nerdlog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[journalctl](/man/journalctl)(1), [lnav](/man/lnav)(1), [lazyjournal](/man/lazyjournal)(1)
