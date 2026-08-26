# TAGLINE

Hyprland（动态平铺 Wayland 合成器）的蓝光过滤工具

# TLDR

**启动**蓝光过滤服务

```hyprsunset```

以指定的**色温**和 **gamma 值**启动

```hyprsunset -t [4000] -g [90]```

运行时**调整色温**（通过 hyprctl）

```hyprctl hyprsunset temperature [4000]```

运行时**调整 gamma 值**（通过 hyprctl）

```hyprctl hyprsunset gamma [90]```

将色温**重置**为默认值（6000K）

```hyprctl hyprsunset reset temperature```

将 gamma 值**重置**为默认值（100%）

```hyprctl hyprsunset reset gamma```

# SYNOPSIS

**hyprsunset** [_options_]

# PARAMETERS

**-t**, **--temperature** _KELVIN_
> 以开尔文设置色温（越低越暖，默认：6000K）

**-g**, **--gamma** _PERCENT_
> 设置 gamma 百分比（默认：100%）

**--identity**
> 禁用色温调整；仅 gamma 变更生效

# DESCRIPTION

**hyprsunset** 是 Hyprland（动态平铺 Wayland 合成器）的蓝光过滤工具。它调整屏幕色温以减少蓝光发射，有助于减轻眼部疲劳并改善夜间使用电脑时的睡眠质量。

服务启动后，可以使用 hyprctl 命令动态调整设置，无需重启。这种方式优于屏幕着色器，因为其效果不会被录屏或截图捕获。

较低的色温值（例如 3000K-4000K）会产生偏暖、偏橙的色彩，适合夜间使用。默认的 6000K 代表标准的日光白。

# CAVEATS

仅适用于 Hyprland 合成器，且要求 Hyprland 正在运行。更改会影响所有显示器。可能干扰对色彩要求精确的工作（如照片编辑）。

# HISTORY

hyprsunset 是 Hyprland 生态的一部分，由 Vaxry 创建。它提供与 redshift 或 gammastep 类似的功能，但专为 Hyprland Wayland 合成器设计。

# INSTALL

```pacman: sudo pacman -S hyprsunset```

```zypper: sudo zypper install hyprsunset```

```nix: nix profile install nixpkgs#hyprsunset```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hyprctl](/man/hyprctl)(1), [redshift](/man/redshift)(1), [gammastep](/man/gammastep)(1)
