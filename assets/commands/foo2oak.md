# TAGLINE

面向 Oak Technology 打印机的 PBM 转 OAKT 转换器

# TLDR

**将 PBM 转换为** OAKT 格式

```foo2oak [options] < [input.pbm] > [output.prn]```

**设置分辨率**

```foo2oak -r [600] < [input.pbm] > [output.prn]```

**设置纸张大小**

```foo2oak -p [letter] < [input.pbm] > [output.prn]```

**彩色模式**

```foo2oak -c < [input.ppm] > [output.prn]```

# SYNOPSIS

**foo2oak** [_options_] < _input_ > _output_

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

**foo2oak** 将 PBM/PPM 图像转换为某些 HP 和 Kyocera 打印机所需的 OAKT 协议。它为使用 Oak Technology 芯片的打印机编码栅格数据。

该工具处理这些打印机所需的专有 OAKT 编码，负责页面设置和色彩转换。它作为 CUPS 过滤器后端工作。

foo2oak 支持 HP LaserJet 1000 及其他使用 Oak Technology 控制器的类似机型。

# CAVEATS

仅适用于配备 Oak Technology 芯片组的打印机。支持的打印机型号各有差异。并非所有特性都可用。

# HISTORY

foo2oak 是 **foo2zjs** 的一部分，通过逆向工程驱动支持使用 Oak Technology 的 OAKT 协议的打印机。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2oak```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2oak-wrapper](/man/foo2oak-wrapper)(1), [foo2zjs](/man/foo2zjs)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
