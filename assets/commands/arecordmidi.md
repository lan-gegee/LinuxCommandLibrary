# TAGLINE

将 MIDI 事件录制为标准 MIDI 文件

# TLDR

**列出**可用的音序器端口

```arecordmidi -l```

将某端口（client:port）的 MIDI **录制**到文件

```arecordmidi -p [20:0] [recording.mid]```

以**指定速度**（BPM）录制

```arecordmidi -p [20:0] -b [120] [recording.mid]```

在另一个端口上播放**节拍器**并录制

```arecordmidi -p [20:0] -m [128:0] [recording.mid]```

# SYNOPSIS

**arecordmidi** **-p** _client:port_[_,..._] [_options_] _midifile_

# DESCRIPTION

**arecordmidi** 将 ALSA 音序器端口的 MIDI 数据录制为标准 MIDI 文件。它从连接的键盘或控制器捕获音符事件、控制变更和其他 MIDI 消息。

端口以 _client:port_ 形式（例如 **20:0**）或名称寻址，可通过 **-l** 选项查看。该工具适合在不运行完整 DAW 应用的情况下捕捉演奏。

# PARAMETERS

**-p** _client:port_[_,..._], **--port** _client:port_
> 要录制的音序器源端口（必需）

**-l**, **--list**
> 列出可能的输入端口后退出

**-b** _bpm_, **--bpm** _bpm_
> 速度，单位为每分钟节拍数（默认：120）

**-t** _ticks_, **--ticks** _ticks_
> 时间分辨率，单位为每拍 tick 数（默认：384）

**-f** _frames_, **--fps** _frames_
> 使用 SMPTE 计时而非音乐节拍（24、25、29.97 或 30 fps）

**-s**, **--split-channels**
> 将每个 MIDI 通道写入单独的轨道（format 1 文件）

**-m** _client:port_, **--metronome** _client:port_
> 在指定端口上播放节拍器滴答声

**-i** _num:den_, **--timesig** _num:den_
> 拍号；分母必须是 2 的幂（默认：4:4）

# CAVEATS

录制立即开始；默认没有倒计时。**arecordmidi** 只从 ALSA 音序器端口读取，不读取原始 MIDI 设备，因此需先通过音序器连接原始硬件（例如用 **amidi** 或虚拟 raw-MIDI 端口）。用 **Ctrl-C** 停止录制；文件在退出时写入。

# HISTORY

**arecordmidi** 是 ALSA 实用工具的一部分，自 **2000 年代初** ALSA 推出以来一直提供基本的 MIDI 录制功能。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aplaymidi](/man/aplaymidi)(1), [aconnect](/man/aconnect)(1), [amidi](/man/amidi)(1)

# RESOURCES

```[Source code](https://github.com/alsa-project/alsa-utils)```

```[Homepage](https://www.alsa-project.org)```

<!-- verified: 2026-06-15 -->
