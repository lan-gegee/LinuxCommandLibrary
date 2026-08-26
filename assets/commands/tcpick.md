# TAGLINE

TCP 流嗅探器与分析器

# TLDR

按**接口**、主机和端口捕获流量

```sudo tcpick -i [interface] -C -h [host] -p [port]```

捕获 **HTTP** 流量

```sudo tcpick -i eth0 -C -h [192.168.1.100] -p 80```

显示**帮助**

```tcpick --help```

# SYNOPSIS

**tcpick** [_OPTIONS_]

# PARAMETERS

**-i, --interface** _INTERFACE_
> 在指定网络接口上捕获

**-C, --colors**
> 以彩色显示输出

**-h** _HOST_
> 按主机过滤

**-p** _PORT_
> 按端口过滤

**-r** _FILE_
> 从 pcap 文件读取

**-w** _FILE_
> 写入 pcap 文件

**-a**
> 以 ASCII 显示数据

**-x**
> 以十六进制显示数据

# DESCRIPTION

**tcpick** 是一个数据包嗅探器和 TCP 流分析器，用于捕获并显示 TCP 连接及其数据。它可以监视特定接口、主机或端口上的网络流量，并以彩色输出。

该工具跟踪 TCP 连接状态，可以重组 TCP 流以显示完整的会话内容。

# CAVEATS

抓包需要 root 权限。使用 libpcap 实现捕获功能。连接跟踪在繁忙网络上可能消耗内存。

# HISTORY

**tcpick** 为网络分析师提供了一个专注于 TCP 流量检查的工具，把捕获和分析集成在同一个实用程序中。

# INSTALL

```apt: sudo apt install tcpick```

```dnf: sudo dnf install tcpick```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(8), [tcpflow](/man/tcpflow)(1), [wireshark](/man/wireshark)(1)
