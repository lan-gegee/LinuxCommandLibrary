# TAGLINE

将位图描摹为矢量图形

# TLDR

**将位图转换为 SVG**

```potrace -s [input.bmp] -o [output.svg]```

**转换为 PDF**

```potrace -b pdf [input.bmp] -o [output.pdf]```

**转换为 EPS**

```potrace -e [input.bmp] -o [output.eps]```

**反转颜色**

```potrace -s --invert [input.bmp] -o [output.svg]```

**从 PBM/PGM/PPM 转换**

```potrace -s [input.pbm] -o [output.svg]```

# SYNOPSIS

**potrace** [_options_] [_files_]

# PARAMETERS

**-b**, **--backend** _format_
> 输出格式（svg、pdf、eps、ps）。

**-s**, **--svg**
> SVG 输出。

**-e**, **--eps**
> EPS 输出。

**-p**, **--postscript**
> PostScript 输出。

**-o** _file_
> 输出文件。

**--invert**
> 反转输入。

**-t**, **--turdsize** _n_
> 抑制斑点。

**-a**, **--alphamax** _n_
> 角点阈值。

# DESCRIPTION

**potrace** 通过描摹黑白区域之间的边界，将位图图像转换为平滑、可缩放的矢量图形。它使用最优多边形拟合算法生成干净的曲线，非常适合将徽标、线稿、扫描图和其他高对比度图像转换为 SVG、PDF、EPS 或 PostScript 格式。

该工具接受 PBM、PGM、PPM 和 BMP 输入格式。调节参数可控制角点检测（alphamax）和斑点抑制（turdsize），在精度与平滑度之间取得平衡。对于照片或彩色图像，需要先用阈值处理或边缘检测工具进行预处理。

# EXAMPLES

```bash
# Bitmap to SVG
potrace -s logo.bmp -o logo.svg

# PDF output with smoothing
potrace -b pdf --alphamax 1 image.bmp -o output.pdf

# Remove small spots
potrace -s --turdsize 5 noisy.bmp -o clean.svg

# From PNG (via conversion)
convert image.png image.bmp && potrace -s image.bmp
```

# INPUT FORMATS

接受 PBM、PGM、PPM 和 BMP 格式。其他格式请先用 ImageMagick 或类似工具转换。

# CAVEATS

对高对比度图像效果最佳。照片的描摹效果不佳。为获得最好效果，输入应为单色图像。

# HISTORY

potrace 由 **Peter Selinger** 编写，采用最优多边形算法，是 autotrace 的改进替代品。

# INSTALL

```apt: sudo apt install potrace```

```dnf: sudo dnf install potrace```

```pacman: sudo pacman -S potrace```

```apk: sudo apk add potrace```

```zypper: sudo zypper install potrace```

```brew: brew install potrace```

```nix: nix profile install nixpkgs#potrace```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inkscape](/man/inkscape)(1), [convert](/man/convert)(1)
