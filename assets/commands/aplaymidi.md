# TAGLINE

通过 ALSA 音序器播放 MIDI 文件

# TLDR

**播放** MIDI 文件

```aplaymidi -p [hw:1,0] [file.mid]```

**列出**可用的 MIDI 端口

```aplaymidi -l```

在每个文件结束后**延迟**一段时间再继续

```aplaymidi -p [hw:1,0] -d [2] [file.mid]```

# SYNOPSIS

**aplaymidi** [_-p port_] [_-d delay_] _files_

# DESCRIPTION

**aplaymidi** 通过 ALSA 音序器端口播放 MIDI 文件。它将 MIDI 事件发送到已连接的硬件合成器、软件合成器或其他 MIDI 应用。

与音频播放器不同，aplaymidi 只发送 MIDI 消息；实际发声取决于接收端设备或软件。

# PARAMETERS

**-p** _client:port_, **--port** _client:port_
> 设置接收 MIDI 事件的音序器端口。客户端可以用编号、名称或名称前缀指定。

**-l**, **--list**
> 列出可用的 MIDI 端口

**-d** _seconds_, **--delay** _seconds_
> 每个 MIDI 文件结束后的延迟时间，让最后的音符自然衰减。

**-h**, **--help**
> 打印选项列表。

**-V**, **--version**
> 打印当前版本。

# CAVEATS

需要连接 MIDI 合成器（硬件或软件）才能发声。重新连接 MIDI 设备后端口号可能变化。只能播放标准 MIDI 文件（SMF）。

# HISTORY

**aplaymidi** 是 ALSA 实用工具的一部分。自 **21 世纪初** ALSA 成为标准 Linux 音频架构以来，它一直提供基础的 MIDI 文件播放功能。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arecordmidi](/man/arecordmidi)(1), [aconnect](/man/aconnect)(1), [timidity](/man/timidity)(1), [fluidsynth](/man/fluidsynth)(1)
