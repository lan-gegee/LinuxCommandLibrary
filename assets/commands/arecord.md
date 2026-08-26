# TAGLINE

从 ALSA 声音设备录制音频

# TLDR

以 **CD 音质**录制（用 Ctrl+C 结束）

```arecord -vv -f cd [path/to/file.wav]```

以 **10 秒固定时长**录制

```arecord -vv -f cd -d 10 [path/to/file.wav]```

录制并保存为 **MP3**（通过 lame）

```arecord -vv -f cd -t raw | lame -r - [path/to/file.mp3]```

**列出**所有声卡和数字音频设备

```arecord -l```

启用**交互式**界面

```arecord -i```

用 5 秒样本**测试麦克风**

```arecord -d 5 test-mic.wav && aplay test-mic.wav && rm test-mic.wav```

# SYNOPSIS

**arecord** [_-d duration_] [_-f format_] [_-r rate_] [_-c channels_] [_file_]

# DESCRIPTION

**arecord** 是面向 ALSA 声卡驱动的命令行录音工具。它从声卡采集音频并以多种格式保存，包括 WAV、AU、VOC 和原始音频。该工具支持可配置的采样率、位深和声道数。简写格式 **cd** 表示 44100 Hz 的 16 位有符号小端序立体声。原始输出可通过管道传给 **lame** 等编码器转换为 MP3。它是 **aplay** 的录音对应工具。

# PARAMETERS

**-d**, **--duration** _seconds_
> 在指定的秒数后停止录音。

**-f**, **--format** _format_
> 采样格式（cd、S16_LE、S16_BE、U8、S32_LE 等）。

**-r**, **--rate** _rate_
> 采样率，单位 Hz（2000-192000）。

**-c**, **--channels** _count_
> 声道数（1 为单声道，2 为立体声）。

**-t**, **--file-type** _type_
> 文件类型（wav、raw、au、voc）。

**-l**, **--list-devices**
> 列出所有声卡和数字音频设备。

**-L**, **--list-pcms**
> 列出所有已定义的 PCM。

**-D**, **--device** _name_
> 按名称选择 PCM 设备。

**-M**, **--mmap**
> 对音频流使用内存映射 I/O 模式。

**-N**, **--nonblock**
> 以非阻塞模式打开音频设备。

**-F**, **--period-time** _microseconds_
> 中断间隔时间，单位微秒。

**-B**, **--buffer-time** _microseconds_
> 缓冲时长，单位微秒。

**-V**, **--vumeter** _type_
> VU 表类型（stereo 或 mono）。

**-i**, **--interactive**
> 允许通过 stdin 进行交互式控制。

**-v**, **--verbose**
> 详细模式；用 -vv 获得更多信息，包括 VU 表。

**-q**, **--quiet**
> 安静模式；抑制消息。

**--disable-resample**
> 禁用自动采样率重采样。

**--disable-channels**
> 禁用自动声道转换。

**--disable-format**
> 禁用自动格式转换。

# CAVEATS

需要安装并配置 ALSA 驱动。**cd** 格式是 16 位有符号小端序、44100 Hz、立体声的简写。

# HISTORY

属于 **ALSA**（Advanced Linux Sound Architecture）实用工具软件包，ALSA 取代 OSS 成为 Linux 标准声音系统。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aplay](/man/aplay)(1), [alsamixer](/man/alsamixer)(1), [amixer](/man/amixer)(1)
