# TAGLINE

用 RTL-SDR 电视棒捕获原始无线电采样数据

# TLDR

**捕获到文件**

```rtl_sdr -f [100M] [capture.bin]```

**设置采样率**

```rtl_sdr -f [100M] -s [2.4M] [capture.bin]```

**设置增益**

```rtl_sdr -f [100M] -g [40] [capture.bin]```

**限定捕获数量**

```rtl_sdr -f [100M] -n [1000000] [capture.bin]```

**频率偏差校正**

```rtl_sdr -f [100M] -p [55] [capture.bin]```

**选择设备**

```rtl_sdr -d [0] -f [100M] [capture.bin]```

**直接采样模式**

```rtl_sdr -f [3M] -D [2] [capture.bin]```

# SYNOPSIS

**rtl_sdr** [_-f freq_] [_-s rate_] [_-g gain_] [_options_] _output_

# PARAMETERS

**-f** _FREQ_
> 中心频率（Hz）。

**-s** _RATE_
> 采样率（Hz）。

**-g** _GAIN_
> 增益（0 表示自动）。

**-n** _SAMPLES_
> 采样数量。

**-p** _PPM_
> 频率校正。

**-d** _INDEX_
> 设备索引。

**-D** _MODE_
> 直接采样模式。

**-S**
> 启用同步模式。

# DESCRIPTION

**rtl_sdr** 使用 RTL-SDR 电视棒捕获原始无线电信号。这类电视棒是基于 RTL2832U 芯片组的廉价 USB 设备，最初为 DVB-T 电视接收而设计。该工具从设备读取原始 I/Q（同相/正交）采样数据，从而支持在很宽的频率范围内开展软件定义无线电实验，典型范围为 24 MHz 至 1766 MHz，具体取决于调谐器芯片。

该工具把原始的 8 位 I/Q 采样数据写入文件或 stdout，之后可以交由其他应用程序处理，解码多种信号类型，包括调频广播、ADS-B 飞机追踪、气象卫星和寻呼系统。采样率参数决定了捕获的带宽：速率越高覆盖的频谱越宽，但占用的 USB 带宽和存储空间也越多。

增益和频率校正参数可以帮助优化接收质量。增益设为零即启用自动增益控制，手动设值则可针对特定信号精细调节。PPM 校正用于补偿廉价电视棒固有的晶振频率误差，可对照已知参考信号加以校准。

# CAVEATS

需要兼容 RTL-SDR 的设备。USB 带宽会限制采样率。发热会影响频率稳定性。

# HISTORY

**rtl_sdr** 属于 **librtlsdr** 项目，让基于 RTL2832U 的 DVB-T 电视棒能够用于 SDR。由 **Steve Markgraf** 等人创建，极大降低了软件定义无线电的使用门槛。

# INSTALL

```apt: sudo apt install rtl-sdr```

```dnf: sudo dnf install rtl-sdr```

```pacman: sudo pacman -S rtl-sdr```

```apk: sudo apk add rtl-sdr```

```zypper: sudo zypper install rtl-sdr```

```brew: brew install rtl-sdr```

```nix: nix profile install nixpkgs#rtl-sdr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rtl_fm](/man/rtl_fm)(1), [rtl_power](/man/rtl_power)(1), [gqrx](/man/gqrx)(1), [gnuradio](/man/gnuradio)(1)
