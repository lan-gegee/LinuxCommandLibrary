# TAGLINE

将 PGM 灰度图像转换为 PBM 位图

# TLDR

**使用默认的 Floyd-Steinberg 抖动将灰度图转换为位图**

```pgmtopbm [input.pgm] > [output.pbm]```

**显式指定 Floyd-Steinberg 抖动进行转换**

```pgmtopbm -fs [input.pgm] > [output.pbm]```

**使用简单阈值转换**

```pgmtopbm -threshold -value [0.5] [input.pgm] > [output.pbm]```

**使用聚簇抖动转换**

```pgmtopbm -cluster3 [input.pgm] > [output.pbm]```

# SYNOPSIS

**pgmtopbm** [**-floyd** | **-fs** | **-threshold** | **-hilbert** | **-dither8** | **-d8** | **-cluster3** | **-c3** | **-cluster4** | **-c4** | **-cluster8** | **-c8**] [**-value** _val_] [**-clump** _size_] [**-randomseed** _integer_] [_pgmfile_]

# PARAMETERS

**-floyd**, **-fs**
> Floyd-Steinberg 抖动（默认）。

**-threshold**
> 简单阈值转换。高于阈值的像素变为白色，低于阈值的变为黑色。

**-value** _val_
> 介于 0.0 和 1.0 之间的阈值。默认为 0.5。与 **-threshold** 搭配使用。

**-hilbert**
> Hilbert 曲线抖动。

**-dither8**, **-d8**
> 使用 8x8 矩阵的有序抖动。

**-cluster3**, **-c3**
> 使用 3x3 图案的聚簇抖动。

**-cluster4**, **-c4**
> 使用 4x4 图案的聚簇抖动。

**-cluster8**, **-c8**
> 使用 8x8 图案的聚簇抖动。

**-clump** _size_
> Hilbert 曲线抖动的簇大小。

**-randomseed** _integer_
> 随机化种子，用于产生可复现的结果。

# DESCRIPTION

**pgmtopbm** 将 PGM 灰度图像转换为 PBM 位图格式。它通过抖动或阈值化从灰度输入生成 1 位输出。属于 Netpbm 工具集。自 Netpbm 10.23（2004 年 7 月）起，此工具已基本过时；推荐改用 [pamditherbw](/man/pamditherbw)(1)，其 gamma 处理更好。

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

[pbmtopgm](/man/pbmtopgm)(1), [pamditherbw](/man/pamditherbw)(1), [pgmtoppm](/man/pgmtoppm)(1)
