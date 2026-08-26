# TAGLINE

为图像应用电视扫描线效果

# TLDR

**应用电视扫描线效果**

```ppmtv [input.ppm] > [output.ppm]```

**在管道中从 stdin 读取**

```pnmtopnm [input.png] | ppmtv > [output.ppm]```

# SYNOPSIS

**ppmtv** [_ppmfile_]

# DESCRIPTION

**ppmtv** 为 PPM 图像应用 CRT 电视扫描线效果，通过调暗交替的行来模拟老式隔行扫描电视显示的外观。未指定文件时从标准输入读取。属于 Netpbm 工具集。

# CAVEATS

输入必须是 PPM 格式。请先使用转换工具（如 jpegtopnm、pngtopam）转换其他格式。

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

[ppmquant](/man/ppmquant)(1), [pamdeinterlace](/man/pamdeinterlace)(1), [netpbm](/man/netpbm)(1)
