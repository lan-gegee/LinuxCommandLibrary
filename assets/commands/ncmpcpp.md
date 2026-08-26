# TAGLINE

基于 ncurses 的 MPD 客户端

# TLDR

**启动 ncmpcpp**

```ncmpcpp```

**连接到指定主机**

```ncmpcpp -h [localhost] -p [6600]```

**以指定界面启动**

```ncmpcpp -s [playlist]```

**显示当前歌曲**

```ncmpcpp --current-song```

# SYNOPSIS

**ncmpcpp** [_options_]

# DESCRIPTION

**ncmpcpp** 是一款基于 ncurses 的 MPD（Music Player Daemon，音乐播放守护进程）客户端。它提供功能丰富的界面，可用于控制 MPD、浏览音乐、管理播放列表以及可视化音频。

该工具提供类似 vim 的按键绑定、频谱可视化器以及大量自定义选项。

# PARAMETERS

**-h** _host_
> MPD 服务器主机。

**-p** _port_
> MPD 服务器端口。

**-c** _file_
> 配置文件。

**-b** _file_, **--bindings** _file_
> 使用指定的按键绑定文件。

**-s** _screen_, **--screen** _screen_
> 启动时显示的界面（playlist、browser、search_engine、media_library、playlist_editor、tag_editor、outputs、visualizer、clock）。

**-S** _screen_, **--slave-screen** _screen_
> 启动时的辅助（slave）界面。

**--current-song**
> 显示当前歌曲信息后退出。

**-q**, **--quiet**
> 抑制消息输出。

**-v**, **--version**
> 显示版本信息。

# KEY BINDINGS

**1-8**: Switch screens
**Enter**: Play/select
**p**: Pause
**s**: Stop
**>/<**: Next/Previous
**f/b**: Seek forward/back
**+/-**: Volume
**/**: Search
**u**: Update database

# SCREENS

Playlist, Browser, Search, Media library, Lyrics, Visualizer, Clock

# CAVEATS

需要正在运行的 MPD 实例。配置可能比较复杂。部分功能需要额外设置。可视化器需要 FIFO 输出。

# HISTORY

**ncmpcpp** 全称为 "NCurses Music Player Client (Plus Plus)"，作为 ncmpc 的增强版而开发。它由 **Andrzej Rybczak** 用 C++ 编写，增加了歌词抓取和音频可视化等功能。

# INSTALL

```apt: sudo apt install ncmpcpp```

```dnf: sudo dnf install ncmpcpp```

```pacman: sudo pacman -S ncmpcpp```

```apk: sudo apk add ncmpcpp```

```zypper: sudo zypper install ncmpcpp```

```brew: brew install ncmpcpp```

```nix: nix profile install nixpkgs#ncmpcpp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpd](/man/mpd)(1), [mpc](/man/mpc)(1), [ncmpc](/man/ncmpc)(1), [cmus](/man/cmus)(1)
