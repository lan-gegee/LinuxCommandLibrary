# TAGLINE

使用灰度共生矩阵从 PGM 图像计算 Haralick 纹理特征

# TLDR

**计算图像纹理度量**

```pgmtexture [input.pgm]```

**指定距离**

```pgmtexture -d [1] [input.pgm]```

# SYNOPSIS

**pgmtexture** [_options_] [_file_]

# PARAMETERS

**-d** _n_
> 共生矩阵的距离。

# DESCRIPTION

**pgmtexture** 使用灰度共生矩阵从 PGM 图像计算 Haralick 纹理特征，输出用于纹理分析的统计度量。属于 Netpbm 工具集。

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

[pgmhist](/man/pgmhist)(1), [pgmkernel](/man/pgmkernel)(1)
