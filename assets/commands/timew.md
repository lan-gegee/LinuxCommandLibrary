# TAGLINE

基于标签的时间区间跟踪

# TLDR

**开始跟踪**

```timew start [tag1] [tag2]```

**停止跟踪**

```timew stop```

**显示当前状态**

```timew```

**显示汇总**

```timew summary```

**显示本周**

```timew summary :week```

**继续上一个任务**

```timew continue```

**补录过去的时间**

```timew track [9:00] - [12:00] [meeting]```

# SYNOPSIS

**timew** [_command_] [_options_] [_args_]

# PARAMETERS

**start**
> 开始跟踪。

**stop**
> 结束跟踪。

**summary**
> 显示报告。

**continue**
> 恢复上一个。

**track**
> 补录过去的时间。

**:day**
> 今天过滤器。

**:week**
> 本周。

# DESCRIPTION

**timew**（Timewarrior）是一款命令行时间跟踪工具，通过灵活的标签体系记录工作区间并分类。用 **start** 加一个或多个描述活动的标签开始跟踪，完成后执行 **stop**。**track** 命令支持事后补录过去的区间。

报告功能是内置的，**summary** 命令提供时间细分，并可使用 **:day**、**:week** 或 **:month** 等 hint 语法的日期范围进行过滤。数据也可以导出给外部报表工具使用。

Timewarrior 与 Taskwarrior 集成，可在任务开始和结束时自动跟踪时间，提供任务与时间管理一体化的工作流。

# CONFIGURATION

**~/.timewarrior/timewarrior.cfg**
> 主配置文件，用于主题、排除项（节假日、周末）和报表设置。

**~/.timewarrior/data/**
> 存放时间跟踪区间数据文件的目录。

# CAVEATS

日期范围的用法需要学习成本。数据存放在 ~/.timewarrior。Taskwarrior 集成为可选。

# HISTORY

**Timewarrior** 由 **Taskwarrior** 团队创建，作为配套的时间跟踪工具。

# INSTALL

```apt: sudo apt install timewarrior```

```dnf: sudo dnf install timew```

```pacman: sudo pacman -S timew```

```zypper: sudo zypper install timewarrior```

```brew: brew install timewarrior```

```nix: nix profile install nixpkgs#timewarrior```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[task](/man/task)(1), [timetrap](/man/timetrap)(1), [watson](/man/watson)(1)
