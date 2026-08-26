# TAGLINE

用于通过 TCP 和 UDP 读写数据的多功能网络工具

# TLDR

**连接到主机**的特定端口

```nc [host] [port]```

**在端口上监听**传入连接

```nc -l [port]```

**持续监听**，客户端断开后不退出

```nc -lk [port]```

**扫描主机**上的端口

```nc -zv [host] [20-30]```

通过网络**发送文件**

```nc [host] [port] < [file.txt]```

在监听端**接收文件**

```nc -l [port] > [received_file.txt]```

通过 UDP 而非 TCP **建立连接**

```nc -u [host] [port]```

**设置连接超时**

```nc -w [5] [host] [port]```

**使用 IPv6**

```nc -6 [host] [port]```

# SYNOPSIS

**nc** [_options_] [_hostname_] [_port_]

**nc** -l [_options_] [_port_]

# PARAMETERS

**-l**
> 监听模式；等待传入连接

**-k**
> 配合 -l 使用，在连接关闭后继续监听

**-n**
> 不做 DNS 查询；仅使用数字地址

**-p** _PORT_
> 指定源端口

**-s** _ADDR_
> 指定源 IP 地址

**-u**
> 使用 UDP 而非 TCP

**-v**
> 详细输出

**-w** _SECS_
> 连接和空闲时间的超时时间

**-z**
> 零输入/输出模式；扫描时不发送数据

**-4**
> 仅强制使用 IPv4

**-6**
> 仅强制使用 IPv6

**-d**
> 不从 stdin 读取数据

**-i** _SECS_
> 发送/接收行之间的延迟时间

**-r**
> 随机化端口号

**-t**
> 启用 telnet 协商

**-C**
> 发送 CRLF 行尾

**-x** _PROXY:PORT_
> 通过代理连接

**-X** _PROTO_
> 代理协议（4=SOCKS4，5=SOCKS5，connect=HTTPS）

**-U**
> 使用 Unix 域套接字

**-e** _CMD_
> 建立连接后执行命令（仅传统 nc 支持）

# DESCRIPTION

**nc**（netcat）是一个多功能网络工具，可通过 TCP 和 UDP 连接读写数据。它常被称为"网络界的瑞士军刀"，几乎可以创建任何类型的网络连接，对调试和测试极为有用。

常见用途包括：端口扫描、传输文件、创建简单的聊天服务器、网络调试以及测试网络服务。在监听模式（**-l**）下，nc 等待传入连接；否则它会主动向远程主机发起连接。

数据从 stdin 读取并写入 stdout，因此可以轻松地通过管道在网络连接中传输数据。存在多种实现（OpenBSD、GNU、Nmap 的 ncat），功能集各不相同。用于执行命令的 **-e** 选项只存在于某些版本中，出于安全考虑，一些实现已将其移除。

# CAVEATS

不同的 netcat 实现具有不同的选项和功能。出于安全原因，OpenBSD netcat 移除了 **-e** 标志。诸如 **-k** 之类的选项可能并非在所有版本中都可用。端口扫描可能被检测为敌意行为。如需跨平台一致的行为，请使用 **ncat**（来自 Nmap）。

# HISTORY

Netcat 最初由一位网名为 **Hobbit** 的黑客编写，于 **1995 年**发布。它迅速成为网络管理员和安全专业人员的重要工具。原始版本包含强大但潜在危险的功能，例如用于执行命令的 **-e**。OpenBSD 于 **2001 年**从零开始重写了 netcat，专注于安全性并移除了有风险的功能。Nmap 项目创建了 **ncat**，作为支持 SSL 并具备额外功能的现代重新实现。

# INSTALL

```dnf: sudo dnf install netcat```

```brew: brew install netcat```

```nix: nix profile install nixpkgs#netcat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ncat](/man/ncat)(1), [socat](/man/socat)(1), [telnet](/man/telnet)(1), [ss](/man/ss)(8)
