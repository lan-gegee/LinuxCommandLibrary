# TAGLINE

OpenBSD 重写版 netcat，用于 TCP/UDP 连接和端口扫描

# TLDR

**在端口上监听传入连接**

```nc.openbsd -l [8080]```

**连接到主机和端口**

```nc.openbsd [host] [port]```

**扫描端口而不发送数据**

```nc.openbsd -zv [host] [20-30]```

**客户端断开后继续监听**

```nc.openbsd -k -l [port]```

**通过 SOCKS5 代理连接**

```nc.openbsd -X 5 -x [proxy_host:proxy_port] [host] [port]```

**用 UDP 代替 TCP**

```nc.openbsd -u [host] [port]```

**传输文件**（接收方）

```nc.openbsd -l [port] > [received_file]```

**发送 CRLF 行结尾**（对 HTTP/SMTP 有用）

```nc.openbsd -C [host] [port]```

# SYNOPSIS

**nc.openbsd** [**-46bCDdFhklNnrStUuvZz**] [**-I** _length_] [**-i** _interval_] [**-M** _ttl_] [**-m** _minttl_] [**-O** _length_] [**-P** _proxy_username_] [**-p** _source_port_] [**-q** _seconds_] [**-s** _sourceaddr_] [**-T** _keyword_] [**-V** _rtable_] [**-W** _recvlimit_] [**-w** _timeout_] [**-X** _proxy_protocol_] [**-x** _proxy_address_[_:port_]] [_destination_] [_port_]

# PARAMETERS

_DESTINATION_
> 目标主机名或 IP 地址。

_PORT_
> 端口号或端口范围（例如 20-30）。

**-4**
> 仅使用 IPv4 地址。

**-6**
> 仅使用 IPv6 地址。

**-C**
> 以 CRLF 作为行结尾发送（LF 会转换为 CR+LF）。

**-D**
> 启用套接字调试。

**-d**
> 不尝试从 stdin 读取。

**-F**
> 用 sendmsg(2) 将第一个已连接的套接字传给 stdout 并退出。

**-i** _interval_
> 发送和接收的文本行之间间隔 interval 秒。

**-k**
> 当前连接完成后继续监听下一个连接（需要 -l）。

**-l**
> 监听传入连接，而不是主动发起连接。

**-M** _ttl_
> 设置发出数据包的 TTL / 跳数限制。

**-m** _minttl_
> 丢弃 TTL / 跳数限制低于 minttl 的传入数据包。

**-N**
> stdin 上遇到 EOF 后关闭网络套接字。

**-n**
> 不执行域名解析。

**-P** _proxy_username_
> 向需要身份验证的代理服务器出示的用户名。

**-p** _source_port_
> 指定 nc 使用的源端口。

**-q** _seconds_
> stdin 上遇到 EOF 后，等待指定秒数然后退出。

**-r**
> 随机选择源端口和/或目标端口。

**-S**
> 启用 RFC 2385 TCP MD5 签名选项。

**-s** _sourceaddr_
> 设置发送数据包所用的源地址。

**-T** _keyword_
> 更改 IPv4 TOS 或 IPv6 流量类别值。

**-U**
> 使用 Unix 域套接字。

**-u**
> 使用 UDP 而不是 TCP。

**-V** _rtable_
> 设置要使用的路由表。

**-v**
> 输出更详细的信息。

**-W** _recvlimit_
> 从网络收到 recvlimit 个数据包后终止。

**-w** _timeout_
> 对无法建立的连接或超过 timeout 秒仍处于空闲状态的连接执行超时。

**-X** _proxy_protocol_
> 代理协议：4（SOCKS4）、5（SOCKS5，默认）或 connect（HTTPS 代理）。

**-x** _proxy_address_[:_port_]
> 通过指定的代理连接目标。

**-z**
> 仅扫描正在监听的守护进程，不发送任何数据。

# DESCRIPTION

**nc.openbsd** 是 netcat 的 OpenBSD 重写版，是一个多功能网络工具，可通过 TCP、UDP 和 Unix 域套接字连接读写数据。它可以建立连接、发送数据包、监听端口、执行端口扫描，并同时支持 IPv4 和 IPv6。

常见用途包括：简单的 TCP 代理、与网络服务交互的 shell 脚本、网络守护进程测试以及临时文件传输。**-X** 和 **-x** 选项提供内置的 SOCKS 和 HTTPS 代理支持，**-z** 选项则用于轻量级端口扫描。

与其他一些 netcat 实现不同，OpenBSD 版本出于安全考虑没有提供连接后执行程序的 **-c** 或 **-e** 选项。

# CAVEATS

OpenBSD 变体的 netcat，通常是 Debian/Ubuntu 系统上的默认版本。端口扫描（**-z**）不能与监听模式（**-l**）一起使用。**-k** 选项只对 **-l** 有效。与其他某些 netcat 变体不同，本版本不存在用于执行命令的 **-c** 或 **-e** 选项。

# HISTORY

nc.openbsd 是 Hobbit 于 1995 年推出的原版 netcat 的 **OpenBSD** 重写版。开发 OpenBSD 版本的目的是提供一个更简洁、更安全的实现，移除了任意命令执行（**-e**）等功能，同时增加了代理支持、TLS 能力（在 OpenBSD 上）以及 Unix 域套接字支持。

# SEE ALSO

[nc](/man/nc)(1), [ncat](/man/ncat)(1), [socat](/man/socat)(1)
