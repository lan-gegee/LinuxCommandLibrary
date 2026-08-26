# TAGLINE

将 X11 或 X10 位图转换为 PBM 格式

# TLDR

**将 XBM 转换为 PBM**

```xbmtopbm [input.xbm] > [output.pbm]```

# SYNOPSIS

**xbmtopbm** [_file_]

# DESCRIPTION

**xbmtopbm** 读取 X11 或 X10 位图（.xbm）作为输入，并生成 PBM 图像作为输出。X 位图文件是将图像数据定义为数组的 C 源代码；本工具提取并转换其中的图像数据。属于 Netpbm 工具集。

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

[pbmtoxbm](/man/pbmtoxbm)(1), [xpmtoppm](/man/xpmtoppm)(1)
