# TAGLINE

使用字符画在终端中查看图片

# TLDR

**在终端中显示图片**

```chafa [image.png]```

**指定输出尺寸**

```chafa -s [80x40] [image.jpg]```

**使用 sixel 图形**

```chafa --format sixels [image.png]```

**使用 kitty 图形协议**

```chafa --format kitty [image.gif]```

**限制颜色数**

```chafa --colors [256] [image.png]```

**显示动画 GIF**

```chafa --animate [animation.gif]```

**仅输出 ASCII**

```chafa --symbols ascii [image.jpg]```

# SYNOPSIS

**chafa** [_options_] _image_...

# DESCRIPTION

**chafa** 将图片转换为字符画，直接在终端中显示。它使用 Unicode 块字符、盲文图案和 ASCII 字符，以终端网格的分辨率来近似呈现图片。

对于支持高级图形的终端，chafa 可以用 Sixel、Kitty 或 iTerm2 图形协议输出，获得更高的还原度。它支持多种图片格式，包括 JPEG、PNG、GIF（含动画）、AVIF、SVG、WebP、TIFF 和 JPEG XL。

输出效果可通过调整尺寸、颜色深度、符号集和动画速度来微调。chafa 会自动检测终端能力并选择最佳的可用输出模式。

# PARAMETERS

**-s**, **--size** _WxH_
> 以字符为单位的输出尺寸

**-f**, **--format** _format_
> 输出格式：symbols、sixels、kitty、iterm

**-c**, **--colors** _n_
> 颜色模式：none、2、8、16、256、full

**--symbols** _set_
> 符号集：all、ascii、block、braille

**--fg** _color_
> 前景色

**--bg** _color_
> 背景色

**--animate**
> 启用 GIF 动画

**--duration** _secs_
> 动画时长

**--speed** _factor_
> 动画速度倍数

**-w**, **--watch**
> 监视文件变化

**--font-ratio** _ratio_
> 字体宽高比

# SUPPORTED FORMATS

JPEG, PNG, GIF, AVIF, SVG, TIFF, WebP, JPEG XL, QOI, XWD

# CAVEATS

输出质量取决于终端能力。Sixel 需要兼容的终端。Truecolor 支持下效果最佳。

# INSTALL

```apt: sudo apt install chafa```

```dnf: sudo dnf install chafa```

```pacman: sudo pacman -S chafa```

```apk: sudo apk add chafa```

```zypper: sudo zypper install chafa```

```brew: brew install chafa```

```nix: nix profile install nixpkgs#chafa```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[catimg](/man/catimg)(1), [timg](/man/timg)(1), [img2txt](/man/img2txt)(1)

# RESOURCES

```[Source code](https://github.com/hpjansson/chafa)```

```[Homepage](https://hpjansson.org/chafa/)```

<!-- verified: 2026-06-22 -->
