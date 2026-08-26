# TAGLINE

重新执行 systemd 管理器二进制文件

# TLDR

**重新执行** systemd 管理器

```systemctl daemon-reexec```

# SYNOPSIS

**systemctl daemon-reexec**

# DESCRIPTION

**systemctl daemon-reexec** 重新执行 systemd 管理器（PID 1），用新副本替换正在运行的 systemd 二进制文件，同时保留所有 unit 的当前状态。它用于升级 systemd 软件包之后，在不重启系统的情况下应用新二进制文件。

与只重新加载配置的 `daemon-reload` 不同，`daemon-reexec` 会替换整个 systemd 进程。转换期间所有运行中的服务不受干扰地继续运行。

# CAVEATS

需要 root 权限。只应在 systemd 软件包升级后使用。服务状态会保留，但任何进行中的事务可能受到影响。日常运行中通常不需要。

# HISTORY

**daemon-reexec** 子命令使 systemd 自身能够在不重启系统的情况下进行在线升级，支持现代的零停机维护实践。

# SEE ALSO

[systemctl-daemon-reload](/man/systemctl-daemon-reload)(1), [systemctl](/man/systemctl)(1)
