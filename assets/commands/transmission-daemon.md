# TAGLINE

无头 BitTorrent 客户端守护进程

# TLDR

**启动守护进程**

```transmission-daemon```

**以认证方式启动**

```transmission-daemon --auth --username [user] --password [pass]```

**指定 Web 界面端口启动**

```transmission-daemon --port [9091]```

**指定下载目录**

```transmission-daemon --download-dir [/path/to/downloads]```

**允许特定 IP 地址**

```transmission-daemon --allowed "[127.0.0.1,192.168.*.*]"```

**监视目录中的种子文件**

```transmission-daemon --watch-dir [/path/to/watch]```

**以前台方式运行**

```transmission-daemon -f```

**要求加密**

```transmission-daemon --encryption-required```

# SYNOPSIS

**transmission-daemon** [_options_]

# PARAMETERS

**-g**, **--config-dir** _dir_
> 配置目录的位置。

**-a**, **--allowed** _list_
> 允许访问的 IP 白名单，以逗号分隔（支持通配符）。

**-b**, **--blocklist**
> 启用对等节点黑名单。

**-t**, **--auth**
> 要求身份认证。

**-u**, **--username** _name_
> 认证用户名。

**-v**, **--password** _pass_
> 认证密码。

**-p**, **--port** _port_
> RPC/Web 界面端口（默认：9091）。

**-w**, **--download-dir** _dir_
> 默认下载目录。

**--incomplete-dir** _dir_
> 存放未完成下载的目录。

**--watch-dir** _dir_
> 监视新 .torrent 文件的目录。

**-er**, **--encryption-required**
> 要求加密连接。

**-ep**, **--encryption-preferred**
> 优先使用加密连接。

**-f**, **--foreground**
> 以前台方式运行。

**--dump-settings**
> 将当前设置转储到标准错误。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**transmission-daemon** 是一个以后台守护进程形式运行的无头 BitTorrent 客户端。它提供完整的 BitTorrent 功能，通过 RPC 接口进行控制，可经由 Web 界面或 transmission-remote 命令访问。

该守护进程支持磁力链接、DHT、节点交换、加密和带宽调度。配置存储在配置目录的 settings.json 中。

Web 界面（默认：http://localhost:9091）提供了图形化的种子管理方式。若要通过命令行控制，可使用 transmission-remote 来添加、删除和管理种子。

手动编辑 settings.json 前必须先停止守护进程，否则更改会在退出时被覆盖。

# CONFIGURATION

**~/.config/transmission-daemon/settings.json**
> JSON 格式的主配置文件，包含所有守护进程设置：下载路径、速度限制、对等节点选项以及 RPC 认证等。

**-g**, **--config-dir** _dir_
> 覆盖默认配置目录的位置。

**TRANSMISSION_HOME**
> 用于覆盖默认配置目录路径的环境变量。

# CAVEATS

守护进程退出时会覆盖设置文件。生产环境中 Web 界面必须启用认证。默认端口 9091 应通过防火墙阻止公开访问。黑名单更新需要重启守护进程。

# HISTORY

**Transmission** 创建于 2005 年，是最古老且仍在积极维护的 BitTorrent 客户端之一。守护进程模式使其能够在服务器和 NAS 设备上无头运行。它以轻量的资源占用和跨平台支持而闻名。

# INSTALL

```apt: sudo apt install transmission-daemon```

```dnf: sudo dnf install transmission-daemon```

```apk: sudo apk add transmission-daemon```

```zypper: sudo zypper install transmission-daemon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-remote](/man/transmission-remote)(1), [transmission-cli](/man/transmission-cli)(1), [rtorrent](/man/rtorrent)(1)
