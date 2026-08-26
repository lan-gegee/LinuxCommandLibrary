# TAGLINE

将 Bio-Rad 共聚焦显微镜图像转换为 PGM 格式

# TLDR

**将 Biorad 共聚焦文件转换为** PGM

```bioradtopgm [bioradfile.pic] > [output.pgm]```

**从多图像文件中提取指定图像**

```bioradtopgm -imagenum [0] [bioradfile.pic] > [output.pgm]```

**保留原始强度值**而不进行缩放

```bioradtopgm -truegrayscale [bioradfile.pic] > [output.pgm]```

**从 stdin 读取**并转换为 JPEG

```cat [bioimage.pic] | bioradtopgm | pnmtojpeg > [output.jpg]```

**显示图像信息**而不转换

```bioradtopgm [bioradfile.pic]```

# SYNOPSIS

**bioradtopgm** [**-imagenum** _n_] [**-truegrayscale**] [**-quiet**] [_bioradfile_]

# PARAMETERS

**-imagenum** _n_
> 从多图像文件中选择要提取的图像。图像编号从零开始。

**-truegrayscale**
> 保留原始强度值而不缩放。对要求光度准确性的科学应用非常重要。

**-quiet**
> 抑制标准错误上的提示信息。

# DESCRIPTION

**bioradtopgm** 将 Biorad 共聚焦显微镜图像文件（PIC 格式）转换为 PGM（Portable GrayMap）格式。它是 Netpbm 图像处理工具集的一部分。

如果不提供文件参数，程序会从标准输入读取，输出写入标准输出。对于多图像文件，不带 **-imagenum** 运行会显示文件的尺寸和图像数量等信息。

默认情况下，强度值会被缩放到完整的 0-255 范围以获得更好的视觉对比度。

# CAVEATS

如果输出图像上下颠倒，可通过管道传给 **pamflip -tb** 纠正方向。输出为 PGM 格式；请使用 **pnmtojpeg** 或 **pnmtopng** 等其他 Netpbm 工具转换成常见格式。

# HISTORY

**bioradtopgm** 是 Netpbm 工具集的一部分，开发目的是将专有的 Bio-Rad 共聚焦显微镜数据转换为开放、可交换的格式，服务于科研和医学工作流程。

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

[pamflip](/man/pamflip)(1), [pnmtojpeg](/man/pnmtojpeg)(1), [pnmtopng](/man/pnmtopng)(1), [netpbm](/man/netpbm)(1)
