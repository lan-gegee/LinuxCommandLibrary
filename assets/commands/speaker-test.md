# TAGLINE

为 ALSA 扬声器生成测试音

# TLDR

用**粉红噪声**测试扬声器

```speaker-test```

用指定频率的**正弦波**测试

```speaker-test -t sine -f [frequency]```

用**预置 WAV** 文件测试

```speaker-test -t wav```

用**自定义 WAV** 文件测试

```speaker-test -t wav -w [path/to/file.wav]```

测试指定的**通道数**

```speaker-test -c [channels]```

测试**特定设备**

```speaker-test -D [device_name]```

测试**单个扬声器**通道

```speaker-test -s [channel_number]```

# SYNOPSIS

**speaker-test** [_OPTIONS_]

# PARAMETERS

**-c, --channels** _num_
> 要测试的通道数（默认：8）

**-D, --device** _name_
> 要使用的 PCM 设备名称

**-f, --frequency** _freq_
> 正弦波频率，单位 Hz（默认：440）

**-t, --test** _type_
> 测试信号：pink、sine、wav 或 st2095

**-l, --nloops** _count_
> 测试循环次数（0 = 无限）

**-s, --speaker** _channel_
> 仅测试单个通道

**-w, --wavfile** _file_
> 用于 wav 测试的自定义 WAV 文件

**-W, --wavdir** _directory_
> 包含 WAV 文件的目录

**-r, --rate** _rate_
> 采样率，单位 Hz

**-b, --buffer** _time_
> 缓冲区大小，单位微秒

**-p, --period** _time_
> 周期大小，单位微秒

**-P, --nperiods** _periods_
> 周期数（默认：4）

**-m, --chmap** _map_
> 通道位置映射覆盖

**-X, --force-frequency**
> 允许超出 30-8000Hz 范围的频率

**--help**
> 显示用法信息

# DESCRIPTION

**speaker-test** 通过 ALSA 声音设备生成测试音，以验证扬声器配置和通道映射。它支持多种测试信号，包括粉红噪声、正弦波和 WAV 文件播放。

该工具会依次轮播每个扬声器通道的测试信号，帮助确认哪个物理扬声器对应哪个音频通道。使用 **aplay -L** 可列出 **-D** 选项可用的 PCM 设备。

# CAVEATS

需要 ALSA 及相应的声卡驱动。过高或过低的频率可能听不见，也可能损坏扬声器。默认设备可能不是预期的输出设备；请用 **-D** 指定。某些测试信号需要安装扬声器测试 WAV 文件。

# HISTORY

**speaker-test** 是 **alsa-utils**——ALSA（Advanced Linux Sound Architecture）实用工具集——的一部分。ALSA 在内核 **2.6**（2003 年）中取代 OSS 成为标准的 Linux 声音系统。speaker-test 工具帮助用户配置多声道音频系统并验证环绕声配置。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aplay](/man/aplay)(1), [arecord](/man/arecord)(1), [amixer](/man/amixer)(1), [alsamixer](/man/alsamixer)(1)
