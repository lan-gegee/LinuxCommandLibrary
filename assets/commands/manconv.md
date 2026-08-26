# TAGLINE

转换 man page 的字符编码

# TLDR

**将编码从** ISO-8859-1 转换为 UTF-8

```manconv -f [ISO-8859-1] -t [UTF-8] < [input] > [output]```

**依次尝试多种输入**编码

```manconv -f [ISO-8859-1:UTF-8] -t [UTF-8] [input.man]```

**转换 man page** 并使用安静模式

```manconv -q -f [latin1] -t [utf-8] [oldpage.1] > [newpage.1]```

# SYNOPSIS

**manconv** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入文件。

**-f** _ENCODINGS_, **--from-code** _ENCODINGS_
> 源编码（冒号分隔的列表，按顺序尝试）。

**-t** _ENCODING_, **--to-code** _ENCODING_
> 目标编码。

**-q**, **--quiet**
> 无法转换手册页时抑制错误信息。

**-d**, **--debug**
> 打印调试信息。

**-V**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**manconv** 将手册页从一种编码转换为另一种编码，类似于 iconv。与 iconv 不同的是，它可以依次尝试多个可能的输入编码。这对于安装在未显式声明编码的目录中的手册页非常有用，因为它们可能是 UTF-8，也可能是旧式字符集。

如果手册页第一行存在编码声明，该声明将覆盖命令行上指定的任何输入编码。该工具属于 **man-db**。

# CAVEATS

如果文件中存在编码声明，它将覆盖 -f 选项。属于 man-db 的一部分；主要针对 man page 设计，不适合一般文本转换。

# HISTORY

manconv 是 **man-db** 的一部分，负责手册页的编码转换。

# SEE ALSO

[man](/man/man)(1), [iconv](/man/iconv)(1), [groff](/man/groff)(1)
