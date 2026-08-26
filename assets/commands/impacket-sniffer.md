# TAGLINE

基于 Impacket 库原始套接字的简易数据包嗅探器

# TLDR

**嗅探默认协议（ICMP、TCP、UDP）**

```sudo impacket-sniffer```

**嗅探指定协议**

```sudo impacket-sniffer [icmp] [tcp]```

**仅嗅探 UDP 流量**

```sudo impacket-sniffer [udp]```

# SYNOPSIS

**impacket-sniffer** [_protocol_ ...]

# PARAMETERS

_protocol_
> 要嗅探的一个或多个协议名（例如 icmp、tcp、udp）。任何能被 **socket.getprotobyname()** 识别的名称均有效。未指定协议时，默认嗅探 icmp、tcp 和 udp。

# DESCRIPTION

**impacket-sniffer** 是一个简单的数据包嗅探器，使用原始套接字监听匹配指定协议的数据包。它为每个协议打开一个原始套接字，用 **select()** 监控传入的数据包，并使用 Impacket 的 **ImpactDecoder.IPDecoder** 解码后显示。

与 **tcpdump** 不同，该工具不接受网卡参数或 BPF 过滤表达式。它通过原始套接字监听所有可用网卡，仅按协议类型过滤。

# CAVEATS

访问原始套接字需要 root/管理员权限。不支持选择网卡或 BPF 过滤。要进行完整的数据包分析，**Wireshark** 或 **tcpdump** 等专用工具更为合适。

# HISTORY

属于 **Impacket** 库，最初由 SecureAuth 开发（现由 Fortra 维护）。演示了 Impacket 在 Python 中进行网络流量捕获和协议解码的能力。

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [impacket-sniff](/man/impacket-sniff)(1), [tshark](/man/tshark)(1), [ngrep](/man/ngrep)(1)
