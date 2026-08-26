# TAGLINE

命令行时间跟踪工具

# TLDR

**开始跟踪**

```watson start [project] +[tag]```

**停止跟踪**

```watson stop```

**显示当前状态**

```watson status```

**列出今天的条目**

```watson log -d```

**列出本周的条目**

```watson log -w```

**显示报告**

```watson report```

**编辑上一条条目**

```watson edit```

**取消当前跟踪**

```watson cancel```

# SYNOPSIS

**watson** _command_ [_options_] [_args_]

# PARAMETERS

**start** _PROJECT_ [_+TAGS_]
> 开始跟踪。

**stop**
> 停止跟踪。

**status**
> 当前时间帧。

**log** [_-d_|_-w_|_-m_]
> 显示条目。

**report** [_-d_|_-w_|_-m_]
> 生成报告。

**edit**
> 编辑条目。

**cancel**
> 取消当前跟踪。

**add**
> 添加过去的条目。

**remove**
> 删除条目。

# DESCRIPTION

**watson** 是一款命令行时间跟踪工具，按命名项目记录工作会话，并可用可选标签进行分类。启动计时器会将当前时刻与某个项目和标签关联，停止时会保存一个已计算时长的完整时间段。

log 命令按时间顺序显示已跟踪的条目，并提供过滤器用于查看今天的工作、本周或特定日期范围的记录。报告按项目汇总时间，显示给定周期内花在每个项目及其标签上的总时长。

可以追溯添加过去的条目，也可以编辑已有条目以纠正错误；cancel 命令则丢弃当前正在运行的计时器而不保存。

# CAVEATS

单用户工具。没有内置同步功能。使用 SQLite 后端。

# HISTORY

**Watson** 的设计目标是提供简单的命令行时间跟踪。它以福尔摩斯的搭档华生命名，帮助你弄清时间去向。

# INSTALL

```zypper: sudo zypper install watson```

```brew: brew install watson```

```nix: nix profile install nixpkgs#watson```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timew](/man/timew)(1), [clockify](/man/clockify)(1)
