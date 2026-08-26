# TAGLINE

使用 Impacket 原始套接字能力的基础数据包捕获工具

# TLDR

在网卡上**捕获网络数据包**

```sudo impacket-sniff [eth0]```

**使用过滤表达式进行嗅探**

```sudo impacket-sniff -filter '[tcp port 80]' [eth0]```

# SYNOPSIS

**impacket-sniff** [_-h_] [_-filter FILTER_] _interface_

# PARAMETERS

**-filter** _FILTER_
> 用于限制捕获数据包的 BPF 过滤表达式

# DESCRIPTION

**impacket-sniff** 是一款基础数据包捕获工具，利用 Impacket 的原始套接字能力。它在指定网卡上捕获网络流量并显示数据包信息。

该工具提供了一种借助 Impacket 协议解析来观察网络流量的简单方式，可用于安全评估期间的调试或理解网络通信。

# CAVEATS

访问原始套接字需要 root/管理员权限。对于生产环境的数据包捕获需求，**tcpdump** 或 **Wireshark** 等工具功能更丰富。网卡必须处于允许混杂模式的状态。

# HISTORY

属于 SecureAuth 的 **Impacket** 库。收录该工具是为了演示如何用 Python 实现 Impacket 的数据包捕获与解析能力。

# INSTALL

```pacman: sudo pacman -S impacket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [impacket-sniffer](/man/impacket-sniffer)(1), [tshark](/man/tshark)(1)
