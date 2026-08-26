# TAGLINE

通过 PipeWire 播放 MIDI 文件

# TLDR

**播放 MIDI 文件**

```pw-midiplay [path/to/file.mid]```

以指定音量**播放**

```pw-midiplay --volume [0.5] [path/to/file.mid]```

**播放**到特定目标节点

```pw-midiplay --target [node_id] [path/to/file.mid]```

以详细输出**播放**

```pw-midiplay -v [path/to/file.mid]```

# SYNOPSIS

**pw-midiplay** [_options_] [_FILE_ | **-**]

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
> 目标节点：auto、0 或特定的节点 ID。

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

**pw-midiplay** 通过 PipeWire 服务器播放 MIDI 文件。它是 **pw-cat --playback --midi** 的便捷封装，使 MIDI 事件能够进入 PipeWire 音频图。

该工具本身不会将 MIDI 渲染为可听到的声音。它把 MIDI 事件发送进 PipeWire 图，事件必须被路由到 MIDI 合成器（如 **qsynth**、**fluidsynth** 或 **timidity**）或硬件 MIDI 设备才能发出声音。

当以 **-** 作为文件时，数据从标准输入读取。

# CAVEATS

自身不会产生可听到的输出。必须在 PipeWire 图中连接单独的 MIDI 合成器或兼容硬件，才能将 MIDI 事件渲染为音频。支持标准 MIDI 文件格式（.mid）。

# HISTORY

**PipeWire** 的一部分，该现代多媒体框架由 Red Hat 的 **Wim Taymans** 创建。PipeWire 于 **2017** 年首次发布，现已成为主流 Linux 发行版中默认的音频和视频服务器，取代了 PulseAudio 和 JACK。pw-cat 系列工具提供简单的命令行媒体播放和采集功能。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cat](/man/pw-cat)(1), [pw-midirecord](/man/pw-midirecord)(1), [pw-mididump](/man/pw-mididump)(1), [pw-play](/man/pw-play)(1), [pipewire](/man/pipewire)(1)
