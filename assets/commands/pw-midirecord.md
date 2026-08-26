# TAGLINE

通过 PipeWire 录制 MIDI 事件

# TLDR

**将 MIDI 输入录制到文件**

```pw-midirecord [path/to/output.mid]```

以详细输出**录制**

```pw-midirecord -v [path/to/output.mid]```

**从特定的源节点录制**

```pw-midirecord --target [node_id] [path/to/output.mid]```

以自定义延迟**录制**

```pw-midirecord --latency [50ms] [path/to/output.mid]```

# SYNOPSIS

**pw-midirecord** [_options_] [_FILE_ | **-**]

# PARAMETERS

**--volume** _level_
> 流音量（默认 1.0）。

**--rate** _hz_
> 以 Hz 表示的采样率（默认 48000）。

**--channels** _num_
> 音频声道数（默认 2）。

**--channel-map** _map_
> 声道布局（如 stereo、surround-51，或自定义的 FL,FR 映射）。

**--format** _fmt_
> 采样格式：u8、s8、s16、s24、s32、f32、f64（默认 s16）。

**--target** _value_
> 源节点：auto、0 或特定的节点 ID。

**--latency** _value_
> 节点延迟（默认 100ms）。

**-q**, **--quality** _level_
> 重采样质量（0-15，默认 4）。

**-R**, **--remote** _name_
> 连接到特定的 PipeWire 实例。

**-P**, **--properties** _json_
> 以 JSON 对象形式提供的额外流属性。

**-v**, **--verbose**
> 启用详细输出。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本详情。

# DESCRIPTION

**pw-midirecord** 从 PipeWire 图中捕获 MIDI 事件并写入文件。它是 **pw-cat --record --midi** 的便捷封装，可从已连接的 MIDI 控制器、软件乐器或通过 PipeWire 可用的其他 MIDI 源录制 MIDI 数据。

该工具只录制原始 MIDI 事件。它不会捕获来自 MIDI 合成器的渲染音频。要录制 MIDI 播放的音频输出，请改用 **pw-record**。

当以 **-** 作为文件时，数据写入标准输出。

# CAVEATS

只录制 MIDI 事件，不录制音频。必须在 PipeWire 图中连接 MIDI 源才能采集到数据。硬件 MIDI 控制器需要相应的设备权限。

# HISTORY

**PipeWire** 的一部分，该现代多媒体框架由 Red Hat 的 **Wim Taymans** 创建。PipeWire 于 **2017** 年首次发布，现已成为主流 Linux 发行版中默认的音频和视频服务器，取代了 PulseAudio 和 JACK。pw-cat 系列工具提供简单的命令行媒体播放和采集功能。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cat](/man/pw-cat)(1), [pw-midiplay](/man/pw-midiplay)(1), [pw-mididump](/man/pw-mididump)(1), [pw-record](/man/pw-record)(1), [pipewire](/man/pipewire)(1)
