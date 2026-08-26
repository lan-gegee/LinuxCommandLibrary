# TAGLINE

基于 MPlayer 和 mplayer2 的现代媒体播放器

# TLDR

**播放视频文件**

```mpv [video.mp4]```

**播放音频文件**

```mpv [audio.mp3]```

**全屏播放**

```mpv --fullscreen [video.mp4]```

**从 URL 播放**

```mpv "[https://example.com/video.mp4]"```

**循环播放**

```mpv --loop [video.mp4]```

**设置起始时间**

```mpv --start=[00:01:30] [video.mp4]```

**不显示视频播放**

```mpv --no-video [file.mp4]```

**指定音频设备**

```mpv --audio-device=[pulse] [file]```

# SYNOPSIS

**mpv** [_options_] _file_|_url_

# PARAMETERS

_FILE_
> 要播放的媒体文件或 URL。

**--fullscreen**
> 以全屏启动。

**--loop**
> 无限循环播放。

**--start** _TIME_
> 从指定时间开始播放。

**--no-video**
> 纯音频模式。

**--volume** _LEVEL_
> 设置音量百分比。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mpv** 是一个基于 MPlayer 和 mplayer2 的现代媒体播放器。它用于播放视频和音频。

该工具支持多种格式，可通过 Lua 和 JavaScript 编写脚本，并且高度可配置。

# CAVEATS

以键盘操作为主。配置位于 ~/.config/mpv/。GPU 加速因平台而异。

# HISTORY

mpv 于 2012 年从 **MPlayer2** fork 而来，旨在提供一个更简洁、更现代且持续活跃开发的媒体播放器。

# INSTALL

```apt: sudo apt install mpv```

```dnf: sudo dnf install mpv```

```pacman: sudo pacman -S mpv```

```apk: sudo apk add mpv```

```zypper: sudo zypper install mpv```

```brew: brew install mpv```

```nix: nix profile install nixpkgs#mpv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mplayer](/man/mplayer)(1), [vlc](/man/vlc)(1), [ffplay](/man/ffplay)(1)
