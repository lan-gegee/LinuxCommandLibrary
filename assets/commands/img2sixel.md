# TAGLINE

将图像转换为 Sixel 格式以便在终端中显示

# TLDR

**在终端中显示图像**

```img2sixel [image.png]```

**设置宽度**

```img2sixel -w [800] [image.png]```

**设置高度**

```img2sixel -h [600] [image.png]```

**指定颜色数**

```img2sixel -p [256] [image.png]```

**管道传输输出**

```curl [url/image.png] | img2sixel```

# SYNOPSIS

**img2sixel** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要显示的图像文件。

**-w** _WIDTH_
> 以像素为单位的输出宽度。

**-h** _HEIGHT_
> 以像素为单位的输出高度。

**-p** _COLORS_
> 颜色数。

**-d** _DIFFUSION_
> 抖动方法。

**-e**
> 仅编码（不显示）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**img2sixel** 将图像转换为 Sixel 格式以便在终端中显示。Sixel 让兼容的终端能够显示内联图形。

该工具支持多种图像格式，并输出 Sixel 转义序列。它可用于 xterm、mlterm 等终端。

# CAVEATS

需要支持 Sixel 的终端。属于 libsixel 项目。画质取决于颜色数。

# HISTORY

img2sixel 是 **Hayaki Saito** 开发的 **libsixel** 的一部分，用于终端图形显示。

# INSTALL

```apt: sudo apt install libsixel-bin```

```apk: sudo apk add libsixel-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[viu](/man/viu)(1), [chafa](/man/chafa)(1), [timg](/man/timg)(1)
