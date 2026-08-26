# TAGLINE

用于文本处理的反向换行过滤器

# TLDR

从输入中过滤**反向换行**

```command | col```

以**空格**而非制表符输出

```command | col -x```

移除**退格符**，只显示最终字符

```command | col -b```

设置**缓冲区大小**（行数）

```command | col -l 256```

将 **man 手册页**格式化为可查看的文本

```man ls | col -b | less```

# SYNOPSIS

**col** [_options_]

# DESCRIPTION

**col** 从输入文本中过滤反向换行（reverse line feed）和半反向换行（half-reverse line feed），确保输出在无法处理这些控制序列的终端上以正确顺序显示。它是一个文本处理过滤器，用于解决换行冲突并优化空白表示。

该工具特别适合处理 nroff、tbl 以及其他使用反向换行实现下划线和叠印效果的文本格式化命令的输出。默认情况下，col 会将连续空格转换为制表符以提高效率，可用 -x 标志禁用此行为。

col 最初设计用于在行式打印机和简单终端上打印格式化文本，如今仍适用于将 man 手册页输出转换为纯文本、预处理格式化文档以及处理遗留文本格式。它从标准输入读取并将清理后的输出发送到标准输出，非常适合 Unix 管道。

# PARAMETERS

**-b, --no-backspaces**
> 不输出退格符；每个位置只显示最终字符

**-f, --fine**
> 启用半正向换行（通常会被推迟到下一行）

**-h, --tabs**
> 将多个空格转换为制表符

**-l, --lines NUM**
> 将内存缓冲区设置为至少 NUM 行（默认：128）

**-p, --pass**
> 允许未识别的控制序列原样通过

**-x, --spaces**
> 输出多个空格而不是制表符

**-H, --help**
> 显示帮助信息并退出

**-V, --version**
> 显示版本信息并退出

# CAVEATS

默认情况下，所有未识别的控制字符和转义序列都会被丢弃。如果输入试图回退越过最后已输出的行，该工具会发出警告。输入假定采用 UTF-8 编码。

# HISTORY

**col** 属于 **util-linux** 软件包，源自 BSD Unix。它的设计初衷是处理 nroff 的输出，以便在无法处理反向换行的终端上显示。

# INSTALL

```apt: sudo apt install bsdextrautils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nroff](/man/nroff)(1), [tbl](/man/tbl)(1), [colcrt](/man/colcrt)(1), [expand](/man/expand)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man1/col.1.html)```

<!-- verified: 2026-06-22 -->
