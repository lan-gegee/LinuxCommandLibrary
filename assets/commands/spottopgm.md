# TAGLINE

将 SPOT 卫星图像转换为 PGM

# TLDR

**将 SPOT 图像的默认波段转换**为 PGM

```spottopgm [input.spot] > [output.pgm]```

**选择特定波段**（1, 2 或 3）

```spottopgm -2 [input.spot] > [output.pgm]```

**裁剪到指定的矩形区域**（按列和行界定）

```spottopgm [firstcol] [firstline] [lastcol] [lastline] [input.spot] > [output.pgm]```

# SYNOPSIS

**spottopgm** [**-1**|**-2**|**-3**] [_firstcol_ _firstline_ _lastcol_ _lastline_] [_file_]

# PARAMETERS

**-1**, **-2**, **-3**
> 选择要提取的三个光谱波段之一（分别为红外、可见光和紫外波段，不过 Netpbm 作者承认确切的对应关系并不确定）。一次只输出一个波段；不支持合并多光谱的 PPM 输出。

_firstcol_ _firstline_ _lastcol_ _lastline_
> 提供这些参数时，将输出裁剪到由给定列/行索引界定的矩形区域。

# DESCRIPTION

**spottopgm** 将 SPOT 卫星格式的图像转换为 PGM（Portable Graymap）格式。SPOT 格式用于来自 SPOT（Satellite Pour l'Observation de la Terre，地球观测卫星）系统的高分辨率影像，该系统为制图、农业和环境监测采集图像。此工具是 Netpbm 图像处理工具包的一部分，该工具包提供多种图像格式之间的转换器。

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

[fitstopnm](/man/fitstopnm)(1), [pgmnorm](/man/pgmnorm)(1)
