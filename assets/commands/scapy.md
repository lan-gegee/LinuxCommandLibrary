# TAGLINE

交互式数据包操纵与网络工具

# TLDR

**启动 scapy 交互式** shell

```scapy```

以更高的详细程度**启动 scapy**

```scapy -d```

使用自定义启动文件**启动 scapy**

```scapy -c [path/to/startup.py]```

不运行启动文件**启动 scapy**

```scapy -C -P```

以无标头模式、较低详细程度**启动 scapy**

```scapy -H```

**发送 ping 数据包**并接收回复

```sr1(IP(dst="[8.8.8.8]")/ICMP())```

对端口**执行 TCP SYN 扫描**

```sr1(IP(dst="[target]")/TCP(dport=[80], flags="S"))```

# SYNOPSIS

**scapy** [**-h**] [**-H**] [**-d**] [**-p** _prestart_file_] [**-P**] [**-c** _startup_file_] [**-C**]

# PARAMETERS

**-h**
> 显示用法信息

**-H**
> 无标头模式；同时降低详细程度

**-d**
> 提高日志详细程度；可多次使用以获得更多细节

**-s** _file_
> 使用该文件保存/加载会话值（变量、函数、实例）

**-p** _prestart_file_
> 使用指定文件代替 ~/.config/scapy/prestart.py 作为预启动文件

**-P**
> 不运行预启动文件

**-c** _startup_file_
> 使用指定文件代替 ~/.config/scapy/startup.py 作为启动文件

**-C**
> 不运行启动文件

# DESCRIPTION

**Scapy** 是一款基于 Python 的交互式数据包操纵程序和库。它能够伪造、解码、发送和捕获多种网络协议的数据包。Scapy 使用 Python 解释器作为其命令接口，可以充分利用 Python 语法，包括变量、循环和函数。

该工具可以替代或补充 **hping**、**nmap**、**arpspoof**、**arping**、**tcpdump** 和 **tshark** 等实用程序。传统工具会把响应简化为 "open" 或 "closed" 这类简单状态，而 Scapy 不同，它提供完整的数据包数据以便进行详细分析。

常用函数包括：用于第三层数据包的 **send()**、用于第二层的 **sendp()**、发送并接收的 **sr()**、接收单个响应的 **sr1()**、抓包用的 **sniff()**，以及操作 PCAP 文件的 **wrpcap()**/**rdpcap()**。

# CAVEATS

Scapy 的大多数涉及原始套接字的操作需要 root 权限。在网络负载较重时可能丢失数据包。会话保存受 Python 序列化（marshaling）能力限制，因此 lambda 函数和生成器无法保存。接口别名可能报告错误的源 IP。

# HISTORY

**Scapy** 由 **Philippe Biondi** 于 **2003 年**创建，旨在成为僵硬的网络工具的灵活替代品。它在安全社区中因渗透测试和网络研究而广受欢迎。该项目已过渡到 Python 3 支持，并在 GitHub 上由安全社区持续积极维护。

# INSTALL

```pacman: sudo pacman -S scapy```

```apk: sudo apk add scapy```

```zypper: sudo zypper install scapy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [nmap](/man/nmap)(1), [hping3](/man/hping3)(1), [tshark](/man/tshark)(1)
