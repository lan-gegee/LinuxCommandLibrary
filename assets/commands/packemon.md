# TAGLINE

用于生成和监控网络数据包的 TUI 工具

# TLDR

**启动数据包监控器**

```sudo packemon monitor```

**启动数据包生成器**

```sudo packemon generator```

**在指定接口上监控**

```sudo packemon monitor --interface [eth0]```

**列出可用的网络接口**

```packemon interfaces```

**显示 packemon 版本**

```packemon version```

# SYNOPSIS

**packemon** _command_ [_options_]

# PARAMETERS

**monitor**, **mon**, **m**
> 监控指定接口上收发的数据包。

**generator**, **gen**, **g**
> 生成并发送任意网络数据包。

**interfaces**, **intfs**, **i**
> 列出可用的网络接口。

**debugging**, **debug**, **d**
> 面向开发的调试模式。

**version**, **v**
> 显示版本信息。

**--interface** _NAME_
> 要使用的网络接口（默认：`eth0`）。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**packemon** 是一款 TUI 工具，用于生成自定义网络数据包并监控网络接口上的流量。它支持 Ethernet、ARP、IPv4/IPv6、ICMP、TCP、UDP、TLS 1.2/1.3、QUIC、DNS 和 HTTP 协议。monitor 模式可以捕获数据包并将其导出为 pcapng 格式，以便在 Wireshark 中分析。

# CAVEATS

需要 root 权限。在 Linux 上，TCP RST 抑制功能依赖 eBPF。在 Windows 上需要 Npcap。

# HISTORY

**packemon** 由 **ddddddO** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S packemon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [nmap](/man/nmap)(1)
