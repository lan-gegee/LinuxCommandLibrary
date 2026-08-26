# TAGLINE

异步无状态网络端口扫描器

# TLDR

**基本 TCP SYN 扫描**

```unicornscan [192.168.1.1]```

**扫描特定端口**

```unicornscan [192.168.1.1]:[22,80,443]```

**扫描端口范围**

```unicornscan [192.168.1.1]:[1-1000]```

**UDP 扫描**

```unicornscan -mU [192.168.1.1]```

**以指定速率扫描**

```unicornscan -r [1000] [192.168.1.1]```

**即时详细输出**

```unicornscan -Iv [192.168.1.1]```

**扫描网段**

```unicornscan [192.168.1.0/24]:[80,443]```

**将结果保存为 pcap**

```unicornscan -w [scan.pcap] [192.168.1.1]```

# SYNOPSIS

**unicornscan** [_options_] _target_[:_ports_]

# PARAMETERS

**-m** _mode_
> 扫描模式：T（TCP SYN）、U（UDP）、sf（connect）、A（ARP）。

**-r** _pps_
> 每秒数据包数。

**-i** _interface_
> 要使用的网络接口。

**-I**
> 即时模式：发现结果立即显示。

**-v**
> 详细输出。

**-H**
> 在输出中解析主机名。

**-l** _file_
> 将输出记录到文件。

**-w** _file_
> 将数据包写入 pcap 文件。

**-L** _seconds_
> 数据包超时时间（默认：7）。

**-p** _ports_
> 要扫描的全局端口。

**-B** _port_
> 用于扫描的源端口。

**-b** _layer_
> 发送损坏的 CRC：T（传输层）、N（网络层）、TN（两者）。

**-e** _module_
> 启用模块（例如 osdetect）。

**-E**
> 处理错误响应（ICMP、RST）。

**-Q**
> 安静模式。

**-h**
> 显示帮助。

# SCAN MODES

**-mT**: TCP SYN 扫描（默认）

**-mTsA**: TCP ACK 扫描

**-mTsF**: TCP FIN 扫描

**-mTs**: TCP NULL 扫描

**-mTsFPU**: TCP Xmas 扫描

**-msf**: TCP connect 扫描

**-mU**: UDP 扫描

# DESCRIPTION

**unicornscan** 是一个专为高速侦察设计的异步网络扫描器。它使用自定义的 TCP/IP 协议栈，将数据包的发送和接收分离到不同线程中，因此扫描速度远快于传统扫描器。

该扫描器支持多种 TCP 标志组合、UDP 扫描，以及通过可加载模块进行操作系统/服务指纹识别。其异步设计使其特别适合扫描大型网络。

输出可以自定义并保存到 pcap 文件供后续分析。该工具还可与数据库集成以存储扫描结果。

# CAVEATS

需要 root 权限才能访问原始套接字。过高的扫描速率可能触发 IDS/IPS。自定义 TCP 协议栈的行为可能与系统协议栈不同。仅在获得目标网络授权的情况下使用。

# HISTORY

**unicornscan** 由 Jack Louis 和 Robert E. Lee 开发，旨在解决同步扫描器的局限性，追求可扩展性和速度。该工具在渗透测试领域广受欢迎，并被收录进 Kali Linux。

# INSTALL

```aur: yay -S unicornscan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [masscan](/man/masscan)(1), [zmap](/man/zmap)(1), [hping3](/man/hping3)(1)
