# TAGLINE

将 scamper warts 文件转换为 pcap 格式

# TLDR

**将 warts 转换为 pcap 格式**

```sc_warts2pcap [input.warts] > [output.pcap]```

**将输出写入指定文件**

```sc_warts2pcap -o [output.pcap] [input.warts]```

**按时间戳顺序排列数据包**

```sc_warts2pcap -s sort [input.warts] > [output.pcap]```

# SYNOPSIS

**sc_warts2pcap** [_options_] _file_

# PARAMETERS

**-o** _file_
> 将输出写入指定文件而不是标准输出。

**-s** _sort_
> 写入前按时间戳顺序对 pcap 记录排序。默认情况下数据包按照在 warts 文件中出现的顺序写出。排序需要先将所有数据包加载到内存。

# DESCRIPTION

**sc_warts2pcap** 将 scamper 的 warts 格式文件转换为 pcap（数据包捕获）格式。这样就可以使用 Wireshark、tcpdump 等标准网络工具分析 scamper 的测量数据。该工具从 tbit、sting 和 sniff 等 warts 对象中提取内嵌的原始数据包，并将其写成 pcap 记录。

**scamper** 网络测量工具集的一部分。

# CAVEATS

只有包含内嵌数据包数据的 warts 文件才能进行有意义的转换。并非所有 scamper 测量类型都会在输出中嵌入原始数据包。

# INSTALL

```apt: sudo apt install scamper```

```zypper: sudo zypper install scamper```

```brew: brew install scamper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sc_warts2json](/man/sc_warts2json)(1), [sc_wartsdump](/man/sc_wartsdump)(1), [scamper](/man/scamper)(1), [tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1)
