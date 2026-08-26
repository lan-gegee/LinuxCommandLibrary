# TAGLINE

为 Cyclades-Z 多端口串口卡调整驱动参数

# TLDR

**获取当前阈值和超时值**

```cytune -g /dev/ttyC0```

**获取默认阈值和超时值**

```cytune -G /dev/ttyC0```

**设置当前阈值**（1-12）

```cytune -s [8] /dev/ttyC0```

**设置当前刷新超时值**（0-255，单位为 5ms）

```cytune -t [10] /dev/ttyC0```

**同时设置阈值和超时值**

```cytune -s [8] -t [10] /dev/ttyC0```

**为下次打开设置默认阈值**

```cytune -S [8] /dev/ttyC0```

**按间隔收集统计信息**（需要 ENABLE_MONITORING）

```cytune -q -i [5] /dev/ttyC0```

# SYNOPSIS

**cytune** [**-q** [**-i** _interval_]] [{**-s**|**-S**} _value_] [**-g**|**-G**] [{**-t**|**-T**} _timeout_] _tty_...

# PARAMETERS

_TTY_
> 要配置的串口设备（例如 /dev/ttyC0）。

**-s** _VALUE_
> 将当前阈值设置为 VALUE 个字符（1-12）。如果 tty 未保持打开，下次打开时会重置。

**-S** _VALUE_
> 将默认阈值设置为 VALUE 个字符（1-12）。在下次打开 tty 时生效。

**-t** _VALUE_
> 将当前刷新超时设置为 VALUE 个单位（0-255），每个单位为 5ms。设为零则强制使用默认超时。

**-T** _VALUE_
> 将默认刷新超时设置为 VALUE 个单位。在下次打开 tty 时生效。

**-g**
> 获取当前阈值和超时值。

**-G**
> 获取默认阈值和刷新超时值。

**-q**
> 收集并报告驱动统计信息（中断次数和传输的字符数）。仅在驱动编译时启用了 ENABLE_MONITORING 时可用。

**-i** _interval_
> 统计信息的收集间隔，单位为秒（与 -q 配合使用）。

# DESCRIPTION

**cytune** 是一个用于调整 Cyclades-Z 多端口串口卡驱动的中断阈值和刷新超时参数的工具。这些参数影响驱动在触发中断前缓冲多少数据，从而在延迟与 CPU 开销之间取得平衡。

Cyclades 卡上的每条串行线路都有 12 字节的输入/输出 FIFO。阈值指定 FIFO 中必须积累多少个字符才触发中断。值越高，中断开销越低，但延迟越大。若设置过高，FIFO 可能溢出导致字符丢失。刷新超时则确保即使未达到阈值，数据也能被送达。

默认阈值在打开 tty 时根据波特率设定：50-4800 波特为 10，9600 为 8，19200 为 4，38400 为 2，57600 及以上为 1。

# CAVEATS

仅适用于 Cyclades 串口硬件及其驱动。不正确的设置可能导致数据丢失或性能下降。修改设置需要 root 权限。不适用于标准串口。-q 监控选项只有在驱动编译时定义了 ENABLE_MONITORING 才可用。

# HISTORY

**cytune** 是为 Linux 下的 Cyclades 多端口串口卡驱动开发的，属于 **util-linux** 软件包。Cyclades 曾为需要大量串口的应用提供高密度串口解决方案。

# SEE ALSO

[setserial](/man/setserial)(8), [stty](/man/stty)(1)
