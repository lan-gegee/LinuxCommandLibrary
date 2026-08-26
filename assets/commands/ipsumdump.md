# TAGLINE

通过提取和显示所选字段来汇总网络流量

# TLDR

从 pcap 文件**转储数据包摘要**

```ipsumdump -r [capture.pcap]```

**抓取实时流量**并进行汇总

```sudo ipsumdump -i [eth0]```

**提取源和目标 IP**

```ipsumdump -r [capture.pcap] --src --dst```

**输出时间戳、源地址、目标地址和协议**

```ipsumdump -r [capture.pcap] --timestamp --src --dst --proto```

使用 BPF 表达式**过滤数据包**

```ipsumdump -r [capture.pcap] --filter '[tcp port 80]' --src --dst```

**以指定格式输出**自定义字段

```ipsumdump -r [capture.pcap] --src --sport --dst --dport --length```

# SYNOPSIS

**ipsumdump** [_-r file_] [_-i interface_] [_--filter expression_] [_--output fields_] [_options_]

# PARAMETERS

**-r** _file_
> 从 pcap 文件读取

**-i** _interface_
> 从接口抓取实时流量

**--filter** _expression_
> BPF 过滤表达式

**--src**
> 输出源 IP 地址

**--dst**
> 输出目标 IP 地址

**--sport**
> 输出源端口

**--dport**
> 输出目标端口

**--proto**
> 输出 IP 协议

**--timestamp**
> 输出数据包时间戳

**--length**
> 输出数据包长度

**--payload**
> 输出载荷数据

**--no-promiscuous**
> 不将接口设为混杂模式

**-o** _file_
> 将输出写入文件

# DESCRIPTION

**ipsumdump** 通过提取并显示数据包头中的选定字段来汇总网络流量。它可以从 pcap 文件读取或抓取实时流量，生成适合进一步处理的紧凑文本输出。

该工具专为网络分析与测量设计，每个数据包输出一行 ASCII 文本。它特别适用于创建分析用数据集、生成聚合统计或提取特定的数据包字段。

# CAVEATS

实时抓包需要 root/管理员权限。高流量可能导致丢包。输出格式为文本；若需二进制分析请考虑其他工具。它是 ipsumdump 套件的一部分，套件还包括 ipaggcreate 和 ipaggmanip。

# HISTORY

**ipsumdump** 由 Eddie Kohler 在 UCLA（后来在 ICSI）开发，用于网络测量研究。首次发布于 **2000 年代**初，基于 Click 模块化路由器框架构建，至今仍可用于网络流量分析和研究。

# INSTALL

```brew: brew install ipsumdump```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [tshark](/man/tshark)(1), [ipaggcreate](/man/ipaggcreate)(1), [ipaggmanip](/man/ipaggmanip)(1)
