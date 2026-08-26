# TAGLINE

轻量级 Spotify Connect 守护进程

# TLDR

以默认配置**启动 spotifyd**

```spotifyd```

**不以守护进程方式启动**（前台模式）

```spotifyd --no-daemon```

**使用指定配置文件启动**

```spotifyd --config-path [~/.config/spotifyd/spotifyd.conf]```

**以详细日志模式启动**

```spotifyd --verbose```

在 Spotify Connect 中**显示设备名称**

```spotifyd --device-name "[My Linux PC]"```

# SYNOPSIS

**spotifyd** [_options_]

# PARAMETERS

**--no-daemon**
> 在前台运行而非转为守护进程。

**-c**, **--config-path** _path_
> 配置文件的路径。

**--verbose**
> 启用详细日志输出。

**--device-name** _name_
> 在 Spotify Connect 设备列表中显示的名称。

**--device-type** _type_
> 设备类型（computer, tablet, smartphone, speaker, tv, avr, stb, audiodongle）。

**--bitrate** _rate_
> 音频比特率：96、160 或 320 kbps。

**--backend** _backend_
> 音频后端：pulseaudio, alsa, rodio, portaudio。

**--device** _device_
> 用于播放的音频设备名称。

**--mixer** _mixer_
> 用于音量控制的混音器。

**--initial-volume** _percent_
> 初始音量（0-100）。

**--volume-normalisation**
> 启用音量均衡。

**--cache-path** _path_
> 缓存目录路径。

**--username** _username_
> Spotify 用户名。

**--password** _password_
> Spotify 密码（出于安全考虑建议使用配置文件）。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**spotifyd** 是实现了 Spotify Connect 协议的轻量级 Spotify 守护进程。它作为后台服务运行在 Linux、macOS 及其他类 Unix 系统上，在 Spotify 生态中表现为一台可控设备。

与完整的 Spotify 桌面客户端不同，spotifyd 没有图形界面，资源占用极小。它可以通过任何 Spotify 客户端（移动应用、网页播放器或桌面应用）借助 Spotify Connect 进行控制。本地控制方面，它与 **spotify-tui**（spt）等终端界面搭配良好。

通常通过 **~/.config/spotifyd/spotifyd.conf** 文件进行配置，其中包含凭据和播放设置。串流需要 Spotify Premium 账户。

# CONFIGURATION

**~/.config/spotifyd/spotifyd.conf**
> 主配置文件，定义 Spotify 凭据、音频后端、设备名称、比特率、音量设置和缓存位置。

**/etc/spotifyd.conf**
> 将 spotifyd 作为系统服务运行时使用的系统级配置。

# CAVEATS

播放需要 Spotify Premium。由于 Spotify API 变更，较新版本的身份验证可能需要进行 OAuth 设置。守护进程必须正在运行，Spotify Connect 才能看到该设备。音频后端的可用性取决于系统配置和编译期选项。将凭据存储在配置文件中存在安全隐患。

# HISTORY

**spotifyd** 作为官方 Spotify 客户端的开源替代品而创建，面向希望获得轻量、无头 Spotify 播放的用户。它基于 **librespot**——一个逆向工程得到的 Spotify 客户端库。该项目因可在服务器、树莓派以及不适合运行完整客户端的系统上运行 Spotify 而广受欢迎。开发仍在继续，依靠社区贡献推进。

# INSTALL

```pacman: sudo pacman -S spotifyd```

```apk: sudo apk add spotifyd```

```zypper: sudo zypper install spotifyd```

```brew: brew install spotifyd```

```nix: nix profile install nixpkgs#spotifyd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ncspot](/man/ncspot)(1)
