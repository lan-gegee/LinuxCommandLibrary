# TAGLINE

低延迟多媒体处理守护进程

# TLDR

启动 **PipeWire** 守护进程

```pipewire```

使用**其他配置**文件

```pipewire --config [path/to/file.conf]```

提高**详细程度**

```pipewire -vvv```

显示**帮助**

```pipewire --help```

# SYNOPSIS

**pipewire** [**-c** _config_] [**-v**...] [**--help**] [**--version**]

# PARAMETERS

**-c, --config _file_**
> 使用备用配置文件

**-v, --verbose**
> 提高详细程度（多次使用可进一步增加）

**-h, --help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pipewire** 是一个现代多媒体处理守护进程，负责处理音频和视频流。它提供低延迟的采集和播放，同时取代了面向消费级音频的 PulseAudio 和面向专业音频应用的 JACK。

该守护进程管理应用与设备之间的连接，处理格式转换，并提供基于图的路由模型。它通常由 systemd 用户服务自动启动。

# CONFIGURATION

**/etc/pipewire/pipewire.conf**
> 系统级 PipeWire 配置文件。

**~/.config/pipewire/pipewire.conf.d/**
> 用户级的配置覆盖 drop-in 目录。

**/etc/pipewire/pipewire.conf.d/**
> 用于附加配置片段的系统级 drop-in 目录。

**PIPEWIRE_RUNTIME_DIR**
> 覆盖 PipeWire 套接字的运行时目录。

# CAVEATS

通常通过 systemd 启动，而非手动启动。需要 pipewire-pulse 以实现 PulseAudio 兼容性。配置更改后需重启守护进程。可能与正在运行的 PulseAudio 实例冲突。

# HISTORY

**PipeWire** 由 Red Hat 的 **Wim Taymans** 开发，源于 PulseVideo 实验，最终成为 Linux 多媒体的统一解决方案，于 2021 年被 Fedora 34 正式采用，随后被其他发行版采纳。

# INSTALL

```apt: sudo apt install pipewire-bin```

```dnf: sudo dnf install pipewire```

```pacman: sudo pacman -S pipewire```

```apk: sudo apk add pipewire```

```zypper: sudo zypper install pipewire```

```brew: brew install pipewire```

```nix: nix profile install nixpkgs#pipewire```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire-pulse](/man/pipewire-pulse)(1), [pw-cli](/man/pw-cli)(1), [pw-top](/man/pw-top)(1), [wireplumber](/man/wireplumber)(1)
