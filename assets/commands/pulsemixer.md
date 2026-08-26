# TAGLINE

PulseAudio 的 CLI 和 TUI 混音器

# TLDR

**启动 TUI 混音器**

```pulsemixer```

**获取**音量

```pulsemixer --get-volume```

**设置**音量

```pulsemixer --set-volume [50]```

按相对数值**调整**音量

```pulsemixer --change-volume [+10]```

带最大上限地**调整**音量

```pulsemixer --change-volume [+10] --max-volume [100]```

切换静音/取消静音

```pulsemixer --toggle-mute```

**列出** sink 设备

```pulsemixer --list-sinks```

为指定的 sink **设置**音量

```pulsemixer --id [sink-1] --set-volume [75]```

# SYNOPSIS

**pulsemixer** [_options_]

# PARAMETERS

**--get-volume**
> 打印当前音量。

**--set-volume** _n_
> 设置音量（0-100）。

**--get-mute**
> 打印静音状态。

**--toggle-mute**
> 切换静音。

**--mute**
> 静音。

**--unmute**
> 取消静音。

**--list-sinks**
> 列出输出设备。

**--list-sources**
> 列出输入设备。

**--change-volume** _+-n_
> 按相对数值调整音量。

**--set-volume-all** _n:n_
> 分别为每个声道设置音量。

**--max-volume** _n_
> 使用 --change-volume 时将音量上限设为 n。

**--id** _id_
> 指定目标 sink/source。

**--server** _server_
> 连接到指定的 PulseAudio 服务器。

**--color** _n_
> 为输出着色（0=无，1=仅选中项，2=全部）。

**--no-mouse**
> 在 TUI 中禁用鼠标支持。

**-l**, **--list**
> 列出所有 sink、source 和 sink 输入流。

# DESCRIPTION

**pulsemixer** 是 PulseAudio 的 CLI 和 TUI 混音器。它同时提供交互式界面和命令行控制方式，用于管理音频音量和路由。

# EXAMPLES

```bash
# Interactive mode
pulsemixer

# Set to 75%
pulsemixer --set-volume 75

# Change specific sink
pulsemixer --id sink-1 --set-volume 50

# Toggle mute
pulsemixer --toggle-mute

# Get current volume
vol=$(pulsemixer --get-volume | cut -d' ' -f1)
```

# TUI KEYS

```
h/l, Left/Right  - Adjust volume
j/k, Up/Down     - Select
m                - Toggle mute
Space            - Lock/unlock channels
1-9, 0           - Set volume 10%-90%, 100%
Enter            - Context menu
F1/F2/F3         - Switch mode (output/input/cards)
q, Esc           - Quit
```

# CAVEATS

需要 PulseAudio。也可通过 PipeWire 的 PulseAudio 兼容层工作。

# HISTORY

pulsemixer 由 **GeorgeFilipkin** 创建，是一个便捷的 PulseAudio 控制 CLI/TUI 工具。

# INSTALL

```pacman: sudo pacman -S pulsemixer```

```apk: sudo apk add pulsemixer```

```nix: nix profile install nixpkgs#pulsemixer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pactl](/man/pactl)(1), [pavucontrol](/man/pavucontrol)(1), [amixer](/man/amixer)(1)
