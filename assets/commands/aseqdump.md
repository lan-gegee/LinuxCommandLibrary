# TAGLINE

显示 ALSA 音序器端口接收到的事件

# TLDR

**转储**来自所有源的 MIDI 事件

```aseqdump```

从**指定端口**转储

```aseqdump -p [20:0]```

**列出**可用的输入端口

```aseqdump -l```

以**规范化**的 MIDI 1.0 值显示事件

```aseqdump -p [20:0] -N```

以**百分比**显示事件

```aseqdump -p [20:0] -P```

# SYNOPSIS

**aseqdump** [**-p** _client:port,..._] [**-l**] [**-u** _version_] [**-r**] [**-R**|**-N**|**-P**]

# DESCRIPTION

**aseqdump** 是一个命令行工具，将它收到的 ALSA 音序器事件以人类可读的文本形式打印出来。它可用于调试 MIDI 连接、测试键盘以及监视 MIDI 数据流。

输出内容包括事件类型、通道、音符编号、力度、控制变更以及其他 MIDI 消息细节。

# PARAMETERS

**-h**, **--help**
> 打印选项列表

**-V**, **--version**
> 打印当前版本

**-l**, **--list**
> 打印可用输入端口的列表

**-p**, **--port**=_client:port,..._
> 设置接收事件的音序器端口。客户端可以用编号、名称或名称前缀指定。端口用编号指定；对于端口 0，":0" 部分可以省略

**-u**, **--ump**=_version_
> 设置客户端 MIDI 版本。0 为传统模式，1 为 UMP MIDI 1.0 模式，2 为 UMP MIDI 2.0 模式

**-r**, **--raw**
> 禁止在 UMP 客户端与传统客户端之间自动转换事件

**-R**, **--raw-view**
> 原样显示原始值。通道号和 UMP 组号从 0 开始计数。这是默认行为

**-N**, **--normalized-view**
> 显示与 MIDI 1.0 对齐的规范化值。通道号和组号从 1 开始计数，力度和数据值被规范化到 0 至 127 之间

**-P**, **--percent-view**
> 以百分比显示数值。通道号和组号从 1 开始计数

# CAVEATS

只显示 ALSA 音序器事件，不显示原始 MIDI。订阅特定端口可以过滤输出。事件只显示不记录。

# HISTORY

**aseqdump** 是 **alsa-utils** 软件包的一部分，自 ALSA 诞生以来就提供 MIDI 调试能力。

# INSTALL

```apt: sudo apt install alsa-utils```

```dnf: sudo dnf install alsa-utils```

```pacman: sudo pacman -S alsa-utils```

```apk: sudo apk add alsa-utils```

```zypper: sudo zypper install alsa-utils```

```nix: nix profile install nixpkgs#alsa-utils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aconnect](/man/aconnect)(1), [amidi](/man/amidi)(1), [arecordmidi](/man/arecordmidi)(1), [aseqnet](/man/aseqnet)(1), [aplaymidi](/man/aplaymidi)(1)
