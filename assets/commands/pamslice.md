# TAGLINE

从 Netpbm 图像中提取单行或单列并以文本形式输出

# TLDR

**提取图像的水平切片**（行）

```pamslice -row=[100] [input.pam]```

**提取图像的垂直切片**（列）

```pamslice -column=[50] [input.pam]```

**只提取红色平面**（平面 0）的内容

```pamslice -row=[100] -plane=[0] [input.ppm]```

**将输出格式化为 xmgr 绘图格式**

```pamslice -row=[100] -xmgr [input.pam]```

# SYNOPSIS

**pamslice** {**-row**=_rownumber_ | **-column**=_columnnumber_} [**-plane**=_planenumber_] [**-xmgr**] [_imagefile_]

# PARAMETERS

_IMAGEFILE_
> 输入的 PAM、PBM、PGM 或 PPM 图像文件。省略时从标准输入读取。

**-row**=_N_
> 将第 N 行提取为水平切片。行号自顶部开始，从 0 起算。

**-column**=_N_
> 将第 N 列提取为垂直切片。列号自左侧开始，从 0 起算。

**-plane**=_N_
> 将输出限制为单一颜色平面。对于 PPM 图像：0 为红、1 为绿、2 为蓝。省略时输出所有平面。

**-xmgr**
> 通过添加头信息，将输出格式化为 xmgr 绘图程序的输入。

# DESCRIPTION

**pamslice** 从 Netpbm 图像中提取一行像素（某一行或某一列），并将采样值以 ASCII 十进制数字打印。每行输出的第一个数字是位置索引（行切片对应列号，列切片对应行号），其后是各平面的采样值。

这可用于从图像生成剖面数据，例如为进行图像分析而沿扫描线绘制强度值。使用 **-xmgr** 选项时，输出可以直接馈入 xmgr 等绘图工具。

**-row** 和 **-column** 必须指定其中一个，但不能同时指定。

# CAVEATS

属于 Netpbm。输出只是纯文本，不是图像。行号和列号均从 0 开始。

# HISTORY

pamslice 是用于图像操作与分析的 **Netpbm** 工具集的一部分。它作为从图像中提取剖面数据的工具而加入。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pamcut](/man/pamcut)(1), [pamfile](/man/pamfile)(1), [pamtopnm](/man/pamtopnm)(1), [netpbm](/man/netpbm)(1)
