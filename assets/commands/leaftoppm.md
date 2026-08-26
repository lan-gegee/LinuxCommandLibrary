# TAGLINE

将 Interleaf 图像格式转换为 PPM

# TLDR

**将 Interleaf 图像转换为 PPM**

```leaftoppm [input.lf] > [output.ppm]```

**从标准输入读取并转换为 PPM**

```cat [input.lf] | leaftoppm > [output.ppm]```

# SYNOPSIS

**leaftoppm** [_leaffile_]

# DESCRIPTION

**leaftoppm** 读取 Interleaf 图像文件作为输入，并生成 PPM（Portable Pixmap）图像作为输出。若未指定输入文件，则从标准输入读取。输出写入标准输出。

Interleaf 是一家在 20 世纪八九十年代颇为流行的技术出版软件公司，约 2000 年被 BroadVision 收购。本程序是 Netpbm 工具集的一部分。

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

[ppmtoleaf](/man/ppmtoleaf)(1), [tifftopnm](/man/tifftopnm)(1), [bmptoppm](/man/bmptoppm)(1)
