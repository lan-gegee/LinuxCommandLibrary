# TAGLINE

面向多个提供方的任务聚合 TUI

# TLDR

**启动任务聚合 TUI**

```tatuin```

**使用自定义配置文件**

```tatuin --config [path/to/config]```

# SYNOPSIS

**tatuin** [_options_]

# DESCRIPTION

**tatuin** 将来自多个提供方的任务聚合到同一个终端界面中。支持的提供方包括 **Todoist** 和 **Obsidian**（完整的增删改查）、**CalDAV**（完整 CRUD）、**GitLab TODOs**（列表和状态更新），以及 **GitHub Issues** 和 **iCal**（只读）。功能包括任务过滤、状态更新、可保存的界面状态、键盘快捷键（例如 `a` 添加、`e` 编辑）以及自定义主题。

Obsidian 集成需要在你的 Obsidian 库中安装 "Local REST API" 插件。

# HISTORY

**tatuin** 由 **Konnov Konstantin**（panter-dsd）创建，使用 **Rust** 编写。

# INSTALL

```aur: yay -S tatuin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[taskwarrior](/man/taskwarrior)(1), [todoist](/man/todoist)(1), [tui-journal](/man/tui-journal)(1)
