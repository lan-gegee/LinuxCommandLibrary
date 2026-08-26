# TAGLINE

暂时挂起 PulseAudio，让另一个应用独占音频设备

# TLDR

运行 **JACK** 时挂起 PulseAudio

```pasuspender -- jackd --driver alsa --device hw:0```

为**任意命令**挂起 PulseAudio

```pasuspender -- [command]```

# SYNOPSIS

**pasuspender** [**-s** _server_] **--** _command_ [_arguments_...]

# PARAMETERS

**-s, --server _server_**
> 连接到指定的 PulseAudio 服务器

**--**
> pasuspender 选项与命令之间的分隔符

**-h, --help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pasuspender** 会暂时挂起 PulseAudio，让另一个应用通过 ALSA 独占访问音频硬件。对于无法在 PulseAudio 下工作或需要直接访问硬件的应用来说，这是必需的。

当指定命令退出后，PulseAudio 会自动恢复正常运行。这通常用于 JACK 等需要低延迟直接硬件访问的专业音频应用。

# CAVEATS

仅适用于 PulseAudio（没有兼容层时不适用于 PipeWire）。该命令以独占方式访问音频，会阻塞其他音频应用。命令要正常工作，PulseAudio 必须正在运行。某些应用可能无法干净地释放音频设备。

# HISTORY

**pasuspender** 是 **Lennart Poettering** 和 freedesktop.org 社区开发的 **PulseAudio** 声音系统的一部分。它满足了应用需要直接访问硬件时暂时绕过声音服务器的常见需求。

# INSTALL

```apt: sudo apt install pulseaudio-utils```

```dnf: sudo dnf install pulseaudio-utils```

```apk: sudo apk add pulseaudio-utils```

```zypper: sudo zypper install pulseaudio-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulseaudio](/man/pulseaudio)(1), [pactl](/man/pactl)(1), [jackd](/man/jackd)(1)
