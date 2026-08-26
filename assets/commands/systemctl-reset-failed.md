# TAGLINE

清除单元的失败状态

# TLDR

重置**所有**失败的单元

```systemctl reset-failed```

重置**特定**单元

```systemctl reset-failed [unit]```

重置**多个**单元

```systemctl reset-failed [unit1 unit2 ...]```

先**列出**失败的单元，再重置它们

```systemctl --failed```

# SYNOPSIS

**systemctl reset-failed** [_PATTERN_...]

# DESCRIPTION

**systemctl reset-failed** 清除一个或多个单元的"failed"状态，并重置其状态计数器。不带参数时会重置所有失败的单元。

当单元失败时（进程以非零码退出、异常终止或超时），它会进入"failed"状态，其退出码和状态会被记录。该状态会一直保持，直到单元被重启或通过此命令显式重置。

除了清除失败状态外，此命令还会重置：

- 所有单元类型的**启动速率限制计数器**（归零）。
- 服务单元的**重启计数器**（归零）。

这在单元达到启动速率限制、systemd 拒绝再次启动它时特别有用。执行 **reset-failed** 会重置计数器，让单元可以立即被再次启动。

# CAVEATS

不会修复导致失败的根本原因。单元再次启动时可能仍会失败。请先调查并修复失败的根本原因，再使用此命令。

# HISTORY

**reset-failed** 子命令提供了一种确认并清除失败单元状态的方式，可用于重新尝试启动，以及在问题解决后清理失败列表。

# SEE ALSO

[systemctl-status](/man/systemctl-status)(1), [systemctl-restart](/man/systemctl-restart)(1), [systemctl-start](/man/systemctl-start)(1), [systemctl](/man/systemctl)(1), [journalctl](/man/journalctl)(1)
