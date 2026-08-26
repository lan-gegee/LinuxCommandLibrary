# TAGLINE

面向 HP LaserJet 打印机的 PBM 转 XQX 转换器

# TLDR

**将 PBM 转换为** XQX 格式

```foo2xqx [options] < [input.pbm] > [output.prn]```

**设置分辨率**

```foo2xqx -r [600] < [input.pbm] > [output.prn]```

**设置纸张大小**

```foo2xqx -p [letter] < [input.pbm] > [output.prn]```

# SYNOPSIS

**foo2xqx** [_options_] < _input_ > _output_

# PARAMETERS

**-r** _DPI_
> 分辨率（300、600、1200）。

**-p** _PAPER_
> 纸张大小（letter、a4、legal）。

**-m** _MEDIA_
> 介质类型。

**-n** _COPIES_
> 打印份数。

**-d** _DUPLEX_
> 双面打印模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**foo2xqx** 将 PBM 图像转换为 HP LaserJet 及兼容打印机所需的 XQX 格式。它为使用 HP 的 XQX 协议的打印机编码栅格数据。

该工具处理单色打印所需的打印机专属编码与压缩。它作为受支持 HP 打印机的 CUPS 过滤器后端工作。

foo2xqx 使某些使用 XQX 的 HP LaserJet 型号得以在 Linux 上打印。

# CAVEATS

仅支持单色。仅限于兼容 XQX 的打印机。支持的型号各有差异。

# HISTORY

foo2xqx 是 **foo2zjs** 的一部分，增加了对使用 XQX 协议的 HP 打印机的支持，该协议经过逆向工程以实现 Linux 兼容。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2xqx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2xqx-wrapper](/man/foo2xqx-wrapper)(1), [foo2zjs](/man/foo2zjs)(1)

# RESOURCES

```[Source code](https://github.com/OpenPrinting/foo2zjs)```

<!-- verified: 2026-07-15 -->
