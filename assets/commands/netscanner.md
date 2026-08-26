# TAGLINE

具有现代 TUI 的终端网络扫描与诊断工具

# TLDR

**启动网络扫描器**

```netscanner```

# SYNOPSIS

**netscanner** [_options_]

# PARAMETERS

**-t**, **--tick-rate** _N_
> 设置每秒的 tick 数（默认：1）。

**-f**, **--frame-rate** _N_
> 设置每秒帧数（默认：10）。

# DESCRIPTION

**netscanner** 是一款基于 TUI 的网络扫描与诊断工具。功能包括列出硬件接口、切换活动接口以进行扫描和数据包转储、带信号强度图表的 WiFi 网络扫描、支持 CIDR 的 IPv4 ping、主机名/OUI/MAC 地址查询，以及针对 TCP、UDP、ICMP 和 ARP 协议的数据包转储。

# CAVEATS

捕获数据包需要提升权限。在 Windows 上必须安装 Npcap。

# HISTORY

**netscanner** 由 **Chleba** 创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S netscanner```

```brew: brew install netscanner```

```nix: nix profile install nixpkgs#netscanner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmap](/man/nmap)(1), [arp-scan](/man/arp-scan)(1), [tcpdump](/man/tcpdump)(8)
