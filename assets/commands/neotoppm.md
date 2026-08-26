# TAGLINE

将 Atari Neochrome .neo 图像转换为 PPM

# TLDR

**将 Atari Neochrome 文件转换为 PPM**

```neotoppm [input.neo] > [output.ppm]```

**从 stdin 读取并转换**

```cat [input.neo] | neotoppm > [output.ppm]```

# SYNOPSIS

**neotoppm** [_neofile_]

# DESCRIPTION

**neotoppm** 以 Atari Neochrome .neo 文件为输入，生成 PPM 图像作为输出。未指定输入文件时从标准输入读取。Neochrome 是 Atari ST 计算机上的一款绘图程序。本程序是 **Netpbm** 工具集的一部分。

neotoppm 没有专属的命令行选项。

# HISTORY

Copyright (C) 2001 by Teemu Hukkanen, based on **pi1toppm** by Steve Belczyk and Jef Poskanzer.

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

[ppmtoneo](/man/ppmtoneo)(1), [pi1toppm](/man/pi1toppm)(1)
