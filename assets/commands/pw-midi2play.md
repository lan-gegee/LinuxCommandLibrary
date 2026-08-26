# TAGLINE

通过 PipeWire 播放 MIDI 2（UMP）文件

# TLDR

**播放 MIDI 2（UMP）文件**

```pw-midi2play [path/to/file.midi2]```

**播放到特定的 PipeWire 目标节点**

```pw-midi2play --target [node_id] [path/to/file.midi2]```

**强制使用旧式 MIDI 1 字节流格式而非 UMP**

```pw-midi2play --force-midi midi [path/to/file.midi2]```

以详细输出**播放**

```pw-midi2play -v [path/to/file.midi2]```

从标准输入读取 MIDI 2 数据

```cat [file.midi2] | pw-midi2play -```

# SYNOPSIS

**pw-midi2play** [_options_] [_FILE_ | **-**]

# PARAMETERS

**-h**, **--help**
> 显示帮助并退出。

**--version**
> 显示版本信息。

**-v**, **--verbose**
> 启用详细输出。

**-R**, **--remote** _NAME_
> 连接到指定名称的 PipeWire 守护进程。

**--target** _VALUE_
> 目标节点的序列号或名称。**0** 表示禁用链接。

**--latency** _VALUE_
> 设置节点延迟，如 **100ms**、**2048** 个采样。

**-P**, **--properties** _JSON_
> 以 JSON 对象形式提供的额外流属性。

**-M**, **--force-midi** _FORMAT_
> 强制指定 MIDI 格式：**midi**（旧式字节）或 **ump**（Universal MIDI Packets，默认）。

# DESCRIPTION

**pw-midi2play** 将 MIDI 2 事件发送到 PipeWire 图中进行播放。它是 **pw-cat**(1) 以 **TYPE_MIDI2** 数据类型调用时的别名，期望接收 MIDI 2.0 规范定义的 **Universal MIDI Packet（UMP）**容器。

UMP 数据包既可承载旧式 MIDI 1 消息，也可承载 MIDI 2 特性，例如每通道 32 位分辨率、按音符控制器，以及 16 组每组 16 通道。该工具本身不合成音频：事件经由 PipeWire 图路由到能够渲染声音的支持 MIDI 2 的合成器或硬件设备。

当以 **-** 作为文件参数时，MIDI 数据从标准输入读取。

# CAVEATS

要求目标合成器、插件或硬件理解 MIDI 2 / UMP。没有下游渲染器时播放是静默的。标准 **.mid**（SMF）文件使用 MIDI 1 字节流，通常应改用 **pw-midiplay**(1)，或使用 **--force-midi midi** 来播放。

# HISTORY

MIDI 2 支持随 pw-cat 更广泛的 MIDI 2（UMP）工作一起进入 **PipeWire**，与较早的 **pw-midiplay**/**pw-midirecord** 组合形成互补。PipeWire 由 Red Hat 的 **Wim Taymans** 创建，于 **2017** 年首次发布，现在是主流 Linux 发行版的默认音频服务器。MIDI 2.0 规范由 MMA 于 **2020** 年批准。

# INSTALL

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cat](/man/pw-cat)(1), [pw-midi2record](/man/pw-midi2record)(1), [pw-midiplay](/man/pw-midiplay)(1), [pw-midirecord](/man/pw-midirecord)(1), [pw-mididump](/man/pw-mididump)(1), [pipewire](/man/pipewire)(1)
