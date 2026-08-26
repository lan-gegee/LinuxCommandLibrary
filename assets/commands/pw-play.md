# TAGLINE

通过 PipeWire 播放音频文件

# TLDR

**播放** WAV 文件

```pw-play [path/to/file.wav]```

以指定音量**播放**文件

```pw-play --volume [0.8] [path/to/file.wav]```

以自定义采样率**播放**

```pw-play --rate [48000] [path/to/file.wav]```

**播放**到特定目标节点

```pw-play --target [node_name] [path/to/file.wav]```

以指定的重采样质量**播放**

```pw-play -q [8] [path/to/file.wav]```

# SYNOPSIS

**pw-play** [_options_] _file_

# PARAMETERS

**--volume** _level_
> 播放音量（1.0 = 100%）。

**--rate** _hz_
> 以 Hz 表示的采样率。

**--channels** _num_
> 音频声道数。

**-q**, **--quality** _level_
> 重采样质量（0-15，默认 4）。

**--target** _target_
> 要连接的目标 PipeWire 节点。

**--channel-map** _map_
> 要使用的声道映射（如立体声用 FL,FR）。

**--format** _format_
> 采样格式（如 s16、s32、f32、f64）。

**--latency** _latency_
> 以毫秒表示的延迟。

# DESCRIPTION

**pw-play** 是 **pw-cat --playback** 的便捷封装，用于通过 PipeWire 播放音频文件。它支持常见的音频格式，包括 WAV、FLAC 和 Ogg。

**pw-cat** 在播放模式下可用的所有选项同样适用于 **pw-play**。完整文档见 **pw-cat**。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-cat](/man/pw-cat)(1), [pw-record](/man/pw-record)(1), [pw-cli](/man/pw-cli)(1), [pipewire](/man/pipewire)(1)
