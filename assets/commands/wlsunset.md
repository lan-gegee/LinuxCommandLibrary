# TAGLINE

Wayland 屏幕色温调节器

# TLDR

**根据位置启动**

```wlsunset -l [51.5] -L [-0.1]```

**手动设置色温**

```wlsunset -t [4000] -T [6500]```

**设置 gamma 值**

```wlsunset -g [0.9]```

**指定输出设备**

```wlsunset -o [DP-1]```

# SYNOPSIS

**wlsunset** [_-l lat_] [_-L lon_] [_-t temp_] [_-T temp_] [_options_]

# PARAMETERS

**-l** _LAT_
> 纬度。

**-L** _LON_
> 经度。

**-t** _TEMP_
> 夜间色温。

**-T** _TEMP_
> 白天色温。

**-g** _GAMMA_
> gamma 值。

**-o** _OUTPUT_
> 指定输出设备。

# DESCRIPTION

**wlsunset** 是面向基于 wlroots 的 Wayland 合成器的昼夜屏幕色温守护进程。它根据一天中的时间自动调整显示器色温，在傍晚切换为较暖的色调，以减少蓝光照射。

日出和日落时间根据提供的地理坐标计算，在可配置的白天与夜间色温之间平滑过渡。还可以调整 gamma 值对显示做进一步微调。该工具以后台守护进程方式运行，是 redshift 或 f.lux 的 Wayland 原生等价物。

# CAVEATS

仅支持 Wayland。需要 wlroots。自动模式需要位置信息。

# HISTORY

**wlsunset** 作为 redshift 的 Wayland 原生替代方案而创建，用于调节屏幕色温。

# INSTALL

```apt: sudo apt install wlsunset```

```dnf: sudo dnf install wlsunset```

```pacman: sudo pacman -S wlsunset```

```apk: sudo apk add wlsunset```

```zypper: sudo zypper install wlsunset```

```nix: nix profile install nixpkgs#wlsunset```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redshift](/man/redshift)(1), [gammastep](/man/gammastep)(1)
