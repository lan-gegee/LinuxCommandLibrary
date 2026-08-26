# TAGLINE

列出自动挂载单元及其状态

# TLDR

列出**自动挂载**单元

```systemctl list-automounts```

列出**全部**单元（包括未激活的）

```systemctl list-automounts -a```

按**状态**过滤

```systemctl list-automounts --state [active|inactive|failed]```

按**模式**过滤

```systemctl list-automounts [pattern]```

# SYNOPSIS

**systemctl list-automounts** [_OPTIONS_] [_PATTERN_...]

# PARAMETERS

**-a, --all**
> 包括未激活的自动挂载单元

**--state=** _STATE_
> 按状态过滤（active、inactive、failed 等）

**--no-legend**
> 不显示表头和页脚

**--no-pager**
> 禁用分页器输出

# DESCRIPTION

**systemctl list-automounts** 显示当前加载到内存中的自动挂载单元，包括挂载路径和对应的单元名称。当访问挂载点时，自动挂载单元会触发按需挂载。

输出内容包含被监视的路径、自动挂载单元名称及其当前状态。

# CAVEATS

只显示自动挂载单元，不显示普通挂载单元。未激活的自动挂载默认会被隐藏。要查看全部挂载信息，请使用 `systemctl list-units --type=mount`。

# HISTORY

**list-automounts** 子命令提供了按需挂载配置的专属视图，将自动挂载单元与普通挂载分开显示，便于管理。

# SEE ALSO

[systemctl-list-units](/man/systemctl-list-units)(1), [systemctl](/man/systemctl)(1), [mount](/man/mount)(8)
