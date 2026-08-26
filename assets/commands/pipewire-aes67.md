# TAGLINE

面向 AES67 音频网络传输的 PipeWire 守护进程变体

# TLDR

以默认配置**启动 AES67 PipeWire 守护进程**

```pipewire-aes67```

**使用自定义配置文件**

```pipewire-aes67 -c [path/to/pipewire-aes67.conf]```

**提高日志详细程度**

```pipewire-aes67 -v```

**显示版本信息**

```pipewire-aes67 --version```

# SYNOPSIS

**pipewire-aes67** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示帮助文本并退出。

**-v**, **--verbose**
> 提高日志详细程度（可重复使用，例如 **-vvv**）。

**--version**
> 显示版本信息并退出。

**-c** _FILE_, **--config**=_FILE_
> 加载给定的配置文件（默认 **pipewire-aes67.conf**）。

**-P** _PROPS_, **--properties**=_PROPS_
> 向守护进程上下文添加 JSON 属性。

# DESCRIPTION

**pipewire-aes67** 是一个以针对 **AES67** 定制的配置启动的 PipeWire 守护进程。AES67 是一个开放的音频网络传输互操作标准（被 Dante 和 RAVENNA 等系统采用），它定义了基于标准以太网的低延迟、未压缩 PCM 音频传输，使用 **RTP**、用于时钟同步的 **PTP** 以及用于流公告的 **SAP/SDP**。

在默认配置下，该守护进程会创建精确时间协议（PTP）硬件时钟节点、组播 RTP 发送器和接收器以及 SAP 公告模块，并将 AES67 流暴露为原生 PipeWire 设备。此后，使用 ALSA、PulseAudio 或 JACK 客户端的现有音频应用可以透明地向 AES67 端点发送或从中接收音频。

该二进制文件通常是 **pipewire**(1) 的符号链接；程序根据 **argv[0]** 选择默认配置。

# CONFIGURATION

默认配置文件是 **/usr/share/pipewire/pipewire-aes67.conf**。如需系统级修改可将其复制到 **/etc/pipewire/**，如需每用户修改则复制到 **~/.config/pipewire/**。也可以将 drop-in 片段放在对应的 **pipewire-aes67.conf.d/** 目录下。

需要配置的关键项包括 PTP 时钟接口或设备、组播网络接口、采样率、通道数以及每条流的 RTP/SAP 参数。

# CAVEATS

要求本地网络中有可用的 **PTP** 时间源，且网络接口支持组播和（理想情况下）硬件时间戳。自 PipeWire **1.1.0** 起已验证可与 Dante 和 RAVENNA 互通。防火墙规则必须放行相关的组播和 PTP 流量。

# HISTORY

AES67 支持作为 **PipeWire** 专业音频能力扩展的一部分被加入，完整的 Dante 和 RAVENNA 互操作能力于 PipeWire **1.1.0**（2024 年）落地。PipeWire 本身由 Red Hat 的 **Wim Taymans** 创建，于 **2017 年**首次发布。

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

[pipewire](/man/pipewire)(1), [pipewire-avb](/man/pipewire-avb)(1), [pipewire-pulse](/man/pipewire-pulse)(1), [pw-cli](/man/pw-cli)(1), [pw-dump](/man/pw-dump)(1)
