# TAGLINE

系统健康监视与复位守护进程

# TLDR

**启动 watchdog 守护进程**

```sudo systemctl start watchdog```

**开机自启**

```sudo systemctl enable watchdog```

**测试配置**

```sudo watchdog -v```

**以前台方式运行**

```sudo watchdog -f```

**强制测试模式**

```sudo watchdog -F```

# SYNOPSIS

**watchdog** [_options_]

# PARAMETERS

**-f**, **--foreground**
> 以前台方式运行，不 fork。

**-F**, **--force**
> 强制测试模式。

**-v**, **--verbose**
> 详细输出。

**-c** _file_
> 使用指定的配置文件。

**-s**, **--sync**
> 重启前同步数据。

**--help**
> 显示帮助。

# CONFIGURATION

配置文件：/etc/watchdog.conf

关键设置：watchdog-device、interval、max-load-1、min-memory 以及测试命令。

# DESCRIPTION

**watchdog** 是一个监视系统健康的守护进程，检测到问题时会复位系统。它周期性地向 /dev/watchdog 写入数据，以阻止内核触发硬件复位。

该守护进程可监视多种系统状态：负载均值、内存用量、文件是否存在、进程是否存在、温度以及自定义测试脚本。任何检查失败时，系统会在记录失败原因后重启。

硬件看门狗需要相应的内核模块（例如 Intel 的 iTCO_wdt）。硬件不可用时，可通过 softdog 模块提供软件看门狗作为后备方案。

# CAVEATS

需要相应的内核看门狗驱动。配置不当可能导致意外重启。投入生产前请充分测试。软件看门狗的可靠性低于硬件看门狗。

# HISTORY

**watchdog** 是为需要在无人干预情况下保持高可用性的 Linux 系统开发的。这一概念可追溯到嵌入式系统时代，当时硬件看门狗定时器用于确保系统从挂死中恢复。Linux 实现将硬件定时器支持与软件监视结合在一起。

# INSTALL

```apt: sudo apt install watchdog```

```dnf: sudo dnf install watchdog```

```zypper: sudo zypper install watchdog```

```nix: nix profile install nixpkgs#watchdog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmesg](/man/dmesg)(1)
