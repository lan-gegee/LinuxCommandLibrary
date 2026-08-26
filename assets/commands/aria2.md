# TAGLINE

多协议多来源下载工具

# TLDR

**下载**文件

```aria2c [https://example.com/file.zip]```

以**多个连接**下载

```aria2c -x 16 -s 16 [https://example.com/file.zip]```

从**多个镜像源**下载

```aria2c [http://mirror1.com/file] [http://mirror2.com/file]```

**续传**中断的下载

```aria2c -c [https://example.com/file.zip]```

下载 **torrent** 文件

```aria2c [file.torrent]```

从**磁力链接**下载

```aria2c "[magnet:?xt=urn:btih:...]"```

从**文件读取 URL** 下载（每行一个 URL）

```aria2c -i [urls.txt]```

**限制下载速度**

```aria2c --max-download-limit=[500K] [https://example.com/file.zip]```

# SYNOPSIS

**aria2c** [_options_] _URL_|_TORRENT_|_METALINK_ ...

# DESCRIPTION

**aria2** 是一个轻量级的多协议下载工具，支持 HTTP/HTTPS、FTP、SFTP、BitTorrent 和 Metalink。它可以同时使用多个连接和多个来源下载文件，以获得更快的速度。

实际命令是 **aria2c**（"c" 表示命令行）。该工具经过高度优化，内存占用极小（通常 4-9 MiB），同时支持分段下载、BitTorrent 和 JSON-RPC 远程控制等高级特性。

# PARAMETERS

**-x** _n_, **--max-connection-per-server** _n_
> 每个服务器的最大连接数（默认：1，最大：16）

**-s** _n_, **--split** _n_
> 将下载分为 n 个部分（默认：5）

**-c**, **--continue**
> 续传未完成的文件

**-d** _dir_, **--dir** _dir_
> 下载目录

**-o** _file_, **--out** _file_
> 输出文件名

**-j** _n_, **--max-concurrent-downloads** _n_
> 最大并行下载数（默认：5）

**-i** _file_, **--input-file** _file_
> 下载文件中列出的 URL

**--max-download-limit** _speed_
> 单个下载的速度限制（如 500K、2M）

**--max-overall-download-limit** _speed_
> 总体下载速度限制

**--enable-rpc**
> 启用 JSON-RPC/XML-RPC 服务器以便远程控制

**--seed-time** _minutes_
> BitTorrent 做种时间（0 表示不做种）

**--select-file** _indices_
> 从 torrent 中选择指定文件（索引以逗号分隔）

**--file-allocation** _method_
> 文件分配方法：none、prealloc、trunc 或 falloc

# CONFIGURATION

**~/.aria2/aria2.conf**
> 默认配置文件，用于设置下载选项、连接限制和协议相关设置。每行一个选项，不带开头的 --。

# CAVEATS

服务器可能限制或节流多连接。要获得最佳 BitTorrent 性能需要正确的端口转发。分段下载时 **-x** 与 **-s** 标志通常应配合使用。

# HISTORY

**aria2** 由 Tatsuhiro Tsujikawa 开发，约于 **2006** 年首次发布。它用 C++ 编写，凭借多连接下载能力成为 wget 和 curl 的流行替代品。

# INSTALL

```dnf: sudo dnf install aria2```

```pacman: sudo pacman -S aria2```

```zypper: sudo zypper install aria2```

```brew: brew install aria2```

```nix: nix profile install nixpkgs#aria2```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aria2c](/man/aria2c)(1), [curl](/man/curl)(1), [wget](/man/wget)(1), [transmission-cli](/man/transmission-cli)(1)
