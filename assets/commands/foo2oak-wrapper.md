# TAGLINE

PostScript/PDF 转 OAKT 包装脚本

# TLDR

**打印 PostScript 文件**

```foo2oak-wrapper [file.ps]```

**设置纸张大小**

```foo2oak-wrapper -p [a4] [file.ps]```

**以彩色打印**

```foo2oak-wrapper -c [file.ps]```

**设置分辨率**

```foo2oak-wrapper -r [600] [file.ps]```

# SYNOPSIS

**foo2oak-wrapper** [_options_] [_files_...]

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

**foo2oak-wrapper** 将 PostScript/PDF 转换为 OAKT 格式，用于在采用 Oak Technology 控制器的 HP 和 Kyocera 打印机上打印。它组合了 Ghostscript 与 foo2oak。

该包装器处理从文档到打印机数据的完整转换过程，为常见打印任务提供简单接口。

foo2oak-wrapper 支持以命令行向 OAKT 协议打印机打印文档。

# CAVEATS

需要 Ghostscript。仅适用于兼容 OAKT 的打印机。部分特性因打印机而异。

# HISTORY

foo2oak-wrapper 是 **foo2zjs** 驱动集合的一部分，简化了向使用 Oak Technology 的 OAKT 协议打印机的打印流程。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2oak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2oak](/man/foo2oak)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
