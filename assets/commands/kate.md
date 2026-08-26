# TAGLINE

KDE 高级文本编辑器，功能丰富的带语法高亮文本编辑器

# TLDR

**在 Kate 中打开文件**

```kate [file]```

**在指定行打开文件**

```kate -l [25] [file]```

**在指定行和列打开文件**

```kate -l [25] -c [15] [file]```

**以指定会话启动**

```kate -s [sessionname]```

**从 stdin 打开**

```cat [file] | kate -i```

**阻塞直到编辑器关闭**

```kate -b [file]```

# SYNOPSIS

**kate** [_options_] [_file_...]

# PARAMETERS

**-l**, **--line** _line_
> 跳转到指定行号。

**-c**, **--column** _column_
> 跳转到指定列号。

**-s**, **--start** _name_
> 以给定会话启动。

**-n**, **--new**
> 强制启动新的 Kate 实例。

**-b**, **--block**
> 阻塞直到编辑器退出。

**-i**, **--stdin**
> 从 stdin 读取文档。

**-e**, **--encoding** _name_
> 设置文件编码。

**--tempfile**
> 关闭后删除文件。

# DESCRIPTION

**kate** 即 KDE Advanced Text Editor，是一个功能丰富的文本编辑器，具有语法高亮、代码折叠、终端集成和多文档支持。适合需要高级编辑功能的程序员和高级用户。

# INSTALL

```apt: sudo apt install kate```

```dnf: sudo dnf install kate```

```pacman: sudo pacman -S kate```

```apk: sudo apk add kate```

```zypper: sudo zypper install kate```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kwrite](/man/kwrite)(1), [nano](/man/nano)(1), [vim](/man/vim)(1)
