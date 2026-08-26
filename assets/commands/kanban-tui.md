# TAGLINE

基于终端的看板任务管理器

# TLDR

**启动看板**

```kanban-tui```

**打开指定的看板文件**

```kanban-tui [path/to/kanban.md]```

# SYNOPSIS

**kanban-tui** [_options_] [_file_]

# DESCRIPTION

**kanban-tui** 是一个基于终端的看板工具，用于管理任务和项目。它提供一个 TUI，包含对应不同任务状态的列（待办、进行中、已完成），并支持以类 Vim 键位创建、编辑、移动和删除卡片。

该工具使用基于文件的结构存储数据，支持嵌套和链接的看板（卡片可以链接到其他 kanban 文件），以及把多个项目看板聚合到单一主视图的元看板。

# CAVEATS

文件格式是该工具专有的。多个编辑器同时编辑同一文件可能产生冲突。

# HISTORY

**kanban-tui** 由 **sokinpui** 创建，用 **Go** 编写。生态中还存在其他若干看板 TUI 实现，包括基于 Python Textual 框架的变体。

# SEE ALSO

[taskwarrior](/man/taskwarrior)(1)
