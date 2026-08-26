# TAGLINE

将 PGM 图像转换为 SBIG ST-4 自动导星格式

# TLDR

**将 PGM 转换为 SBIG ST-4 格式**

```pgmtost4 [input.pgm] > [output.st4]```

# SYNOPSIS

**pgmtost4** [_file_]

# DESCRIPTION

**pgmtost4** 读取一幅 PGM 图像作为输入，生成 SBIG ST-4 相机的 CCD 图像作为输出。ST-4 格式由 Santa Barbara Instrument Group 的天文自动导星相机使用。此格式与大多数其他 SBIG 相机使用的 SBIG 格式不同。属于 Netpbm 工具集。

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

[st4topgm](/man/st4topgm)(1), [pgmtosbig](/man/pgmtosbig)(1)
