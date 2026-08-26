# TAGLINE

网络探测与安全审计工具

# TLDR

**扫描单个主机**

```nmap [192.168.1.1]```

**扫描一个网络范围**

```nmap [192.168.1.0/24]```

**扫描特定端口**

```nmap -p [22,80,443] [host]```

**服务与版本检测**

```nmap -sV [host]```

**操作系统检测**（需要 root）

```sudo nmap -O [host]```

**激进扫描**（OS、版本、脚本、traceroute）

```sudo nmap -A [host]```

**隐蔽 SYN 扫描**（需要 root）

```sudo nmap -sS [host]```

**UDP 扫描**（需要 root）

```sudo nmap -sU [host]```

**扫描全部 65535 个端口**

```nmap -p- [host]```

**以所有格式保存输出**

```nmap -oA [output_basename] [host]```

**运行特定的 NSE 脚本**

```nmap --script [vuln] [host]```

# SYNOPSIS

**nmap** [_scan type_] [_options_] _target specification_

# PARAMETERS

_TARGETS_
> 要扫描的主机/网络。接受主机名、IP、CIDR 范围或形如 192.168.1.1-254 的范围。

**-p** _PORTS_
> 要扫描的端口。可以是范围（1-1024）、列表（22,80,443），或用 -p- 表示全部 65535 个端口。

**-sS**
> TCP SYN 扫描（隐蔽/半开连接）。以 root 运行时的默认扫描类型。

**-sT**
> TCP connect 扫描。不以 root 运行时的默认方式。

**-sU**
> UDP 扫描。比 TCP 扫描慢。

**-sn**
> Ping 扫描（仅主机发现，不进行端口扫描）。

**-sV**
> 探测开放端口以获取服务版本信息。

**-O**
> 启用操作系统检测（需要 root）。

**-A**
> 激进扫描：启用 -O、-sV、--script=default 和 --traceroute。

**-T**_0-5_
> 时间模板，从偏执（0）到疯狂（5）。默认为 -T3。

**--script** _scripts_
> 运行指定的 NSE（Nmap Scripting Engine）脚本。

**-oN** _FILE_
> 将普通文本输出保存到文件。

**-oX** _FILE_
> 将 XML 输出保存到文件。

**-oG** _FILE_
> 将可 grep 的输出保存到文件。

**-oA** _BASENAME_
> 以所有格式输出（普通、XML、可 grep）。

**-v**
> 提高详细程度（更多可用 -vv）。

**--top-ports** _N_
> 只扫描最常见的 N 个端口。

**-Pn**
> 跳过主机发现（将所有主机视为在线）。

**-iL** _FILE_
> 从文件读取目标。

**--open**
> 结果中只显示开放端口。

# DESCRIPTION

**nmap**（Network Mapper）是一款免费开源的网络发现与安全审计工具。它使用原始 IP 数据包来确定可用主机及其服务、操作系统、防火墙规则等特征。

Nmap 内置 Nmap 脚本引擎（NSE），包含数百个用于漏洞检测、服务枚举和暴力破解测试的脚本。输出可以多种格式保存，便于与其他工具集成。

常见扫描类型包括：面向隐蔽性的 TCP SYN 扫描（-sS）、适合非特权用户的 TCP connect 扫描（-sT）、UDP 扫描（-sU），以及用于主机发现的 ping 扫描（-sn）。

# CAVEATS

未经授权的扫描可能违法。许多扫描类型（SYN、OS 检测）需要 root/sudo 权限。激进的扫描可能触发 IDS/IPS 告警或造成网络中断。UDP 扫描明显慢于 TCP 扫描。

# HISTORY

Nmap 由 **Gordon Lyon (Fyodor)** 创建，于 **1997 年**首次发布。此后它成为网络扫描的事实标准，被世界各地的安全专业人员使用。

# INSTALL

```apt: sudo apt install nmap```

```dnf: sudo dnf install nmap```

```pacman: sudo pacman -S nmap```

```apk: sudo apk add nmap```

```brew: brew install nmap```

```nix: nix profile install nixpkgs#nmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[masscan](/man/masscan)(1), [netcat](/man/netcat)(1), [zenmap](/man/zenmap)(1), [ss](/man/ss)(8), [tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1)
