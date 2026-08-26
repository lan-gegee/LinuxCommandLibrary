# TAGLINE

创建随机噪点图像

# TLDR

**创建随机噪点位图**

```pbmnoise [100] [100] > [noise.pbm]```

**设置密度**

```pbmnoise -ratio=[0.5] [100] [100] > [noise.pbm]```

**设置随机种子**

```pbmnoise -randomseed=[12345] [100] [100] > [noise.pbm]```

# SYNOPSIS

**pbmnoise** [_options_] _width_ _height_

# PARAMETERS

_WIDTH_
> 图像宽度。

_HEIGHT_
> 图像高度。

**-ratio** _RATIO_
> 黑色像素比例（0-1）。

**-randomseed** _SEED_
> 随机种子。

# DESCRIPTION

**pbmnoise** 创建随机噪点图像。生成随机的黑白像素。

该工具用于产生噪点图案。属于 Netpbm 的一部分。

# CAVEATS

Netpbm 的组成部分。输出是随机的。使用种子可复现结果。

# HISTORY

pbmnoise 属于 **Netpbm**，用于生成随机位图噪点。

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

[pbm](/man/pbm)(5), [pgmnoise](/man/pgmnoise)(1), [netpbm](/man/netpbm)(1)
