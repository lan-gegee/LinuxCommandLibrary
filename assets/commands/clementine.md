# TAGLINE

跨平台音乐播放器与音乐库管理器

# TLDR

**启动 Clementine** 音乐播放器

```clementine```

**播放/暂停**当前曲目

```clementine -t```

**跳到下一首**曲目

```clementine -f```

**跳到上一首**曲目

```clementine -r```

**停止**播放

```clementine -s```

**将文件或 URL 添加**到播放列表

```clementine -a [path/to/music.mp3]```

**立即加载并播放**文件或 URL

```clementine -l [path/to/music.mp3]```

在当前曲目中**定位到指定位置**（秒）

```clementine --seek-to [120]```

# SYNOPSIS

**clementine** [_options_] [_URL_...]

# PARAMETERS

**-t**, **--play-pause**
> 切换播放/暂停状态。

**-f**, **--next**
> 跳到播放列表中的下一首曲目。

**-r**, **--previous**
> 跳到上一首曲目。

**-s**, **--stop**
> 停止播放。

**-a**, **--append**
> 将文件或 URL 追加到当前播放列表。

**-l**, **--load**
> 加载文件或 URL，替换当前播放列表并开始播放。

**-k**, **--play-track** _N_
> 播放播放列表中的第 N 首曲目。

**--seek-to** _SECONDS_
> 定位到以秒计的绝对位置。

**--seek-by** _SECONDS_
> 以秒为单位相对跳转。

**-v**, **--volume** _N_
> 设置音量级别（0-100）。

**--volume-up**
> 将音量提高 4%。

**--volume-down**
> 将音量降低 4%。

**-q**, **--quiet**
> 等同于 --volume 0。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Clementine** 是一款受 Amarok 1.4 启发的跨平台音乐播放器与音乐库管理器。它拥有简洁的界面、智能播放列表、网络电台支持，并与 Google Drive、Dropbox 和 OneDrive 等云存储服务集成。

命令行界面可以远程控制正在运行的 Clementine 实例，使其可以通过脚本实现自动化，或与媒体键和桌面快捷方式集成。在命令行上传入的文件和 URL 可以追加到播放列表，也可以立即播放。

Clementine 通过 GStreamer 支持多种音频格式，包括 MP3、FLAC、OGG 和 AAC。它可以转码音频、获取歌词和专辑封面、标记文件，并通过高级搜索和过滤功能管理大型音乐库。

# CAVEATS

远程控制命令要求 Clementine 实例已经在运行，且在 Linux 上支持 D-Bus，或在 macOS/Windows 上支持其他 IPC 机制。部分网络电台服务需要身份验证，或存在地区限制。

# HISTORY

Clementine 创建于 **2010 年**，是 Amarok 1.4 的一个分支，在 Amarok 迁移到 KDE4 时保留了其基于 Qt4 的界面。它的名字取自游戏《Portal》中的水果，凭借简洁性和跨平台支持迅速流行。该项目在 **2018 年**催生了作为现代化延续的 Strawberry。

# INSTALL

```apt: sudo apt install clementine```

```dnf: sudo dnf install clementine```

```zypper: sudo zypper install clementine```

```nix: nix profile install nixpkgs#clementine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpc](/man/mpc)(1), [mpv](/man/mpv)(1), [cmus](/man/cmus)(1), [vlc](/man/vlc)(1)

# RESOURCES

```[Source code](https://github.com/clementine-player/Clementine)```

```[Homepage](https://www.clementine-player.org/)```

<!-- verified: 2026-06-22 -->
