# TAGLINE

从网络流量转储或 pcap 文件创建 IP 地址聚合

# TLDR

**从转储文件聚合 IP 地址**

```ipaggcreate [input.dump] > [output.agg]```

**从 pcap 文件创建聚合**

```ipaggcreate -r [capture.pcap] > [output.agg]```

**按源 IP 地址聚合**

```ipaggcreate --src [input.dump]```

**按目标 IP 地址聚合**

```ipaggcreate --dst [input.dump]```

**按 TCP/UDP 流聚合**

```ipaggcreate --flows -r [capture.pcap]```

**统计字节数而非数据包数**

```ipaggcreate --bytes [input.dump]```

# SYNOPSIS

**ipaggcreate** [_options_] [_files_]

# PARAMETERS

**-r**, **--tcpdump** _FILE_
> 从一个或多个 tcpdump/pcap 文件读取

**-s**, **--src**
> 按 IP 源地址打标签

**-d**, **--dst**
> 按 IP 目标地址打标签（默认）

**--flows**
> 按 TCP 或 UDP 流打标签

**--address-pairs**
> 按地址对打标签

**--packets**
> 统计每个标签的数据包数（默认）

**-B**, **--bytes**
> 统计每个标签的字节数（含 IP 和传输层头部，不含链路层头部）

**-o**, **--output** _FILE_
> 将输出写入文件而非 stdout

**-f**, **--filter** _FILTER_
> 仅包含匹配 tcpdump 过滤表达式的数据包

**-b**, **--binary**
> 以二进制格式写出摘要

**-A**, **--anonymize**
> 匿名化输出中的 IP 地址

**-t**, **--interval** _TIME_
> 记录指定时长的聚合数据后停止

**-q**, **--quiet**
> 不显示进度条输出

# DESCRIPTION

**ipaggcreate** 从一个或多个数据源读取 IP 数据包，将每个数据包映射为一个标签（如源地址、目标地址或流），并输出一个聚合文件，报告每个标签观测到的数据包数或字节数。

该工具是 **ipsumdump** 软件包的一部分，与 **ipsumdump** 和 **ipaggmanip** 配合使用，进行网络流量分析与汇总。

# CAVEATS

输入格式必须兼容 ipsumdump 输出格式或 pcap 格式。大型抓包文件可能需要大量内存进行聚合。输出格式为 ipagg 工具套件专用。

# HISTORY

由 Eddie Kohler 在 UCLA 以及后来的 ICSI 开发的 **ipsumdump** 软件包的一部分。该工具套件为网络测量研究而创建，于 **2000 年代**初作为开源软件发布。

# SEE ALSO

[ipsumdump](/man/ipsumdump)(1), [ipaggmanip](/man/ipaggmanip)(1), [tcpdump](/man/tcpdump)(1)
