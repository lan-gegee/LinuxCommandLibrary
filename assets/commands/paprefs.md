# TAGLINE

PulseAudio 首选项图形界面

# TLDR

**打开 PulseAudio 首选项**

```paprefs```

# SYNOPSIS

**paprefs**

# PARAMETERS

没有命令行参数。这是一个 GUI 应用程序。

# DESCRIPTION

**paprefs** 是基于 GTK 的 PulseAudio 声音服务器配置对话框。它提供多个标签页，用于配置网络访问（允许其他机器在本地设备上播放声音）、网络服务器设置（让本地 PulseAudio 可被其他机器发现）、同步输出（同时向多个 sink 播放音频）以及组播/RTP 流。

# CAVEATS

需要声音服务器中加载了 module-gconf 的 PulseAudio。只能配置本地服务器。除非启用了 PulseAudio 兼容支持，否则不适用于仅使用 PipeWire 的环境。

# HISTORY

paprefs 是为 **PulseAudio** 的网络和模块配置而开发的。

# INSTALL

```apt: sudo apt install paprefs```

```dnf: sudo dnf install paprefs```

```pacman: sudo pacman -S paprefs```

```zypper: sudo zypper install paprefs```

```nix: nix profile install nixpkgs#paprefs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pavucontrol](/man/pavucontrol)(1), [pulseaudio](/man/pulseaudio)(1), [pactl](/man/pactl)(1)
