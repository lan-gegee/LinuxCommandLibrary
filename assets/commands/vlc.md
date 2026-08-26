# TAGLINE

跨平台多媒体播放器和流媒体工具

# TLDR

**播放媒体文件**

```vlc [file]```

**播放多个文件**

```vlc [file1] [file2] [file3]```

**播放 URL/流**

```vlc [https://example.com/stream.m3u8]```

**全屏播放**

```vlc --fullscreen [file]```

**不用 GUI 播放**（命令行）

```cvlc [file]```

**循环播放**

```vlc --loop [file]```

**以指定音量播放**（0-1024，256 = 100%）

```vlc --volume=[200] [file]```

**通过 HTTP 推流**

```vlc [file] --sout '#standard{access=http,mux=ts,dst=:8080}'```

# SYNOPSIS

**vlc** [_options_] [_file_|_url_...]

# PARAMETERS

**--fullscreen**, **-f**
> 以全屏模式启动

**--loop**, **-L**
> 循环播放列表

**--repeat**, **-R**
> 重复当前项目

**--random**, **-Z**
> 随机播放

**--volume** _N_
> 设置音量（0-1024，256 = 100%）

**--play-and-exit**
> 播放完毕后退出

**--start-time** _N_
> 从第 N 秒开始

**--stop-time** _N_
> 在第 N 秒停止

**--rate** _N_
> 播放速度（1.0 = 正常）

**--no-video**
> 仅音频

**--no-audio**
> 仅视频

**--sout** _chain_
> 流输出链

**--intf** _interface_
> 界面模块（qt、ncurses、dummy）

**-I dummy**, **--intf=dummy**
> 无界面（后台运行）

# VARIANTS

**vlc**：完整 GUI 版本
**cvlc**：仅命令行（无 GUI）
**nvlc**：NCurses 文本界面
**rvlc**：远程控制界面
**svlc**：可换肤界面

# DESCRIPTION

**VLC** 是一款免费开源的多媒体播放器，无需外部编解码器即可支持几乎所有音频和视频格式。它可以播放本地文件、光盘、网络流和采集设备。

除了播放之外，VLC 还具备强大的串流和转码能力。它可以充当流媒体服务器、在不同格式之间转换，并应用各种滤镜和效果。

命令行界面提供了对 VLC 全部功能的访问，适合脚本化和自动化。使用 **cvlc** 可在不启动 GUI 的情况下无头运行。

VLC 的媒体库和播放列表功能有助于整理大量收藏，其网络串流支持 HTTP、RTSP 和 HLS 等协议。

# CAVEATS

**--sout** 的串流语法较为复杂。构建流输出链时请查阅 VLC 文档。

硬件加速选项因平台而异。使用 **--avcodec-hw** 可控制硬件解码。

由于授权原因，某些专有格式可能存在播放问题。VLC 使用的开源实现可能与商业解码器不完全一致。

# HISTORY

VLC 于 **1996 年**作为**巴黎中央理工学院**的学生项目诞生，当时名为 VideoLAN Client。它于 **2001 年**开源，随后发展为最受欢迎的媒体播放器之一，以“无需编解码器包也能播放任何内容”而闻名。

# INSTALL

```apt: sudo apt install vlc-bin```

```dnf: sudo dnf install vlc```

```pacman: sudo pacman -S vlc```

```apk: sudo apk add vlc```

```zypper: sudo zypper install vlc```

```nix: nix profile install nixpkgs#vlc-bin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpv](/man/mpv)(1), [ffmpeg](/man/ffmpeg)(1), [mplayer](/man/mplayer)(1), [ffplay](/man/ffplay)(1)
