# TAGLINE

基于 Git 的终端待办事项管理器

# TLDR

**添加**新任务

```dstask add [task description]```

**列出**所有任务

```dstask```

**标记**任务为完成

```dstask done [task_id]```

按上下文/项目**查看**任务

```dstask context [context_name]```

# SYNOPSIS

**dstask** [_command_] [_arguments_]

# PARAMETERS

**-c, --context** _CONTEXT_
> 设置上下文过滤器

**-p, --project** _PROJECT_
> 设置项目过滤器

**-P, --priority** _PRIORITY_
> 设置优先级：low、medium、high、critical

**-t, --tag** _TAG_
> 为任务添加标签

**-n, --note** _NOTE_
> 为任务添加备注

**--due** _DATE_
> 设置截止日期（YYYY-MM-DD）

**-v, --verbose**
> 启用详细输出

**-h, --help**
> 显示帮助并退出

**--version**
> 显示版本并退出

# DESCRIPTION

**dstask** 是一款将待办事项存储在 Git 仓库中的任务管理器，支持版本控制、跨设备同步和离线访问。它遵循 GTD（Getting Things Done）方法论，支持上下文、项目和优先级。

任务以简单文本文件的形式存储在 Git 仓库中，便于携带且避免厂商锁定。该工具提供简洁的命令行界面来管理任务，没有多余的复杂度。

# COMMANDS

**add** _TASK_
> 添加新任务

**edit** _ID_
> 编辑现有任务

**done** _ID_
> 将任务标记为已完成

**rm** _ID_
> 移除任务

**list**
> 列出任务（默认命令）

**next**
> 显示下一个可执行的任务

**context** _CONTEXT_
> 切换到上下文

**project** _PROJECT_
> 切换到项目视图

**sync**
> 与远程 Git 仓库同步

**undo**
> 撤销上一次操作

# CAVEATS

需要先初始化并配置 Git。远程同步需要有效的 Git remote。任务 ID 是内部引用，在不同操作之间并不稳定。不原生支持复杂的周期性任务。

# HISTORY

**dstask** 由 Cody Chan 创建，是一款拥抱纯文本存储并用 Git 做同步的任务管理器。它受 todo.txt 启发，但增加了 Git 集成和更现代的界面。

# INSTALL

```brew: brew install dstask```

```nix: nix profile install nixpkgs#dstask```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [task](/man/task)(1)
