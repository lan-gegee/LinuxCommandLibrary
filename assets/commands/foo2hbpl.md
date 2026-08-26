# TAGLINE

面向 Dell 和 Xerox 打印机的 pbmraw 转 HBPL2 转换器

# TLDR

**将 pbmraw 转换为 HBPL2** 流以供打印

```gs -q -dBATCH -dNOPAUSE -sDEVICE=pbmraw -sOutputFile=- [file.ps] | foo2hbpl2 > [output.hbpl]```

**使用包装脚本**直接转换 PostScript

```foo2hbpl2-wrapper [file.ps] > [output.prn]```

以指定分辨率**转换**

```foo2hbpl2 -r[1200x600] < [input.pbm] > [output.hbpl]```

使用 bitcmyk 输入**打印彩色文档**

```gs -sDEVICE=bitcmyk -sOutputFile=- [file.ps] | foo2hbpl2 -c > [output.hbpl]```

以像素为单位**设置页面尺寸**

```foo2hbpl2 -p[10200x6600] < [input.pbm] > [output.hbpl]```

# SYNOPSIS

**foo2hbpl2** [_OPTIONS_] < _PBMFILE_ > _HBPL2FILE_

**foo2hbpl2-wrapper** [_OPTIONS_] [_PS-FILE_]

# PARAMETERS

**-c**
> 强制彩色模式输出。

**-r** _XRESxYRES_
> 设置设备分辨率（每英寸像素数，默认：1200x600）。

**-p** _WIDTHxHEIGHT_
> 以像素为单位设置页面尺寸。

**-n** _COPIES_
> 打印份数（默认：1）。

**-d** _DUPLEX_
> 发送给打印机的双面打印代码。

**-u** _XOFFxYOFF_
> 以像素为单位设置可打印区域距左上角的偏移。

**-A**
> AllIsBlack：将 C=1,M=1,Y=1 转换为 K=1（仅限 bitcmyk 输入）。

**-B**
> BlackClears：K=1 时强制 C,M,Y 为 0（仅限 bitcmyk 输入）。

**-D** _LEVEL_
> 设置调试级别。

# DESCRIPTION

**foo2hbpl2** 将 Ghostscript 的 pbmraw、bitcmyk 或 pksmraw 输出转换为某些激光打印机所需的 HBPL2（HP Bi-directional Printer Language 2）流。支持的打印机包括 Dell 1355、Dell C1765、Epson AcuLaser M1400、富士施乐 DocuPrint 系列、Xerox Phaser 3010/3040 以及 Xerox WorkCentre 3045/6015 多功能一体机。

该工具通常与 Ghostscript 一起在管道中使用，将 PostScript 或 PDF 文件转换为打印机就绪格式。**foo2hbpl2-wrapper** 脚本提供便捷的接口，自动处理 Ghostscript 转换。

foo2hbpl2 是 **foo2zjs** 项目的一部分，该项目为多种使用专有页面描述语言的激光打印机提供开源驱动。

# CAVEATS

PostScript/PDF 处理需要 Ghostscript。只适用于使用 HBPL2 协议的特定打印机型号。该驱动绕过标准 CUPS/PPD 机制，因此打印机专属设置可能需要手动配置。

# HISTORY

foo2hbpl2 属于由 Rick Richardson 发起的 **foo2zjs** 项目。该项目为缺乏原生 Linux 支持的打印机提供开源驱动，逆向工程了 ZjStream、HBPL 等专有协议。自 2000 年代初以来，foo2zjs 家族使众多平价激光打印机得以在 Linux 上打印。

# INSTALL

```dnf: sudo dnf install foo2hbpl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gs](/man/gs)(1), [foo2zjs](/man/foo2zjs)(1), [cups](/man/cups)(8), [lpr](/man/lpr)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
