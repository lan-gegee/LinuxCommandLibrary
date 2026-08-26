# TAGLINE

从命令行控制 PulseAudio 和 PipeWire 的音量

# TLDR

**获取当前音量**

```pamixer --get-volume```

**设置音量**

```pamixer --set-volume [50]```

**增大音量**

```pamixer -i [5]```

**减小音量**

```pamixer -d [5]```

**静音**

```pamixer -m```

**取消静音**

```pamixer -u```

**切换静音状态**

```pamixer -t```

**为指定的 sink 设置音量**

```pamixer --sink [1] --set-volume [50]```

# SYNOPSIS

**pamixer** [_--get-volume_] [_--set-volume n_] [_-i n_] [_-d n_] [_-m_] [_-u_] [_options_]

# PARAMETERS

**--get-volume**
> 显示当前音量。

**--set-volume** _N_
> 设置音量百分比。

**-i** _N_, **--increase** _N_
> 将音量增大 N%。

**-d** _N_, **--decrease** _N_
> 将音量减小 N%。

**-m**, **--mute**
> 静音。

**-u**, **--unmute**
> 取消静音。

**-t**, **--toggle-mute**
> 切换静音状态。

**--get-mute**
> 显示静音状态。

**--sink** _ID_
> 选择 sink（输出设备）。

**--source** _ID_
> 选择 source（输入设备）。

**--default-source**
> 使用默认 source。

**--list-sinks**
> 列出可用的 sink。

**--list-sources**
> 列出可用的 source。

**--allow-boost**
> 允许音量超过 100%。

# DESCRIPTION

**pamixer** 从命令行控制 PulseAudio 和 PipeWire 的音量。它为脚本和快捷键绑定提供简单的音量管理。

音量操作均以百分比进行。增大和减小是相对当前音量进行调整，而 set-volume 则是设置一个绝对百分比。

静音控制可以在不改变音量的情况下切换声音开关。切换命令提供了单键静音/取消静音的功能。

存在多个 sink 时，可以选择特定的音频输出。未指定时使用默认 sink。source 用于控制麦克风等输入设备的电平。

allow-boost 允许音量超过 100%，适用于音源本身较小的情况。但对于已经很响的内容，这样做可能导致失真。

该工具同时支持 PulseAudio 和 PipeWire（通过其 PulseAudio 兼容层）。

# CAVEATS

需要 PulseAudio 或 PipeWire。音量超过 100% 可能产生失真。sink ID 在重启后可能会改变。

# HISTORY

**pamixer** 是作为图形化 PulseAudio 混音器的命令行替代品而开发的。它让极简窗口管理器用户可以通过脚本、快捷键绑定和状态栏来控制音量。

# INSTALL

```apt: sudo apt install pamixer```

```dnf: sudo dnf install pamixer```

```pacman: sudo pacman -S pamixer```

```apk: sudo apk add pamixer```

```zypper: sudo zypper install pamixer```

```nix: nix profile install nixpkgs#pamixer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pactl](/man/pactl)(1), [pulsemixer](/man/pulsemixer)(1), [amixer](/man/amixer)(1), [wpctl](/man/wpctl)(1)
