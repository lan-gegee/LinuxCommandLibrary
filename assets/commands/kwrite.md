# TAGLINE

来自 KDE 项目的简易文本编辑器

# TLDR

**打开**文本文件

```kwrite [path/to/file]```

打开**多个**文件

```kwrite [file1] [file2]```

以指定的**编码**打开

```kwrite --encoding [UTF-8] [path/to/file]```

打开并定位到指定的**行和列**

```kwrite --line [line_number] --column [column_number] [path/to/file]```

# SYNOPSIS

**kwrite** [_options_] [_file_...]

# PARAMETERS

**--encoding** _ENCODING_
> 以指定的字符编码打开文件

**--line** _LINE_
> 定位到指定的行号

**--column** _COLUMN_
> 定位到指定的列号

**--stdin**
> 从 stdin 读取文档

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

**kwrite** 是 KDE 项目推出的简易文本编辑器。它为众多编程语言提供语法高亮和代码折叠，并与 KDE 服务集成。

KWrite 与 Kate 共用同一个编辑器组件（KTextEditor），因此在不需要完整 IDE 功能时，可以作为轻量的单文档替代选择。

# CAVEATS

需要 KDE Frameworks 库。仅支持单文档编辑；如需多文档和会话功能，请改用 **kate**。包含在 KDE Applications 软件包中。

# HISTORY

KWrite 自 KDE 早期版本起便一直是其组成部分，为 KDE 桌面环境提供了一个简单而实用的文本编辑器。

# INSTALL

```apt: sudo apt install kwrite```

```dnf: sudo dnf install kwrite```

```apk: sudo apk add kwrite```

```zypper: sudo zypper install kwrite```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kate](/man/kate)(1), [gedit](/man/gedit)(1), [nano](/man/nano)(1)
