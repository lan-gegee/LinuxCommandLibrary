# TAGLINE

命令行网络数据包分析器

# TLDR

**监控**本地主机上的所有流量

```tshark```

只捕获匹配**捕获过滤器**的数据包

```tshark -f 'udp port 53'```

只显示匹配**输出过滤器**的数据包

```tshark -Y 'http.request.method == "GET"'```

用指定协议**解码** TCP 端口

```tshark -d tcp.port==8888,http```

指定捕获输出的**格式**

```tshark -T [json|text|ps]```

选择要输出的**特定字段**

```tshark -T fields -e http.request.method -e ip.src```

将捕获的数据包**写入**文件

```tshark -w [path/to/file]```

从文件中**分析**数据包

```tshark -r [path/to/file.pcap]```

# SYNOPSIS

**tshark** [_options_] [_filter_]

# PARAMETERS

**-i** _interface_
> 在指定网络接口上捕获

**-f** _filter_
> 捕获过滤器（BPF 语法）

**-Y** _filter_
> 显示过滤器（Wireshark 语法）

**-r** _file_
> 从文件读取数据包

**-w** _file_
> 将数据包写入文件

**-T** _format_
> 输出格式（text、json、pdml、ps、fields 等）

**-e** _field_
> 要打印的字段（配合 -T fields/json/pdml 使用）

**-d** _spec_
> 按指定协议解码（例如 tcp.port==8080,http）

**-c** _count_
> 捕获 count 个数据包后停止

**-a** _condition_
> 自动停止条件（duration:sec、filesize:KB）

**-V**
> 详细输出（数据包树）

**-x**
> 打印数据包数据的十六进制转储

**-q**
> 安静模式（减少输出）

# DESCRIPTION

**tshark** 是 Wireshark 的命令行版本，提供网络数据包捕获与分析能力。它可以从网络接口捕获实时流量、从捕获文件读取数据包，并解码协议数据。

该工具同时支持捕获过滤器（BPF 语法，在捕获时应用）和显示过滤器（Wireshark 语法，应用于输出）。它可以以多种格式输出数据，包括 text、JSON 和 PDML，便于后续处理。

# CAVEATS

实时捕获需要 root 权限或相应的能力（capabilities）。捕获过滤器与显示过滤器的语法不同。大型捕获可能占用大量磁盘空间和内存。某些协议的解码需要通过 **-d** 选项提供端口提示。

# HISTORY

属于 **Wireshark** 项目（最初名为 Ethereal）的一部分。命令行版本自项目早期就已存在。tshark 提供与 Wireshark 相同的协议分析引擎，但更适合脚本和无界面系统。

# INSTALL

```apt: sudo apt install tshark```

```apk: sudo apk add tshark```

```nix: nix profile install nixpkgs#tshark```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wireshark](/man/wireshark)(1), [tcpdump](/man/tcpdump)(8), [dumpcap](/man/dumpcap)(1)
