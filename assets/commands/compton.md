# TAGLINE

X11 窗口系统的独立合成器

# TLDR

以默认设置**启动 compton**

```compton```

**使用配置文件启动**

```compton --config [~/.config/compton.conf]```

为窗口**启用阴影**

```compton -c```

为窗口**启用淡入淡出**效果

```compton -f```

**设置阴影不透明度**

```compton -c -o [0.5]```

对 dock 和面板窗口**禁用阴影**

```compton -c -C```

以后台守护进程方式**运行**

```compton -b```

**启用垂直同步**以防止画面撕裂

```compton --vsync opengl```

# SYNOPSIS

**compton** [_options_]

# PARAMETERS

**-c**, **--shadow**
> 为窗口启用客户端阴影。

**-C**, **--no-dock-shadow**
> 对 dock/面板窗口禁用阴影。

**-f**, **--fading**
> 在窗口打开/关闭时进行淡入/淡出。

**-o** _OPACITY_
> 阴影不透明度（0.0 到 1.0）。

**-r** _RADIUS_
> 阴影模糊半径（像素）。

**-l** _OFFSET_
> 阴影左偏移量（像素）。

**-t** _OFFSET_
> 阴影顶部偏移量（像素）。

**--vsync** _METHOD_
> 垂直同步方法：none、drm、opengl、opengl-oml、opengl-swc。

**-b**, **--daemon**
> 作为后台守护进程运行。

**--config** _FILE_
> 从指定文件读取配置。

**-i** _OPACITY_
> 非活动窗口的不透明度（0.0 到 1.0）。

**-e** _OPACITY_
> 窗口标题栏和边框的不透明度。

**--backend** _BACKEND_
> 渲染后端：xrender、glx。

# CONFIGURATION

**~/.config/compton.conf**
> compton 设置的用户配置文件。

**/etc/xdg/compton.conf**
> 系统级默认配置。

# DESCRIPTION

**compton** 是 X11 的独立合成器，提供窗口阴影、透明度、淡入淡出动画以及防止画面撕裂的垂直同步等视觉效果。它可以与任何支持合成的窗口管理器配合工作。

该合成器通过拦截窗口渲染并在显示最终图像之前应用特效来工作。它同时支持 XRender 和 OpenGL 后端，其中 GLX 通常能提供更好的性能。可以通过命令行选项或配置文件进行配置。

compton 常与 i3、openbox、bspwm 等轻量级窗口管理器搭配使用，在不承担完整桌面环境合成器开销的前提下增添视觉质感。它也有助于解决没有内置合成功能的系统上的画面撕裂问题。

# CAVEATS

Compton 的开发已经停止；**picom** 是持续维护的分支版本，推荐新安装使用。OpenGL 后端在某些图形驱动上可能存在兼容性问题。合成会增加 GPU 开销，在老旧硬件上可能影响性能。

# HISTORY

Compton 由 Christopher Jeffrey（chjj）于 **2011** 年从 **xcompmgr** 分支而来，旨在添加功能并修复缺陷。它凭借高度的可配置性在 Linux 美化社区广受欢迎。其开发在 **2017** 年前后陷入停滞，由此催生了持续维护的分支版本 **picom**。

# INSTALL

```apt: sudo apt install compton```

```dnf: sudo dnf install picom```

```pacman: sudo pacman -S picom```

```apk: sudo apk add picom```

```zypper: sudo zypper install picom```

```nix: nix profile install nixpkgs#picom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[picom](/man/picom)(1), [xcompmgr](/man/xcompmgr)(1), [i3](/man/i3)(1)

# RESOURCES

```[Source code](https://github.com/chjj/compton)```

<!-- verified: 2026-06-22 -->
