# TAGLINE

PostScript/PDF 转 SLX 包装脚本

# TLDR

**打印 PostScript 文件**

```foo2slx-wrapper [file.ps]```

**设置纸张大小**

```foo2slx-wrapper -p [a4] [file.ps]```

**彩色打印**

```foo2slx-wrapper -c [file.ps]```

**设置分辨率**

```foo2slx-wrapper -r [600] [file.ps]```

# SYNOPSIS

**foo2slx-wrapper** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要打印的 PostScript 或 PDF 文件。

**-p** _PAPER_
> 纸张大小（letter、a4、legal）。

**-r** _DPI_
> 分辨率。

**-c**
> 彩色打印。

**-n** _COPIES_
> 打印份数。

**-m** _MEDIA_
> 介质类型。

**--help**
> 显示帮助信息。

# DESCRIPTION

**foo2slx-wrapper** 将 PostScript/PDF 文档转换为 Lexmark 打印机所需的 SLX 格式。它组合了 Ghostscript 栅格化与 foo2slx 编码。

该包装器处理转换流水线，让打印变得简单。它为受支持的 Lexmark 打印机提供命令行接口。

foo2slx-wrapper 简化了向 SLX 协议打印机打印文档的流程。

# CAVEATS

需要 Ghostscript。仅适用于兼容 SLX 的 Lexmark 型号。特性支持各有差异。

# HISTORY

foo2slx-wrapper 是 **foo2zjs** 驱动集合的一部分，为使用 SLX 协议的 Lexmark 打印机提供便捷的打印方式。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2slx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2slx](/man/foo2slx)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
