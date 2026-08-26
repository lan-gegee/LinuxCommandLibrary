# TAGLINE

配置 NVIDIA 显卡驱动设置

# TLDR

**打开设置图形界面**

```nvidia-settings```

**查询 GPU 温度**

```nvidia-settings -q GPUCoreTemp```

**设置风扇转速**

```nvidia-settings -a "[gpu:0]/GPUFanControlState=1" -a "[fan:0]/GPUTargetFanSpeed=[70]"```

**查询所有属性**

```nvidia-settings -q all```

**从文件加载设置**

```nvidia-settings --load-config-only```

**设置 PowerMizer 模式**

```nvidia-settings -a "[gpu:0]/GPUPowerMizerMode=[1]"```

# SYNOPSIS

**nvidia-settings** [_options_]

# PARAMETERS

**-q** _attr_
> 查询属性。

**-a** _attr=value_
> 赋值属性。

**-c** _display_
> 要使用的 X display。

**--load-config-only**
> 加载配置后退出。

**-t**
> 简洁输出。

**-V** _attr_
> 显示有效取值。

# DESCRIPTION

**nvidia-settings** 用于配置 NVIDIA 显卡驱动设置。它提供图形界面和命令行接口，用于调整显示、性能和 GPU 设置。

# COMMON ATTRIBUTES

```
GPUCoreTemp          - GPU temperature
GPUCurrentClockFreqs - Clock speeds
GPUFanControlState   - Manual fan control
GPUTargetFanSpeed    - Fan speed %
GPUPowerMizerMode    - Performance mode
```

# CONFIG FILE

```
# ~/.nvidia-settings-rc
[gpu:0]/GPUPowerMizerMode=1
[gpu:0]/GPUFanControlState=1
```

# CAVEATS

需要 NVIDIA 专有驱动。部分设置需要 X 正在运行。风扇控制可能导致保修失效。驱动更新后设置会重置。

# HISTORY

nvidia-settings 由 **NVIDIA Corporation** 开发，是其 Linux 显卡驱动的官方配置工具。

# INSTALL

```pacman: sudo pacman -S nvidia-settings```

```zypper: sudo zypper install nvidia-settings```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [xrandr](/man/xrandr)(1)
