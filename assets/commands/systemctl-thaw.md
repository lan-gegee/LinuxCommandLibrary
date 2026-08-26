# TAGLINE

恢复已冻结单元的进程

# TLDR

**解冻**（恢复）一个单元

```systemctl thaw [unit]```

解冻**多个**单元

```systemctl thaw [unit1 unit2 ...]```

解冻**所有**冻结的单元

```systemctl thaw '*'```

# SYNOPSIS

**systemctl thaw** _PATTERN_...

# DESCRIPTION

**systemctl thaw** 恢复之前通过 `systemctl freeze` 冻结的一个或多个单元。被冻结的单元，其所有进程都会经由内核的 freezer cgroup 控制器挂起。

解冻让单元的进程从暂停之处继续执行。

# CAVEATS

只对曾被冻结的单元有效。对未冻结的单元执行解冻没有任何效果。需要 cgroup freezer 控制器可用。

# HISTORY

**thaw** 子命令与 freeze 功能互为补充，支持受控的进程暂停与恢复，可用于调试或资源管理。

# SEE ALSO

[systemctl-freeze](/man/systemctl-freeze)(1), [systemctl](/man/systemctl)(1)
