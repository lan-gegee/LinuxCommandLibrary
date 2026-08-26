# TAGLINE

使用 ANSI 在终端中显示图像

# TLDR

**显示一张图像**

```tiv [image.png]```

**以指定宽度显示**

```tiv -w [80] [image.jpg]```

**以指定高度显示**

```tiv -h [24] [image.png]```

**显示多张图像**

```tiv [image1.png] [image2.jpg] [image3.gif]```

**将目录显示为缩略图网格**

```tiv [/path/to/images/]```

**使用自定义的缩略图列数**

```tiv -c [5] [/path/to/images/]```

**使用 256 色模式**（如 macOS 终端）

```tiv -2 [image.png]```

# SYNOPSIS

**tiv** [_options_] _image_ [_image_...]

# PARAMETERS

**-w** _num_
> 将最大输出宽度设置为 _num_ 个字符。

**-h** _num_
> 将最大输出高度设置为 _num_ 行。

**-2**, **--256**
> 使用 256 色而不是 24 位真彩色。在 macOS 终端上正常显示时需要此选项。

**-0**
> 不进行块字符调整：始终使用上半块字符。

**-c** _num_
> 'dir' 模式下缩略图的列数（默认为 3）。

**-d**, **--dir**
> 强制使用 'dir'（缩略图网格）模式。输入多于一个时自动选择。

**-f**, **--full**
> 强制使用 'full' 模式。单一输入时自动选择。

**-C** _hex_
> 使用 _hex_ 颜色（默认为 0xFFFFFF 白色）作为透明 PNG/GIF 的背景色。

**-x**
> 使用新的 Unicode Teletext/传统字符（实验性）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**tiv**（Terminal Image Viewer）使用 RGB ANSI 转义码和 Unicode 块图形字符直接在终端中显示图像。它将每个 4x8 像素单元映射到最接近原图的块字符以及前景/背景颜色。

图像通过内置的 CImg 库加载：PNG 支持已编译在内，而其他格式（JPEG、GIF、BMP 等）则通过调用 ImageMagick 的 `convert` 来处理。图像会在保持宽高比的同时缩放以适应终端。

当给定一个目录或多个文件时，**tiv** 会切换到 'dir' 模式并渲染缩略图网格（可用 **-f**/**-d** 覆盖）。为获得最佳效果，请使用支持真彩色（24 位）的终端。**-2** 的 256 色模式适用于较旧的终端，但输出质量较低。与标准字符相比，块字符可提供约 2 倍的垂直分辨率。

# CAVEATS

质量取决于终端能力和字体。支持真彩色的终端效果最佳。非 PNG 格式需要安装 ImageMagick。动画 GIF 只显示第一帧。不同终端模拟器之间的效果差异很大。

# HISTORY

**tiv** 是 Stefan Haustein 开发的 C++ TerminalImageViewer，一种不离开终端即可预览图像的轻量方式。它使用 RGB ANSI 码和 Unicode 块字符进行渲染，深受主要在终端中工作的开发者欢迎。还有几个无关的工具也提供 `tiv` 二进制文件，因此不同安装环境下的行为可能有所不同。

# INSTALL

```apt: sudo apt install tiv```

```brew: brew install tiv```

```nix: nix profile install nixpkgs#tiv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chafa](/man/chafa)(1), [viu](/man/viu)(1), [timg](/man/timg)(1), [catimg](/man/catimg)(1), [img2txt](/man/img2txt)(1), [jp2a](/man/jp2a)(1)
