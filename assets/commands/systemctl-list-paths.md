# TAGLINE

列出由路径激活的单元

# TLDR

列出**路径**单元

```systemctl list-paths```

按**模式**过滤

```systemctl list-paths [pattern]```

列出**全部**单元（包括未激活的）

```systemctl list-paths -a```

按**状态**过滤

```systemctl list-paths --state [state]```

显示**单元类型**

```systemctl list-paths --show-types```

# SYNOPSIS

**systemctl list-paths** [_OPTIONS_] [_PATTERN_...]

# PARAMETERS

**-a, --all**
> 包括未激活的路径单元

**--state=** _STATE_
> 按状态过滤

**--show-types**
> 在输出中显示单元类型

**--no-legend**
> 不显示表头和页脚

**--no-pager**
> 禁用分页器

# DESCRIPTION

**systemctl list-paths** 显示当前加载到内存中的路径单元，并按其监视的路径排序。当指定的文件系统路径被修改时，路径单元会激活其他单元。

输出内容包括被监视的路径、路径单元名称及其当前状态。

# CAVEATS

只显示路径单元，不显示相关的服务单元。未激活的路径单元默认会被隐藏。路径监控基于 inotify，内核对可监视的路径数量有限制。

# HISTORY

**list-paths** 子命令提供了文件系统触发单元的专属视图，这类单元是 systemd 对 incron 或类似文件监视机制的替代方案。

# SEE ALSO

[systemctl-list-units](/man/systemctl-list-units)(1), [systemctl](/man/systemctl)(1)
