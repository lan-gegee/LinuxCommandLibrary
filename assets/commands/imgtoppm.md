# TAGLINE

将 Img-whatnot 图像文件转换为 PPM 格式

# TLDR

**将 IMG 转换为 PPM**

```imgtoppm [file.img] > [output.ppm]```

**从 stdin 转换**

```cat [file.img] | imgtoppm > [output.ppm]```

# SYNOPSIS

**imgtoppm** [_imgfile_]

# DESCRIPTION

**imgtoppm** 将 Img-whatnot 图像文件转换为 PPM（Portable Pixmap）格式。它是 Netpbm 图像处理工具包的一员。未指定文件时从 stdin 读取。

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

[ppmtogif](/man/ppmtogif)(1), [netpbm](/man/netpbm)(1)
