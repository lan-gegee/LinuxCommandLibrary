# TAGLINE

计算 VESA Generalized Timing Formula 时序行

# TLDR

**生成 1920x1080@60Hz 的时序行**

```gtf 1920 1080 60```

**按指定刷新率生成**

```gtf [1280] [1024] [75]```

**以 X 格式输出**

```gtf 1920 1080 60 -x```

**详细输出**

```gtf 1920 1080 60 -v```

# SYNOPSIS

**gtf** _h-pixels_ _v-pixels_ _refresh_ [_options_]

# PARAMETERS

_H-PIXELS_
> 水平分辨率。

_V-PIXELS_
> 垂直分辨率。

_REFRESH_
> 以 Hz 为单位的刷新率。

**-x**
> 以 X11 modeline 格式输出。

**-v**, **--verbose**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gtf** 计算 VESA Generalized Timing Formula 时序行。它为特定分辨率下的 X11 配置生成所需的时序参数。

该工具输出适用于 xorg.conf 的 modeline。对于未被自动检测到的自定义显示模式，它很有用。

# CAVEATS

现代系统会自动检测模式。可能损坏老旧显示器。较新的标准请使用 cvt。

# HISTORY

gtf 为 **XFree86/X.Org** 开发，用于生成符合 VESA GTF 规范的时序行以配置显示器。

# INSTALL

```apt: sudo apt install xserver-xorg-core```

```pacman: sudo pacman -S xorg-server```

```apk: sudo apk add xorg-server```

```brew: brew install xorg-server```

```nix: nix profile install nixpkgs#xorg-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cvt](/man/cvt)(1), [xrandr](/man/xrandr)(1)
