# TAGLINE

PostScript/PDF 转 HBPL2 包装脚本

# TLDR

**打印 PostScript 文件**

```foo2hbpl2-wrapper [file.ps]```

**设置纸张大小**

```foo2hbpl2-wrapper -p [a4] [file.ps]```

**打印多份**

```foo2hbpl2-wrapper -n [3] [file.ps]```

**设置分辨率**

```foo2hbpl2-wrapper -r [600] [file.ps]```

# SYNOPSIS

**foo2hbpl2-wrapper** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要打印的 PostScript 或 PDF 文件。

**-p** _PAPER_
> 纸张大小（letter、a4、legal）。

**-r** _DPI_
> 分辨率（300、600、1200）。

**-n** _COPIES_
> 打印份数。

**-m** _MEDIA_
> 介质类型。

**-d** _DUPLEX_
> 双面打印模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**foo2hbpl2-wrapper** 是一个包装脚本，用于将 PostScript/PDF 转换为 HBPL2 格式以便打印。它将 Ghostscript 栅格化与 foo2hbpl2 编码串联起来。

该包装器自动处理转换流水线，简化了打印操作。它接受常见的打印选项并将其传递给底层工具。

foo2hbpl2-wrapper 为 foo2hbpl2 转换过程提供了易用的接口。

# CAVEATS

需要已安装 Ghostscript。彩色输出取决于打印机支持。部分选项因打印机而异。

# HISTORY

foo2hbpl2-wrapper 是 **foo2zjs** 驱动集合的一部分，为 foo2hbpl2 转换器支持的 HBPL2 协议打印机提供便捷的命令行打印方式。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2hbpl2](/man/foo2hbpl2)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
