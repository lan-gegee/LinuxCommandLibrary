# TAGLINE

X11 桌面泰迪熊吉祥物

# TLDR

**显示泰迪熊**

```xteddy```

**使用不同图片**

```xteddy -f [image.png]```

**在指定位置启动**

```xteddy -geometry [+100+100]```

# SYNOPSIS

**xteddy** [_-f image_] [_-geometry pos_] [_options_]

# PARAMETERS

**-f** _FILE_
> 图片文件。

**-geometry** _POS_
> 窗口位置。

**-display** _DPY_
> X display。

# DESCRIPTION

**xteddy** 是一款经典的 X11 桌面玩具，它在一个异形无边框窗口中显示泰迪熊图片。可以用鼠标把小熊拖到屏幕上的任意位置，充当有趣的桌面伙伴。点击泰迪熊即可退出程序。

可以通过 **-f** 选项提供自定义图片，用任意 PNG 图像替代默认的泰迪熊。该程序是 X11 异形窗口能力的一个轻松示例，也是桌面个性化早期岁月里令人怀念的小玩意。

# CAVEATS

仅支持 X11。纯属娱乐。怀旧之作。

# HISTORY

**xteddy** 是一款经典的 X11 桌面玩具，显示一只可在屏幕上拖动的泰迪熊。

# INSTALL

```dnf: sudo dnf install xteddy```

```zypper: sudo zypper install xteddy```

```nix: nix profile install nixpkgs#xteddy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xeyes](/man/xeyes)(1), [oneko](/man/oneko)(1), [xcowsay](/man/xcowsay)(1)
