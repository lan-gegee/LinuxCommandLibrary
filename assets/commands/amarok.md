# TAGLINE

功能丰富的 KDE 音乐播放器

# TLDR

**启动** Amarok

```amarok```

打开**指定文件**

```amarok [music.mp3]```

将文件**加入**当前播放列表

```amarok --enqueue [file1.mp3] [file2.mp3]```

**播放/暂停**当前曲目

```amarok --play-pause```

**跳到**下一曲

```amarok --next```

显示**上一**曲目

```amarok --previous```

# SYNOPSIS

**amarok** [_options_] [_files_|_urls_]

# DESCRIPTION

**amarok** 是一款面向 Linux/KDE 的强大音乐播放器，支持多种音频格式、播客管理以及与在线音乐服务的集成。它拥有完善的媒体库管理器、动态播放列表和丰富的插件支持。

该播放器可以扫描你的音乐库、获取专辑封面和歌词，并提供可脚本化的接口以便自动化操作。

# PARAMETERS

**--play**
> 开始播放

**--play-pause**
> 切换播放/暂停

**--pause**
> 暂停播放

**--stop**
> 停止播放

**--next**
> 跳到下一曲

**--previous**
> 回到上一曲

**--enqueue** _files_
> 将文件加入播放列表但不播放

**--append** _files_
> 将文件追加到播放列表

**--load** _files_
> 加载文件并替换播放列表

**-s**, **--stop-after-current**
> 播完当前曲目后停止

**--volume** _percent_
> 设置音量级别

**--engine** _engine_
> 使用指定的音频引擎

# CONFIGURATION

**~/.config/amarokrc**（KF5/Qt5 版本）、**~/.kde/share/config/amarokrc**（KDE4 版本）
> 主配置文件，存储播放器设置、媒体库路径和插件偏好。

# CAVEATS

与更简单的播放器相比较消耗系统资源。部分功能需要 KDE 框架。插件兼容性因版本而异。

# HISTORY

**Amarok** 于 **2003** 年首次发布，是一款 KDE 音乐播放器。2008 年的 2.0 版本带来了大规模重写。它曾是功能最丰富的 Linux 音乐播放器之一，不过近年开发节奏已放缓。

# INSTALL

```apt: sudo apt install amarok```

```dnf: sudo dnf install amarok```

```pacman: sudo pacman -S amarok```

```zypper: sudo zypper install amarok```

```nix: nix profile install nixpkgs#amarok```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[vlc](/man/vlc)(1), [clementine](/man/clementine)(1)
