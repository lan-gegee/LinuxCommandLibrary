# TAGLINE

PipeWire 的 PulseAudio 兼容层

# TLDR

启动 **PulseAudio 兼容**守护进程

```pipewire-pulse```

使用**指定的配置**文件

```pipewire-pulse -c [path/to/pipewire-pulse.conf]```

提高**详细程度**

```pipewire-pulse -vvv```

显示**帮助**

```pipewire-pulse -h```

# SYNOPSIS

**pipewire-pulse** [**-c** _config_] [**-v**...] [**-h**|**--help**] [**--version**]

# PARAMETERS

**-c, --config** _file_
> 使用备用配置文件（默认：pipewire-pulse.conf）

**-v, --verbose**
> 提高详细程度（可叠加）

**-h, --help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pipewire-pulse** 为 PipeWire 提供 PulseAudio 协议兼容性。它使为 PulseAudio 编写的应用无需修改即可与 PipeWire 无缝协作，并监听与 PulseAudio 相同的套接字。

该守护进程将 PulseAudio 协议消息转换为 PipeWire 操作，在利用 PipeWire 改进架构和更低延迟的同时，保持与现有应用的兼容性。

# CONFIGURATION

**/etc/pipewire/pipewire-pulse.conf**
> 系统级 PipeWire-Pulse 配置文件。

**~/.config/pipewire/pipewire-pulse.conf.d/**
> 用户级的配置覆盖 drop-in 目录。

# ENVIRONMENT

**PULSE_RUNTIME_PATH**, **XDG_RUNTIME_DIR**
> 用于创建原生协议 PulseAudio 套接字的目录。

**PULSE_LATENCY_MSEC**
> 为 libpulse 客户端应用增加的额外缓冲延迟（毫秒）。

# CAVEATS

不能与真正的 PulseAudio 守护进程同时运行。通常由 systemd 自动启动。需要主 pipewire 守护进程正在运行。某些高级 PulseAudio 特性可能不被完全支持。

# HISTORY

**pipewire-pulse** 作为 **PipeWire** 的一部分开发，以确保从 PulseAudio 平滑迁移。它让发行版可以在保持与庞大 PulseAudio 应用生态兼容的同时切换到 PipeWire。

# INSTALL

```apt: sudo apt install pipewire-pulse```

```pacman: sudo pacman -S pipewire-pulse```

```apk: sudo apk add pipewire-pulse```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pulseaudio](/man/pulseaudio)(1), [pactl](/man/pactl)(1), [pacmd](/man/pacmd)(1), [wpctl](/man/wpctl)(1), [pw-top](/man/pw-top)(1)
