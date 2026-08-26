# TAGLINE

显示图像文件的信息

# TLDR

**显示图像信息**

```magick identify [image.png]```

**显示详细信息**

```magick identify -verbose [image.png]```

**显示特定属性**

```magick identify -format "%wx%h" [image.png]```

**显示目录中的所有图像**

```magick identify [*.jpg]```

# SYNOPSIS

**magick** **identify** [_options_] _image_...

# PARAMETERS

**-verbose**
> 显示详细信息。

**-format** _string_
> 输出格式字符串。

**-quiet**
> 抑制警告。

**-ping**
> 只读取基本属性。

# DESCRIPTION

**magick identify** 显示图像文件的信息。它是 ImageMagick 的一部分，可展示格式、尺寸、色彩空间、文件大小以及其他元数据。支持通过格式字符串自定义输出。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[magick](/man/magick)(1), [file](/man/file)(1)
