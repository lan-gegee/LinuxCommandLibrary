# TAGLINE

服务端音乐播放器

# TLDR

**启动 MPD**

```mpd```

**使用配置文件启动**

```mpd [~/.config/mpd/mpd.conf]```

**终止正在运行的 MPD**

```mpd --kill```

**在前台运行**

```mpd --no-daemon```

**显示版本**

```mpd --version```

**详细输出**

```mpd --verbose```

# SYNOPSIS

**mpd** [_options_] [_config_file_]

# PARAMETERS

_CONFIG_FILE_
> 配置文件的路径。

**--kill**
> 终止正在运行的 MPD 实例。

**--no-daemon**
> 在前台运行。

**--verbose**
> 启用详细输出。

**--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mpd**（Music Player Daemon）是一个服务端音乐播放器。它播放音频并管理播放列表。

该工具以守护进程方式运行，由 mpc 或 ncmpcpp 等客户端连接并控制播放。

# CAVEATS

仅提供服务端功能。需要客户端进行控制。音频输出需要进行配置。

# HISTORY

MPD 作为一个**灵活的音乐服务器**而创建，支持多种客户端界面和远程控制。

# INSTALL

```apt: sudo apt install mpd```

```dnf: sudo dnf install mpd```

```pacman: sudo pacman -S mpd```

```apk: sudo apk add mpd```

```zypper: sudo zypper install mpd```

```brew: brew install mpd```

```nix: nix profile install nixpkgs#mpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpc](/man/mpc)(1), [ncmpcpp](/man/ncmpcpp)(1), [pulseaudio](/man/pulseaudio)(1)
