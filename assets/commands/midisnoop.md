# TAGLINE

监视 MIDI 消息

# TLDR

**启动 MIDI 监视器**

```midisnoop```

**监视指定端口**

```midisnoop -i [port]```

**列出 MIDI 端口**

```midisnoop -l```

**十六进制输出**

```midisnoop -x```

**详细输出**

```midisnoop -v```

# SYNOPSIS

**midisnoop** [_options_]

# PARAMETERS

**-i** _PORT_
> 输入端口。

**-l**
> 列出端口。

**-x**
> 十六进制输出。

**-v**
> 详细模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**midisnoop** 监视 MIDI 消息。它实时显示传入的 MIDI 数据。

该工具用于调试 MIDI 设备和软件。显示音符、控制和系统消息。

# CAVEATS

需要 MIDI 端口。支持 ALSA 或 JACK 后端。实时监视。

# HISTORY

midisnoop 通过显示来自已连接 MIDI 设备的消息来提供 **MIDI** 调试功能。

# INSTALL

```apt: sudo apt install midisnoop```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aconnect](/man/aconnect)(1), [pmidi](/man/pmidi)(1), [amidi](/man/amidi)(1)
