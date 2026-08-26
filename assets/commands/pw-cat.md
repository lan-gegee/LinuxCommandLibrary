# TAGLINE

通过 PipeWire 播放和录制音频

# TLDR

**播放** WAV 文件

```pw-cat -p [path/to/file.wav]```

以指定的**重采样质量**播放

```pw-cat -q [8] -p [path/to/file.wav]```

**录制**到文件并调整音量

```pw-cat -r --volume [1.25] [path/to/file.wav]```

以**自定义采样率**录制

```pw-cat -r --rate [48000] [path/to/file.wav]```

显示**帮助**

```pw-cat -h```

# SYNOPSIS

**pw-cat** [**-p**|**-r**] [**-q** _quality_] [**--volume** _vol_] [**--rate** _rate_] _file_

# PARAMETERS

**-p, --playback**
> 播放音频文件

**-r, --record**
> 录制到音频文件

**-q, --quality _level_**
> 重采样质量（0-15，默认 4）

**--volume _level_**
> 音量级别（1.0 = 100%）

**--rate _hz_**
> 以 Hz 表示的采样率

**--channels _num_**
> 声道数

**--target _target_**
> 要连接的目标节点

# DESCRIPTION

**pw-cat** 通过 PipeWire 播放和录制音频文件。它提供简单的命令行界面进行音频播放和录制，类似于 PulseAudio 的 pacat。

该工具支持多种音频格式，并可连接到特定的 PipeWire 节点。它适合用于测试音频配置和简单的录音任务。

# CAVEATS

需要正在运行的 PipeWire 实例。相比完整的音频播放器，格式支持有限。可用 pw-play 和 pw-record 作为更简单的别名。

# HISTORY

**pw-cat** 是 **PipeWire** 多媒体框架的一部分。它为 PipeWire 生态系统提供与 PulseAudio 的 pacat 工具类似的功能。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pw-play](/man/pw-play)(1), [pw-record](/man/pw-record)(1), [pw-cli](/man/pw-cli)(1), [wpctl](/man/wpctl)(1)
