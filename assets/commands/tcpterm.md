# TAGLINE

TUI 数据包可视化工具，给人看的 tcpdump

# TLDR

**在网络接口上捕获数据包**

```tcpterm -i [eth0]```

**从 pcap 文件读取数据包**

```tcpterm -r [capture.pcap]```

**应用 BPF 过滤器**（以位置参数传入）

```tcpterm -i [eth0] [port 80]```

# SYNOPSIS

**tcpterm** [_options_]

# PARAMETERS

**-i** _INTERFACE_
> 从指定网络接口捕获数据包。

**-r** _FILE_
> 从 pcap 文件读取数据包。

**-s** _SNAPLEN_
> 每个数据包的快照长度（默认 65535）。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

_expression_
> 可选的 BPF 过滤表达式（位置参数），例如 `port 80`。

# DESCRIPTION

**tcpterm** 是一个基于终端的数据包可视化工具，为 tcpdump 提供了更友好的替代方案。它可以从网络接口捕获实时流量，也可以读取 pcap 文件，并支持 BPF 过滤器。

# HISTORY

**tcpterm** 由 **Takumasa Sakao**（sachaos）创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S tcpterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [tshark](/man/tshark)(1)
