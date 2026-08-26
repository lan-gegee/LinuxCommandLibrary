# TAGLINE

基于终端的 Markdown 笔记管理器

# TLDR

**在已配置的目录中打开笔记管理器**

```rucola```

**为特定目录打开笔记管理器**

```rucola [~/notes]```

# SYNOPSIS

**rucola** [_options_] [_directory_]

# DESCRIPTION

**rucola** 是一个用于管理 zettelkasten 风格互链 Markdown 笔记的 TUI 工具。它显示笔记统计信息，让你可以通过链接和反向链接探索笔记之间的关联，并能启动你偏好的终端文本编辑器。它还可以选择将笔记编译为 HTML，支持 LaTeX 和代码高亮。

# HISTORY

**rucola** 由 **Linus Mussmaecher** 创建，使用 **Rust** 语言和 ratatui 框架编写。

# INSTALL

```pacman: sudo pacman -S rucola```

```nix: nix profile install nixpkgs#rucola```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nb](/man/nb)(1), [wiki-tui](/man/wiki-tui)(1)
