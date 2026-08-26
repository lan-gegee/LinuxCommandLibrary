# TAGLINE

生成 PGM 格式的卷积核，供 pnmconvol 使用

# TLDR

**生成卷积核**

```pgmkernel [7] [7] > [kernel.pgm]```

**带权重生成**

```pgmkernel -weight [6.0] [5] [5] > [kernel.pgm]```

# SYNOPSIS

**pgmkernel** [_options_] _width_ _height_

# PARAMETERS

_width_
> 卷积核宽度。

_height_
> 卷积核高度。

**-weight** _n_
> 中心像素的权重。

# DESCRIPTION

**pgmkernel** 生成 PGM 格式的卷积核，供 pnmconvol 使用。它创建类高斯的加权模式。属于 Netpbm 工具集。

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

[pnmconvol](/man/pnmconvol)(1), [pgmtexture](/man/pgmtexture)(1)
