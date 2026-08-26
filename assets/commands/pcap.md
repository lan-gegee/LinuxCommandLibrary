# TAGLINE

libpcap 用于存储网络数据包数据的文件格式

# TLDR

**用 tcpdump 读取 pcap**

```tcpdump -r [capture.pcap]```

**用 tshark 读取**

```tshark -r [capture.pcap]```

**写入 pcap**

```tcpdump -i [eth0] -w [capture.pcap]```

**过滤并读取**

```tcpdump -r [capture.pcap] 'port 80'```

**用 editcap 转换**

```editcap [input.pcap] [output.pcapng]```

# SYNOPSIS

**pcap** - 数据包捕获文件格式

# DESCRIPTION

**pcap**（Packet Capture）是 libpcap 用于存储网络数据包数据的文件格式。它是网络抓包的标准格式，被 tcpdump、Wireshark 和众多安全工具使用。

# FILE STRUCTURE

```
Global Header (24 bytes)
├── Magic Number (0xa1b2c3d4)
├── Version
├── Timestamp offset
├── Snap length
└── Link type

Packet Records
├── Timestamp
├── Captured length
├── Original length
└── Packet data
```

# TOOLS

```
tcpdump    - CLI capture/read
wireshark  - GUI analysis
tshark     - CLI analysis
editcap    - Edit captures
mergecap   - Merge captures
```

# CAVEATS

pcap 是二进制格式。pcapng 提供更多功能。大型抓包文件需要大量存储空间。

# HISTORY

pcap 格式和 libpcap 由 **Van Jacobson**、**Craig Leres** 和 **Steven McCanne** 在 **劳伦斯伯克利实验室（Lawrence Berkeley Laboratory）** 开发。

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [tshark](/man/tshark)(1), [editcap](/man/editcap)(1)
