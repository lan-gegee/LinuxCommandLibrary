# TAGLINE

PBM 转 HP ZjStream 转换器

# TLDR

**将 PBM 转换为** HP 格式

```foo2hp [options] < [input.pbm] > [output.prn]```

**设置分辨率**

```foo2hp -r [600] < [input.pbm] > [output.prn]```

**设置纸张大小**

```foo2hp -p [letter] < [input.pbm] > [output.prn]```

**彩色模式**

```foo2hp -c < [input.ppm] > [output.prn]```

# SYNOPSIS

**foo2hp** [_options_] < _input_ > _output_

# PARAMETERS

**-r** _DPI_
> 分辨率（300、600、1200）。

**-p** _PAPER_
> 纸张大小（letter、a4、legal）。

**-c**
> 彩色模式（需要 PPM 输入）。

**-m** _MEDIA_
> 介质类型。

**-n** _COPIES_
> 打印份数。

**-d** _DUPLEX_
> 双面打印模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**foo2hp** 将 PBM/PPM 图像转换为某些 HP Color LaserJet 打印机所需的 HP 专有 ZjStream 格式。它让缺乏原生 Linux 驱动的打印机也能打印。

该工具负责栅格到打印机协议的转换，处理页面设置、色彩管理以及 HP 专属编码。它作为 CUPS 过滤器后端工作。

foo2hp 支持 HP Color LaserJet 1600、2600n 及其他使用 ZjStream 协议的类似机型。

# CAVEATS

仅适用于特定 HP 打印机型号。质量取决于输入分辨率。可能不支持全部打印机特性。

# HISTORY

foo2hp 属于 **foo2zjs**——Rick Richardson 的开源驱动集合。它通过逆向工程 HP 的 ZjStream 协议，使基于 GDI 的 HP 打印机获得了 Linux 支持。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2hp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2hp2600-wrapper](/man/foo2hp2600-wrapper)(1), [foo2zjs](/man/foo2zjs)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
