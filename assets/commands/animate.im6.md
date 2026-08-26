# TAGLINE

以动画形式显示图像序列（ImageMagick 6）

# TLDR

**播放**图像动画（ImageMagick 6）

```animate.im6 [image1.png] [image2.png]```

播放**动态 GIF**

```animate.im6 [animation.gif]```

设置**帧延迟**

```animate.im6 -delay [10] [*.png]```

设置**无限循环**

```animate.im6 -loop [0] [animation.gif]```

# SYNOPSIS

**animate.im6** [_options_] _files_

# DESCRIPTION

**animate.im6** 是 animate 命令的 ImageMagick 6 版本，用于同时安装了 ImageMagick 6 和 7 的系统。它在 X Window 中将图像序列显示为动画。

.im6 后缀将其与 ImageMagick 7 版本区分开，使两个版本可以在同一系统上共存。

# PARAMETERS

**-delay** _ticks_
> 帧间延迟（百分之一秒）

**-loop** _count_
> 循环次数（0 = 无限）

**-geometry** _WxH_
> 显示几何尺寸

**-coalesce**
> 合并 GIF 动画图层

**-remote**
> 启用远程控制

# CAVEATS

这是 ImageMagick 6 版本；语法可能与 ImageMagick 7 略有不同。需要 X Window 系统。某些选项在较新版本中可能已被弃用。

# HISTORY

.im6 命名约定是在 **2016** 年 ImageMagick 7 发布时引入的，允许两个主要版本并行安装。

# SEE ALSO

[animate](/man/animate)(1), [display.im6](/man/display.im6)(1)
