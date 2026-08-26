# TAGLINE

屏幕色温调节工具

# TLDR

**以自动定位方式启动**

```gammastep```

**设置手动位置**

```gammastep -l [37.7749:-122.4194]```

**设置色温**

```gammastep -t [6500:3500]```

**一次性模式（只应用一次）**

```gammastep -O [3500]```

**重置屏幕**

```gammastep -x```

**使用 Wayland 后端**

```gammastep -m wayland```

# SYNOPSIS

**gammastep** [_options_]

# PARAMETERS

**-l** _lat:lon_
> 手动位置（纬度:经度）。

**-t** _day:night_
> 色温（白天:夜间，开尔文）。

**-b** _day:night_
> 亮度（白天:夜间，0.1-1.0）。

**-O** _temp_
> 指定色温的一次性模式。

**-x**
> 重置并退出。

**-g** _R:G:B_
> 额外应用的伽马校正。

**-m** _method_
> 调节方法：randr、wayland、drm（用 -m list 查看可用选项）。

**-c** _file_
> 从指定配置文件加载设置。

**-o**
> 一次性模式（按当前时间应用一次，不持续调节）。

**-p**
> 打印模式（仅打印参数后退出）。

**-P**
> 应用前先重置已有的伽马映射表。

**-v**
> 详细输出。

**-V**
> 显示程序版本。

**-r**
> 禁用色温之间的渐变过渡。

# DESCRIPTION

**gammastep** 根据一天中的时间调整屏幕色温，以减轻眼睛疲劳并改善睡眠。它让屏幕在夜间偏暖（偏红），白天偏冷（偏蓝）。

Gammastep 是 Redshift 的分支，增加了 Wayland 支持。它常与平铺窗口管理器搭配使用，支持自动定位或手动坐标。

# CONFIGURATION

**~/.config/gammastep/config.ini**
> 用于配置色温、亮度和位置设置。

# CONFIGURATION EXAMPLE

```ini
# ~/.config/gammastep/config.ini
[general]
temp-day=6500
temp-night=3500
brightness-day=1.0
brightness-night=0.8

[manual]
lat=37.7749
lon=-122.4194
```

# CAVEATS

需要兼容的显示服务器（X11/Wayland）。自动定位需要 geoclue 或手动坐标。部分应用的颜色显示可能不准确。桌面环境的护眼夜光功能可能与之冲突。

# HISTORY

Gammastep 由 **Maxime Coste** 从 **Redshift** 分支而来，目的是增加 Wayland 支持。Redshift 由 **Jon Lund Steffensen** 于 2009 年创建，其依据是关于蓝光影响昼夜节律的研究。

# INSTALL

```apt: sudo apt install gammastep```

```dnf: sudo dnf install gammastep```

```pacman: sudo pacman -S gammastep```

```zypper: sudo zypper install gammastep```

```nix: nix profile install nixpkgs#gammastep```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redshift](/man/redshift)(1), [xrandr](/man/xrandr)(1), [wlsunset](/man/wlsunset)(1)
