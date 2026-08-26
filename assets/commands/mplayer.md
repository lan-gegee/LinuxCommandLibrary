# TAGLINE

功能强大的媒体播放器

# TLDR

**播放视频文件**

```mplayer [video.mp4]```

**播放音频文件**

```mplayer [audio.mp3]```

**全屏播放**

```mplayer -fs [video.mp4]```

**指定音频输出**

```mplayer -ao [alsa] [file]```

**循环播放**

```mplayer -loop [0] [file]```

**设置起始位置**

```mplayer -ss [00:01:30] [video.mp4]```

**导出音频流**

```mplayer -dumpaudio -dumpfile [out.mp3] [video.mp4]```

# SYNOPSIS

**mplayer** [_options_] _file_

# PARAMETERS

_FILE_
> 要播放的媒体文件。

**-fs**
> 全屏模式。

**-ao** _DRIVER_
> 音频输出驱动。

**-vo** _DRIVER_
> 视频输出驱动。

**-loop** _N_
> 循环次数（0=无限）。

**-ss** _TIME_
> 跳转到指定位置。

**-dumpaudio**
> 将原始音频流导出到文件。

**-dumpfile** _FILE_
> 导出的音频/视频流的文件名。

**-speed** _FACTOR_
> 播放速度倍率（0.01-100，默认：1.0）。

**-quiet**
> 抑制大多数状态消息。

**-identify**
> 打印媒体属性（便于脚本处理）。

# DESCRIPTION

**mplayer** 是一个功能强大的命令行媒体播放器，支持极其丰富的音视频格式。它使用 FFmpeg 的 libavcodec 和 libavformat 进行解码，部分格式也使用原生编解码器。

键盘快捷键控制播放：方向键跳转，**p** 暂停，**q** 退出，**f** 切换全屏，**+/-** 调整音频延迟。该播放器还可以通过 FIFO 管道或 slave 模式控制，便于脚本化操作。

# CAVEATS

MPlayer 已被视为遗留软件；**mpv** 是其积极维护的后继者，拥有现代化的代码库。某些发行版已不再打包 MPlayer。配置文件位于 **~/.mplayer/**。

# HISTORY

**MPlayer** 由 **Árpád Gereöffy** 于 **2000 年**发起。它曾是 Linux 上最受欢迎的开源媒体播放器之一，并影响了多个后继项目，包括 **mpv**（2013 年 fork）和 **MPlayer2**。

# INSTALL

```apt: sudo apt install mplayer```

```pacman: sudo pacman -S mplayer```

```apk: sudo apk add mplayer```

```brew: brew install mplayer```

```nix: nix profile install nixpkgs#mplayer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpv](/man/mpv)(1), [vlc](/man/vlc)(1), [ffplay](/man/ffplay)(1)
