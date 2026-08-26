# TAGLINE

键盘驱动的命令行任务管理器

# TLDR

**启动任务管理器**

```omm```

**从标准输入导入任务**

```echo "[task]" | omm import```

**为任务详情使用指定编辑器**

```omm --editor [editor]```

# SYNOPSIS

**omm** [_command_] [_options_]

# DESCRIPTION

**omm**（on-my-mind）是一款键盘驱动的终端任务管理器。它的设计理念是：你通常一次只专注一个任务，而优先级经常变化，因此它让你可以用简单的按键快速调整任务顺序。

其 TUI 包含活跃任务和已归档任务的视图、任务书签、上下文与详情窗格，以及任务录入/更新界面。它支持紧凑和宽松两种显示模式，并支持自定义主题。

# CAVEATS

任务保存在本地。没有内置的同步或协作功能。

# HISTORY

**omm** 由 **dhth** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S omm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[taskwarrior](/man/taskwarrior)(1)
