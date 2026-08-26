# TAGLINE

在 ALSA 设备之间创建音频环回。

# TLDR

将音频从采集设备**循环转发**到播放设备

```alsaloop -C [hw:0,0] -P [hw:1,0]```

以**指定采样率**进行循环转发

```alsaloop -C [hw:0,0] -P [hw:1,0] -r [48000]```

以**指定格式**进行循环转发

```alsaloop -C [hw:0,0] -P [hw:1,0] -f [S16_LE]```

以**守护进程**模式运行

```alsaloop -C [hw:0,0] -P [hw:1,0] -d```

# SYNOPSIS

**alsaloop** [**-C** _capture_] [**-P** _playback_] [**-r** _rate_] [**-f** _format_] [_options_]

# DESCRIPTION

**alsaloop** 在 ALSA 采集设备和播放设备之间创建环回。它从一个设备实时读取音频并写入另一个设备，可用于在不同硬件接口之间路由音频。

该工具会处理缓冲区管理，必要时进行采样率转换，并尽力保持设备之间的同步。

# PARAMETERS

**-C**, **--cdevice** _device_
> 采集（输入）PCM 设备。默认为 **default**。

**-P**, **--pdevice** _device_
> 播放（输出）PCM 设备。默认为 **default**。

**-r**, **--rate** _rate_
> 采样率，单位为 Hz。默认为 **48000**。

**-f**, **--format** _format_
> 采样格式，如 S16_LE 或 S32_LE。默认为 **S16_LE**。

**-c**, **--channels** _channels_
> 声道数。默认为 **2**。

**-d**, **--daemonize**
> 将主进程转为守护进程，并将日志写入 syslog。

**-s**, **--seconds** _seconds_
> 循环转发的时长，单位为秒。

**-t**, **--tlatency** _usec_
> 期望的延迟，单位为微秒（1/1000000 秒）。

**-S**, **--sync** _mode_
> 同步模式：none、simple、captshift、playshift、samplerate 或 auto。

**-n**, **--resample**
> 使用 alsa-lib 启用采样率重采样。

**-T**, **--thread** _number_
> 线程编号；-1 表示创建唯一线程。相同编号的任务共享一个线程。

# CAVEATS

延迟取决于缓冲区大小和硬件能力。设备之间采样率不同时需要进行重采样。更低的延迟设置会增加 CPU 占用。

# HISTORY

**alsaloop** 是 alsa-utils 软件包的一部分，提供了一个简单的音频路由工具，与更复杂的 ALSA 环回内核模块互为补充。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arecord](/man/arecord)(1), [aplay](/man/aplay)(1), [alsactl](/man/alsactl)(1)

# RESOURCES

```[Source code](https://github.com/alsa-project/alsa-utils)```

```[Homepage](https://www.alsa-project.org/)```

<!-- verified: 2026-06-11 -->
