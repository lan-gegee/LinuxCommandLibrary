# TAGLINE

简单的 PulseAudio 音量控制命令

# TLDR

音量**增大** 5%

```pulseaudio-ctl up```

按**指定数值**增大音量

```pulseaudio-ctl up 10```

音量**减小** 5%

```pulseaudio-ctl down```

将音量**设置**为指定百分比

```pulseaudio-ctl set 50```

仅当当前音量**高于**给定值时设置音量

```pulseaudio-ctl atmost 80```

切换**静音**

```pulseaudio-ctl mute```

切换**麦克风静音**

```pulseaudio-ctl mute-input```

# SYNOPSIS

**pulseaudio-ctl** _command_ [_amount_]

# PARAMETERS

**up** [_amount_]
> 增大音量（默认 5%）

**down** [_amount_]
> 减小音量（默认 5%）

**set** _percentage_
> 将音量设置为指定百分比

**atmost** _percentage_
> 仅当当前音量更高时设置音量

**mute**
> 切换扬声器静音

**mute-input**
> 切换麦克风静音

# DESCRIPTION

**pulseaudio-ctl** 提供控制 PulseAudio 音量的简单命令。它提供直观的命令来增大、减小和设置音量，以及静音扬声器和麦克风。

该工具专为与键盘快捷键和桌面环境轻松集成而设计。

# CAVEATS

需要 PulseAudio 正在运行。除非启用了 PulseAudio 兼容层，否则可能无法与 PipeWire 配合工作。

# HISTORY

作为一个便于 PulseAudio 音量控制的轻量级 shell 脚本而开发，常与窗口管理器和键盘快捷键守护进程配合使用。

# INSTALL

```apk: sudo apk add pulseaudio-ctl```

```nix: nix profile install nixpkgs#pulseaudio-ctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pactl](/man/pactl)(1), [pamixer](/man/pamixer)(1), [amixer](/man/amixer)(1)
