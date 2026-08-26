# TAGLINE

创建 PBM 图像

# TLDR

**创建白色位图**

```pbmmake -white [100] [100] > [white.pbm]```

**创建黑色位图**

```pbmmake -black [100] [100] > [black.pbm]```

**创建灰色图案**

```pbmmake -gray [100] [100] > [gray.pbm]```

# SYNOPSIS

**pbmmake** [_options_] _width_ _height_

# PARAMETERS

_WIDTH_
> 图像宽度（像素）。

_HEIGHT_
> 图像高度（像素）。

**-white**
> 白色背景。

**-black**
> 黑色背景。

**-gray**
> 棋盘格图案。

# DESCRIPTION

**pbmmake** 创建 PBM 图像。可生成纯色或图案背景。

该工具用于生成空白位图。属于 Netpbm 的一部分。

# CAVEATS

Netpbm 的组成部分。仅支持简单图案。PBM 格式。

# HISTORY

pbmmake 属于 **Netpbm**，用于创建位图图像。

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

[pbm](/man/pbm)(5), [ppmmake](/man/ppmmake)(1), [netpbm](/man/netpbm)(1)
