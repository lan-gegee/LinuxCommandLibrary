# TAGLINE

通过 PipeWire 播放编码音频流

# TLDR

**播放编码音频文件**

```pw-encplay [path/to/file]```

以指定音量**播放**

```pw-encplay --volume [0.8] [path/to/file]```

**播放**到特定目标节点

```pw-encplay --target [node_id] [path/to/file]```

以详细输出**播放**

```pw-encplay -v [path/to/file]```

# SYNOPSIS

**pw-encplay** [_options_] [_FILE_ | **-**]

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

**pw-encplay** 通过 PipeWire 服务器播放已编码（压缩）的音频流。它是 **pw-cat** 编码播放模式的便捷封装，将编码音频数据直接传入 PipeWire 图，而无需先解码。

这样可以将以压缩格式（如 AC3、DTS 或 AAC）的音频直通（passthrough）到支持原生解码的硬件解码器或接收器，保留原始编码流的音质。

当以 **-** 作为文件时，数据从标准输入读取。

# CAVEATS

需要支持相应编码格式的输出设备才能进行直通播放。如果所连接的输出不支持该格式，则不会产生声音。通常与连接到 AV 功放的 HDMI 或 S/PDIF 输出配合使用。

# HISTORY

**PipeWire** 的一部分，该现代多媒体框架由 Red Hat 的 **Wim Taymans** 创建。PipeWire 于 **2017** 年首次发布，提供统一的音频和视频处理，取代了 PulseAudio 和 JACK。pw-cat 系列工具提供简单的命令行媒体播放和采集功能。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cat](/man/pw-cat)(1), [pw-play](/man/pw-play)(1), [pw-record](/man/pw-record)(1), [pipewire](/man/pipewire)(1)
