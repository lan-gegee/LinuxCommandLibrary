# TAGLINE

将 PPM 转换为 Interleaf 图像格式

# TLDR

**将 PPM 转换为 Interleaf 图像**格式并写到 stdout

```ppmtoleaf [input.ppm] > [output.leaf]```

**从 stdin 读取**并将 Interleaf 写到 stdout

```cat [input.ppm] | ppmtoleaf > [output.leaf]```

# SYNOPSIS

**ppmtoleaf** [_ppmfile_]

# DESCRIPTION

**ppmtoleaf** 读取一幅 PPM 图像，并以 Interleaf 光栅图像的形式写到标准输出。Interleaf 格式曾在 20 世纪 80 年代末至 90 年代初被 Interleaf 桌面出版系统使用。

没有输入文件时，**ppmtoleaf** 从标准输入读取。属于 Netpbm 工具集。

# CAVEATS

Interleaf 格式已过时；此工具仅为兼容旧文档而存在。除输入文件名外不提供其他选项。输出发送到 stdout，请重定向到文件。

# HISTORY

属于 **Netpbm** 软件包，最初来自 Jef Poskanzer 的 PBMplus 工具集。

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

[leaftoppm](/man/leaftoppm)(1), [ppmtopict](/man/ppmtopict)(1), [ppm](/man/ppm)(5)
