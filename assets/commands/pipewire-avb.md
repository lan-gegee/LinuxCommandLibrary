# TAGLINE

面向 AVB 音视频桥接的 PipeWire 守护进程变体

# TLDR

以默认配置**启动 AVB PipeWire 守护进程**

```pipewire-avb```

**使用自定义配置文件**

```pipewire-avb -c [path/to/pipewire-avb.conf]```

**提高日志详细程度**

```pipewire-avb -v```

**显示版本信息**

```pipewire-avb --version```

# SYNOPSIS

**pipewire-avb** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示帮助文本并退出。

**-v**, **--verbose**
> 提高日志详细程度（可重复使用）。

**--version**
> 显示版本信息并退出。

**-c** _FILE_, **--config**=_FILE_
> 加载给定的配置文件（默认 **pipewire-avb.conf**）。

**-P** _PROPS_, **--properties**=_PROPS_
> 向守护进程上下文添加 JSON 属性。

# DESCRIPTION

**pipewire-avb** 是一个以针对 **AVB** 定制的配置启动的 PipeWire 守护进程。AVB（Audio Video Bridging，音视频桥接）是一组 IEEE 802.1 标准（gPTP、FQTSS、MSRP、AVTP），可在标准以太网上提供确定性、低延迟、时间同步的媒体流传输，广泛用于专业音频、汽车和广播领域。

该守护进程加载 **avb** 模块，在选定的网络接口上发现和公告 AVB 流（talker 和 listener），建立由 gPTP 驱动的媒体时钟，并将这些流暴露为原生 PipeWire 节点。标准的 PulseAudio、ALSA 和 JACK 客户端即可向 AVB 端点发送或从中接收音频。

该二进制文件通常是 **pipewire**(1) 的符号链接；程序根据 **argv[0]** 选择默认配置。

# CONFIGURATION

默认配置文件是 **/usr/share/pipewire/pipewire-avb.conf**。如需系统级修改可将其复制到 **/etc/pipewire/**，如需每用户修改则复制到 **~/.config/pipewire/**。也可以将 drop-in 片段放在对应的 **pipewire-avb.conf.d/** 目录下。

配置内容涉及 AVB 网络接口的选择、gPTP 时钟参数以及流拓扑。

# CAVEATS

需要支持 **AVB/TSN**（gPTP 和 SRP）的网络接口和交换机基础设施以保证带宽和时序。流发现使用二层协议 MSRP 和 MVRP，通常需要 **CAP_NET_ADMIN** 能力或 root 权限。在上游 PipeWire 发布中被标记为**实验性**。

# HISTORY

AVB 支持作为 **PipeWire** 进军专业网络化音频的一部分被加入。PipeWire 由 Red Hat 的 **Wim Taymans** 创建，于 **2017 年**首次发布，如今已是主流 Linux 发行版中的默认音频服务器。

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

[pipewire](/man/pipewire)(1), [pipewire-aes67](/man/pipewire-aes67)(1), [pipewire-pulse](/man/pipewire-pulse)(1), [pw-cli](/man/pw-cli)(1), [pw-dump](/man/pw-dump)(1)
