# TAGLINE

PostScript/PDF 转 QPDL 包装脚本

# TLDR

**打印 PostScript 文件**

```foo2qpdl-wrapper [file.ps]```

**设置纸张大小**

```foo2qpdl-wrapper -p [a4] [file.ps]```

**彩色打印**

```foo2qpdl-wrapper -c [file.ps]```

**打印多份**

```foo2qpdl-wrapper -n [3] [file.ps]```

# SYNOPSIS

**foo2qpdl-wrapper** [_options_] [_files_...]

# PARAMETERS

_FILES_
> 要打印的 PostScript 或 PDF 文件。

**-p** _PAPER_
> 纸张大小（letter、legal、a4、a5、a6、b5 等）。

**-r** _XRESxYRES_
> 分辨率（每英寸像素数，默认 1200x600）。

**-c**
> 以彩色打印（默认为单色）。

**-n** _COPIES_
> 打印份数（默认 1）。

**-m** _MEDIA_
> 介质类型代码（0=普通纸，1=厚纸，2=薄纸，3=胶版纸，4=彩纸，5=卡片纸，6=标签纸，7=信封）。

**-s** _SOURCE_
> 输入纸槽（1=自动，2=手动，3=多页，4=tray1；默认 255）。

**-d** _DUPLEX_
> 双面打印模式（1=关闭，2=长边，3=短边；默认 1）。

**-t**
> 草稿模式。隔一个像素输出一个白色像素。

**-z** _MODEL_
> 打印机型号（0=CLP-300，1=CLP-600，2=CLP-310，3=CLP-620）。

**-D** _LEVEL_
> 设置调试级别（默认 0）。

**-g** _GSOPTS_
> 传给 Ghostscript 的额外选项。

# DESCRIPTION

**foo2qpdl-wrapper** 将 PostScript/PDF 文档转换为 Samsung 和 Xerox 激光打印机所需的 QPDL 格式。它将 Ghostscript 栅格化与 foo2qpdl 编码串联起来。

该包装器提供简化的打印接口，自动处理转换流水线。它将常见打印选项转换为底层工具所需的参数。

foo2qpdl-wrapper 支持以命令行向 QPDL 协议打印机打印文档。

# CAVEATS

需要 Ghostscript。仅适用于兼容 QPDL 的打印机。色彩质量因型号而异。

# HISTORY

foo2qpdl-wrapper 是 **foo2zjs** 驱动集合的一部分，简化了向使用 QPDL 协议的 Samsung 打印机打印文档的流程。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2qpdl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2qpdl](/man/foo2qpdl)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1)
