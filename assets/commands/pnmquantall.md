# TAGLINE

将多幅图像量化到共享调色板

# TLDR

**将多幅图像量化到同一调色板**

```pnmquantall [256] [image1.pnm] [image2.pnm] ...```

# SYNOPSIS

**pnmquantall** _ncolors_ _files_...

# PARAMETERS

_ncolors_
> 最大颜色数。

_files_
> 输入的图像文件（会被原地修改）。

# DESCRIPTION

**pnmquantall** 将多幅 PNM 图像缩减为共用同一个调色板。适合制作色彩一致的动画。属于 Netpbm 工具集。

# CAVEATS

会直接修改原文件。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm-extras```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppmquantall](/man/ppmquantall)(1), [pnmquant](/man/pnmquant)(1)
