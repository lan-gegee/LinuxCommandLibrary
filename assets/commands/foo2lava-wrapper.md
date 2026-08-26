# TAGLINE

PostScript/PDF 转 LAVAFLOW 包装脚本

# TLDR

**打印 PostScript 文件**

```foo2lava-wrapper [file.ps]```

**设置纸张大小**

```foo2lava-wrapper -p [a4] [file.ps]```

**彩色打印**

```foo2lava-wrapper -c [file.ps]```

**打印多份**

```foo2lava-wrapper -n [3] [file.ps]```

# SYNOPSIS

**foo2lava-wrapper** [_options_] [_files_...]

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

**foo2lava-wrapper** 将 PostScript/PDF 文档转换为 Konica Minolta magicolor 打印机所需的 LAVAFLOW 格式。它将 Ghostscript 栅格化与 foo2lava 编码串联起来。

该包装器自动处理格式转换，为打印提供简化接口。它将标准打印选项转换为底层工具所需的参数。

foo2lava-wrapper 支持直接以命令行向受支持的 Konica Minolta 打印机打印文档。

# CAVEATS

需要 Ghostscript。仅限于受支持的打印机型号。彩色输出质量参差不齐。

# HISTORY

foo2lava-wrapper 是 **foo2zjs** 驱动集合的一部分，为使用 LAVAFLOW 协议的 Konica Minolta 打印机提供便捷的文档打印方式。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2lava```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2lava](/man/foo2lava)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
