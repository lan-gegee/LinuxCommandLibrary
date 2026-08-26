# TAGLINE

通过 ALSA 音序器播放 MIDI 文件

# TLDR

**播放 MIDI 文件**

```pmidi -p [port] [file.mid]```

**列出 MIDI 端口**

```pmidi -l```

**带延迟播放**

```pmidi -d [seconds] -p [port] [file.mid]```

# SYNOPSIS

**pmidi** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要播放的 MIDI 文件。

**-p** _PORT_
> MIDI 输出端口。

**-l**
> 列出可用端口。

**-d** _SECONDS_
> 播放前的延迟秒数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**pmidi** 通过 ALSA 音序器接口播放标准 MIDI 文件。它将 MIDI 事件发送到指定的输出端口，该端口可以是硬件合成器、FluidSynth 或 TiMidity 之类的软件合成器，或任何 ALSA MIDI 设备。

使用 **-l** 列出可用的 MIDI 端口，用 **-p** 选择播放的目标端口。该工具提供简单直接的 MIDI 文件播放功能，无需承受完整媒体播放器的额外开销。

# CAVEATS

仅支持 ALSA。需要 MIDI 端口。仅限 Linux。

# HISTORY

pmidi 属于 **ALSA 实用工具集**中负责 MIDI 播放的部分。

# INSTALL

```apt: sudo apt install pmidi```

```zypper: sudo zypper install pmidi```

```nix: nix profile install nixpkgs#pmidi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aplaymidi](/man/aplaymidi)(1), [timidity](/man/timidity)(1), [fluidsynth](/man/fluidsynth)(1)
