# TAGLINE

轻量级 X11 壁纸设置工具

# TLDR

**居中设置壁纸**

```xwallpaper --center [image.jpg]```

**缩放填满设置壁纸**

```xwallpaper --zoom [image.jpg]```

**拉伸以适应屏幕**

```xwallpaper --stretch [image.jpg]```

**平铺壁纸**

```xwallpaper --tile [image.png]```

**为特定输出设置**

```xwallpaper --output [HDMI-1] --zoom [image.jpg]```

**每个输出使用不同壁纸**

```xwallpaper --output [HDMI-1] --zoom [wall1.jpg] --output [eDP-1] --center [wall2.jpg]```

以守护进程方式**运行**以响应输出变化

```xwallpaper --daemon --zoom [image.jpg]```

# SYNOPSIS

**xwallpaper** [_options_] [_mode_] _file_...

# PARAMETERS

**--center** _file_
> 居中显示图片，不缩放。

**--zoom** _file_
> 缩放至填满，必要时裁剪。

**--maximize** _file_
> 缩放以适应屏幕，不裁剪。

**--stretch** _file_
> 拉伸填满，忽略宽高比。

**--tile** _file_
> 从左上角开始平铺图片。

**--focus** _file_
> 配合 --trim 聚焦于选定区域。

**--output** _name_
> 定位到特定输出（可用 xrandr 列出）。

**--screen** _screen_
> 定位到特定的 X screen。

**--trim** _WxH[+X+Y]_
> 裁剪输入图像。

**--daemon**
> 输出变化时重新绘制。

**--clear**
> 清除壁纸。

**--no-randr**
> 禁用 RandR 支持。

**--no-atoms**
> 不设置壁纸 atom。

**--debug**
> 启用调试输出。

**--version**
> 显示版本信息。

# DESCRIPTION

**xwallpaper** 是一款 X11 壁纸设置工具。它支持 JPEG、PNG 和 XPM 格式，并提供多种缩放模式以适应不同的显示配置。

该工具通过 RandR 支持多显示器设置，可以为每个输出设置不同的壁纸。守护进程模式下，它会监视输出变化，并在显示器连接或分辨率改变时自动重绘壁纸。

它会设置壁纸 atom，以支持兼容应用中的半透明背景。

Wayland 下请改用 swaybg 或 wbg。

# CAVEATS

仅支持 X11；纯 Wayland 环境下无法工作。守护进程模式需要 RandR 支持。图像格式取决于编译配置。某些窗口管理器可能会覆盖壁纸。

# HISTORY

**xwallpaper** 由 Tobias Stoeckmann 创建，是一款轻量、依赖极少的 X11 壁纸设置工具。与 feh 等大型工具相比，它更注重正确性和最小的资源占用。

# INSTALL

```apt: sudo apt install xwallpaper```

```pacman: sudo pacman -S xwallpaper```

```apk: sudo apk add xwallpaper```

```zypper: sudo zypper install xwallpaper```

```nix: nix profile install nixpkgs#xwallpaper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[feh](/man/feh)(1), [nitrogen](/man/nitrogen)(1), [hsetroot](/man/hsetroot)(1), [xrandr](/man/xrandr)(1)
