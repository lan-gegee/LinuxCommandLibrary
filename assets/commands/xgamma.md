# TAGLINE

调整 X11 显示器伽马校正

# TLDR

**显示当前伽马值**

```xgamma```

**为所有通道设置伽马**

```xgamma -gamma [1.2]```

**分别设置各通道的伽马**

```xgamma -rgamma [1.1] -ggamma [1.0] -bgamma [0.9]```

**在指定显示器上设置伽马**

```xgamma -display [:0] -gamma [1.2]```

**在指定屏幕上设置伽马**

```xgamma -screen [0] -gamma [1.1]```

# SYNOPSIS

**xgamma** [_options_]

# PARAMETERS

**-gamma** _value_
> 为所有颜色通道设置伽马。

**-rgamma** _value_
> 设置红色通道的伽马。

**-ggamma** _value_
> 设置绿色通道的伽马。

**-bgamma** _value_
> 设置蓝色通道的伽马。

**-display** _name_
> 要使用的 X 显示器。

**-screen** _num_
> 要调整的屏幕编号。

**-quiet**
> 抑制正常输出。

**-help**
> 显示用法摘要并退出。

# DESCRIPTION

**xgamma** 通过 XFree86-VidModeExtension 查询和修改显示器的伽马校正。伽马会影响中间调亮度；低于 1.0 的值会增大对比度，高于 1.0 的值会减小对比度。

不带伽马参数调用时，xgamma 会将当前的红色、绿色和蓝色伽马值打印到标准输出。伽马值以三位小数的精度传输给 X server。红、绿、蓝三个通道可分别控制，从而实现色温调整。

设置是临时的，X server 重启后会恢复原状。若要持久化，可将 xgamma 命令加入 ~/.xinitrc 或 ~/.xprofile，或在 xorg.conf 中配置。**DISPLAY** 环境变量提供默认的主机和显示器编号。

# CAVEATS

仅支持 X11，对 Wayland 无效。不通过脚本处理时，设置不会在重启后保留。可能与 Redshift 等色彩管理工具冲突。硬件支持情况因设备而异。

# HISTORY

**xgamma** 是 X.Org 工具集的一部分，最初由 **Kaleb Keithley** 和 **David Dawes** 编写。它依赖的 XFree86-VidModeExtension 已被视为过时；现代环境应改用支持 RandR 1.2+ 伽马属性的 **xrandr**。

# INSTALL

```apt: sudo apt install x11-xserver-utils```

```dnf: sudo dnf install xgamma```

```apk: sudo apk add xgamma```

```zypper: sudo zypper install xgamma```

```nix: nix profile install nixpkgs#xgamma```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xrandr](/man/xrandr)(1), [redshift](/man/redshift)(1)
