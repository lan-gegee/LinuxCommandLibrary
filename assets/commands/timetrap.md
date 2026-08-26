# TAGLINE

简单的命令行时间跟踪工具

# TLDR

**启动计时器**

```timetrap in "[task description]"```

**停止计时器**

```timetrap out```

**显示当前状态**

```timetrap now```

**显示今天**

```timetrap display```

**切换表单**

```timetrap sheet [project]```

**列出表单**

```timetrap list```

**编辑条目**

```timetrap edit```

# SYNOPSIS

**timetrap** _command_ [_options_] [_args_]

# PARAMETERS

**in**
> 开始跟踪。

**out**
> 停止跟踪。

**now**
> 当前状态。

**display**
> 显示条目。

**sheet**
> 切换时间表。

**list**
> 列出表单。

**edit**
> 编辑条目。

# DESCRIPTION

**timetrap** 是一款简单的命令行时间跟踪工具，采用打卡进出模式。用 **in** 启动计时器，用 **out** 停止，条目存储在本地 SQLite 数据库中，可靠且便于迁移。

时间条目按表单组织，每个表单相当于不同项目或客户独立的时间表。通过 **sheet** 命令在多个表单之间切换，可以轻松跟踪多项活动而不会混淆条目。

**display** 命令显示已记录的条目及其计算出的时长，报表功能可生成用于计费或回顾的时间汇总。条目可以事后编辑，以纠正错误或添加备注。

# CAVEATS

需要 Ruby。仅支持命令行。手动录入。

# HISTORY

**timetrap** 诞生之初就是一个使用 SQLite 存储的简单命令行时间跟踪工具。

# INSTALL

```nix: nix profile install nixpkgs#timetrap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watson](/man/watson)(1), [timew](/man/timew)(1)
