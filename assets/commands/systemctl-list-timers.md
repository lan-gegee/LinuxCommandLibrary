# TAGLINE

列出已调度的定时器单元

# TLDR

列出**活动的**定时器

```systemctl list-timers```

列出**全部**定时器

```systemctl list-timers -a```

按**模式**过滤

```systemctl list-timers [pattern]```

按**状态**过滤

```systemctl list-timers --state [active|inactive|failed]```

# SYNOPSIS

**systemctl list-timers** [_OPTIONS_] [_PATTERN_...]

# PARAMETERS

**-a, --all**
> 包括未激活的定时器

**--state=** _STATE_
> 按状态过滤

**--no-legend**
> 不显示表头和页脚

**--no-pager**
> 禁用分页器

# DESCRIPTION

**systemctl list-timers** 显示当前内存中处于活动状态的定时器单元。输出内容包括下次触发时间、距离下次触发的剩余时间、上次触发时间、距上次触发经过的时间、定时器单元以及它激活的单元。

定时器单元是 systemd 对 cron 的替代方案，以更高的灵活性和更好的日志集成来提供服务的定时激活。

# OUTPUT COLUMNS

**NEXT** - 下次计划触发时间

**LEFT** - 距离下次触发的剩余时间

**LAST** - 上次触发时间

**PASSED** - 距上次触发经过的时间

**UNIT** - 定时器单元名称

**ACTIVATES** - 由该定时器触发的单元

# CAVEATS

时间是相对于当前时间的。通过 `systemd-run` 创建的临时定时器也会出现在这里。某些系统定时器的运行频率很低（每周、每月一次）。

# HISTORY

**list-timers** 子命令提供定时任务的概览，取代传统的 `crontab -l` 列表，并提供更丰富的时间和触发服务信息。

# SEE ALSO

[systemctl](/man/systemctl)(1), [crontab](/man/crontab)(1)
