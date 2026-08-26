# TAGLINE

获取并显示频道通知

# TLDR

**显示频道通知**

```conda notices```

**显示来自特定频道的通知**

```conda notices -c [channel_name]```

# SYNOPSIS

**conda** **notices** [_options_]

# PARAMETERS

**-c**, **--channel** _CHANNEL_
> 包含指定的频道。可以多次指定。

**--use-local**
> 使用本地构建的软件包。

**--override-channels**
> 不搜索默认频道或 .condarc 中的频道。需要配合 **--channel**。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda notices** 获取并显示来自 conda 频道的通知。频道可以发布重要公告、弃用警告或安全通告，这些内容会通过此命令展示。通知会在本地缓存，只有在缓存过期后才会重新获取。

# SEE ALSO

[conda](/man/conda)(1), [conda-config](/man/conda-config)(1), [conda-info](/man/conda-info)(1)
