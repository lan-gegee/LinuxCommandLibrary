# TAGLINE

MATE 桌面文本编辑器

# TLDR

**启动**编辑器

```pluma```

**打开**指定文件

```pluma [file1] [file2]```

以指定**编码**打开

```pluma --encoding [WINDOWS-1252] [file]```

列出受支持的**编码**

```pluma --list-encodings```

打开并跳转到**行号**

```pluma +[10] [file]```

# SYNOPSIS

**pluma** [**--encoding** _encoding_] [**+**_line_] [_files_...]

# PARAMETERS

**--encoding _encoding_**
> 要使用的字符编码

**--list-encodings**
> 列出所有受支持的编码

**+_line_**
> 在指定行号打开文件

**--new-window**
> 在新窗口中打开

**--new-document**
> 在现有窗口中打开新文档

# DESCRIPTION

**pluma** 是 MATE 桌面环境的默认文本编辑器。它是 gedit 2 的分支版本，提供了一个简洁而功能完备的编辑器，适合编程和文本编辑。

该编辑器支持语法高亮、插件、多文档标签页和外部工具集成。它在保持易用性的同时不失强大功能。

# CAVEATS

需要 GTK+ 库。插件系统可以扩展功能。部分 gedit 2 插件兼容。某些文件的编码检测可能失败。

# HISTORY

**pluma** 作为 **MATE** 桌面项目的一部分而创建。该项目是在 GNOME 3 发布时对 GNOME 2 组件进行分支的结果。其名字来源于拉丁语/葡萄牙语的"羽毛"（笔）。

# INSTALL

```apt: sudo apt install pluma```

```dnf: sudo dnf install pluma```

```pacman: sudo pacman -S pluma```

```apk: sudo apk add pluma```

```zypper: sudo zypper install pluma```

```nix: nix profile install nixpkgs#pluma```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gedit](/man/gedit)(1), [nano](/man/nano)(1), [vim](/man/vim)(1)
