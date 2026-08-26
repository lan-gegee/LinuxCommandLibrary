# TAGLINE

使用抖动技术将灰度图像转换为黑白图像

# TLDR

**抖动转换为黑白**

```pamditherbw [input.pgm] > [output.pbm]```

**使用 Floyd-Steinberg 抖动**

```pamditherbw -fs [input.pgm] > [output.pbm]```

**使用阈值抖动**

```pamditherbw -threshold -value [0.5] [input.pgm] > [output.pbm]```

# SYNOPSIS

**pamditherbw** [_options_] [_file_]

# PARAMETERS

**-fs**
> Floyd-Steinberg 抖动。

**-threshold**
> 简单阈值法。

**-hilbert**
> Hilbert 曲线抖动。

**-value** _n_
> 阈值（0.0-1.0）。

# DESCRIPTION

**pamditherbw** 使用抖动技术将灰度图像转换为黑白图像。提供多种算法以适应不同的质量/速度权衡。属于 Netpbm 工具集。

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

[pgmtopbm](/man/pgmtopbm)(1), [ppmquant](/man/ppmquant)(1)
