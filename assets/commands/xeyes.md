# TAGLINE

X11 鼠标追踪眼睛演示程序

# TLDR

**启动** xeyes

```xeyes```

在**远程**显示器上启动

```xeyes -display [remote_host]:[0].[0]```

# SYNOPSIS

**xeyes** [_OPTIONS_]

# PARAMETERS

**-display** _HOST:DISPLAY.SCREEN_
> 要连接的 X 显示器

**-geometry** _WxH+X+Y_
> 窗口大小和位置

**-fg** _COLOR_
> 前景色

**-bg** _COLOR_
> 背景色

**-center** _COLOR_
> 瞳孔中心的颜色

# DESCRIPTION

**xeyes** 在屏幕上显示一双跟随鼠标光标移动的眼睛。它是一个经典的 X11 演示程序，常用于验证 X11 显示连接是否正常。

这双眼睛会追踪鼠标指针在整个屏幕上的位置。

# HISTORY

**xeyes** 是最早的 X11 演示程序之一，可以追溯到 20 世纪 80 年代。它作为简单的测试和趣味应用，一直随 X Window System 发行版一同提供。

# CAVEATS

仅支持 X11。除测试显示连接外实际用途有限。

# INSTALL

```apt: sudo apt install x11-apps```

```dnf: sudo dnf install xeyes```

```apk: sudo apk add xeyes```

```zypper: sudo zypper install xeyes```

```brew: brew install xeyes```

```nix: nix profile install nixpkgs#xeyes```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xclock](/man/xclock)(1), [xlogo](/man/xlogo)(1)
