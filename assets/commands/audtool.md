# TAGLINE

控制 Audacious 媒体播放器的命令行界面。

# TLDR

**获取**当前曲目

```audtool current-song```

**播放/暂停**播放

```audtool playback-playpause```

**跳转**到下一曲

```audtool playlist-advance```

获取**播放状态**

```audtool playback-status```

设置**音量**

```audtool set-volume [75]```

# SYNOPSIS

**audtool** [_instance_] _command_ [_parameter_ ...] ...

命令可以选择加上 **--** 前缀（GNU 长选项风格）；**current-song** 和 **--current-song** 均可使用。

# DESCRIPTION

**audtool** 是控制 Audacious 媒体播放器的命令行界面。它可以在不打开 GUI 的情况下进行远程控制、播放列表管理和状态查询。

该工具适用于脚本、快捷键绑定和自动化场景。

# PARAMETERS

**playback-play**
> 开始播放

**playback-pause**
> 暂停播放

**playback-playpause**
> 切换播放/暂停

**playback-stop**
> 停止播放

**playback-status**
> 显示播放状态

**playlist-advance**
> 下一曲

**playlist-reverse**
> 上一曲

**current-song**
> 打印当前曲目信息

**current-song-filename**
> 打印当前曲目的文件名

**current-song-length**
> 以 M:SS 格式打印当前曲目长度

**set-volume** _n_
> 设置音量（0-100）

**get-volume**
> 获取当前音量

**playlist-length**
> 播放列表中的曲目数量

**playlist-song** _n_
> 获取位于第 n 位的曲目

# CAVEATS

需要 Audacious 正在运行。播放器未启动时命令会失败。部分功能取决于 Audacious 的版本。

# HISTORY

**audtool** 与 Audacious 一同开发，提供可脚本化的控制能力，延续了 beep-media-player-control 和 xmmsctrl 的传统。

# INSTALL

```apt: sudo apt install audacious```

```dnf: sudo dnf install audacious```

```pacman: sudo pacman -S audacious```

```apk: sudo apk add audacious```

```zypper: sudo zypper install audacious```

```brew: brew install audacious```

```nix: nix profile install nixpkgs#audacious```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[audacious](/man/audacious)(1), [playerctl](/man/playerctl)(1)

# RESOURCES

```[Source code](https://github.com/audacious-media-player/audacious)```

```[Homepage](https://audacious-media-player.org/)```

<!-- verified: 2026-06-17 -->
