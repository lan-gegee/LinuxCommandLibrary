# TAGLINE

来自 Nmap 项目的网络工具，用于读取、写入

# TLDR

在端口上**监听**并保存到文件

```ncat -l [port] > [path/to/file]```

**监听**多个连接（保持开启）

```ncat -lk [port]```

向远程主机**发送文件**

```ncat < [path/to/file] [address] [port]```

通过 **SSL** 接受连接

```ncat --ssl -lk [port]```

**连接**到 SSL 服务器

```ncat --ssl [host] [port]```

带超时的**连通性检查**

```ncat -w [seconds] -vz [host] [port]```

创建**聊天服务器**

```ncat -l [port] --chat```

# SYNOPSIS

**ncat** [**-l**] [**-k**] [**--ssl**] [**-w** _timeout_] [**-v**] [**-z**] [_host_] [_port_]

# PARAMETERS

**-l, --listen**
> 监听传入连接

**-k, --keep-open**
> 在监听模式下接受多个连接

**--ssl**
> 使用 SSL/TLS 加密

**--ssl-cert _file_**
> 指定 SSL 证书文件

**--ssl-key _file_**
> 指定 SSL 私钥文件

**-w, --wait _seconds_**
> 连接超时时间（秒）

**-v, --verbose**
> 启用详细输出

**-z**
> 零 I/O 模式；仅报告连接状态

**-p, --source-port _port_**
> 指定源端口

**-e, --exec _command_**
> 连接后执行命令

**--chat**
> 启用多用户聊天模式

**--proxy _host:port_**
> 通过代理连接

**--proxy-type _type_**
> 代理类型：http、socks4、socks5

**-4**
> 仅使用 IPv4

**-6**
> 仅使用 IPv6

# DESCRIPTION

**ncat** 是 Nmap 项目出品的网络工具，用于跨网络读取、写入、重定向和加密数据。它是 netcat 的重新实现，额外提供了 SSL 支持、代理连接和 IPv6 等特性。

Ncat 可以作为简单的 TCP/UDP 客户端或服务器、端口扫描器或网络中继运行。它支持连接代理（brokering）和访问控制，可用于文件传输、端口转发和网络调试。

# CAVEATS

--exec 选项可能带来危险，应谨慎使用。SSL 连接需要正确处理证书以确保安全。绑定特权端口等部分功能可能需要 root 权限。

# HISTORY

**ncat** 由 Fyodor 及贡献者作为 **Nmap** 项目的一部分开发。它被设计为传统 netcat 工具的现代替代品，具备更强的功能和更好的安全选项。

# INSTALL

```apt: sudo apt install ncat```

```dnf: sudo dnf install nmap-ncat```

```apk: sudo apk add nmap-ncat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nc](/man/nc)(1), [netcat](/man/netcat)(1), [nmap](/man/nmap)(1), [socat](/man/socat)(1)
