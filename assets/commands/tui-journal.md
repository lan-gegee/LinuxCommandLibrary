# TAGLINE

终端日志与笔记应用

# TLDR

**启动日志 TUI**

```tjournal```

**使用 JSON 文件后端**

```tjournal --backend json```

**使用 SQLite 数据库后端**

```tjournal --backend sqlite```

# SYNOPSIS

**tjournal** [_options_]

# DESCRIPTION

**tui-journal** 是一个基于终端的日志应用，支持创建、编辑和删除日志条目，并带有 Markdown 高亮。它支持 JSON 和 SQLite 后端、自定义彩色标签、模糊搜索，以及使用外部文本编辑器。

# HISTORY

**tui-journal** 由 **Ammar Abou Zor**（AmmarAbouZor）创建，用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S tui-journal```

```zypper: sudo zypper install tui-journal```

```nix: nix profile install nixpkgs#tui-journal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jrnl](/man/jrnl)(1), [nb](/man/nb)(1), [rucola](/man/rucola)(1)
