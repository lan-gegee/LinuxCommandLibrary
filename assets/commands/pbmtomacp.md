# TAGLINE

将 PBM 位图转换为经典 Macintosh 的 MacPaint 格式

# TLDR

**将 PBM 转换为 MacPaint 格式**

```pbmtomacp [input.pbm] > [output.macp]```

**指定位置**

```pbmtomacp -left [100] -top [50] [input.pbm] > [output.macp]```

# SYNOPSIS

**pbmtomacp** [_options_] [_file_]

# PARAMETERS

**-left** _n_
> 左边距像素。

**-top** _n_
> 顶部边距像素。

# DESCRIPTION

**pbmtomacp** 将 PBM 位图转换为经典 Macintosh 的 MacPaint 格式。MacPaint 使用固定的 576x720 画布。属于 Netpbm 工具集。

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

[macptopbm](/man/macptopbm)(1), [picttoppm](/man/picttoppm)(1)
