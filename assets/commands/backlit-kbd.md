# TAGLINE

控制 Linux 键盘背光亮度

# TLDR

**显示当前背光**状态及设备信息

```backlit-kbd info```

按百分比**设置亮度**（0-100）

```backlit-kbd percent [75]```

按原始电平值**设置亮度**

```backlit-kbd set [value]```

按步长**增加或减少**亮度

```backlit-kbd inc [step]```

```backlit-kbd dec [step]```

以特定百分比**打开背光**

```backlit-kbd on --percent [40]```

**关闭背光**

```backlit-kbd off```

让键盘**闪烁**作为视觉通知

```backlit-kbd blink --count [4] --on-ms [100] --off-ms [100]```

使用 mock 后端在**无硬件情况下测试**

```backlit-kbd --mock percent [50]```

# SYNOPSIS

**backlit-kbd** [_options_] _command_ [_args_]

# PARAMETERS

**info**
> 显示当前背光状态和检测到的设备信息。

**set** _value_
> 将亮度设置为设备支持的原始电平值。

**percent** _value_
> 以 0 到 100 之间的百分比设置亮度。

**inc** [_step_]
> 将亮度增加 _step_（默认：1）。

**dec** [_step_]
> 将亮度降低 _step_（默认：1）。

**on** [**--percent** _N_]
> 打开背光，可选指定百分比。

**off**
> 关闭背光。

**blink** [_options_]
> 在键盘上运行同步闪烁模式。

**notify** [_options_]
> 运行异步通知闪烁，不阻塞 Shell。

**--mock**
> 使用内存中的后端进行安全测试，不写入硬件。

**--device-path** _PATH_
> 指定特定的 sysfs 设备路径，而不自动发现。

**--count** _N_
> 闪烁循环次数（配合 _blink_ / _notify_ 使用）。

**--on-ms** _N_
> 闪烁期间亮起状态的持续时间（毫秒）。

**--off-ms** _N_
> 闪烁期间熄灭状态的持续时间（毫秒）。

**--level-percent** _N_
> 闪烁循环期间的亮度等级。

**--name** _NAME_
> 通知标识符（配合 _notify_ 使用）。

# DESCRIPTION

**backlit-kbd** 是一个用于控制 Linux 键盘背光的 Python 命令行工具。它会自动发现内核在 **/sys/class/leds/** 下暴露的兼容 LED 设备，通常是一些厂商特定的路径，例如 **tpacpi::kbd_backlight**（联想 ThinkPad）、**asus::kbd_backlight**（华硕）或 **dell::kbd_backlight**（戴尔）。

该工具提供面向日常亮度控制的高层命令（_set_、_percent_、_inc_、_dec_、_on_、_off_），并提供一对 _blink_ / _notify_ 命令，通过键盘 LED 产生视觉通知。**--mock** 标志可将后端替换为内存模拟器，从而在没有真实背光设备的机器上也能安全地进行实验或集成到脚本中。

# CONFIGURATION

通过 **pip install backlit-kbd** 安装。该工具从 **/sys/class/leds/*kbd_backlight*** 读取亮度路径，通常需要 root 权限（或授予写权限的 udev 规则）才能更改亮度等级。可使用 **--device-path** 覆盖设备自动发现。

# CAVEATS

写入 sysfs 亮度文件通常需要 **root** 权限。并非所有笔记本都有键盘背光 LED；在不支持的硬件上，除非使用 **--mock**，否则工具将无法发现设备。各设备的原始电平范围不同，因此百分比模式在不同机器间的可移植性更好。

# HISTORY

**backlit-kbd** 是一个托管在 GitHub 并发布到 PyPI 的开源 Python 包，旨在为 Linux 笔记本提供一款对新手友好的键盘背光控制 CLI。

# SEE ALSO

[brightnessctl](/man/brightnessctl)(1), [light](/man/light)(1), [xbacklight](/man/xbacklight)(1)
