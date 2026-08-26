# TAGLINE

将 PPM 拆分为独立的 RGB 通道文件

# TLDR

**拆分**一幅 PPM 图像为三个 PGM 分量文件

```ppmtorgb3 [input.ppm]```

**从 stdin 读取**（生成 noname.red/.grn/.blu）

```cat [input.ppm] | ppmtorgb3```

# SYNOPSIS

**ppmtorgb3** [_ppmfile_]

# DESCRIPTION

**ppmtorgb3** 读取一幅 PPM（Portable Pixmap）图像，并输出三幅 PGM（Portable Graymap）图像：分别对应红、绿、蓝通道。

输出文件名由输入文件名派生：去掉所有扩展名后追加 **.red**、**.grn** 和 **.blu**。例如，分离 **lenna.ppm** 会产生 **lenna.red**、**lenna.grn** 和 **lenna.blu**。当输入来自 stdin 时，文件名默认为 **noname.red**、**noname.grn** 和 **noname.blu**。

**ppmtorgb3** 没有专属选项，但接受所有基于 libnetpbm 的程序共享的通用选项。

# HISTORY

由 **Jef Poskanzer** 于 1991 年编写，作为 **Netpbm**（最初名为 **Pbmplus**）的一部分。这是一个经典的图像处理工具集，以简单的 PBM/PGM/PPM 格式作为管道中间格式。

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

[rgb3toppm](/man/rgb3toppm)(1), [ppmtopgm](/man/ppmtopgm)(1), [pgmtoppm](/man/pgmtoppm)(1), [ppmtoyuvsplit](/man/ppmtoyuvsplit)(1), [ppm](/man/ppm)(5), [pgm](/man/pgm)(5)
