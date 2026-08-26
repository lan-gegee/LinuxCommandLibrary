# TAGLINE

通用 groff 文档查看器

# TLDR

**查看 man page**

```groffer [man-page]```

**在 X 窗口中查看文件**

```groffer --x [file.roff]```

**以 PDF 查看**

```groffer --pdf [file.roff]```

**以文本方式在终端查看**

```groffer --tty [file.roff]```

**指定查看器**

```groffer --viewer [evince] [file.roff]```

# SYNOPSIS

**groffer** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要显示的文件或 man page。

**--pdf**
> 以 PDF 输出。

**--ps**
> 以 PostScript 输出。

**--tty**
> 输出到终端。

**--x**
> 在 X 窗口中显示。

**--viewer** _PROG_
> 指定查看器程序。

**--mode** _MODE_
> 显示模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**groffer** 是 groff 的一个封装工具，能为文档自动选择最佳的显示方式。它可以处理 man page、roff 文件以及各种输入格式。

该工具会检测环境，并在 X 查看器、PDF 查看器或终端显示之间做出选择，显著简化了 groff 的使用流程。

# CAVEATS

属于 groff 软件包。查看器的选择取决于已安装的应用程序。某些模式需要 X 显示服务。

# HISTORY

groffer 作为 **GNU groff** 的一部分开发，旨在为查看 groff 文档提供友好的界面。

# SEE ALSO

[groff](/man/groff)(1), [man](/man/man)(1), [xpdf](/man/xpdf)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/groff.git)```

```[Homepage](https://www.gnu.org/software/groff/)```

<!-- verified: 2026-07-17 -->
