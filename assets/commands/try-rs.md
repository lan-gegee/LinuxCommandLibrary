# TAGLINE

带 TUI 的临时实验工作区管理器

# TLDR

启动 TUI 管理实验

```try-rs```

创建新的实验目录

```try-rs [rust-test]```

将仓库克隆到实验目录

```try-rs [https://github.com/user/repo]```

# SYNOPSIS

**try-rs** [_options_] [_name_]

# DESCRIPTION

**try-rs** 将临时的项目实验组织到以日期为前缀的目录中，避免弄乱你的桌面或 /tmp。它提供功能丰富的 TUI，用于创建、浏览和清理实验，并具备模糊搜索和 git 集成（自动克隆 URL）等特性。

# HISTORY

**try-rs** 由 **Tassio Virginio**（tassiovirginio）创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install try-rs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [direnv](/man/direnv)(1), [git](/man/git)(1)
