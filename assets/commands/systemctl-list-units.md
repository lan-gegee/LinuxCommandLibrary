# TAGLINE

列出已加载的单元及其状态

# TLDR

列出**活动的**单元

```systemctl list-units```

列出**全部**单元

```systemctl list-units -a```

按**类型**过滤

```systemctl list-units -t [service|socket|timer]```

按**状态**过滤

```systemctl list-units --state [running|listening|dead]```

按**模式**过滤

```systemctl list-units '[pattern*]'```

输出时不使用**分页器**

```systemctl list-units --no-pager```

输出时不带**表头**

```systemctl list-units --no-legend```

只列出**失败的**单元

```systemctl list-units --failed```

列出**完整名称的**单元（不用省略号）

```systemctl list-units --full```

# SYNOPSIS

**systemctl list-units** [_OPTIONS_] [_PATTERN_...]

# PARAMETERS

**-a, --all**
> 包括未激活的单元和跟随其他单元的单元

**-t, --type=** _TYPE_
> 按单元类型过滤（逗号分隔的列表，如 service、socket、timer）

**--state=** _STATE_
> 按 LOAD、SUB 或 ACTIVE 状态过滤（逗号分隔的列表）

**--failed**
> 只显示失败的单元（等同于 --state=failed）

**-l, --full**
> 输出中不省略单元名称、描述或其他字段

**-r, --recursive**
> 同时显示本地容器的单元

**--with-dependencies**
> 显示指定单元及其依赖

**--no-pager**
> 禁用分页器输出

**--no-legend**
> 不显示表头和页脚（便于脚本使用）

# DESCRIPTION

**systemctl list-units** 显示 systemd 当前加载到内存中的单元。默认情况下，它会显示处于活动状态、有待处理任务或失败的单元。

输出内容包括单元名称、加载状态、活动状态、子状态和描述。这是查看系统当前状态的主要命令。

# OUTPUT COLUMNS

**UNIT** - 单元名称

**LOAD** - 加载状态（loaded、not-found、error）

**ACTIVE** - 活动状态（active、inactive、failed）

**SUB** - 子状态（running、exited、dead、listening）

**DESCRIPTION** - 单元描述

# CAVEATS

只显示当前已加载的单元。要查看所有已安装的单元请使用 `list-unit-files`。失败的单元在被 `systemctl reset-failed` 确认之前会一直可见。

# HISTORY

**list-units** 子命令是 systemd 中最主要的状态总览命令，取代了各种 init 脚本列表机制。

# SEE ALSO

[systemctl-list-unit-files](/man/systemctl-list-unit-files)(1), [systemctl-list-timers](/man/systemctl-list-timers)(1), [systemctl-status](/man/systemctl-status)(1), [systemctl](/man/systemctl)(1), [journalctl](/man/journalctl)(1)
