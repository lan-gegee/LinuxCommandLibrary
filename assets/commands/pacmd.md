# TAGLINE

在运行时重新配置 PulseAudio 的命令行工具

# TLDR

**列出 sink（输出设备）**

```pacmd list-sinks```

**列出 source（输入设备）**

```pacmd list-sources```

**设置默认 sink**

```pacmd set-default-sink [sink_name]```

**设置 sink 音量**

```pacmd set-sink-volume [sink_name] [65536]```

**将流移动到另一个 sink**

```pacmd move-sink-input [index] [sink_name]```

**交互模式**

```pacmd```

# SYNOPSIS

**pacmd** [_command_]

# PARAMETERS

**list-sinks**
> 列出输出设备。

**list-sources**
> 列出输入设备。

**list-sink-inputs**
> 列出播放流。

**list-source-outputs**
> 列出录制流。

**list-modules**
> 列出已加载的 PulseAudio 模块。

**set-default-sink** _name_
> 设置默认输出。

**set-default-source** _name_
> 设置默认输入。

**set-sink-volume** _name_ _vol_
> 设置 sink 音量（线性值 0-65536）。

**set-source-volume** _name_ _vol_
> 设置 source 音量。

**set-sink-mute** _name_ _0|1_
> 静音/取消静音某个 sink。

**set-source-mute** _name_ _0|1_
> 静音/取消静音某个 source。

**move-sink-input** _idx_ _sink_
> 将播放流移动到另一个 sink。

**move-source-output** _idx_ _source_
> 将录制流移动到另一个 source。

**load-module** _name_ [_args_]
> 加载 PulseAudio 模块。

**unload-module** _id_
> 按索引或名称卸载模块。

**help**
> 显示所有支持的命令。

**exit**
> 终止 PulseAudio 守护进程（交互模式下按 Ctrl+D 退出）。

# DESCRIPTION

**pacmd** 是一款在运行时重新配置 PulseAudio 的命令行工具。它提供对 PulseAudio 内部配置和状态的完整访问能力。

不带参数运行会进入支持 Tab 补全的交互模式。

# VOLUME SCALE

```
0     = 0%   (muted)
32768 = 50%
65536 = 100% (normal)
98304 = 150% (amplified)
```

# CAVEATS

PulseAudio 专属。更简单的操作可使用 pactl。更改可能不会在重启后保留。可以考虑迁移到 PipeWire。

# HISTORY

pacmd 是 **PulseAudio** 的一部分，后者由 **Lennart Poettering** 自 **2004** 年起开发，作为新一代声音服务器。

# INSTALL

```apt: sudo apt install pulseaudio-utils```

```dnf: sudo dnf install pulseaudio-utils```

```apk: sudo apk add pulseaudio-utils```

```zypper: sudo zypper install pulseaudio-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pactl](/man/pactl)(1), [pulseaudio](/man/pulseaudio)(1), [pavucontrol](/man/pavucontrol)(1)
