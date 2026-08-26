# TAGLINE

捕获并分析网络数据包

# TLDR

**在默认接口上捕获**数据包

```tcpdump```

**在指定接口上捕获**

```tcpdump -i [eth0]```

**只捕获**发往/来自主机的数据包

```tcpdump host [192.168.1.1]```

**捕获指定端口上的**数据包

```tcpdump port [80]```

**捕获并保存**到文件

```tcpdump -w [capture.pcap]```

**从文件读取**数据包

```tcpdump -r [capture.pcap]```

**以详细输出捕获**

```tcpdump -v```

**捕获 HTTP 流量**

```tcpdump -A port [80]```

**捕获指定协议的**数据包

```tcpdump icmp```

**限制捕获数量**的数据包

```tcpdump -c [100]```

**不解析主机名**

```tcpdump -n```

# SYNOPSIS

**tcpdump** [_options_] [_filter expression_]

# DESCRIPTION

**tcpdump** 是一个数据包分析器，用于捕获并显示网络流量。它使用 libpcap 从网络接口捕获数据包，并可用 Berkeley 包过滤器（BPF）语法过滤流量。

该工具可以实时捕获数据包、以多种格式显示其内容，并将其保存到文件供日后分析。输出可以只显示包头、完整内容，或十六进制转储。

tcpdump 是网络故障排查、安全分析和协议调试的必备工具。它是 Wireshark 等图形化工具的命令行对应物。

# PARAMETERS

**-i** _interface_
> 在指定接口上捕获。

**-w** _file_
> 将数据包写入文件。

**-r** _file_
> 从文件读取数据包。

**-c** _count_
> 只捕获 count 个数据包。

**-n**
> 不解析主机名。

**-nn**
> 不解析主机名和端口。

**-v**, **-vv**, **-vvv**
> 详细输出级别。

**-A**
> 以 ASCII 打印数据包。

**-X**
> 以十六进制和 ASCII 打印数据包。

**-s** _snaplen_
> 每个数据包捕获 snaplen 字节（0=全部）。

**-e**
> 打印链路层头部。

**-q**
> 快速输出（较少协议信息）。

**-D**, **--list-interfaces**
> 列出可用接口。

**-t**
> 不在每行打印时间戳。

**-tt**
> 在每行打印未格式化的时间戳。

**-p**, **--no-promiscuous-mode**
> 不将接口置于混杂模式。

**-F** _file_
> 使用文件作为过滤表达式的输入。

# FILTER EXPRESSIONS

**host** _ip_
> 匹配发往/来自指定主机的数据包。

**net** _cidr_
> 匹配指定网络内的数据包（例如 `net 10.0.0.0/8`）。

**port** _num_
> 匹配源或目标端口为指定值的数据包。

**portrange** _lo-hi_
> 匹配端口范围内的数据包。

**src** / **dst**
> 将前一个原语限定为源或目标。

**tcp** / **udp** / **icmp**
> 匹配指定协议的数据包。

**and** / **or** / **not**
> 用布尔逻辑组合各原语。

示例：`tcpdump 'tcp port 80 and host 192.168.1.1'`

# CAVEATS

需要 root 权限。在高流量网络上抓包可能影响性能。完整抓包会占用大量磁盘空间。某些协议经过加密，无法查看其内容。

# HISTORY

**tcpdump** 由 **Van Jacobson**、**Craig Leres** 和 **Steven McCanne** 于 **1988 年**在 **劳伦斯伯克利国家实验室**编写。它成为 Unix 系统上网络包分析的基石。libpcap 库从 tcpdump 中剥离出来，如今被包括 Wireshark 在内的众多网络分析工具使用。

# INSTALL

```apt: sudo apt install tcpdump```

```dnf: sudo dnf install tcpdump```

```pacman: sudo pacman -S tcpdump```

```apk: sudo apk add tcpdump```

```zypper: sudo zypper install tcpdump```

```brew: brew install tcpdump```

```nix: nix profile install nixpkgs#tcpdump```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wireshark](/man/wireshark)(1), [tshark](/man/tshark)(1), [ngrep](/man/ngrep)(1), [iftop](/man/iftop)(1)
