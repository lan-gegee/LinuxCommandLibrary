# TAGLINE

支持 Winamp 皮肤的 Qt 音频播放器

# TLDR

**打开 qmmp**

```qmmp```

**播放文件**

```qmmp [file1.mp3] [file2.ogg]```

**将文件加入队列**

```qmmp --enqueue [files]```

**播放后退出**

```qmmp --play [file.mp3]```

**暂停播放**

```qmmp --pause```

**停止播放**

```qmmp --stop```

**下一曲**

```qmmp --next```

# SYNOPSIS

**qmmp** [_options_] [_files_]

# PARAMETERS

**--enqueue**
> 加入播放队列。

**--play**
> 开始播放。

**--pause**
> 暂停播放。

**--stop**
> 停止播放。

**--next**
> 下一曲。

**--previous**
> 上一曲。

**--toggle-visibility**
> 显示/隐藏窗口。

**--volume-up**
> 提高音量。

**--volume-down**
> 降低音量。

# DESCRIPTION

**Qmmp** 是一个基于 Qt 的音频播放器。其界面类似 Winamp/XMMS 经典皮肤。

它支持多种音频格式，包括 MP3、FLAC、OGG 和 APE。插件架构可以扩展其功能。

Winamp 皮肤提供个性化定制。经典 2.x 皮肤可以直接使用。

可视化插件展示音频分析。内置频谱分析仪和示波器。

队列管理负责处理播放列表。提供随机、重复和排序等选项。

# CAVEATS

需要 Qt 依赖。某些皮肤可能无法使用。插件可用性因平台而异。

# HISTORY

**Qmmp** 起初是 XMMS 和 Audacious 的 Qt 替代品。它在现代媒体播放器中保留了经典的 Winamp 界面风格。

# INSTALL

```apt: sudo apt install qmmp```

```dnf: sudo dnf install qmmp```

```pacman: sudo pacman -S qmmp```

```zypper: sudo zypper install qmmp```

```brew: brew install qmmp```

```nix: nix profile install nixpkgs#qmmp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[audacious](/man/audacious)(1), [mpv](/man/mpv)(1), [vlc](/man/vlc)(1), [cmus](/man/cmus)(1)
