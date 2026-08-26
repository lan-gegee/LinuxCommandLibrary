# TAGLINE

将 Ghostscript 的 pbmraw 或 bitcmyk 格式转换为 LAVAFLOW 打印机流

# TLDR

**将 PBM 转换为** LAVAFLOW

```foo2lava [options] < [input.pbm] > [output.prn]```

**设置分辨率**

```foo2lava -r [600] < [input.pbm] > [output.prn]```

**设置纸张大小**

```foo2lava -p [letter] < [input.pbm] > [output.prn]```

**彩色模式**

```foo2lava -c < [input.ppm] > [output.prn]```

# SYNOPSIS

**foo2lava** [_options_] < _input_ > _output_

# PARAMETERS

**-r** _XRESxYRES_
> 设置分辨率（每英寸像素数，默认 1200x600）。

**-g** _XPIXxYPIX_
> 设置页面尺寸（以像素为单位，默认 10200x6600）。

**-p** _PAPER_
> 发送给打印机的纸张代码（letter 默认为 2）。

**-c**
> 强制彩色模式。

**-m** _MEDIA_
> 发送给打印机的介质类型代码（默认 0）。

**-n** _COPIES_
> 打印份数（默认 1）。

**-d** _DUPLEX_
> 双面打印代码（1=关闭，2=长边，3=短边）。

**-s** _SOURCE_
> 来源（InputSlot）代码（默认 255，自动）。

**-t**
> 草稿模式。隔一个像素输出一个白色像素。

**-S** _PLANE_
> 为调试输出单一颜色平面。

# DESCRIPTION

**foo2lava** 将 Ghostscript 的 pbmraw、bitcmyk 或 pksmraw 输出格式转换为 Konica Minolta magicolor 打印机所需的单色或彩色 LAVAFLOW 或 OPL 流。

支持的打印机包括 magicolor 2530 DL、2490 MF 及其他基于 Zenographics 的 LAVAFLOW 打印机。它作为 foo2lava-wrapper CUPS 过滤器的后端工作。

# CAVEATS

仅适用于特定 Konica Minolta 型号。质量取决于输入分辨率。部分特性可能不可用。

# HISTORY

foo2lava 是 **foo2zjs** 的一部分，增加了对使用 LAVAFLOW 协议的 Konica Minolta 打印机的支持，该协议经过逆向工程以实现 Linux 兼容。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2lava```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2lava-wrapper](/man/foo2lava-wrapper)(1), [foo2zjs](/man/foo2zjs)(1)
