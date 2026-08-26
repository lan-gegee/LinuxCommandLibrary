# TAGLINE

图像处理工具集

# TLDR

**将 JPEG 转换为 PPM**

```jpegtopnm [image.jpg] > [image.ppm]```

**将 PNG 转换为 PPM**

```pngtopam [image.png] > [image.ppm]```

**将 PPM 转换为 JPEG**

```pnmtojpeg [image.ppm] > [image.jpg]```

**调整图像大小**

```pamscale -width [800] [input.ppm] > [output.ppm]```

**翻转图像**

```pamflip -lr [input.ppm] > [output.ppm]```

# SYNOPSIS

**netpbm** [_tool_] [_options_] [_files_]

# COMMON TOOLS

**jpegtopnm**
> 将 JPEG 转换为 PNM 格式。

**pngtopam**
> 将 PNG 转换为 PAM 格式。

**pnmtojpeg**
> 将 PNM 转换为 JPEG 格式。

**pnmtopng**
> 将 PNM 转换为 PNG 格式。

**ppmtogif**
> 将 PPM 转换为 GIF 格式。

**giftopnm**
> 将 GIF 转换为 PNM 格式。

**pamscale**
> 缩放（调整大小）图像。

**pamflip**
> 翻转或旋转图像。

**pnmcrop**
> 裁掉边缘的空白区域。

**ppmbrighten**
> 调整亮度和饱和度。

**pnmcat**
> 将图像横向或纵向拼接在一起。

# DESCRIPTION

**netpbm** 是一个包含 350 多个独立程序的工具集，用于处理图形图像，支持约 100 种图形格式之间的相互转换。这些程序使用 PNM（Portable Any Map）和 PAM 作为中间格式，实现基于管道的图像处理。

这些工具专为命令行使用和管道组合而设计。典型的工作流程是：先将输入格式转换为 PNM，应用各种变换，再转换为输出格式。每个工具只做一件事，在 shell 管道中组合使用时威力最大。

# CAVEATS

不是交互式工具。需要在 PNM/PAM 中间格式之间来回转换。各工具有独立的 man page。某些工具已被新的等价工具取代（例如在许多场景下 pnmtopng 取代了 ppmtogif）。

# HISTORY

Netpbm 由 **PBMPLUS** 演化而来，后者是 Jef Poskanzer 于 1988 年创建的开创性图像处理软件包。

# INSTALL

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[imagemagick](/man/imagemagick)(1), [convert](/man/convert)(1), [gimp](/man/gimp)(1)
