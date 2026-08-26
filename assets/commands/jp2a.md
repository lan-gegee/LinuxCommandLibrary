# TAGLINE

将 JPEG 图像转换为 ASCII 字符画

# TLDR

**将图像转换为 ASCII**

```jp2a [image.jpg]```

**设置输出宽度**

```jp2a --width=[80] [image.jpg]```

**彩色 ASCII**

```jp2a --colors [image.jpg]```

**反转颜色**

```jp2a --invert [image.jpg]```

**自定义字符集**

```jp2a --chars="[.:-=+*#%@]" [image.jpg]```

**输出到文件**

```jp2a [image.jpg] --output=[output.txt]```

# SYNOPSIS

**jp2a** [_options_] _file_...

# PARAMETERS

_FILE_
> 要转换的图像文件。

**--width** _N_
> 以字符数表示的输出宽度。

**--height** _N_
> 输出高度。

**--colors**
> 使用 ANSI 颜色。

**--invert**
> 反转明暗。

**--chars** _STRING_
> 要使用的字符梯度。

**--output** _FILE_
> 输出文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jp2a** 将 JPEG 图像转换为 ASCII 字符画。它把像素亮度映射到字符上，实现基于文本的显示。

该工具支持终端彩色输出，可以处理多张图像和 URL。

# CAVEATS

仅接受 JPEG 输入。终端宽度会影响输出效果。需注意宽高比问题。

# HISTORY

jp2a 的诞生是为了将 JPEG 图像转换为 ASCII 字符画，用于终端显示和基于文本的图像呈现。

# INSTALL

```apt: sudo apt install jp2a```

```pacman: sudo pacman -S jp2a```

```zypper: sudo zypper install jp2a```

```brew: brew install jp2a```

```nix: nix profile install nixpkgs#jp2a```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[img2txt](/man/img2txt)(1), [cacaview](/man/cacaview)(1)
