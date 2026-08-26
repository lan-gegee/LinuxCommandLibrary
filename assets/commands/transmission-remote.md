# TAGLINE

远程控制 Transmission 守护进程

# TLDR

**列出所有种子**

```transmission-remote -l```

**添加种子**

```transmission-remote -a [path/to/file.torrent]```

**添加磁力链接**

```transmission-remote -a "[magnet:?xt=urn:btih:...]"```

**按 ID 启动特定种子**

```transmission-remote -t [id] -s```

**暂停种子**

```transmission-remote -t [id] -S```

**移除种子**（保留已下载的文件）

```transmission-remote -t [id] -r```

**移除种子并删除文件**

```transmission-remote -t [id] -rad```

**以认证方式连接远程守护进程**

```transmission-remote [host:port] --auth [user:password] -l```

# SYNOPSIS

**transmission-remote** [_host:port_] [**--auth** _user:pass_] [**-t** _id_] [_options_]

# PARAMETERS

**-l**, **--list**
> 列出所有种子的状态、进度和速度。

**-a** _file_, **--add** _file_
> 添加种子文件或磁力 URI。

**-t** _id_
> 按 ID 选择一个或多个种子。可以是单个 ID、范围 (1-5)、逗号列表 (1,3,5) 或 'all'。

**-s**, **--start**
> 启动选定的种子。

**-S**, **--stop**
> 停止（暂停）选定的种子。

**-r**, **--remove**
> 移除选定的种子，但保留已下载的文件。

**-rad**, **--remove-and-delete**
> 移除选定的种子并删除已下载的文件。

**-d** _limit_, **--downlimit** _limit_
> 设置全局下载速度限制，单位 KB/s。

**-u** _limit_, **--uplimit** _limit_
> 设置全局上传速度限制，单位 KB/s。

**--auth** _user:pass_
> 提供守护进程的认证凭据。

**--port** _port_
> 连接到指定的 RPC 端口（默认：9091）。

**--ssl**
> RPC 连接使用 SSL/TLS。

**-i**, **--info**
> 显示选定种子的详细信息。

**-if**, **--info-files**
> 列出选定种子中的文件。

**-ip**, **--info-peers**
> 列出选定种子已连接的对等节点。

# DESCRIPTION

**transmission-remote** 是一个用于远程控制 Transmission BitTorrent 守护进程的命令行工具。它连接到 transmission-daemon（默认：localhost:9091），用于管理种子、配置设置以及监控传输状态。

该工具提供对守护进程的完全控制：添加和移除种子、启动和停止传输、设置速度限制、查看种子详细信息，以及管理种子内的单个文件。可以通过 **-t** 选项配合 ID、范围或 'all' 来选择多个种子。

认证可通过 **--auth** 选项、TR_AUTH 环境变量或 .netrc 文件提供。对于远程守护进程，将主机和端口作为第一个参数传入即可。

# CAVEATS

需要 transmission-daemon 正在运行。默认连接 localhost:9091；远程连接可能需要配置防火墙。命令行参数中的认证凭据可能通过进程列表被其他用户看到；在敏感环境中建议改用环境变量或 .netrc。

# HISTORY

**transmission-remote** 是始于 **2005 年**的 **Transmission** 项目的一部分。开发这一远程控制工具是为了支持无头运行，让系统管理员能够在没有图形界面的服务器上管理种子下载。如今它已成为脚本和服务器环境中自动化种子管理的标准工具。

# INSTALL

```apt: sudo apt install transmission-cli```

```dnf: sudo dnf install transmission-cli```

```pacman: sudo pacman -S transmission-cli```

```apk: sudo apk add transmission-remote```

```brew: brew install transmission-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-daemon](/man/transmission-daemon)(1), [transmission-cli](/man/transmission-cli)(1), [transmission-create](/man/transmission-create)(1), [transmission-show](/man/transmission-show)(1)
