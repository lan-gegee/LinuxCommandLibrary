# TAGLINE

为 PPM 图像添加文字标签

# TLDR

**在图像上添加文字标签**

```ppmlabel -text "[Hello World]" [input.ppm] > [output.ppm]```

**在指定位置添加标签**

```ppmlabel -x [10] -y [20] -text "[Label]" [input.ppm] > [output.ppm]```

**以自定义颜色和大小添加标签**

```ppmlabel -color [white] -size [24] -text "[Label]" [input.ppm] > [output.ppm]```

**添加旋转的标签**

```ppmlabel -angle [45] -text "[Watermark]" [input.ppm] > [output.ppm]```

**添加带背景高亮的标签**

```ppmlabel -background [black] -color [yellow] -text "[Warning]" [input.ppm] > [output.ppm]```

**添加多个标签**，使用脚本文件

```ppmlabel -file [labels.txt] [input.ppm] > [output.ppm]```

# SYNOPSIS

**ppmlabel** [_options_] [_file_]

# PARAMETERS

**-text** _string_
> 要渲染到图像上的文字字符串。

**-file** _filename_
> 从文件读取标签命令，每行一条。

**-x** _pixels_
> 标签相对于左边缘的水平位置。

**-y** _pixels_
> 标签基线相对于顶边缘的垂直位置。

**-color** _color_
> 文字颜色（Netpbm 颜色名或 #rrggbb 十六进制值）。

**-background** _color_
> 文字背后的背景色。默认透明（无背景）。

**-angle** _degrees_
> 以度为单位的逆时针旋转角度。默认为 0。

**-size** _pixels_
> 字体高度（像素）。默认值取决于内置字体。

# DESCRIPTION

**ppmlabel** 为 PPM（Portable Pixmap）图像添加文字标签。它读取一幅 PPM 图像，在指定位置渲染一个或多个文字字符串（可选颜色、大小和旋转），并将结果写成新的 PPM 图像。属于 Netpbm 工具集。

可以通过指定多个 **-text** 选项，或用 **-file** 选项从文件读取标签定义，在同一幅图像上放置多个标签。每个标签都可以有独立的位置、颜色、大小和角度设置。

# CAVEATS

使用内置位图字体；不支持 TrueType 或外部字体。如需更高级的文字渲染，可考虑将 **pbmtext** 的输出通过管道交给 **pnmcomp**。输入和输出仅支持 PPM 格式。

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

[pbmtext](/man/pbmtext)(1), [pnmcomp](/man/pnmcomp)(1), [ppmdraw](/man/ppmdraw)(1), [ppmchange](/man/ppmchange)(1)
