# TAGLINE

显示 PPM 图像的颜色直方图

# TLDR

**显示颜色直方图**

```ppmhist [input.ppm]```

**以映射文件形式显示**

```ppmhist -map [input.ppm]```

**限制输出的颜色数**

```ppmhist -noheader [input.ppm] | head -20```

# SYNOPSIS

**ppmhist** [_options_] [_file_]

# DESCRIPTION

**ppmhist** 读取一幅 PPM（Portable Pixmap）图像并输出颜色直方图，列出每种不同的颜色及其使用的像素数量。它属于 Netpbm 工具集，可用于分析调色板使用情况、识别主色调，以及为量化准备颜色映射表。

默认输出为排序后的文本表格。使用 **-map** 时，输出本身是一个表示颜色映射表的有效 PPM 文件，可直接提供给其他 Netpbm 工具。

# PARAMETERS

**-map**
> 以 PPM 文件的形式输出颜色映射表，而不是文本表格。

**-nomap**
> 强制输出文本形式的直方图（默认行为）。

**-noheader**
> 在文本输出中省略开头的标题行。

**-sort** _method_
> 按 _frequency_ 或 _rgb_ 对条目排序。

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

[pgmhist](/man/pgmhist)(1), [pnmcolormap](/man/pnmcolormap)(1), [ppmtopgm](/man/ppmtopgm)(1)
