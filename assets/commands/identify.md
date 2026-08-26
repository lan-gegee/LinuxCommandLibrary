# TAGLINE

描述图片格式和特性

# TLDR

**显示图片信息**

```identify [image.jpg]```

**详细信息**

```identify -verbose [image.png]```

**显示特定属性**

```identify -format "%wx%h" [image.jpg]```

**检查多张图片**

```identify [*.png]```

**只显示格式**

```identify -format "%m\n" [image]```

# SYNOPSIS

**identify** [_options_] _files_

# PARAMETERS

_FILES_
> 要识别的图片文件。

**-verbose**
> 详细输出。

**-format** _STRING_
> 自定义输出格式。

**-quiet**
> 抑制警告。

**-ping**
> 高效获取图片属性，无需完整解码像素。

**-regard-warnings**
> 加载图片时关注警告信息。

**-list** _type_
> 列出指定选项支持的取值（如 format、color）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**identify** 描述图片的格式和特性。它显示尺寸、颜色深度、格式以及其他元数据。

该工具是 ImageMagick 的一部分。它能读取多种图片格式，并提供关于图片的详细技术信息。在 ImageMagick 7 中，等价命令为 **magick identify**。

# CAVEATS

属于 ImageMagick。大图片会占用内存。某些格式需要委托（delegate）程序支持。

# HISTORY

identify 是 **ImageMagick** 的组成部分，后者是功能全面的图像处理套件。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[convert](/man/convert)(1), [mogrify](/man/mogrify)(1), [magick](/man/magick)(1), [file](/man/file)(1)
