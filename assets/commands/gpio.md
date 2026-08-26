# TAGLINE

树莓派 GPIO 引脚控制工具

# TLDR

**读取 GPIO 引脚状态**

```gpio read [pin]```

**设置 GPIO 引脚输出**

```gpio write [pin] [0|1]```

**设置引脚模式**

```gpio mode [pin] [in|out|pwm]```

**读取所有引脚**

```gpio readall```

**导出引脚供用户访问**

```gpio export [pin] [in|out]```

**取消导出引脚**

```gpio unexport [pin]```

# SYNOPSIS

**gpio** [_options_] _command_ [_args_]

# PARAMETERS

**read** _pin_
> 读取引脚值。

**write** _pin_ _value_
> 向引脚写入值（0 或 1）。

**mode** _pin_ _mode_
> 设置引脚模式：in、out、pwm、clock。

**readall**
> 显示所有 GPIO 引脚的状态。

**export** _pin_ _mode_
> 导出引脚供用户空间访问。

**unexport** _pin_
> 取消导出引脚。

**pwm** _pin_ _value_
> 设置 PWM 值（0-1023）。

**-g**
> 使用 BCM GPIO 编号。

**-1**
> 使用物理引脚编号。

# DESCRIPTION

**gpio** 是 WiringPi 的命令行工具，用于控制树莓派及类似开发板上的 GPIO 引脚。它允许通过 shell 脚本和命令行读取、写入和配置 GPIO 引脚。

该工具支持多种引脚编号方案：WiringPi 编号（默认）、BCM GPIO 编号（**-g**）以及物理引脚编号（**-1**）。**readall** 命令会显示完整的引脚状态表。

# CAVEATS

WiringPi 已被弃用但仍可使用。不同的编号方案容易造成混淆。需要相应的权限。引脚功能因开发板而异。部分引脚具有特殊功能。

# HISTORY

gpio 是 **WiringPi** 的一部分，由 **Gordon Henderson** 创建，用于访问树莓派的 GPIO。虽然 WiringPi 于 2019 年被弃用，但它仍被广泛使用。替代方案包括 libgpiod 和 Python 的 RPi.GPIO。

# SEE ALSO

[raspi-gpio](/man/raspi-gpio)(1)
