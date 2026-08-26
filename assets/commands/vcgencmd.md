# TAGLINE

查询 Raspberry Pi 硬件状态

# TLDR

列出所有**命令**

```vcgencmd commands```

打印 CPU **温度**

```vcgencmd measure_temp```

打印**电压**

```vcgencmd measure_volts```

打印**降频（throttled）状态**

```vcgencmd get_throttled```

打印 **bootloader** 配置

```vcgencmd bootloader_config```

显示**帮助**

```vcgencmd --help```

# SYNOPSIS

**vcgencmd** _COMMAND_

# COMMANDS

**commands**
> 列出所有可用命令

**measure_temp**
> 打印当前 CPU 温度

**measure_volts**
> 打印当前电压

**get_throttled**
> 以位模式打印降频状态

**bootloader_config**
> 打印 bootloader 配置（仅限 Pi 4）

**get_config** _OPTION_
> 获取配置值

**version**
> 打印固件版本

# DESCRIPTION

**vcgencmd** 输出 Raspberry Pi 的系统信息。它与 VideoCore GPU 交互，查询硬件状态、温度、电压和配置。

该命令提供诊断信息，有助于监控 Raspberry Pi 的健康状况和排查故障。

# CAVEATS

仅限 Raspberry Pi。某些命令只在特定型号上可用。bootloader 命令需要 Pi 4 或更新型号。

# SEE ALSO

[raspi-config](/man/raspi-config)(1), [raspinfo](/man/raspinfo)(1)
