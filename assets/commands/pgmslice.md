# TAGLINE

从 PGM 图像中提取一行或一列并输出灰度值

# TLDR

**从图像提取行或列切片**

```pgmslice -row [100] [input.pgm]```

**提取列切片**

```pgmslice -col [200] [input.pgm]```

# SYNOPSIS

**pgmslice** [_options_] [_file_]

# PARAMETERS

**-row** _n_
> 提取第 n 行的水平切片。

**-col** _n_
> 提取第 n 列的垂直切片。

# DESCRIPTION

**pgmslice** 从 PGM 图像中提取一行或一列并输出其灰度值。适合分析图像的横截面。属于 Netpbm 工具集。

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

[pamcut](/man/pamcut)(1), [pgmhist](/man/pgmhist)(1)
