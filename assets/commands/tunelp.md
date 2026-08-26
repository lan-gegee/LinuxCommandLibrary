# TAGLINE

配置并行端口设备参数

# TLDR

检查并行端口的**状态**

```tunelp -s [/dev/lp0]```

**重置**并行端口

```tunelp -r [/dev/lp0]```

为设备设置 **IRQ**

```tunelp -i 5 [/dev/lp0]```

设置重试**次数**和计时

```tunelp -c [times] -t [time_in_centiseconds] [/dev/lp0]```

切换出错时是否**中止**

```tunelp -a [on|off]```

# SYNOPSIS

**tunelp** [_OPTIONS_] _DEVICE_

# PARAMETERS

**-s, --status**
> 检查设备状态

**-r, --reset**
> 重置并行端口

**-i, --irq** _N_
> 设置中断线（IRQ）

**-c, --chars** _N_
> 休眠前尝试输出的次数

**-t, --time** _N_
> 休眠时长（百分之一秒）

**-a, --abort** _on|off_
> 启用或禁用出错时中止

# DESCRIPTION

**tunelp** 为并行端口设备设置各种参数。它用于排查打印机连接问题，或优化并行端口打印机及其他设备的性能。

tunelp 属于 util-linux 软件包，可为旧式并行端口硬件调整 IRQ 设置、超时值和错误处理行为。

# CAVEATS

并行端口已基本过时。需要 root 权限。不正确的 IRQ 设置可能导致系统冲突。只影响旧式 lp 设备。

# HISTORY

**tunelp** 属于 **util-linux** 软件包，用于配置早期计算时代常见的并行端口设备。

# SEE ALSO

[lp](/man/lp)(4)
