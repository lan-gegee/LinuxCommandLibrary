# TAGLINE

将 SVG 文件按指定分辨率转换为 PNG 格式

# TLDR

将 **SVG 转换为 PNG**

```ksvgtopng5 [width] [height] [path/to/file.svg] [output.png]```

# SYNOPSIS

**ksvgtopng5** _width_ _height_ _input.svg_ _output.png_

# DESCRIPTION

**ksvgtopng5** 将 SVG (Scalable Vector Graphics) 文件按指定分辨率转换为 PNG (Portable Network Graphics) 格式。它是 KDE CLI 工具的一部分，使用 Qt 的 SVG 渲染。

# PARAMETERS

**width**
> 输出图像宽度（像素）

**height**
> 输出图像高度（像素）

**input.svg**
> 输入 SVG 文件的路径（应使用绝对路径）

**output.png**
> 输出 PNG 文件的路径

# CAVEATS

为获得可靠结果，SVG 输入路径应为绝对路径。复杂的 SVG 特性渲染结果可能与 Web 浏览器不一致。

# INSTALL

```apt: sudo apt install kde-cli-tools```

```dnf: sudo dnf install kde-cli-tools```

```pacman: sudo pacman -S kde-cli-tools```

```apk: sudo apk add kde-cli-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsvg-convert](/man/rsvg-convert)(1), [inkscape](/man/inkscape)(1), [convert](/man/convert)(1)
