# TAGLINE

将 QRT 光线追踪器输出转换为 PPM

# TLDR

**将 QRT 光线追踪器输出转换为 PPM**

```qrttoppm [input.qrt] > [output.ppm]```

# SYNOPSIS

**qrttoppm** [_file_]

# DESCRIPTION

**qrttoppm** 将 QRT 光线追踪器输出格式的图像转换为 PPM（Portable Pixmap）格式。QRT 是一款早期的光线追踪程序，本工具是 Netpbm 图像处理工具集的一部分，可将旧式 QRT 渲染结果转换为广泛支持的格式，以便查看或进一步处理。

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

[mtvtoppm](/man/mtvtoppm)(1), [rawtoppm](/man/rawtoppm)(1), [ppmtopgm](/man/ppmtopgm)(1)
