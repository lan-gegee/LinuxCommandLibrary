# TAGLINE

根据 PBM 图像中图形的轮廓创建掩码位图

# TLDR

**从位图边缘创建掩码**

```pbmmask [input.pbm] > [output.pbm]```

**按像素扩展掩码**

```pbmmask -expand [2] [input.pbm] > [output.pbm]```

# SYNOPSIS

**pbmmask** [_options_] [_file_]

# PARAMETERS

**-expand** _n_
> 将掩码扩展 n 个像素。

# DESCRIPTION

**pbmmask** 根据 PBM 图像中图形的轮廓创建掩码位图。可用于创建选区掩码或轮廓线。属于 Netpbm 工具集。

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

[ppmcolormask](/man/ppmcolormask)(1), [pbmtext](/man/pbmtext)(1)
