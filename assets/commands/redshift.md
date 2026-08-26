# TAGLINE

调节屏幕色温以保护眼睛

# TLDR

**启动 redshift** 并自动检测位置

```redshift```

**手动设置色温**（白天:夜间）

```redshift -O [3500]```

**设置白天和夜间色温**

```redshift -t [5500]:[3500]```

**手动设置位置**（纬度:经度）

```redshift -l [40.7]:[74.0]```

**将屏幕重置为正常色温**

```redshift -x```

**以一次性模式运行**（设置后退出）

```redshift -o```

**打印当前色温**

```redshift -p```

# SYNOPSIS

**redshift** [**-l** _lat_:_lon_] [**-t** _day_:_night_] [**-b** _day_:_night_] [**-m** _method_] [_options_]

# PARAMETERS

**-l** _lat_:_lon_
> 设置位置（纬度:经度），用于计算日出/日落时间

**-t** _day_:_night_
> 设置色温，单位开尔文（默认：5500:3500）

**-b** _day_:_night_
> 设置屏幕亮度（0.1-1.0）

**-O** _temp_
> 立即设置指定色温

**-o**
> 一次性模式；设置色温后退出

**-x**
> 将色温重置为默认值

**-p**
> 打印当前设置和参数

**-m** _method_
> 调节方法（randr、vidmode、drm、wayland）

**-g** _r_:_g_:_b_
> 设置伽马校正

**-r**
> 禁用色温渐变过渡

**-v**
> 详细输出

**-c** _file_
> 从文件加载配置

# DESCRIPTION

**redshift** 根据一天中的时间调节屏幕色温，减少夜间的蓝光暴露。通过使屏幕颜色与环境光线相匹配，这有助于缓解眼睛疲劳并改善睡眠质量。

白天，屏幕保持正常色温（约 5500-6500K）。日落之后，redshift 逐渐过渡到更暖的颜色（3000-4000K），减少可能干扰昼夜节律的蓝光。

位置可以通过地理位置服务（geoclue）自动确定，也可以手动指定。程序会持续运行，根据计算出的日出和日落时间全天调节色温。

不同后端支持不同的显示系统：X11 使用 **randr**，Wayland 合成器使用 **wayland**，控制台/帧缓冲使用 **drm**。

# CONFIGURATION

**~/.config/redshift/redshift.conf**
> 用户配置文件，用于指定默认位置、色温范围、亮度、调节方法和过渡设置。

# CAVEATS

自动位置检测需要 geoclue 及相应权限。如果检测失败，请用 **-l** 手动指定位置。

某些应用（照片/视频编辑、对颜色敏感的工作）可能需要准确的颜色。可使用 **redshift -x** 暂时禁用调节，或排除特定时间段。

Wayland 支持取决于合成器的支持情况。一些 Wayland 合成器实现了自己的夜间模式功能。

同时运行多个实例可能引发冲突。请使用单个实例，或与桌面环境的夜间模式设置集成。

# INSTALL

```apt: sudo apt install redshift```

```dnf: sudo dnf install redshift```

```pacman: sudo pacman -S redshift```

```apk: sudo apk add redshift```

```zypper: sudo zypper install redshift```

```brew: brew install redshift```

```nix: nix profile install nixpkgs#redshift```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xrandr](/man/xrandr)(1), [xgamma](/man/xgamma)(1), [gammastep](/man/gammastep)(1)
