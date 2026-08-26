# TAGLINE

使用 shared-mime-info 数据库确定文件的 MIME 类型

# TLDR

打印给定文件的 **MIME 类型**

```mimetype [path/to/file]```

只显示 MIME 类型，**不显示文件名**

```mimetype --brief [path/to/file]```

显示 MIME 类型的**描述**

```mimetype --describe [path/to/file]```

判断 **stdin** 的 MIME 类型

```[command] | mimetype --stdin```

显示关于 MIME 类型判定方式的**调试信息**

```mimetype --debug [path/to/file]```

按置信度顺序显示**所有可能的 MIME 类型**

```mimetype --all [path/to/file]```

指定输出的**语言代码**

```mimetype --language [path/to/file]```

# SYNOPSIS

**mimetype** [_options_] _files_...

# PARAMETERS

**--brief, -b**
> 只输出 MIME 类型，不带文件名

**--describe, -d**
> 输出 MIME 类型的可读描述

**--stdin, -i**
> 从标准输入而非文件读取数据

**--debug, -D**
> 显示类型检测的调试信息

**--all, -a**
> 列出所有可能的 MIME 类型及其置信度分数

**--language _code_**
> 用两位字母的语言代码设置输出语言

# DESCRIPTION

**mimetype** 使用 shared-mime-info 数据库确定文件的 MIME 类型。它检查文件内容（magic 字节）和文件名模式来识别类型，类似于 **file** 命令，但输出标准 MIME 类型。

该工具是 File::MimeInfo Perl 模块的一部分，使用 freedesktop.org 共享 MIME 数据库。它能检测数千种文件类型，包括文档、图像、音频、视频和特定应用程序格式。

与简单的基于扩展名的检测不同，mimetype 会检查实际文件内容，因此对于扩展名错误或缺失的文件更加可靠。

# CAVEATS

需要安装 shared-mime-info 数据库。检测准确性取决于数据库中 magic 模式的质量和完整性。某些专有格式可能无法识别。

# INSTALL

```pacman: sudo pacman -S perl-file-mimeinfo```

```apk: sudo apk add perl-file-mimeinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[file](/man/file)(1), [xdg-mime](/man/xdg-mime)(1)
