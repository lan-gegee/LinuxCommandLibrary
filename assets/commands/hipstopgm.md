# TAGLINE

将 HIPS 图像文件转换为 PGM 格式

# TLDR

**将 HIPS 文件转换为 PGM**

```hipstopgm [file.hip] > [output.pgm]```

**从 stdin 转换**

```cat [file.hip] | hipstopgm > [output.pgm]```

# SYNOPSIS

**hipstopgm** [_hipsfile_]

# DESCRIPTION

**hipstopgm** 将 HIPS（Human Information Processing Laboratory, NYU）图像文件转换为 PGM（Portable Graymap）格式。它是 Netpbm 图像处理工具包的一部分。如果 HIPS 文件包含多帧，各帧会在输出中垂直拼接。除标准 Netpbm 选项外，该工具没有专属选项。

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

[pgm](/man/pgm)(1), [pgmtoppm](/man/pgmtoppm)(1), [ppmtogif](/man/ppmtogif)(1), [netpbm](/man/netpbm)(1)
