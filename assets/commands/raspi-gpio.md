# TAGLINE

查询和设置树莓派 GPIO 引脚状态

# TLDR

**显示所有 GPIO 引脚状态**

```raspi-gpio get```

**获取指定引脚的状态**

```raspi-gpio get [17]```

**将引脚配置为输出**

```sudo raspi-gpio set [17] op```

**将引脚驱动为高电平**

```sudo raspi-gpio set [17] dh```

**将引脚驱动为低电平**

```sudo raspi-gpio set [17] dl```

**设置为带拉上拉的输入**

```sudo raspi-gpio set [18] ip pu```

**列出引脚的复用功能**

```raspi-gpio funcs [17]```

**转储原始寄存器值**

```sudo raspi-gpio raw```

# SYNOPSIS

**raspi-gpio** _command_ [_pin_] [_options_]

# COMMANDS

**get** [_pin_|_pin1,pin2,..._]
> 显示引脚状态。不带引脚号时显示所有 GPIO（0-53）。

**set** _pin_ _options..._
> 配置引脚方向、驱动电平、上下拉或复用功能。

**funcs** [_pin_]
> 打印给定引脚（或所有引脚）由 BCM 定义的复用功能。

**raw**
> 打印 GPIO 寄存器的原始值。

# OPTIONS FOR SET

**ip** / **op**
> 设为输入 / 输出。

**a0** ... **a5**
> 选择复用功能 0-5。

**dl** / **dh**
> 驱动为低电平 / 高电平（仅在设置了 **op** 时有意义）。

**pu** / **pd** / **pn**
> 拉高 / 拉低 / 无上下拉。

# DESCRIPTION

**raspi-gpio** 是一个底层工具，用于检查和操控树莓派板卡上的 GPIO 引脚。它通过 /dev/gpiomem（以 root 运行时用 /dev/mem）直接写入 BCM GPIO 控制器寄存器，绕过 libgpiod 等更高层的库。

该工具主要用于调试硬件接线、验证 DT overlay 是否应用了预期的引脚功能，以及编写一次性脚本。生产环境建议使用内核的 **gpiod** 接口（通过 **libgpiod** 的 **gpioget**/**gpioset**），因为它与内核的 GPIO 子系统集成，并尊重内核已占用的线路。

# CAVEATS

仅适用于树莓派。**set** 和 **raw** 需要 root 权限，因为它们会写入硬件。对连接了外部硬件的引脚写入错误的方向或驱动电平可能损坏 SoC。所用的编号是 BCM（Broadcom）编号——而不是物理板卡引脚编号。

# HISTORY

**raspi-gpio** 随 **Raspberry Pi OS** 附带，是由 Raspberry Pi 基金会维护的小型工具。它是对更高级库（如已弃用的 **wiringPi**）和内核 **gpiod** 接口的补充。

# SEE ALSO

[gpio](/man/gpio)(1), [vcgencmd](/man/vcgencmd)(1)
