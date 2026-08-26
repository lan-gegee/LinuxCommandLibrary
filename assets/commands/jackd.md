# TAGLINE

JACK 音频服务器守护进程

# TLDR

**以 ALSA 驱动启动 JACK**

```jackd -d alsa```

**指定采样率和缓冲区**

```jackd -d alsa -r [48000] -p [256]```

**以实时模式启动**

```jackd -R -d alsa```

**使用指定设备**

```jackd -d alsa -d [hw:0]```

**以详细输出启动**

```jackd -v -d alsa```

# SYNOPSIS

**jackd** [_options_] **-d** _driver_ [_driver-options_]

# PARAMETERS

**-d** _driver_
> 音频驱动（alsa、coreaudio、dummy）。

**-R**, **--realtime**
> 使用实时调度。

**-r** _rate_
> 采样率（44100、48000 等）。

**-p** _frames_
> 每周期的帧数（缓冲区大小）。

**-n** _periods_
> 周期数。

**-P**
> 仅播放。

**-C**
> 仅捕获。

**-v**, **--verbose**
> 详细输出。

**-T**, **--temporary**
> 所有客户端断开后退出。

# DRIVER OPTIONS (ALSA)

**-d** _device_
> ALSA 设备（hw:0、hw:1）。

**-S**
> 强制 16 位采样。

**-H**
> 硬件监听。

# DESCRIPTION

**jackd** 是 JACK 音频服务器守护进程。它为应用程序之间提供低延迟的音频连接，并实现采样级精确同步。

JACK 是 Linux 上专业音频的基础，支持 DAW、合成器、效果器和硬件之间的复杂路由。

# CAVEATS

要获得低延迟需要实时权限。缓冲区大小会影响延迟与稳定性的平衡。现代系统可考虑 JACK2（jackdbus）。

# HISTORY

JACK 主要由 **Paul Davis** 自 **2002 年**起创建。它成为 Linux 上专业音频的标准，实现了可媲美商业系统的专业音频工作流。

# INSTALL

```apt: sudo apt install jackd1```

```apk: sudo apk add jack```

```zypper: sudo zypper install jack```

```brew: brew install jack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jack_connect](/man/jack_connect)(1), [pulseaudio](/man/pulseaudio)(1)
