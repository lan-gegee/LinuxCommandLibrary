# TAGLINE

命令行任务管理系统

# TLDR

**添加新任务**

```task add "[description]"```

**添加**带项目和截止日期的**任务**

```task add "[description]" project:[project_name] due:[tomorrow]```

**列出所有待办任务**

```task list```

**将任务标记为完成**

```task [task_id] done```

**修改已有任务**

```task [task_id] modify priority:[H] due:[friday]```

**删除任务**

```task [task_id] delete```

查看任务的**详细信息**

```task [task_id] info```

**开始处理某个任务**

```task [task_id] start```

# SYNOPSIS

**task** [_global_options_] [_filter_] _command_ [_arguments_]

# PARAMETERS

**add**
> 向任务列表添加新任务。

**done**
> 将任务标记为已完成。

**delete**
> 从列表中删除任务。

**modify**
> 修改已有任务的属性。

**start**
> 将任务标记为进行中（active）。

**stop**
> 将任务标记为不再进行。

**annotate**
> 为任务添加注释。

**list**
> 使用默认报告显示待办任务。

**info**
> 显示任务的所有数据和元数据。

**undo**
> 撤销最近一次更改。

**log**
> 添加一条本就已完成（无需再做）的任务。

**duplicate**
> 创建任务的副本。

**projects**
> 列出所有项目及其任务数量。

**tags**
> 列出所有在用的标签。

**--rc** _file_
> 使用备用的配置文件。

**--force**
> 跳过确认提示。

**--verbose**
> 显示更详细的输出。

**--quiet**
> 抑制非必要的输出。

**--debug**
> 启用调试输出。

**--version**
> 显示版本信息。

# DESCRIPTION

**Taskwarrior** 是一个命令行任务管理应用，它维护一个任务列表，支持项目、标签、优先级、截止日期和自定义属性，并提供强大的过滤和报表功能。

任务可以带有 **project**、**priority**（H/M/L）、**due** 截止日期、**tags** 标签、**wait** 等待日期以及用户自定义属性。过滤器支持按属性的任意组合来筛选任务。报表提供可定制的任务数据视图。

配置存储在 **~/.taskrc**，任务数据存储在 **~/.task/**。这些位置可以通过环境变量 **TASKRC** 和 **TASKDATA** 覆盖。只要前缀唯一，所有命令都可以缩写。

# CONFIGURATION

**~/.taskrc**
> 主配置文件，控制报表、颜色、别名和默认行为

**~/.task/**
> 默认数据目录，包含任务数据库、撤销日志和用于同步的 backlog

**TASKRC**
> 用于覆盖配置文件位置的环境变量

**TASKDATA**
> 用于覆盖数据目录位置的环境变量

# CAVEATS

任务 ID 是临时的，同步或撤销操作后可能变化。脚本和自动化场景请改用 UUID。**undo** 命令只撤销最近一次操作。与 Taskserver 同步需要额外的设置。

# HISTORY

Taskwarrior 由 **Paul Beckingham** 创建，于 **2006 年**首次发布。它从一个简单的待办清单发展为具备同步能力、钩子和丰富自定义功能的成熟任务管理系统。该项目由 **Gothenburg Bit Factory** 维护，并催生了众多前端和集成方案。**2024 年**发布的 3.0 版本引入了重大的架构调整和性能提升。

# INSTALL

```apt: sudo apt install taskwarrior```

```dnf: sudo dnf install task```

```pacman: sudo pacman -S task```

```apk: sudo apk add go-task-task```

```zypper: sudo zypper install taskwarrior```

```brew: brew install task```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[todo.txt-cli](/man/todo.txt-cli)(1), [remind](/man/remind)(1), [calcurse](/man/calcurse)(1)
