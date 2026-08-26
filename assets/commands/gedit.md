# TAGLINE

GNOME 桌面环境的文本编辑器

# TLDR

**打开**文本文件

```gedit [path/to/file]```

打开**多个**文本文件

```gedit [file1] [file2] ...```

以**指定编码**打开文本文件

```gedit --encoding UTF-8 [path/to/file]```

显示**支持的编码**列表

```gedit --list-encodings```

# SYNOPSIS

**gedit** [_options_] [_file_...]

# PARAMETERS

**--encoding** _ENCODING_
> 设置打开文件时使用的字符编码

**--list-encodings**
> 显示支持的字符编码列表

**-s**, **--standalone**
> 以独立模式运行 gedit（单独进程）

**-w**, **--wait**
> 打开文件并等待其关闭后再返回

**--new-window**
> 创建新的顶层窗口

**--new-document**
> 在已有实例中创建新文档

**+LINE**
> 在指定行号打开文件

**+LINE:COLUMN**
> 在指定行和列打开文件

# CONFIGURATION

**~/.config/gedit/gedit.ini**
> 用户偏好设置，包括编辑器设置、颜色和已启用的插件。

# DESCRIPTION

**gedit** 是 GNOME 桌面环境的默认文本编辑器。它提供简洁的界面来编辑文本文件，具备编程语言语法高亮、拼写检查、查找替换以及插件支持等特性。

gedit 支持多文件标签页编辑、自动文件备份、可配置的字体和颜色，并与 GNOME 的文件管理器集成。它可以处理多种字符编码和换行符格式。

插件可以扩展功能，例如代码片段、括号匹配、文件浏览器面板和外部工具集成。

# CAVEATS

作为 GTK 应用，在 GNOME 环境未完全加载时 gedit 启动可能较慢。超大文件可能影响性能。插件生态的质量和维护状况参差不齐。

# HISTORY

gedit 创建于 **1998 年**，是 GNOME 项目的一部分。它按照 GNOME 人机界面指南设计成一个简单而功能完备的文本编辑器。该编辑器历经多个 GNOME 版本演进，始终保持对简洁性和易用性的专注。

# INSTALL

```apt: sudo apt install gedit```

```dnf: sudo dnf install gedit```

```pacman: sudo pacman -S gedit```

```apk: sudo apk add gedit```

```zypper: sudo zypper install gedit```

```brew: brew install gedit```

```nix: nix profile install nixpkgs#gedit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nano](/man/nano)(1), [vim](/man/vim)(1), [kate](/man/kate)(1)
