# TAGLINE

在 X Window 系统上显示图像

# TLDR

**显示一张图片**

```display [image.jpg]```

**以指定的窗口标题**显示

```display -title "[My Image]" [image.jpg]```

**显示并调整大小**

```display -resize [800x600] [image.jpg]```

以幻灯片形式**显示多张图片**

```display [*.jpg]```

**从 URL 显示**

```display "[https://example.com/image.jpg]"```

**按窗口几何尺寸**显示

```display -geometry [+100+100] [image.jpg]```

# SYNOPSIS

**magick display** [_options_] _input-file_

# PARAMETERS

_FILE_
> 要显示的图像文件。

**-resize** _GEOMETRY_
> 将图像调整为指定尺寸。

**-title** _STRING_
> 窗口标题。

**-geometry** _GEOMETRY_
> 窗口位置和大小。

**-delay** _centiseconds_
> 幻灯片中图像之间的延迟（单位为百分之一秒）。

**-update** _seconds_
> 检测图像文件被修改并重新显示。

**-loop** _iterations_
> 循环播放图像后退出。

**-immutable**
> 防止图像被修改。

**-verbose**
> 打印图像的详细信息。

**-help**
> 显示帮助信息。

# DESCRIPTION

**display** 是一个 ImageMagick 程序，用于在 X Window 系统上显示图像。它提供支持缩放、平移和基本编辑功能的交互式查看器。在 ImageMagick 7 中，需以 **magick display** 调用。

该查看器通过 ImageMagick 的格式处理支持众多图像格式。交互功能包括缩放、旋转、裁剪、颜色调整和标注。多张图像可以幻灯片方式查看。

display 提供一个点击图像即可打开的命令菜单，可进行变换、特效和文件操作。修改后的图像可以保存为多种格式。

# CAVEATS

需要 X11 显示环境。处理大图像时资源占用较高。功能丰富的界面对简单的查看需求可能过于复杂。属于 ImageMagick，后者曾发布过安全公告。

# HISTORY

display 是 **ImageMagick** 的一部分，由 **John Cristy** 于 **1987** 年创建。数十年来 ImageMagick 一直是首选的开源图像处理套件，而 display 则提供交互式可视化能力。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [eog](/man/eog)(1), [convert](/man/convert)(1), [identify](/man/identify)(1), [magick](/man/magick)(1), [mogrify](/man/mogrify)(1)
