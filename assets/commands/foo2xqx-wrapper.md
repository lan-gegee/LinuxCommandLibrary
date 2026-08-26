# TAGLINE

PostScript/PDF 转 XQX 包装脚本

# TLDR

**打印 PostScript 文件**

```foo2xqx-wrapper [file.ps]```

**设置纸张大小**

```foo2xqx-wrapper -p [a4] [file.ps]```

**设置分辨率**

```foo2xqx-wrapper -r [600] [file.ps]```

**打印多份**

```foo2xqx-wrapper -n [3] [file.ps]```

# SYNOPSIS

**foo2xqx-wrapper** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要打印的 PostScript 或 PDF 文件。

**-p** _PAPER_
> 纸张大小（letter、a4、legal）。

**-r** _DPI_
> 分辨率。

**-n** _COPIES_
> 打印份数。

**-m** _MEDIA_
> 介质类型。

**--help**
> 显示帮助信息。

# DESCRIPTION

**foo2xqx-wrapper** 将 PostScript/PDF 文档转换为 HP LaserJet 打印机所需的 XQX 格式。它将 Ghostscript 栅格化与 foo2xqx 编码串联起来。

该包装器自动处理转换流水线，简化打印操作。它将标准打印选项转换为底层工具所需的参数。

foo2xqx-wrapper 支持以命令行向使用 XQX 协议的 HP 打印机打印文档。

# CAVEATS

需要 Ghostscript。仅支持单色。仅限于兼容 XQX 的 HP 型号。

# HISTORY

foo2xqx-wrapper 是 **foo2zjs** 驱动集合的一部分，为使用 XQX 协议的 HP 打印机提供文档打印能力。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2xqx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2xqx](/man/foo2xqx)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
