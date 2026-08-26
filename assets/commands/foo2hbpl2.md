# TAGLINE

将 Ghostscript 输出转换为 Dell 和 Xerox 打印机所需的 HBPL2 格式

# TLDR

**将 PBM 转换为 HBPL2**

```foo2hbpl2 [options] < [input.pbm] > [output.hbpl]```

**设置分辨率**

```foo2hbpl2 -r [1200x600] < [input.pbm] > [output.hbpl]```

**将纸张大小设为 letter**

```foo2hbpl2 -p 4 < [input.pbm] > [output.hbpl]```

**打印多份**

```foo2hbpl2 -n [3] < [input.pbm] > [output.hbpl]```

**启用长边装订双面打印**

```foo2hbpl2 -d 2 < [input.pbm] > [output.hbpl]```

**强制彩色模式**

```foo2hbpl2 -c < [input.pbm] > [output.hbpl]```

# SYNOPSIS

**foo2hbpl2** [_options_] < _input_ > _output_

# PARAMETERS

**-c**
> 在自动检测失效时强制彩色模式。

**-d** _duplex_
> 双面打印代码：1=关闭（默认），2=长边，3=短边。

**-g** _xpix_**x**_ypix_
> 页面尺寸（以像素为单位）[10200x6600]。

**-m** _media_
> 介质代码：1=普通纸（默认），2=胶版纸，3=lwcard，4=lwgcard，5=标签纸，6=信封，7=再生纸。

**-n** _copies_
> 打印份数 [1]。

**-p** _paper_
> 纸张代码：1=A4，2=B5jis，3=A5，4=letter，5=executive，6=folio，7=legal，9=env#10，10=envMonarch，11=envC5，12=envDL。

**-r** _xres_**x**_yres_
> 设备分辨率（每英寸像素数）[1200x600]。

**-s** _source_
> 输入纸槽代码：1=上层，2=下层，4=手动，7=自动（默认）。

**-t**
> 草稿模式。隔一个像素输出一个白色像素。

**-J** _filename_
> 发送给打印机的文件名字符串。

**-U** _username_
> 发送给打印机的用户名字符串。

**-u** _xoff_**x**_yoff_
> 可打印区域左上角偏移（像素）[0x0]。

**-l** _xoff_**x**_yoff_
> 可打印区域右下角偏移（像素）[0x0]。

**-L** _mask_
> 逻辑裁剪：0=禁用，1=仅 Y，2=仅 X，3=两者（默认）。

**-A**
> AllIsBlack：将 C=1,M=1,Y=1 转换为 K=1（bitcmyk 输入）。

**-B**
> BlackClears：K=1 时强制 C,M,Y 为 0（bitcmyk 输入）。

**-D** _level_
> 调试详细级别 [0]。

# DESCRIPTION

**foo2hbpl2** 将 Ghostscript 的 pbmraw、bitcmyk 或 pksmraw 输出格式转换为单色或彩色 HBPL 第 2 版流。它支持的打印机包括 Dell 1355、Dell C1765、Epson AcuLaser M1400、富士施乐 DocuPrint CM205/CM215/M215/P205、Xerox Phaser 3010/3040 以及 Xerox WorkCentre 3045/6015。

它是 **foo2zjs** 打印机驱动集合的一部分，作为 CUPS 过滤器后端工作，让原本不受支持的 GDI 打印机得以打印。

# CAVEATS

需要兼容的打印机型号。输入数据必须来自正确栅格格式的 Ghostscript。打印质量取决于输入分辨率。

# HISTORY

foo2hbpl2 是 **foo2zjs** 的一部分，后者是由 Rick Richardson 创建的开源打印机驱动集合，通过逆向工程专有协议在 Linux 上支持 GDI 打印机。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[foo2hbpl2-wrapper](/man/foo2hbpl2-wrapper)(1), [foo2zjs](/man/foo2zjs)(1), [hbpldecode](/man/hbpldecode)(1)
