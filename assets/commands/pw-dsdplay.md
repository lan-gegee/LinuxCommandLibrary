# TAGLINE

通过 PipeWire 播放 DSD 音频文件

# TLDR

**播放 DSF 文件**

```pw-dsdplay [path/to/file.dsf]```

以指定音量**播放**

```pw-dsdplay --volume [0.5] [path/to/file.dsf]```

**播放**到特定目标节点

```pw-dsdplay --target [node_id] [path/to/file.dsf]```

以详细输出**播放**

```pw-dsdplay -v [path/to/file.dsf]```

# SYNOPSIS

**pw-dsdplay** [_options_] [_FILE_ | **-**]

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

**pw-dsdplay** 通过 PipeWire 服务器播放 DSF 格式的 DSD（Direct Stream Digital，直接流数字）音频文件。它是 **pw-cat --playback --dsd** 的便捷封装，使 DSD 数据能够进入 PipeWire 音频图。

DSD 是一种高分辨率音频格式，用于 Super Audio CD（SACD），它将音频编码为以极高采样率（通常为 2.8224 MHz 或更高）传输的单比特值流。原生 DSD 播放需要原生支持 DSD 的兼容硬件。

当以 **-** 作为文件时，数据从标准输入读取。

# CAVEATS

需要原生支持 DSD 的硬件才能产生可听到的输出。没有兼容的硬件时，不会听到任何声音。DSF 是 DSD 播放唯一支持的文件格式。

# HISTORY

**PipeWire** 的一部分，该现代多媒体框架由 Red Hat 的 **Wim Taymans** 创建。PipeWire 于 **2017** 年首次发布，现已成为主流 Linux 发行版中默认的音频和视频服务器，取代了 PulseAudio 和 JACK。pw-cat 系列工具提供简单的命令行媒体播放和采集功能。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cat](/man/pw-cat)(1), [pw-play](/man/pw-play)(1), [pw-record](/man/pw-record)(1), [pipewire](/man/pipewire)(1)
