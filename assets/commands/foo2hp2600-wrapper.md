# TAGLINE

PostScript/PDF 转 HP ZjStream 包装脚本

# TLDR

**打印 PostScript 文件**

```foo2hp2600-wrapper [file.ps]```

**设置纸张大小**

```foo2hp2600-wrapper -p [a4] [file.ps]```

**彩色打印**

```foo2hp2600-wrapper -c [file.ps]```

**设置分辨率**

```foo2hp2600-wrapper -r [600] [file.ps]```

**打印多份**

```foo2hp2600-wrapper -n [3] [file.ps]```

**单色打印**

```foo2hp2600-wrapper [file.ps]```

# SYNOPSIS

**foo2hp2600-wrapper** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要打印的 PostScript 或 PDF 文件。

**-p** _PAPER_
> 纸张大小（letter、a4、legal）。

**-r** _DPI_
> 分辨率（300、600、1200）。

**-c**
> 彩色打印。

**-n** _COPIES_
> 打印份数。

**-m** _MEDIA_
> 介质类型（plain、thick、envelope、transparency）。

**-s** _SOURCE_
> 纸张来源纸槽。

**-2**
> 双面打印。

**--help**
> 显示帮助信息。

# DESCRIPTION

**foo2hp2600-wrapper** 将 PostScript/PDF 文件转换为 HP Color LaserJet 2600n 及类似打印机所需的 HP ZjStream 格式。它封装了 Ghostscript 与 foo2hp 以简化打印。

该脚本处理从输入文档到打印机就绪数据的完整转换流水线。支持彩色和单色模式，以及多种纸张大小和质量设置。

foo2hp2600-wrapper 为受支持的 HP 打印机提供直接的命令行打印能力。

# CAVEATS

需要 Ghostscript。仅适用于受支持的 HP 打印机型号。色彩准确性取决于打印机校准。

# HISTORY

foo2hp2600-wrapper 是 **foo2zjs** 项目的一部分，通过逆向工程协议提供易用的界面，用于在 HP Color LaserJet 打印机上打印文档。

# SEE ALSO

[foo2hp](/man/foo2hp)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1)
