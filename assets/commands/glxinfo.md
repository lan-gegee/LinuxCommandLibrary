# TAGLINE

OpenGL 与 GLX 能力显示工具

# TLDR

**显示 OpenGL 信息**

```glxinfo```

**显示简要摘要**

```glxinfo -B```

**只显示厂商和版本信息**

```glxinfo | grep "OpenGL"```

**列出受支持的扩展**

```glxinfo | grep "GL_"```

**在指定屏幕上显示**

```DISPLAY=:0 glxinfo```

**显示详细的限制信息**

```glxinfo -l```

# SYNOPSIS

**glxinfo** [_options_]

# PARAMETERS

**-B**
> 简要输出（仅摘要）。

**-l**
> 显示扩展限制。

**-v**
> 以详细输出显示 visual 列表。

**-t**
> 为 visual 列表生成更宽、更易读的表格格式。

**-s**
> 每行打印一个扩展。

**-i**
> 强制间接渲染。

**-b**
> 找出"最佳"的 visual 并打印其编号。

**-display** _dpy_
> 指定 X display。

**-h**
> 显示帮助。

# DESCRIPTION

**glxinfo** 显示图形系统的 GLX 实现和 OpenGL 能力信息。它可用于诊断显卡驱动问题和检查硬件能力。

该工具查询 X server 和显卡驱动，报告 OpenGL 版本、渲染器、厂商以及受支持的扩展。

# CAVEATS

需要连接 X server。结果取决于驱动和配置。间接渲染可能显示不同的能力。Wayland 下需要 XWayland。

# HISTORY

**glxinfo** 是 **mesa-utils** 软件包的一部分，与 **Mesa** 3D 图形库相关联。Mesa 由 **Brian Paul** 于 **1993** 年启动，自 GLX 早期开始，glxinfo 就一直是 X11 系统上 OpenGL 的标准诊断工具。

# INSTALL

```apt: sudo apt install mesa-utils```

```pacman: sudo pacman -S mesa-utils```

```apk: sudo apk add mesa-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glxgears](/man/glxgears)(1), [xdpyinfo](/man/xdpyinfo)(1), [vulkaninfo](/man/vulkaninfo)(1), [nvidia-smi](/man/nvidia-smi)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/mesa/demos)```

```[Manual page](https://manpages.debian.org/testing/mesa-utils/glxinfo.1.en.html)```

<!-- verified: 2026-07-17 -->
