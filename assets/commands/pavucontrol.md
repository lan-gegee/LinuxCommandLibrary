# TAGLINE

PulseAudio 音量控制

# TLDR

**打开音量控制**

```pavucontrol```

**在指定标签页启动**

```pavucontrol -t [1]```

# SYNOPSIS

**pavucontrol** [_options_]

# PARAMETERS

**-t**, **--tab=**_NUMBER_
> 在指定编号的标签页启动（1=Playback，2=Recording，3=Output Devices，4=Input Devices，5=Configuration）。

**--maximize**
> 以最大化窗口启动。

**--retry**
> PulseAudio 连接失败时重试。

**--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**pavucontrol** 即 PulseAudio 音量控制。是面向 PulseAudio 的图形化混音器。

该应用控制每个应用的音量，提供流和设备管理功能。

# CAVEATS

GUI 应用。需要 PulseAudio。支持按流控制。

# HISTORY

pavucontrol 是为 **PulseAudio 图形化**音量控制而创建的。

# INSTALL

```apt: sudo apt install pavucontrol```

```dnf: sudo dnf install pavucontrol```

```pacman: sudo pacman -S pavucontrol```

```apk: sudo apk add pavucontrol```

```zypper: sudo zypper install pavucontrol```

```nix: nix profile install nixpkgs#pavucontrol```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulseaudio](/man/pulseaudio)(1), [pactl](/man/pactl)(1), [alsamixer](/man/alsamixer)(1)
