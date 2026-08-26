# TAGLINE

通过 cgroup 冻结 unit 进程

# TLDR

**冻结**一个 unit

```systemctl freeze unit_name```

冻结**多个** unit

```systemctl freeze unit1 unit2```

冻结**所有**运行中的 unit

```systemctl freeze '*'```

# SYNOPSIS

**systemctl freeze** _PATTERN_...

# DESCRIPTION

**systemctl freeze** 使用 cgroup freezer 冻结一个或多个 unit。被冻结的 unit 的所有进程都被挂起，在解冻之前不会被调度。这适合在不停止服务的情况下暂时将其暂停。

# PARAMETERS

**PATTERN**
> 一个或多个要冻结的 unit 名称或模式

# CAVEATS

被冻结的 unit 仍留在内存中，但无法执行。使用 "systemctl thaw" 恢复被冻结的 unit。只有 service、scope 和 slice 类型的 unit 支持冻结。需要内核支持 cgroup v2（统一层级）。

# HISTORY

**systemctl freeze** 是 **systemd** 的一部分，为服务管理提供基于 cgroup 的进程冻结功能。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-thaw](/man/systemctl-thaw)(1)
