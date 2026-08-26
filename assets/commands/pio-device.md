# TAGLINE

管理已连接的开发板

# TLDR

**列出已连接的设备**

```pio device list```

**打开串口监视器**

```pio device monitor```

**以指定波特率监视**

```pio device monitor -b [115200]```

**监视指定端口**

```pio device monitor -p [/dev/ttyUSB0]```

# SYNOPSIS

**pio device** _command_ [_options_]

# PARAMETERS

**list**
> 列出已连接的设备。

**monitor**
> 打开串口监视器。

**-p**, **--port** _port_
> 串口。

**-b**, **--baud** _rate_
> 波特率（默认 9600）。

**-f**, **--filter** _filter_
> 应用输出过滤器。

**--raw**
> 禁用输入/输出过滤器。

# DESCRIPTION

**pio device** 管理已连接的开发板。列出串口设备，并提供用于调试嵌入式应用的串口监视器。支持过滤和自定义波特率。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-run](/man/pio-run)(1), [pio-debug](/man/pio-debug)(1)
