# TAGLINE

VESA CVT 显示 modeline 计算器

# TLDR

为指定分辨率和刷新率**生成 modeline**

```cvt [1920] [1080] [60]```

生成缩减消隐 modeline（适用于 LCD 显示器）

```cvt -r [1920] [1080] [60]```

使用缩减消隐 v2 生成 modeline

```cvt -r2 [2560] [1440] [144]```

生成含更多细节的详细输出

```cvt -v [1920] [1200] [75]```

# SYNOPSIS

**cvt** [_options_] _width_ _height_ [_refresh_]

# PARAMETERS

_WIDTH_
> 水平分辨率（像素）。

_HEIGHT_
> 垂直分辨率（像素）。

_REFRESH_
> 刷新率（Hz，默认：60）。

**-r**, **--reduced**
> 生成缩减消隐时序（CVT-RB）。

**-r2**, **--reduced-v2**
> 生成缩减消隐 v2 时序（CVT-RBv2）。

**-v**, **--verbose**
> 启用详细输出。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**cvt** 为 X11 显示配置计算 VESA Coordinated Video Timing（CVT）modeline。它输出适合配合 xrandr 使用或写入 xorg.conf 文件的 modeline 参数。

CVT 是根据分辨率和刷新率计算显示时序参数的标准公式。该工具生成的时序值包括像素时钟、水平和垂直同步参数以及消隐间隔。

缩减消隐模式（**-r**、**-r2**）专为 LCD 显示器和数字连接（HDMI、DisplayPort）设计，比传统兼容 CRT 的时序占用更少带宽。这使得在有限带宽的连接上实现更高的分辨率和刷新率成为可能。

# CAVEATS

生成的 modeline 不一定被所有显示器或显卡硬件支持。缩减消隐与 CRT 显示器不兼容。错误的自定义时序可能损坏显示器。务必确认时序处于显示器规格范围之内。

# HISTORY

CVT 标准由 **VESA**（视频电子标准协会）制定，提供了一种标准化的显示时序计算方法。cvt 工具是 xorg-server 工具集的一部分，实现了 CVT 1.1 和 CVT-RB 规范。

# INSTALL

```apt: sudo apt install xcvt```

```dnf: sudo dnf install libxcvt```

```pacman: sudo pacman -S libxcvt```

```apk: sudo apk add libxcvt```

```zypper: sudo zypper install libxcvt```

```brew: brew install libxcvt```

```nix: nix profile install nixpkgs#libxcvt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gtf](/man/gtf)(1), [xrandr](/man/xrandr)(1)
