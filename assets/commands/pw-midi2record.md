# TAGLINE

通过 PipeWire 录制 MIDI 2（UMP）事件

# TLDR

**将 MIDI 2 输入录制为 UMP 文件**

```pw-midi2record [path/to/output.midi2]```

**从特定的源节点录制**

```pw-midi2record --target [node_id] [path/to/output.midi2]```

**强制使用旧式 MIDI 1 字节流格式**

```pw-midi2record --force-midi midi [path/to/output.midi2]```

以详细输出**录制**

```pw-midi2record -v [path/to/output.midi2]```

将 MIDI 2 采集结果**管道传输**到另一个程序

```pw-midi2record - | [tool]```

# SYNOPSIS

**pw-midi2record** [_options_] [_FILE_ | **-**]

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
> 源节点的序列号或名称。**0** 表示禁用链接。

**--latency** _VALUE_
> 设置节点延迟，如 **100ms**、**2048** 个采样。

**-P**, **--properties** _JSON_
> 以 JSON 对象形式提供的额外流属性。

**-M**, **--force-midi** _FORMAT_
> 强制指定 MIDI 格式：**midi**（旧式字节）或 **ump**（Universal MIDI Packets，默认）。

**-C**, **--monitor**
> 捕获输出节点的监视（monitor）端口（在录制时）。

# DESCRIPTION

**pw-midi2record** 从 PipeWire 图中捕获 MIDI 2 事件并写入文件。它是 **pw-cat**(1) 以 **TYPE_MIDI2** 数据类型调用时的别名，按 MIDI 2.0 规范将事件编码为 **Universal MIDI Packets（UMP）**。

UMP 既可承载旧式 MIDI 1 消息，也可承载 MIDI 2 特性（按音符控制器、32 位数值、16 组每组 16 通道）。必须有支持 MIDI 2 的源——控制器、软件乐器或上游 PipeWire 节点——连接到图上，才能录到事件。

当以 **-** 作为文件参数时，MIDI 数据写入标准输出。

# CAVEATS

只录制 MIDI 事件，不录制渲染后的音频；如需捕获合成器的音频输出，请使用 **pw-record**(1)。没有已连接的 MIDI 源时，文件中将只包含头信息。生成的文件是 UMP 格式，而非旧式的 SMF（**.mid**）格式。

# HISTORY

MIDI 2 支持随 pw-cat 更广泛的 MIDI 2（UMP）工作一起进入 **PipeWire**，与较早的 **pw-midiplay**/**pw-midirecord** 组合形成互补。PipeWire 由 Red Hat 的 **Wim Taymans** 创建，于 **2017** 年首次发布。MIDI 2.0 规范由 MMA 于 **2020** 年批准。

# INSTALL

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cat](/man/pw-cat)(1), [pw-midi2play](/man/pw-midi2play)(1), [pw-midiplay](/man/pw-midiplay)(1), [pw-midirecord](/man/pw-midirecord)(1), [pw-mididump](/man/pw-mididump)(1), [pw-record](/man/pw-record)(1), [pipewire](/man/pipewire)(1)
