# TAGLINE

按整数倍缩小 PBM 位图尺寸

# TLDR

**按指定倍数缩小位图**

```pbmreduce [4] [input.pbm] > [output.pbm]```

**使用 Floyd-Steinberg 抖动缩小**

```pbmreduce -floyd [4] [input.pbm] > [output.pbm]```

# SYNOPSIS

**pbmreduce** [_options_] _n_ [_file_]

# PARAMETERS

_n_
> 缩小倍数。

**-floyd**
> 使用 Floyd-Steinberg 抖动。

**-threshold**
> 使用简单阈值（默认）。

# DESCRIPTION

**pbmreduce** 按整数倍缩小 PBM 位图尺寸。缩小时可使用阈值或抖动处理。属于 Netpbm 工具集。

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

[pbmpscale](/man/pbmpscale)(1), [pamscale](/man/pamscale)(1)
