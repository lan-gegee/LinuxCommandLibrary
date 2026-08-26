# TAGLINE

将 PNM 图像转换为 PostScript

# TLDR

**将 PNM 转换为 PostScript**

```pnmtops [input.pnm] > [output.ps]```

**创建 EPS 文件**

```pnmtops -nocenter -noturn -nosetpage [input.pnm] > [output.eps]```

**以指定 DPI 转换**

```pnmtops -dpi [300] [input.pnm] > [output.ps]```

**缩放以适应页面**

```pnmtops -scale [0.5] [input.pnm] > [output.ps]```

# SYNOPSIS

**pnmtops** [_options_] [_file_]

# PARAMETERS

**-dpi** _n_
> 图像分辨率。

**-scale** _factor_
> 缩放倍数。

**-width** _inches_
> 最大宽度。

**-height** _inches_
> 最大高度。

**-nocenter**
> 不在页面上居中。

**-noturn**
> 不旋转。

**-nosetpage**
> 不设置页面尺寸。

# DESCRIPTION

**pnmtops** 将 PNM 图像转换为 PostScript 格式，适合用于打印或嵌入文档。输出既可以是整页的 PostScript 文档，也可以是封装的 PostScript（EPS）文件。

**-dpi** 与 **-scale** 选项控制输出尺寸，**-width** 与 **-height** 设置最大尺寸。把 **-nocenter**、**-noturn** 和 **-nosetpage** 组合使用可以生成便于嵌入其他文档的最小化 EPS。属于 Netpbm 工具集。

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

[pstopnm](/man/pstopnm)(1), [pnmtopng](/man/pnmtopng)(1)
