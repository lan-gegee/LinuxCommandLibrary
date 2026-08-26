# TAGLINE

从命令行控制正在运行的 PulseAudio 声音服务器

# TLDR

**列出所有音频 sink**（输出设备）

```pactl list sinks short```

**设置默认音频输出**

```pactl set-default-sink [sink_name]```

将**音量设置**为某个百分比

```pactl set-sink-volume @DEFAULT_SINK@ [50%]```

**音量提高** 10%

```pactl set-sink-volume @DEFAULT_SINK@ +[10%]```

对默认 sink 进行**静音/取消静音**

```pactl set-sink-mute @DEFAULT_SINK@ toggle```

**列出所有音频 source**（输入设备）

```pactl list sources short```

**将应用程序移动**到另一个输出设备

```pactl move-sink-input [stream_index] [sink_name]```

**加载 PulseAudio 模块**

```pactl load-module [module-null-sink]```

# SYNOPSIS

**pactl** [_options_] _command_ [_args_]

**pactl** set-sink-volume _SINK_ _VOLUME_

**pactl** list [short] [_TYPE_]

# PARAMETERS

**-s** _SERVER_, **--server** _SERVER_
> 连接到指定的 PulseAudio 服务器

**-n** _NAME_, **--client-name** _NAME_
> 连接使用的客户端名称

**-f** _FORMAT_, **--format** _FORMAT_
> 输出格式（text 或 json）

**-v**, **--verbose**
> 启用详细输出

**--version**
> 显示版本信息

**-h**, **--help**
> 显示帮助信息

# COMMANDS

**stat**
> 显示内存使用统计

**info**
> 显示服务器信息

**list** [short] [_TYPE_]
> 列出对象（modules、sinks、sources、sink-inputs、source-outputs、clients、samples、cards）

**exit**
> 终止 PulseAudio 服务器

**set-default-sink** _NAME|INDEX_
> 设置默认音频输出

**set-default-source** _NAME|INDEX_
> 设置默认音频输入

**set-sink-volume** _SINK_ _VOLUME_
> 设置 sink 音量（百分比、dB 或绝对值）

**set-source-volume** _SOURCE_ _VOLUME_
> 设置 source 音量

**set-sink-mute** _SINK_ _0|1|toggle_
> 对 sink 静音/取消静音

**set-source-mute** _SOURCE_ _0|1|toggle_
> 对 source 静音/取消静音

**move-sink-input** _INDEX_ _SINK_
> 将播放流移动到另一个 sink

**move-source-output** _INDEX_ _SOURCE_
> 将录制流移动到另一个 source

**load-module** _NAME_ [_ARGS_]
> 加载 PulseAudio 模块

**unload-module** _INDEX|NAME_
> 卸载模块

**set-card-profile** _CARD_ _PROFILE_
> 更改声卡配置档

**subscribe**
> 监听 PulseAudio 事件

# DESCRIPTION

**pactl** 从命令行控制正在运行的 PulseAudio 声音服务器。它提供可脚本化的接口来管理音频设备、流、音量和模块。

音量可以用百分比（50%）、分贝（0dB）或绝对值指定。加 + 或 - 前缀表示相对调整。特殊名称 **@DEFAULT_SINK@**、**@DEFAULT_SOURCE@** 和 **@DEFAULT_MONITOR@** 指代默认设备。

**list** 命令显示音频对象的详细信息。使用 **short** 可获得适合脚本的精简输出。**list sink-inputs** 返回的流索引可用于通过 **move-sink-input** 在不同输出设备之间移动应用程序。

# CAVEATS

需要 PulseAudio 守护进程正在运行。在使用带 PulseAudio 兼容层的 PipeWire 的系统上，pactl 命令可以工作但实际操作的是 PipeWire。**pacmd** 命令已被弃用，建议改用 pactl。允许超过 100% 的音量值，但可能导致失真。

# HISTORY

pactl 是 **PulseAudio** 的一部分，后者是由 **Lennart Poettering** 开发的面向 Linux 及其他类 Unix 系统的声音服务器。PulseAudio 于 **2004 年**首次发布，到 2009 年已成为大多数 Linux 发行版的默认声音系统。pactl 实用工具提供了访问 PulseAudio D-Bus 接口的命令行方式。近年来，**PipeWire** 开始取代 PulseAudio，同时保持与 pactl 命令的兼容性。

# INSTALL

```apt: sudo apt install pulseaudio-utils```

```dnf: sudo dnf install pulseaudio-utils```

```apk: sudo apk add pulseaudio-utils```

```zypper: sudo zypper install pulseaudio-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulseaudio](/man/pulseaudio)(1), [pacmd](/man/pacmd)(1), [pavucontrol](/man/pavucontrol)(1), [amixer](/man/amixer)(1)
