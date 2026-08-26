# TAGLINE

发送和接收原始 MIDI 数据

# TLDR

**列出** MIDI 硬件端口

```amidi -l```

向端口**发送** MIDI 文件

```amidi -p [hw:1,0,0] -s [file.syx]```

将 MIDI 数据**接收**到文件

```amidi -p [hw:1,0,0] -r [output.syx]```

**转储**收到的 MIDI 消息

```amidi -p [hw:1,0,0] -d```

发送**系统专有**数据

```amidi -p [hw:1,0,0] -S "F0 43 10 4C 00 00 7E 00 F7"```

# SYNOPSIS

**amidi** [_-l_] [_-p port_] [_-s file_] [_-r file_] [_-S hex_] [_-d_] [_options_]

# DESCRIPTION

**amidi** 是一个用于发送和接收原始 MIDI 数据的 ALSA 工具。它在字节层面工作，适合发送系统专有（SysEx）消息、向 MIDI 设备推送固件更新或捕获 MIDI 转储数据。

与更高层的 MIDI 音序器不同，amidi 不解释 MIDI 时序或乐曲结构；它只是在硬件端口之间传输原始数据。

# PARAMETERS

**-l**, **--list-devices**
> 列出可用的硬件 MIDI 端口

**-L**, **--list-rawmidis**
> 列出所有 RawMIDI 定义（调试配置文件时很有用）

**-p** _port_, **--port=**_port_
> 要使用的 RawMIDI 端口（如 hw:1,0,0）。默认为卡 0 上的端口 0

**-s** _file_, **--send=**_file_
> 将 file 中的原始 MIDI 命令发送到端口（如 .syx 文件）

**-r** _file_, **--receive=**_file_
> 从端口接收数据并写入 file

**-S** _hex_, **--send-hex=**_hex_
> 将以十六进制表示的字节发送到端口

**-d**, **--dump**
> 以十六进制字节形式打印接收到的数据

**-t** _seconds_, **--timeout=**_seconds_
> 在给定时间内没有数据到达时停止接收

**-a**, **--active-sensing**
> 不忽略 Active Sensing 字节（FEh）

**-c**, **--clock**
> 不忽略 Clock 字节（F8h）

**-i** _ms_, **--sysex-interval=**_ms_
> 在每条 SysEx 消息之间加入延迟，固件更新时很有用

# CAVEATS

仅支持硬件 MIDI 端口，不支持虚拟/软件端口。SysEx 传输可能数据量大且速度慢。某些设备对消息间的时序有特殊要求。

# HISTORY

**amidi** 是 ALSA 工具集的一部分，自 **2000** 年代初 ALSA 在 Linux 内核中取代 OSS 以来一直提供底层 MIDI 访问能力。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aconnect](/man/aconnect)(1), [aplaymidi](/man/aplaymidi)(1), [arecordmidi](/man/arecordmidi)(1)

# RESOURCES

```[Source code](https://github.com/alsa-project/alsa-utils)```

```[Homepage](https://www.alsa-project.org)```

<!-- verified: 2026-06-11 -->
