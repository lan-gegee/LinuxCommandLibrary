# TAGLINE

面向 Lexmark 打印机的 PBM 转 SLX 转换器

# TLDR

**将 PBM 转换为** SLX 格式

```foo2slx [options] < [input.pbm] > [output.prn]```

**设置分辨率**

```foo2slx -r [600] < [input.pbm] > [output.prn]```

**设置纸张大小**

```foo2slx -p [letter] < [input.pbm] > [output.prn]```

**彩色模式**

```foo2slx -c < [input.ppm] > [output.prn]```

# SYNOPSIS

**foo2slx** [_options_] < _input_ > _output_

# PARAMETERS

**-r** _DPI_
> 分辨率。

**-p** _PAPER_
> 纸张大小（letter、a4、legal）。

**-c**
> 彩色模式。

**-m** _MEDIA_
> 介质类型。

**-n** _COPIES_
> 打印份数。

**-d** _DUPLEX_
> 双面打印模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**foo2slx** 将 PBM/PPM 图像转换为 Lexmark C500 及类似打印机所需的 SLX 格式。它以 Lexmark 的 Software Imaging Solutions 协议编码栅格数据。

该工具处理打印机专属的编码、压缩和页面格式化。它作为受支持 Lexmark 打印机的 CUPS 过滤器后端工作。

foo2slx 使使用 SLX 协议的 Lexmark 彩色激光打印机得以在 Linux 上打印。

# CAVEATS

仅适用于兼容 SLX 的 Lexmark 打印机。支持的型号有限。部分特性可能无法工作。

# HISTORY

foo2slx 是 **foo2zjs** 的一部分，通过逆向工程驱动为使用 SLX 协议的 Lexmark 打印机提供 Linux 支持。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2slx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2slx-wrapper](/man/foo2slx-wrapper)(1), [foo2zjs](/man/foo2zjs)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
