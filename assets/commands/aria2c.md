# TAGLINE

多协议多来源下载工具

# TLDR

**下载**单个文件

```aria2c [URL]```

以 **16 个连接**下载

```aria2c -x 16 -s 16 [URL]```

下载到**指定目录**

```aria2c -d [/path/to/dir] [URL]```

**继续**中断的下载

```aria2c -c [URL]```

从**磁力链接**下载

```aria2c "[magnet:?xt=urn:btih:...]"```

**启用 RPC** 后运行下载

```aria2c --enable-rpc --rpc-listen-all```

# SYNOPSIS

**aria2c** [_options_] [_URL_|_TORRENT_|_METALINK_]

# DESCRIPTION

**aria2c** 是 aria2 的命令行接口。aria2 是一个多协议下载工具，支持并行下载、分段下载和多个来源 URL，以最大化下载速度。

它支持 HTTP/HTTPS、FTP、SFTP、BitTorrent 和 Metalink，并提供丰富的配置选项。

# PARAMETERS

**-x** _n_
> 每个服务器的最大连接数（默认：1）

**-s** _n_
> 将文件分为 n 个片段

**-c**
> 继续/恢复下载

**-d** _dir_
> 下载目录

**-o** _file_
> 输出文件名

**--file-allocation** _method_
> none、prealloc、trunc、falloc

**--max-overall-download-limit** _speed_
> 总体速度限制

**--enable-rpc**
> 启用 RPC 接口

**--bt-enable-lpd**
> 启用本地节点发现（Local Peer Discovery）

**--dht-listen-port** _port_
> BitTorrent 的 DHT 端口

**-j** _n_
> 最大并行下载数（默认：5）

**--seed-time** _minutes_
> BitTorrent 做种时间，单位分钟（0 = 不做种）

**-i** _file_, **--input-file** _file_
> 从文件读取 URL

**-q**, **--quiet**
> 安静模式

# CONFIGURATION

**~/.aria2/aria2.conf**
> 默认配置文件，用于设置下载选项、连接限制和协议相关设置。

# CAVEATS

aria2c 就是 aria2；"c" 代表命令行。无论客户端如何设置，服务器都可能限制连接数。BitTorrent 功能需要正确的网络配置。

# HISTORY

**aria2** 由 **Tatsuhiro Tsujikawa** 开发，约于 **2006** 年首次发布。它用 C++ 编写，支持 HTTP/HTTPS、FTP、SFTP、BitTorrent 和 Metalink。

# INSTALL

```apt: sudo apt install aria2```

```dnf: sudo dnf install aria2```

```pacman: sudo pacman -S aria2```

```apk: sudo apk add aria2```

```zypper: sudo zypper install aria2```

```brew: brew install aria2```

```nix: nix profile install nixpkgs#aria2```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aria2](/man/aria2)(1), [wget](/man/wget)(1), [curl](/man/curl)(1)
