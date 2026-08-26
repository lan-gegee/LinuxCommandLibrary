# TAGLINE

命令行 BitTorrent 下载器

# TLDR

**下载种子**

```transmission-cli [path/to/file.torrent]```

**下载磁力链接**

```transmission-cli "[magnet:?xt=urn:btih:...]"```

**下载到指定目录**

```transmission-cli -w [path/to/download/dir] [file.torrent]```

**限速下载** (KB/s)

```transmission-cli -d [500] -u [100] [file.torrent]```

**完成后立即退出**（不做种）

```transmission-cli -m [file.torrent]```

**启用对等节点黑名单下载**

```transmission-cli -b [file.torrent]```

**以静默模式运行**

```transmission-cli -q [file.torrent]```

# SYNOPSIS

**transmission-cli** [**-b**] [**-d** _limit_] [**-u** _limit_] [**-g** _dir_] [**-m**] [**-w** _dir_] [**-q**] _torrent-file_|_magnet-uri_

# PARAMETERS

**-b**, **--blocklist**
> 启用对等节点黑名单。Transmission 支持 bluetack 黑名单格式。

**-d** _limit_
> 设置最大下载速度，单位 KB/s。0 表示不限制。

**-u** _limit_
> 设置最大上传速度，单位 KB/s。0 表示不限制。

**-f** _script_
> 种子下载完成时运行指定脚本。

**-g**, **--config-dir** _dir_
> 配置文件所在目录。可在不同 Transmission 客户端之间共享配置。

**-m**
> 下载完成后不做种；立即退出。

**-p**, **--port** _port_
> 设置监听传入对等节点的端口。默认：51413。

**-w** _dir_
> 保存下载文件的目录。默认为当前目录。

**-q**
> 静默模式。屏蔽大部分输出，仅显示关键消息。

**-h**, **--help**
> 显示帮助信息并退出。

**-v**, **--version**
> 显示版本号并退出。

# DESCRIPTION

**transmission-cli** 是一个轻量级的命令行 BitTorrent 客户端，用于下载和上传种子。它同时支持 .torrent 文件和磁力 URI，适用于服务器、无头系统以及脚本化的种子操作。

每次调用只处理一个种子：下载内容并可选择在完成后做种。进度会显示在终端中，包括下载/上传速度、对等节点连接数和完成百分比。

配置默认存储在 ~/.config/transmission 中，下载中断后可据此恢复。该客户端会遵循 TRANSMISSION_HOME 环境变量指定的自定义配置位置，并遵循 http_proxy 进行 tracker 通告。

向正在运行的 transmission-cli 进程发送 SIGHUP 可联系 tracker 以获取更多对等节点。

# CAVEATS

transmission-cli 一次只能处理一个种子，且并非为持续运行而设计。若要管理多个种子或将其作为服务运行，请改用 **transmission-daemon** 配合 **transmission-remote**。客户端必须在整个下载期间保持运行；关闭它会中断传输。

# HISTORY

**Transmission** 由 **Eric Petit** 和 **Josh Elsasser** 于 **2005 年**为 macOS 创建，随后不久加入了对 Linux 的支持。命令行界面的加入使其具备无头运行能力。Transmission 以轻量设计和跨平台支持著称，成为许多 Linux 发行版的默认 BitTorrent 客户端之一。

# INSTALL

```apt: sudo apt install transmission-cli```

```dnf: sudo dnf install transmission-cli```

```pacman: sudo pacman -S transmission-cli```

```apk: sudo apk add transmission-cli```

```brew: brew install transmission-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-daemon](/man/transmission-daemon)(1), [transmission-remote](/man/transmission-remote)(1)
