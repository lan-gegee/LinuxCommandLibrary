# TAGLINE

基于 curses 的 MPD 客户端

# TLDR

**启动 ncmpc**

```ncmpc```

**连接到指定主机**

```ncmpc -h [hostname]```

**连接到指定端口**

```ncmpc -p [6600]```

**使用密码连接**

```ncmpc --password=[password]```

# SYNOPSIS

**ncmpc** [_options_]

# PARAMETERS

**-h**, **--host** _host_
> MPD 服务器主机。

**-p**, **--port** _port_
> MPD 服务器端口。

**--password** _pass_
> MPD 密码。

**-c**, **--colors**
> 启用颜色。

**-C**, **--no-colors**
> 禁用颜色。

# DESCRIPTION

**ncmpc** 是一款基于 curses 的 MPD（Music Player Daemon，音乐播放守护进程）客户端。它提供文字界面，用于浏览音乐、管理播放列表和控制播放。

ncmpc 轻量且完全由键盘驱动，是在终端中控制音乐的理想选择。

# KEY BINDINGS

```
Space/p  - Play/pause
s        - Stop
>/<      - Next/previous
+/-      - Volume up/down
1-5      - Switch screens
q        - Quit
```

# SCREENS

```
1 - Playlist
2 - Browse
3 - Search
4 - Library
5 - Outputs
```

# CAVEATS

需要正在运行的 MPD 服务器。可通过 ~/.ncmpc/config 配置默认值。仅限于 MPD 提供的功能。

# HISTORY

ncmpc 由 **Kalle Wallin** 创建，是最早的 MPD curses 客户端之一，提供了类似 vim 的音乐控制界面。

# INSTALL

```apt: sudo apt install ncmpc```

```dnf: sudo dnf install ncmpc```

```pacman: sudo pacman -S ncmpc```

```apk: sudo apk add ncmpc```

```brew: brew install ncmpc```

```nix: nix profile install nixpkgs#ncmpc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpd](/man/mpd)(1), [mpc](/man/mpc)(1), [ncmpcpp](/man/ncmpcpp)(1)
