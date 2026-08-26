# TAGLINE

面向 HP 和 Minolta 打印机的 PBM 转 ZjStream 转换器

# TLDR

**将 PBM 转换为** ZjStream 格式

```foo2zjs [options] < [input.pbm] > [output.prn]```

**设置分辨率**

```foo2zjs -r [600] < [input.pbm] > [output.prn]```

**设置纸张大小（1=letter，9=A4，5=legal）**

```foo2zjs -p [9] < [input.pbm] > [output.prn]```

**彩色模式**

```foo2zjs -c < [input.ppm] > [output.prn]```

**打印多份**

```foo2zjs -n [3] < [input.pbm] > [output.prn]```

# SYNOPSIS

**foo2zjs** [_options_] < _input_ > _output_

# PARAMETERS

**-r** _DPI_
> 分辨率（300、600、1200）。

**-p** _CODE_
> 纸张大小代码：1=letter，5=legal，7=executive，9=A4，11=A5，13=B5。默认为 1。

**-c**
> 彩色模式（输入必须是 PPM）。

**-m** _MEDIA_
> 介质类型代码。

**-n** _COPIES_
> 打印份数。

**-d** _DUPLEX_
> 双面打印模式：1=关闭，2=长边，3=短边。

**-g** _XPIXxYPIX_
> 页面尺寸（以像素为单位，默认 10200x6600）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**foo2zjs** 将 PBM/PPM 图像转换为 HP LaserJet 和 Minolta/QMS magicolor 打印机所需的 ZjStream 格式。它是 foo2zjs 打印机驱动套件的核心工具。

该工具以专有的 ZjStream 协议编码栅格数据，处理页面设置、压缩和打印机命令。它作为受支持打印机的 CUPS 过滤器工作。

foo2zjs 使众多缺乏标准驱动支持的"GDI 打印机"得以在 Linux 上打印。

# CAVEATS

仅适用于兼容 ZjStream 的打印机。支持的型号各有差异。使用前请确认兼容性。

# HISTORY

foo2zjs 由 **Rick Richardson** 创建，旨在为"仅限 Windows"的 GDI 打印机提供 Linux 驱动。该项目逆向工程了多个专有协议，使许多消费级激光打印机获得了 Linux 支持。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2zjs```

```nix: nix profile install nixpkgs#foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2zjs-wrapper](/man/foo2zjs-wrapper)(1), [foo2hp](/man/foo2hp)(1), [foo2lava](/man/foo2lava)(1)
