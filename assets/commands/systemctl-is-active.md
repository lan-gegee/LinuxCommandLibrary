# TAGLINE

检查单元是否正在运行

# TLDR

检查单元是否**处于活动状态**

```systemctl is-active [unit]```

检查**多个**单元

```systemctl is-active [unit1 unit2 ...]```

**安静**模式（仅返回退出码）

```systemctl is-active [unit] -q```

检查**用户**单元

```systemctl is-active [unit] --user```

# SYNOPSIS

**systemctl is-active** [_OPTIONS_] _PATTERN_...

# PARAMETERS

**-q, --quiet**
> 不输出内容，仅返回退出码

**--user**
> 检查用户单元

**--system**
> 检查系统单元（默认）

# DESCRIPTION

**systemctl is-active** 检查一个或多个单元当前是否处于活动状态（正在运行）。它会打印活动状态，并且只要至少有一个单元处于活动状态就返回退出码 0。

可能的状态包括：active、inactive、activating、deactivating、failed。对于多个单元，每个状态各占一行输出。

# EXIT STATUS

如果至少有一个单元处于活动状态则返回 **0**，否则返回**非零值**。这使得它可以在 Shell 脚本中用于基于服务状态的条件判断。

# CAVEATS

只检查当前的运行时状态，而非开机启用状态。一个单元可以被启用但未处于活动状态，也可能处于活动状态但未被启用。请使用 `is-enabled` 检查开机配置。

# HISTORY

**is-active** 子命令提供了一种可脚本化的方式来查询服务状态，取代了对 `systemctl status` 输出的解析。

# SEE ALSO

[systemctl-is-enabled](/man/systemctl-is-enabled)(1), [systemctl-status](/man/systemctl-status)(1), [systemctl](/man/systemctl)(1)
