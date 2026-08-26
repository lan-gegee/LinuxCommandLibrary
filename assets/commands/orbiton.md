# TAGLINE

零配置的终端文本编辑器和极简 IDE

# TLDR

**打开文件**

```o [path/to/file]```

**打开并定位到指定行**

```o [path/to/file]:[line_number]```

# SYNOPSIS

**o** [_options_] [_file_[:_line_]]

# DESCRIPTION

**orbiton**（命令名：**o**）是一款响应迅速、无需配置的终端文本编辑器，以单个独立的可执行文件形式发布。它支持语法高亮、跳转到错误位置、彩虹括号、宏、剪切/粘贴传送门、简单的 gdb 前端、终端内图像预览，以及内置拼写检查器。

无需任何配置文件——凭借合理的默认设置开箱即用。

# CAVEATS

并非用来取代完整的 IDE。与 Neovim 或 VS Code 相比，高级 LSP 功能有限。

# HISTORY

**orbiton** 由 **Alexander F. Rodseth**（xyproto）创建，使用 **Go** 编写。

# INSTALL

```pacman: sudo pacman -S orbiton```

```brew: brew install orbiton```

```nix: nix profile install nixpkgs#orbiton```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[micro](/man/micro)(1), [nano](/man/nano)(1), [ox](/man/ox)(1)
