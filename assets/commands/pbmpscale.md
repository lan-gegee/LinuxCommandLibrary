# TAGLINE

以抗锯齿方式按整数倍缩放 PBM 位图，输出灰度图像

# TLDR

**以抗锯齿方式缩放位图**

```pbmpscale [4] [input.pbm] > [output.pgm]```

# SYNOPSIS

**pbmpscale** _scale_ [_file_]

# PARAMETERS

_scale_
> 整数缩放倍数。

# DESCRIPTION

**pbmpscale** 以抗锯齿方式按整数倍缩放 PBM 位图，输出灰度图像。适用于平滑放大 1 位图像。属于 Netpbm 工具集。

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

[pbmreduce](/man/pbmreduce)(1), [pamscale](/man/pamscale)(1)
