# TAGLINE

将 PNM 图像转换为 HP PPA 打印机格式

# TLDR

**将彩色 PNM 转换为 PPA 格式**

```pnm2ppa --eco -i [input.pnm] -o [output.ppa]```

**将 PNM 文件直接送到打印机打印**

```pnm2ppa -i [image.pnm] -o - | lpr```

**以指定纸张尺寸转换**

```pnm2ppa --paper [a4] -i [input.pnm] -o [output.ppa]```

**转换黑白 PNM**

```pbm2ppa -i [input.pbm] -o [output.ppa]```

# SYNOPSIS

**pnm2ppa** [_options_] [**-i** _infile_] [**-o** _outfile_]

# PARAMETERS

**-i** _FILE_
> 输入的 PNM 文件（用 - 表示标准输入）。

**-o** _FILE_
> 输出的 PPA 文件（用 - 表示标准输出）。

**--paper** _SIZE_
> 纸张尺寸（letter、a4、legal）。

**--dpi** _DPI_
> 分辨率（300 或 600）。

**--eco**
> 经济模式：节省墨水。

**--bw**
> 仅以黑白方式打印。

**-v** _PRINTER_
> 打印机型号（710、720、820、1000）。

**--gamma** _VALUE_
> 用于色彩调整的 Gamma 校正值。

**-f** _FILE_
> 从文件读取配置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**pnm2ppa** 将 PNM（Portable Any Map）图像转换为某些 HP DeskJet 喷墨打印机（710、720、820、1000 系列）所使用的 HP PPA（Printer Performance Architecture）格式。这些打印机缺少对标准 PCL 或 PostScript 的支持，需要基于主机的驱动程序来渲染页面。

该工具生成的是原始打印机数据流，可以直接发送到打印机设备，也可以经管道交给打印假脱机程序处理。它通常用于 GhostScript 流水线中：先用 GhostScript 把 PostScript 或 PDF 文件渲染成 PNM 格式，再由 pnm2ppa 转换为 PPA。配套工具 **pbm2ppa** 负责处理黑白的 PBM 图像。纸张尺寸、分辨率和经济模式等选项控制输出的版面格式。

# CAVEATS

只适用于特定的 HP DeskJet PPA 打印机。已被视为遗留技术；大多数现代打印机都使用标准驱动。仅支持 300 和 600 DPI 分辨率。

# HISTORY

pnm2ppa 是为缺乏标准驱动支持的 **HP PPA 打印机**而创建的。

# INSTALL

```apt: sudo apt install printer-driver-pnm2ppa```

```dnf: sudo dnf install pnm2ppa```

```zypper: sudo zypper install pnm2ppa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pnm](/man/pnm)(5), [pbmtoppa](/man/pbmtoppa)(1), [gs](/man/gs)(1), [lpr](/man/lpr)(1), [lpstat](/man/lpstat)(1)
