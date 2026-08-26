# TAGLINE

将 SBIG 天文 CCD 图像转换为 PGM

# TLDR

**将 SBIG 图像转换**为 PGM

```sbigtopgm [image.sbig] > [image.pgm]```

在管道中**从标准输入读取**

```cat [image.sbig] | sbigtopgm > [image.pgm]```

**转换并用 pnmnorm 拉伸对比度**

```sbigtopgm [image.sbig] | pnmnorm > [stretched.pgm]```

**转换并编码**为 PNG

```sbigtopgm [image.sbig] | pnmtopng > [image.png]```

# SYNOPSIS

**sbigtopgm** [_sbigfile_]

# DESCRIPTION

**sbigtopgm** 读取 SBIG（Santa Barbara Instrument Group）原生 Type 3 文件格式的天文 CCD 图像，并将像素值以 PGM（portable graymap，可移植灰度图）图像的形式写到标准输出。若未指定文件名，程序将从标准输入读取。

SBIG Type 3 格式由 SBIG ST 系列 CCD 相机附带的 CCDOPS 软件生成。它由一个 ASCII 头部（大小写灵活、行尾符宽容）后接一个 16 位灰度像素数组组成。**sbigtopgm** 保留源数据的完整 16 位精度，因此输出 PGM 的 maxval 与原始 ADU 范围相匹配。它是 **Netpbm** 工具集的一部分。

# CAVEATS

上游 Netpbm 中没有反向转换的 **pgmtosbig**。即使相机报告的精度更低，输出也始终是 16 位。天文领域专用的 FITS 文件应改用 **fitstopnm** 转换。

# HISTORY

**sbigtopgm** 被贡献给 **Netpbm**，用于在 SBIG 自家 CCDOPS 软件不可用的 Unix 系统上支持业余及专业天文工作流程。自加入以来基本没有变化。

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

[fitstopnm](/man/fitstopnm)(1), [pnmtopng](/man/pnmtopng)(1), [pamtopnm](/man/pamtopnm)(1), [pnmnorm](/man/pnmnorm)(1)
