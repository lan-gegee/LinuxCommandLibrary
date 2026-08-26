# TAGLINE

ImageMagick 6 版本的 identify

# TLDR

**显示图片信息**

```identify.im6 [image.jpg]```

**详细输出**

```identify.im6 -verbose [image.png]```

**自定义格式**

```identify.im6 -format "%wx%h" [image]```

**快速探测模式**

```identify.im6 -ping [image.jpg]```

# SYNOPSIS

**identify.im6** [_options_] _files_

# PARAMETERS

_FILES_
> 要识别的图片文件。

**-verbose**
> 详细信息。

**-format** _STRING_
> 自定义格式字符串。

**-ping**
> 快速识别。

**--help**
> 显示帮助信息。

# DESCRIPTION

**identify.im6** 是 ImageMagick 6 版本的 identify。用于描述图片的格式、尺寸和特性。

该工具与 identify 功能相同，但专门来自 ImageMagick 第 6 版。两者可能共存于同一系统。

# CAVEATS

ImageMagick 6 特有。可能与 IM7 冲突。属于旧版本。

# HISTORY

identify.im6 是 **ImageMagick 6** 的一部分，与 ImageMagick 7 分开维护。

# SEE ALSO

[identify](/man/identify)(1), [mogrify.im6](/man/mogrify.im6)(1)
