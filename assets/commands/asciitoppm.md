# TAGLINE

将 ASCII 文本转换为 PPM 彩色图像

# TLDR

**将 ASCII 文本文件转换为 PPM 图像**

```asciitoppm < [ascii.txt] > [output.ppm]```

**使用指定的颜色定义文件进行转换**

```asciitoppm -d [colorfile] < [ascii.txt] > [output.ppm]```

# SYNOPSIS

**asciitoppm** [_options_] [_height_ _width_] < _input_ > _output_

# DESCRIPTION

**asciitoppm** 将 ASCII 文本转换为 PPM（Portable Pixmap）彩色图像。输入中的每个字符被映射为一个带颜色的像素，从而生成文本内容的可视化表示。

与产生灰度输出的 **asciitopgm** 不同，**asciitoppm** 生成全彩图像。输入从标准输入读取，输出写到标准输出。它是 Netpbm 图像处理工具集的一部分。

# PARAMETERS

**-d** _colorfile_
> 使用指定的颜色定义文件将字符映射为颜色。

# HISTORY

Netpbm 图像处理工具集的组成部分。

# SEE ALSO

[asciitopgm](/man/asciitopgm)(1), [ppmtopgm](/man/ppmtopgm)(1), [pbmtoascii](/man/pbmtoascii)(1), [ppmtoascii](/man/ppmtoascii)(1)
