# TAGLINE

OpenGL 旋转齿轮演示与健全性检查工具

# TLDR

**运行齿轮演示**（在终端中显示 FPS）

```glxgears```

**以全屏模式运行**

```glxgears -fullscreen```

**打印 OpenGL 渲染器信息**

```glxgears -info```

**以指定的窗口尺寸运行**

```glxgears -geometry [800x600]```

**启用立体渲染运行**（如果受支持）

```glxgears -stereo```

**不播放动画运行**（静态画面）

```glxgears -iacknowledgethatthistoolisnotabenchmark```

# SYNOPSIS

**glxgears** [_-display display_] [_-info_] [_-stereo_] [_-fullscreen_] [_-geometry WxH_]

# PARAMETERS

**-display** _display_
> 指定要使用的 X display。

**-info**
> 打印 OpenGL 渲染器和 GLX visual 信息。

**-stereo**
> 启用立体渲染（需要硬件支持）。

**-fullscreen**
> 以全屏模式运行。

**-geometry** _WxH_
> 设置窗口尺寸（宽 x 高）。

**-iacknowledgethatthistoolisnotabenchmark**
> 禁用动画（用于静态截图）。

# DESCRIPTION

**glxgears** 是一个渲染三个旋转齿轮的 OpenGL 演示程序。它每 5 秒在终端中显示一次帧率（FPS），因此常被用来验证 OpenGL 和 GPU 加速是否正常工作。

该程序创建一个简单的 GLX 窗口，并用 OpenGL 渲染经典的齿轮动画。工作正常时，现代系统通常能显示数千 FPS（在合成器开启时受 vsync 限制为显示器刷新率，未限流时则可能高得多）。

FPS 显示让 **glxgears** 成为快速的 GPU 健全性检查工具：如果你看到合理的 FPS（几百到几千）且动画流畅，说明 OpenGL 加速正常。FPS 极低（低于 60）可能表示软件渲染或驱动存在问题。

尽管常被当作"基准测试"使用，glxgears 对现代 GPU 能力的测试非常有限。它使用的是古老的 OpenGL 特性，不能代表真实应用的性能。

# CAVEATS

**不是有效的 GPU 性能基准测试**。FPS 会随 vsync、窗口大小、合成器和驱动设置大幅波动。只测试了最基础的 OpenGL 功能。无法检测许多 GPU 驱动问题。立体模式需要特定硬件。

# HISTORY

**glxgears** 由 Brian Paul 于 **1999** 年前后编写，是开源 OpenGL 实现 Mesa 的一部分。它最初只是用来测试 GLX（X11 的 OpenGL 扩展）功能的简单演示。尽管附有免责声明，但由于 FPS 计数一目了然，它仍被广泛误用作基准测试。"iacknowledgethatthistoolisnotabenchmark" 这个标志正是对这种误用的幽默回应。

# INSTALL

```apt: sudo apt install mesa-utils```

```pacman: sudo pacman -S mesa-utils```

```apk: sudo apk add mesa-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glxinfo](/man/glxinfo)(1), [vulkaninfo](/man/vulkaninfo)(1), [xdpyinfo](/man/xdpyinfo)(1), [vkcube](/man/vkcube)(1)
