# TAGLINE

将 Ghostscript 的 pbmraw 或 bitcmyk 格式转换为 QPDL 打印机流

# TLDR

**将 PBM 转换为** QPDL 格式

```foo2qpdl [options] < [input.pbm] > [output.prn]```

**设置分辨率**

```foo2qpdl -r [600] < [input.pbm] > [output.prn]```

**将纸张大小设为 A4**

```foo2qpdl -p 9 < [input.pbm] > [output.prn]```

**彩色模式**

```foo2qpdl -c < [input.ppm] > [output.prn]```

**设置打印份数**

```foo2qpdl -n [3] < [input.pbm] > [output.prn]```

**启用双面打印（长边）**

```foo2qpdl -d 2 < [input.pbm] > [output.prn]```

**指定打印机型号**

```foo2qpdl -z [2] < [input.pbm] > [output.prn]```

# SYNOPSIS

**foo2qpdl** [_options_] < _input_ > _output_

# PARAMETERS

**-r** _xres_**x**_yres_
> 设置分辨率（每英寸像素数）[1200x600]。

**-g** _xpix_**x**_ypix_
> 设置页面尺寸（以像素为单位）[10200x6600]。

**-p** _paper_
> 纸张代码：0=letter，1=legal，2=A5，3=B5，6=folio，7=quarto，8=10x14，9=A4，11=executive，以及各种信封代码。

**-c**
> 强制彩色模式。

**-m** _media_
> 介质类型代码：0=普通纸，1=厚纸，2=薄纸，3=胶版纸，4=彩纸，5=卡片纸，6=标签纸，7=信封，8=预印纸，9=棉纸，19=再生纸，20=归档纸。

**-n** _copies_
> 打印份数 [1]。

**-d** _duplex_
> 双面打印模式：1=关闭，2=长边，3=短边。

**-s** _source_
> 来源（InputSlot）代码：1=自动，2=手动，3=多页，4=tray1。

**-t**
> 草稿模式。隔一个像素输出一个白色像素。

**-z** _model_
> 打印机型号：0=CLP-300/CLX-2160/CLX-3160，1=CLP-600，2=CLP-310/CLP-315/CLP-610/CLX-3175，3=CLP-620。

**-J** _filename_
> 发送给打印机的文件名字符串。

# DESCRIPTION

**foo2qpdl** 将 Ghostscript 的 pbmraw、bitcmyk 或 pksmraw 输出格式转换为单色或彩色 QPDL 流。它支持 Samsung CLP-300、CLX-2160、CLP-600、CLX-3160、CLP-610、CLP-620、CLP-360、CLP-365 以及 Xerox Phaser 6110 打印机。

该工具处理 QPDL 打印机所需的打印机专属编码，管理色彩模式、压缩和页面设置。它通常通过 foo2qpdl-wrapper 脚本调用，后者会自动处理 Ghostscript 转换。

# CAVEATS

仅适用于兼容 QPDL 的打印机。支持的型号各有差异。部分特性可能并非在所有打印机上都可用。

# HISTORY

foo2qpdl 是 **foo2zjs** 的一部分，通过逆向工程驱动支持使用 QPDL 协议的 Samsung 打印机。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

```dnf: sudo dnf install foo2qpdl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2qpdl-wrapper](/man/foo2qpdl-wrapper)(1), [foo2zjs](/man/foo2zjs)(1)
