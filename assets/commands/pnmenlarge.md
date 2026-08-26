# TAGLINE

通过像素复制放大 PNM 图像

# TLDR

**将图像放大 2 倍**

```pnmenlarge [2] [input.pnm] > [output.pnm]```

**将图像放大 4 倍**

```pnmenlarge [4] [input.pnm] > [output.pnm]```

# SYNOPSIS

**pnmenlarge** _factor_ [_file_]

# PARAMETERS

_factor_
> 放大倍数（整数）。

# DESCRIPTION

**pnmenlarge** 通过复制像素来放大 PNM 图像。这是不插值的简单最近邻缩放。属于 Netpbm 工具集。想要更平滑的缩放效果请使用 pamscale。

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

[pamscale](/man/pamscale)(1), [pnmscale](/man/pnmscale)(1)
