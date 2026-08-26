# TAGLINE

快速的互联网范围网络扫描器

# TLDR

**扫描网络上的 80 端口**

```sudo zmap -p [80] [192.168.1.0/24]```

**在特定端口上扫描整个互联网**

```sudo zmap -p [443] -o [results.txt]```

**以速率限制扫描**

```sudo zmap -p [22] -r [10000] [10.0.0.0/8]```

**以带宽限制扫描**

```sudo zmap -p [80] -B [10M] [target_subnet]```

**使用指定的网络接口**

```sudo zmap -p [80] -i [eth0] [target]```

**以 CSV 格式输出**

```sudo zmap -p [80] -o [results.csv] -O csv [target]```

# SYNOPSIS

**zmap** [**-p** _port_] [**-o** _outfile_] [**-b** _blacklist_] [_options_] [_target_]

# PARAMETERS

**-p**, **--target-port** _port_
> 要扫描的端口

**-o**, **--output-file** _file_
> 将结果输出到文件

**-b**, **--blacklist-file** _file_
> 要排除的地址列表文件

**-w**, **--whitelist-file** _file_
> 要包含的地址文件（只扫描这些地址）

**-r**, **--rate** _pps_
> 每秒发包数（默认：无限制）

**-B**, **--bandwidth** _bps_
> 带宽限制（例如 10M、1G）

**-i**, **--interface** _iface_
> 网络接口

**-G**, **--gateway-mac** _mac_
> 网关 MAC 地址

**-O**, **--output-module** _module_
> 输出格式（csv、json、extended_file）

**-f**, **--output-fields** _fields_
> 以逗号分隔的输出字段

**-n**, **--max-targets** _n_
> 最大扫描目标数

**-N**, **--max-results** _n_
> 收集到 N 个结果后停止

# DESCRIPTION

**ZMap** 是一款面向全网测量设计的快速网络扫描器。借助优化的数据包生成和无状态扫描，它能在一台机器上于 45 分钟内扫完整个 IPv4 地址空间。

与维护连接状态的 nmap 不同，ZMap 发送探测包并单独监听响应，因而可以达到高得多的吞吐量。它使用循环乘法群随机化扫描顺序，避免形成网络热点。

ZMap 通过模块支持多种探测类型（TCP SYN、ICMP、UDP）和多种输出格式。它常用于安全研究、测量全网漏洞暴露面以及普查式研究。

# CAVEATS

**警告**：未经授权扫描网络在许多司法辖区属于违法行为。只扫描你拥有的或已获得明确测试许可的网络。

需要 root/CAP_NET_RAW 才能访问原始套接字。

过高的扫描速率可能压垮网络或触发安全告警。请使用速率限制并遵守网络策略。

务必使用黑名单排除敏感地址（RFC 1918、军事及关键基础设施）。

# INSTALL

```apt: sudo apt install zmap```

```dnf: sudo dnf install zmap```

```pacman: sudo pacman -S zmap```

```apk: sudo apk add zmap```

```brew: brew install zmap```

```nix: nix profile install nixpkgs#zmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [masscan](/man/masscan)(1), [unicornscan](/man/unicornscan)(1)
