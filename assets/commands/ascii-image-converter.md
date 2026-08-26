# TAGLINE

将图片转换为可在终端显示的 ASCII 艺术

# TLDR

**将图片转换为 ASCII 艺术**

```ascii-image-converter [image.png]```

**以彩色输出转换**

```ascii-image-converter -C [image.png]```

**以指定宽度转换**

```ascii-image-converter -W [80] [image.png]```

**使用盲文字符转换**

```ascii-image-converter -b [image.png]```

**使用自定义字符映射**（由深到浅）

```ascii-image-converter -m " .:-=+*#%@" [image.png]```

**让输出适应终端宽度**

```ascii-image-converter -f [image.png]```

**将输出保存为 PNG 图片**

```ascii-image-converter -s [output_dir] -C [image.png]```

# SYNOPSIS

**ascii-image-converter** [_options_] _image_

# DESCRIPTION

**ascii-image-converter** 将图片转换为 ASCII 艺术。它分析像素亮度并将数值映射为 ASCII 字符，生成可在终端查看的图像文本表示。

该工具支持多种图片格式，并可使用 ANSI 转义码输出彩色结果。

# PARAMETERS

**-C**, **--color**
> 使用原图的颜色显示

**-b**, **--braille**
> 使用盲文字符代替 ASCII

**-g**, **--grayscale**
> 以灰度颜色显示

**-n**, **--negative**
> 反转颜色

**-c**, **--complex**
> 使用更宽泛的 ASCII 字符集以呈现更多细节

**-m** _chars_, **--map** _chars_
> 自定义字符串（由深到浅）

**-d** _width_,_height_, **--dimensions** _width_,_height_
> 按字符数设置宽度和高度

**-W** _width_, **--width** _width_
> 设置宽度；高度按纵横比计算

**-H** _height_, **--height** _height_
> 设置高度；宽度按纵横比计算

**-f**, **--full**
> 在保持纵横比的前提下适应终端宽度

**-x**, **--flipX**
> 水平翻转

**-y**, **--flipY**
> 垂直翻转

**--dither**
> 为盲文艺术应用抖动处理

**--threshold** _value_
> 盲文像素比较的阈值（0-255）

**--color-bg**
> 将颜色应用到字符背景而非前景

**-s** _dir_, **--save-img** _dir_
> 将输出保存为 PNG 图片

**--save-txt** _dir_
> 将输出保存为 TXT 文件

**--save-gif** _dir_
> 将转换后的 GIF 保存为 ASCII 艺术 GIF

**--only-save**
> 保存时不向终端输出

**--formats**
> 显示支持的输入图片格式

# CAVEATS

输出质量取决于终端字体和大小。彩色输出需要支持 24 位或 8 位 ANSI 颜色的终端。盲文字符需要终端支持 UTF-8。宽幅图片需要足够大的终端宽度。

# HISTORY

**ascii-image-converter** 是一个基于 Go 的现代 ASCII 艺术生成工具，比 jp2a 等传统工具功能更丰富。

# INSTALL

```aur: yay -S ascii-image-converter```

```nix: nix profile install nixpkgs#ascii-image-converter```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[jp2a](/man/jp2a)(1), [img2txt](/man/img2txt)(1)
