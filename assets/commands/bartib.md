# TAGLINE

基于纯文本日志的简易命令行时间跟踪器

# TLDR

**开始**跟踪任务，可选指定项目

```bartib start -d "[description]" -p "[project]"```

**停止**当前活动

```bartib stop```

**显示**正在运行的活动

```bartib current```

**列出**今天的活动

```bartib list --today```

**报告**今天花费的时间

```bartib report --today```

**继续**上一个任务

```bartib continue```

# SYNOPSIS

**bartib** *command* [*options*]

# DESCRIPTION

**bartib** 是一款用 Rust 编写的轻量级时间跟踪 CLI。活动记录存储在纯文本日志文件中（路径由 **BARTIB_FILE** 或配置指定），数据易于编辑、备份和版本管理。子命令涵盖任务的开始/停止、继续先前工作、列出历史记录，以及按天、项目或日期范围过滤生成报告。

非常适合希望在终端内原生跟踪时间、又不想依赖笨重 GUI 或云服务的自由职业者和开发者。

# PARAMETERS

**start** **-d** *description* [**-p** *project*]

> 开始一个新活动。

**stop**

> 停止正在运行的活动。

**continue** [*number*]

> 恢复先前的活动（可选按列表索引指定）。

**current**

> 显示当前正在运行的活动。

**list** [**--today**] [**--yesterday**] [**--date** *date*] [**--project** *name*]

> 按过滤条件列出已记录的活动。

**report** [与 **list** 相同的过滤条件]

> 汇总花费的时间。

**edit** / **cancel** / **change**

> 更正或取消条目（见 **bartib --help**）。

**projects**

> 列出已知的项目名称。

设置 **BARTIB_FILE** 可选择日志路径（默认位于用户主目录下）。

# CAVEATS

所有状态都存放在本地文件中——如果依赖历史记录，请务必备份。多台机器并发写入需要外部同步。精度基于墙上时钟；它不是采样式性能分析器。

# INSTALL

```aur: yay -S bartib```

```brew: brew install bartib```

```nix: nix profile install nixpkgs#bartib```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[timew](/man/timew)(1), [watson](/man/watson)(1), [timetrap](/man/timetrap)(1)

# RESOURCES

```[Source code](https://github.com/nikolassv/bartib)```

<!-- verified: 2026-07-19 -->
