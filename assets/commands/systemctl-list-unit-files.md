# TAGLINE

列出已安装的单元文件及其状态

# TLDR

列出**已安装的**单元文件

```systemctl list-unit-files```

按**状态**过滤

```systemctl list-unit-files --state [enabled|disabled|static]```

按**类型**过滤

```systemctl list-unit-files -t [service|socket|timer]```

按**名称模式**过滤

```systemctl list-unit-files '[pattern*]'```

输出时不使用**分页器**

```systemctl list-unit-files --no-pager```

输出时不带**表头**

```systemctl list-unit-files --no-legend```

# SYNOPSIS

**systemctl list-unit-files** [_OPTIONS_] [_PATTERN_...]

# PARAMETERS

**--state=** _STATE_
> 按启用状态过滤（enabled、disabled、static、masked 等）

**-t, --type=** _TYPE_
> 按单元类型过滤

**--no-pager**
> 禁用分页器输出

**--no-legend**
> 不显示表头和页脚

# DESCRIPTION

**systemctl list-unit-files** 显示所有已安装的单元文件及其启用状态。与显示运行时状态的 `list-units` 不同，它显示的是所有可用单元的开机配置。

输出内容包括单元文件名及其状态：enabled、disabled、static、masked、generated、transient、indirect 或 alias。

# ENABLEMENT STATES

**enabled** - 开机自动启动

**disabled** - 开机不启动

**static** - 没有 install 区段，作为依赖被启动

**masked** - 完全禁止启动

**indirect** - 通过另一个单元间接启用

# CAVEATS

会显示所有已安装的单元文件，无论其运行时状态如何。某些单元文件可能存在但从未被使用。static 单元无法被直接启用。

# HISTORY

**list-unit-files** 子命令展示全部可用单元及其开机配置，与只显示当前已加载单元的 `list-units` 互为补充。

# SEE ALSO

[systemctl-list-units](/man/systemctl-list-units)(1), [systemctl-enable](/man/systemctl-enable)(1), [systemctl](/man/systemctl)(1)
