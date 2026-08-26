# TAGLINE

调试和监控 MIDI 事件

# TLDR

监听并转储所有**传入的 MIDI** 事件

```pw-mididump```

从**特定文件**转储 MIDI 事件

```pw-mididump path/to/file.mid```

连接到特定的**远程** PipeWire 实例

```pw-mididump -r remote_instance```

显示**帮助**

```pw-mididump -h```

显示**版本**

```pw-mididump --version```

# SYNOPSIS

**pw-mididump** [_options_] [_file_]

# PARAMETERS

**-r**, **--remote** _name_
> 连接到特定的远程 PipeWire 实例（默认：本地实例）

**-h**, **--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pw-mididump** 将 MIDI 消息转储到标准输出，用于调试和监控。它既可以监听来自已连接设备的实时 MIDI 事件，也可以从文件读取 MIDI 数据。

这对排查 MIDI 连接问题以及验证 MIDI 数据是否被正确接收很有用。

# CAVEATS

实时 MIDI 监控需要相应的设备权限。输出格式面向调试设计，不适合用于创建 MIDI 文件。

# HISTORY

**PipeWire**（Linux 上的现代多媒体框架）的一部分。在 PipeWire 生态内提供 MIDI 调试能力。

# INSTALL

```apt: sudo apt install pipewire-bin```

```apk: sudo apk add pipewire-tools```

```zypper: sudo zypper install pipewire-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1), [pw-cat](/man/pw-cat)(1), [aconnect](/man/aconnect)(1), [aplaymidi](/man/aplaymidi)(1), [amidi](/man/amidi)(1)
