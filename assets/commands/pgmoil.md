# TAGLINE

通过选取最常见灰度值为 PGM 图像应用油画效果

# TLDR

**应用油画效果**

```pgmoil [input.pgm] > [output.pgm]```

**指定涂抹半径**

```pgmoil -n [3] [input.pgm] > [output.pgm]```

# SYNOPSIS

**pgmoil** [_options_] [_file_]

# PARAMETERS

**-n** _radius_
> 涂抹半径（默认 3）。

# DESCRIPTION

**pgmoil** 通过选取邻域内最常见的灰度值，为 PGM 图像应用油画效果。属于 Netpbm 工具集。

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

[pgmbentley](/man/pgmbentley)(1), [ppmspread](/man/ppmspread)(1)
