# TAGLINE

ALSA MIDI 端口连接管理器

# TLDR

**列出**所有 MIDI 输入和输出端口

```aconnect -l```

**连接**两个 MIDI 端口

```aconnect [sender_client]:[port] [receiver_client]:[port]```

**断开**两个 MIDI 端口

```aconnect -d [sender_client]:[port] [receiver_client]:[port]```

断开**所有**连接

```aconnect -x```

只列出**输入**端口

```aconnect -i```

# SYNOPSIS

**aconnect** [_-options_] _sender_ _receiver_

**aconnect** **-d** [_-options_] _sender_ _receiver_

**aconnect** **-i**|**-o** [_-options_]

**aconnect** **-x**

# DESCRIPTION

**aconnect** 是一个 ALSA（Advanced Linux Sound Architecture）实用工具，用于连接和断开 MIDI 端口。它管理 ALSA 音序器连接，在应用程序、硬件 MIDI 接口和虚拟 MIDI 端口之间路由 MIDI 数据。

在 Linux 音频工作流中设置 MIDI 路由时，这个工具不可或缺：可以把 MIDI 控制器连接到合成器、在 DAW 之间路由数据，或将 MIDI 效果处理器串联起来。

# PARAMETERS

**-l**, **--list**
> 列出当前的 MIDI 端口和连接

**-i**, **--input**
> 只列出输入（可读）端口

**-o**, **--output**
> 只列出输出（可写）端口

**-d**, **--disconnect**
> 断开指定的端口

**-x**, **--removeall**
> 移除所有连接

**-e**, **--exclusive**
> 以独占方式连接端口（不允许其他连接）

**-r**, **--real** _queue_
> 使用给定的实时队列转换时间戳

**-t**, **--tick** _queue_
> 使用给定的 tick 队列转换时间戳

# CAVEATS

用 aconnect 建立的连接不是持久的；MIDI 设备拔出或系统重启后连接即失效。要建立持久连接，请使用 **qjackctl** 等工具或编写启动脚本。客户端编号在不同会话之间可能变化。

# HISTORY

**aconnect** 于 **20 世纪 90 年代**末作为 ALSA 项目的一部分开发。它为 ALSA 音序器系统提供了命令行接口，该系统取代了 Linux 中较旧的 OSS（Open Sound System）MIDI 处理机制。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[amidi](/man/amidi)(1), [aplaymidi](/man/aplaymidi)(1), [arecordmidi](/man/arecordmidi)(1), [aseqdump](/man/aseqdump)(1)

# RESOURCES

```[Source code](https://github.com/alsa-project/alsa-utils)```

```[Homepage](https://www.alsa-project.org/)```

<!-- verified: 2026-06-10 -->
