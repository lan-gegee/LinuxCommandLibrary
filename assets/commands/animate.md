# TAGLINE

以动画形式显示图像序列

# TLDR

**播放**图像序列动画

```animate [image1.png] [image2.png] [image3.png]```

播放 **GIF** 文件

```animate [animation.gif]```

设置帧间**延迟**（单位为百分之一秒）

```animate -delay [50] [*.png]```

**循环**播放动画

```animate -loop [0] [animation.gif]```

设置**显示尺寸**

```animate -geometry [800x600] [animation.gif]```

# SYNOPSIS

**animate** [_options_] _files_

# DESCRIPTION

**animate** 是一款 ImageMagick 工具，可在 X Window 中将图像序列显示为动画。它支持众多图像格式，可以播放动态 GIF、多页文件或独立图像组成的序列。

该查看器提供交互式播放控制，包括暂停、单步播放、速度调节和循环选项。

# PARAMETERS

**-delay** _ticks_
> 帧间延迟（百分之一秒）

**-loop** _count_
> 循环次数（0 = 无限）

**-geometry** _WxH_
> 窗口尺寸

**-colorspace** _type_
> 图像色彩空间

**-coalesce**
> 将 GIF 动画序列合并为完整帧

**-dispose** _method_
> 帧处置方式

**-display** _server_
> 显示动画的 X server

**-backdrop**
> 在背景上居中显示图像

**-window** _id_
> 在已有窗口中显示

**-remote** _command_
> 向已在运行的 animate 程序发送命令

**-pause** _seconds_
> 每次动画循环结束后的额外停顿

# CAVEATS

需要 X Window 系统。大型动画会占用大量内存。并非所有系统上的帧时序都精确。在某些使用场景下已被带 -coalesce 的 display 命令取代。

# HISTORY

自 **1990** 年代初以来，**animate** 就一直是 ImageMagick 的一部分，为图像处理工作流提供动画预览功能。

# INSTALL

```pacman: sudo pacman -S imagemagick```

```apk: sudo apk add imagemagick```

```brew: brew install imagemagick```

```nix: nix profile install nixpkgs#imagemagick```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[display](/man/display)(1), [magick](/man/magick)(1), [convert](/man/convert)(1), [identify](/man/identify)(1)

# RESOURCES

```[Source code](https://github.com/ImageMagick/ImageMagick)```

```[Homepage](https://imagemagick.org)```

```[Documentation](https://imagemagick.org/script/animate.php)```

<!-- verified: 2026-06-11 -->
