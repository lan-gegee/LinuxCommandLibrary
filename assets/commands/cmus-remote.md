# TAGLINE

cmus 音乐播放器的远程控制接口

# TLDR

**切换播放/暂停**

```cmus-remote -u```

**播放**

```cmus-remote -p```

**暂停**

```cmus-remote -U```

**停止播放**

```cmus-remote -s```

**下一曲**

```cmus-remote -n```

**上一曲**

```cmus-remote -r```

**向前快进** 10 秒

```cmus-remote -k +10```

**设置音量**

```cmus-remote -v [50]%```

**将文件加入队列**

```cmus-remote -q [file.mp3]```

# SYNOPSIS

**cmus-remote** [_options_] [_file_|_dir_|_playlist_]

# DESCRIPTION

**cmus-remote** 是 cmus（一款基于 ncurses 的音乐播放器）的远程控制接口。它通过套接字连接向正在运行的 cmus 实例发送命令。

该工具允许从脚本或其他应用程序控制播放、管理播放列表以及查询播放器状态。它常用于媒体键绑定和状态栏集成。

# PARAMETERS

**-p**, **--play**
> 开始播放。

**-u**, **--pause**
> 切换暂停状态。

**-U**, **--pause-playback**
> 暂停但不切换。

**-s**, **--stop**
> 停止播放。

**-n**, **--next**
> 播放下一曲。

**-r**, **--prev**
> 播放上一曲。

**-k** _seconds_
> 相对定位（+/-秒数）。

**-v** _volume_
> 设置音量（绝对值或 +/-）。

**-q** _file_
> 将文件加入队列。

**-c** _file_
> 将文件添加到曲库。

**-l** _file_
> 加载播放列表。

**-S** _name_
> 切换设置项。

**-Q**
> 查询并打印状态。

**-C** _command_
> 发送原始 cmus 命令。

# CAVEATS

需要正在运行的 cmus 实例。套接字权限必须允许连接。如果 cmus 未在播放，某些命令可能无效。

# HISTORY

**cmus-remote** 是 **cmus** 项目的一部分，该项目由 **Timo Hirvonen** 于 **2005 年**创建。它为这款基于终端的音乐播放器提供了可脚本化的控制能力，使其能够与窗口管理器、状态栏和多媒体键盘集成。

# INSTALL

```apt: sudo apt install cmus```

```pacman: sudo pacman -S cmus```

```apk: sudo apk add cmus```

```zypper: sudo zypper install cmus```

```brew: brew install cmus```

```nix: nix profile install nixpkgs#cmus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmus](/man/cmus)(1), [mpd](/man/mpd)(1), [mpc](/man/mpc)(1), [playerctl](/man/playerctl)(1)

# RESOURCES

```[Source code](https://github.com/cmus/cmus)```

<!-- verified: 2026-06-22 -->
