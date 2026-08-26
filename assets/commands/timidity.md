# TAGLINE

软件 MIDI 合成器与转换器

# TLDR

**播放 MIDI 文件**

```timidity [path/to/file.mid]```

**使用 ncurses 界面播放**

```timidity -in [path/to/file.mid]```

**将 MIDI 转换为 WAV**

```timidity -Ow -o [output.wav] [input.mid]```

**将 MIDI 转换为 WAV 并输出到 stdout**以便管道处理

```timidity -Ow -o - [input.mid]```

**提高音量播放**

```timidity -A [150] [path/to/file.mid]```

**作为 ALSA 音序器客户端运行**

```timidity -iA```

**播放多个文件**并在每个文件之间卸载乐器数据

```timidity -U [file1.mid] [file2.mid]```

# SYNOPSIS

**timidity** [_options_] _file_ [_file_...]

# PARAMETERS

**-A** _n_
> 将主音量放大设为 n%。默认 70%，范围 0-800。

**-a**
> 启用抗混叠。让采样经过低通滤波器以减少混叠噪声。

**-B** _n_,_m_
> 为音频驱动设置缓冲区分片数为 n、分片大小为 2^m 字节。

**-i** _mode_
> 界面模式：d（dumb）、n（ncurses）、g（GTK+）、r（MIDI 服务器）、A（ALSA 音序器）。

**-o** _file_
> 输出到文件。使用 - 表示 stdout。

**-O** _mode_
> 输出模式：d（音频设备）、w（RIFF WAVE）、a（AIFF）、r（raw）、u（Sun audio）、v（Ogg Vorbis）、F（FLAC）、l（列出 MIDI 事件）、M（MOD 转 MIDI）。

**-s** _freq_
> 设置采样频率（Hz）。默认 44100。

**-F**
> 启用快速声像，让声像调整能影响已在播放的音符。

**-f**
> 启用快速包络，以更短的音符释放时间为代价换取更好的性能。

**-p** _voices_
> 设置同时发声的最大数量（复音数）。默认取决于系统。

**-U**
> 在文件之间从内存卸载乐器数据，降低内存占用。

**-c** _file_
> 读取额外的配置文件。

**-L** _path_
> 添加搜索音色补丁文件的路径。

**-E** _mode_
> 设置 TiMidity++ 扩展模式，用于效果和混响。

**-Q** _channels_
> 忽略 MIDI 通道。以逗号分隔的要静音通道号列表（1-16）。

**-T** _n_
> 将速度调整为 n%。默认 100。

**-h**
> 显示帮助信息以及可用输出模式和界面列表。

# DESCRIPTION

**TiMidity++** 是一款软件 MIDI 合成器，使用 SoundFont 或 GUS 补丁乐器将 MIDI 文件转换为音频。它可以通过音频设备实时播放 MIDI 文件，也可以将其转换为 WAV、AIFF 或 raw PCM 等音频格式。

该程序支持标准 MIDI 文件（.mid）、Recomposer 文件（.rcp、.r36、.g18、.g36）以及模块文件（.mod）。它使用 Gravis Ultrasound 兼容的补丁文件或 SoundFont（.sf2），从 MIDI 数据合成音频。

TiMidity++ 提供多种界面，包括哑终端界面、基于 ncurses 的界面、GTK+ GUI，还可作为 ALSA 音序器客户端或 MIDI 服务器运行。这种灵活性使它既能用于播放，也能作为系统级 MIDI 合成器。

# CONFIGURATION

**/etc/timidity/timidity.cfg**
> 系统级配置，指定 SoundFont 和补丁文件路径、默认输出模式和音频设置。

**~/.timidity.cfg**
> 各用户的覆盖配置。

**-c** _file_
> 运行时加载额外的配置文件。

# CAVEATS

TiMidity++ 需要 SoundFont 或补丁文件才能发出声音。如果 /etc/timidity/timidity.cfg（或类似位置）中的乐器文件没有正确配置，将不会产生任何音频。音质和 CPU 占用在很大程度上取决于所用的 SoundFont 文件。

# HISTORY

TiMidity 最初由 **Tuukka Toivonen** 于 **1995 年**编写。增强版 **TiMidity++** 由 **Masanao Izumo** 自 **1999 年**起开发，加入了众多重要特性，包括多种输出模式、实时 MIDI 合成以及各种用户界面。对于没有硬件合成器的 Linux 系统，它是流行的 MIDI 播放方案。

# INSTALL

```apt: sudo apt install timidity```

```zypper: sudo zypper install timidity```

```brew: brew install timidity```

```nix: nix profile install nixpkgs#timidity```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fluidsynth](/man/fluidsynth)(1), [aplaymidi](/man/aplaymidi)(1), [aplay](/man/aplay)(1), [pmidi](/man/pmidi)(1)
