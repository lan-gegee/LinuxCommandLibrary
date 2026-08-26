# TAGLINE

Minolta PagePro 打印机驱动

# TLDR

**打印文件**

```min12xxw [file.prn]```

**设置分辨率**

```min12xxw -r [600] [file.prn]```

**设置纸张大小**

```min12xxw -p [a4] [file.prn]```

**详细输出**

```min12xxw -v [file.prn]```

# SYNOPSIS

**min12xxw** [_options_] [_file_]

# PARAMETERS

_FILE_
> PostScript 或已预转换的输入文件。若省略，则从 stdin 读取。

**-r** _DPI_
> 分辨率：300、600 或 1200 dpi（默认 600）。

**-p** _SIZE_
> 纸张大小：a4、letter、legal、executive、com10、monarch、dl、c5。

**-m**
> 使用最高密度（更深）打印模式。

**-e**
> 使用经济（省碳粉）模式。

**-t**
> 厚纸模式。

**-c** _N_
> 打印份数。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**min12xxw** 是面向 Minolta PagePro 12xxW 基于主机激光打印机系列（PagePro 1200W、1250W、1300W、1350W、1400W 等）的 CUPS 过滤器和独立转换器。这些打印机使用专有的基于主机的协议，而非 PCL 或 PostScript；min12xxw 从输入数据生成打印机所期望的二进制流。

它通常由 CUPS 通过附带的 PPD 文件自动调用，但也可以独立使用，将打印作业转换为原始打印机数据。

# CAVEATS

仅支持 PagePro 12xxW/13xxW/14xxW 系列。打印机必须能作为原始设备访问，生成的数据流才能正确打印。更高的分辨率需要打印机具备更多内存。

# HISTORY

**min12xxw** 由 **Manuel Tobias Schiller** 编写，在 Debian 及其他发行版中打包为 Minolta 基于主机的 PagePro 激光打印机的 Linux 驱动——这些打印机没有内置 PostScript 或 PCL 解释器。

# INSTALL

```apt: sudo apt install printer-driver-min12xxw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpr](/man/lpr)(1), [cups](/man/cups)(1), [cupsd](/man/cupsd)(8)
