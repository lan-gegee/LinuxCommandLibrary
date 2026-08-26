# TAGLINE

以 PBM 图像形式生成打印机校准页和测试页

# TLDR

**生成打印机测试页**

```pbmpage [1] > [output.pbm]```

**生成 A4 测试页**

```pbmpage -a4 [1] > [output.pbm]```

# SYNOPSIS

**pbmpage** [_options_] _pagenum_

# PARAMETERS

_pagenum_
> 测试页编号（1-3）。

**-a4**
> 生成 A4 尺寸而不是 US letter（默认）。

# DESCRIPTION

**pbmpage** 以 600 dpi 分辨率生成 PBM 格式的打印机校准页和测试页。不同的页码会产生不同的测试图案，可用于校准边距、对齐和打印质量。默认输出面向 US letter 纸张；A4 尺寸请使用 **-a4**。属于 Netpbm 工具集。

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

[pbmtext](/man/pbmtext)(1), [pbmtolj](/man/pbmtolj)(1)
