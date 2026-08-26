# TAGLINE

将 XV 缩略图转换为 PPM 格式

# TLDR

**将 XV 缩略图转换为 PPM**

```xvminitoppm [input.xv] > [output.ppm]```

# SYNOPSIS

**xvminitoppm** [_file_]

# DESCRIPTION

**xvminitoppm** 读取 XV "缩略图"图片（由 XV visual schnauzer 浏览器创建的微型图像）作为输入，生成 PPM 图像作为输出。XV 是 20 世纪 90 年代流行的 Unix 图像查看器。属于 Netpbm 工具集。

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

[pamtoxvmini](/man/pamtoxvmini)(1), [xwdtopnm](/man/xwdtopnm)(1)
