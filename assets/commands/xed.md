# TAGLINE

Cinnamon 桌面文本编辑器

# TLDR

**启动**编辑器

```xed```

**打开**文件

```xed [path/to/file1 path/to/file2 ...]```

以指定**编码**打开

```xed --encoding [WINDOWS-1252] [path/to/file]```

列出**编码**

```xed --list-encodings```

跳转到指定**行号**

```xed +[10] [path/to/file]```

# SYNOPSIS

**xed** [_OPTIONS_] [_FILE..._]

# PARAMETERS

**--encoding** _ENCODING_
> 使用指定的字符编码打开文件

**--list-encodings**
> 打印所有支持的编码

**+**_LINE_
> 跳转到指定行号

**--new-window**
> 在新窗口中打开

**--new-document**
> 打开新文档

# DESCRIPTION

**xed** 是 Cinnamon 桌面环境的默认文本编辑器。它基于 gedit，提供语法高亮、标签页、拼写检查和插件支持。

该编辑器支持多种字符编码，并可在它们之间转换。

# CAVEATS

为 Cinnamon 桌面设计。在其他环境下可能需要 GTK 库。插件需要 Python。

# INSTALL

```dnf: sudo dnf install xed```

```pacman: sudo pacman -S xed```

```zypper: sudo zypper install xed```

```nix: nix profile install nixpkgs#xed```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gedit](/man/gedit)(1), [pluma](/man/pluma)(1), [nano](/man/nano)(1)
