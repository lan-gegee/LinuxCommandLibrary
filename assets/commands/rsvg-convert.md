# TAGLINE

将 SVG 图像转换为其他格式

# TLDR

**将 SVG 转换为 PNG**

```rsvg-convert [input.svg] -o [output.png]```

**转换为 PDF**

```rsvg-convert -f pdf [input.svg] -o [output.pdf]```

**调整输出尺寸**

```rsvg-convert -w [800] -h [600] [input.svg] -o [output.png]```

**设置 DPI**

```rsvg-convert -d [300] [input.svg] -o [output.png]```

# SYNOPSIS

**rsvg-convert** [_options_] [_files_...]

# PARAMETERS

**-o**, **--output** _file_
> 输出文件。

**-f**, **--format** _format_
> 输出格式（png、pdf、ps、eps、svg）。

**-w**, **--width** _px_
> 宽度（像素）。

**-h**, **--height** _px_
> 高度（像素）。

**-d**, **--dpi-x** _dpi_
> 水平 DPI。

**-p**, **--dpi-y** _dpi_
> 垂直 DPI。

**-a**, **--keep-aspect-ratio**
> 保持宽高比。

**-b**, **--background-color** _color_
> 背景颜色。

# DESCRIPTION

**rsvg-convert** 将 SVG 文件渲染成多种光栅或矢量格式。它借助 librsvg 库实现高质量的 SVG 渲染。

# EXAMPLES

```bash
# SVG to PNG
rsvg-convert icon.svg -o icon.png

# SVG to PDF
rsvg-convert -f pdf diagram.svg -o diagram.pdf

# Resize to width
rsvg-convert -w 512 logo.svg -o logo.png

# High DPI for print
rsvg-convert -d 300 -p 300 graphic.svg -o print.png

# With background
rsvg-convert -b white input.svg -o output.png

# Multiple files
rsvg-convert -f pdf *.svg -o combined.pdf
```

# CAVEATS

并非所有 SVG 特性都受支持。它是 librsvg 的一部分。遇到复杂的 SVG 可以考虑改用 Inkscape。

# HISTORY

rsvg-convert 是 **GNOME Project** 的 **librsvg** 项目的组成部分（最初由 **Raph Levien** 开发），用于渲染 SVG。

# INSTALL

```apt: sudo apt install librsvg2-bin```

```apk: sudo apk add rsvg-convert```

```zypper: sudo zypper install rsvg-convert```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inkscape](/man/inkscape)(1), [convert](/man/convert)(1)
