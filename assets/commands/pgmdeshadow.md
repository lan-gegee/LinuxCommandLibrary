# TAGLINE

尝试补偿扫描图像中不均匀的光照或阴影

# TLDR

**去除扫描件中不均匀的光照**

```pgmdeshadow [input.pgm] > [output.pgm]```

# SYNOPSIS

**pgmdeshadow** [_file_]

# DESCRIPTION

**pgmdeshadow** 通过分析并归一化局部亮度，尝试补偿扫描图像中不均匀的光照或阴影。属于 Netpbm 工具集。

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

[pgmnorm](/man/pgmnorm)(1), [ppmntsc](/man/ppmntsc)(1)
