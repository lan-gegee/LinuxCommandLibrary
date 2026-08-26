# TAGLINE

网络密码嗅探器

# TLDR

在网卡接口上**嗅探密码**

```sudo dsniff -i [eth0]```

从抓包文件读取

```dsniff -p [capture.pcap]```

写入文件

```sudo dsniff -i [eth0] -w [output.txt]```

**启用自动协议检测**

```sudo dsniff -i [eth0] -m```

从先前保存的会话文件读取

```dsniff -r [savefile]```

使用自定义触发定义**嗅探**

```sudo dsniff -i [eth0] -t [80/tcp=http]```

# SYNOPSIS

**dsniff** [_options_]

# DESCRIPTION

**dsniff** 是一款密码嗅探器，通过被动监控网络流量来捕获明文传输的身份验证凭据。它支持一整套协议，包括 FTP、Telnet、HTTP、SNMP、IMAP、POP、LDAP、rlogin、RPC、NFS、X11、Oracle、PostgreSQL 等等。

该工具的工作方式是分析数据包流并在用户名和密码经过网络时将其提取出来。它会自动检测协议并进行 TCP 流重组，从而正确捕获多包交换中的凭据。

dsniff 为经授权的网络安全审计和渗透测试而设计，展示了以明文传输凭据的重大安全风险。它的存在推动了 SSH 和 HTTPS 等加密替代方案的普及。该工具至今仍适用于安全评估以及识别仍在使用不安全认证方式的遗留系统。

# PARAMETERS

**-i** _interface_
> 要嗅探的网络接口。

**-p** _file_
> 从 pcap 文件读取。

**-w** _file_
> 将输出写入文件。

**-m**
> 启用自动协议检测。

**-n**
> 不解析主机名。

**-c**
> 执行半双工 TCP 流重组。

**-s** _snaplen_
> 每个 TCP 连接最多只分析前 snaplen 个字节（默认 1024）。

**-f** _services_
> 从服务配置文件加载触发定义。

**-t** _trigger[,...]_
> 从逗号分隔的列表加载触发器，格式为 port/proto=service。

**-r** _savefile_
> 从保存的文件读取先前捕获的会话。

**-d**
> 启用调试。

_expression_
> 指定 tcpdump(8) 过滤表达式来选择要嗅探的流量。

# SUPPORTED PROTOCOLS

FTP, Telnet, SMTP, HTTP, POP, poppass, NNTP, IMAP, SNMP, LDAP, Rlogin, RIP, OSPF, PPTP MS-CHAP, NFS, VRRP, YP/NIS, SOCKS, X11, CVS, IRC, AIM, ICQ, Napster, PostgreSQL, Meeting Maker, Citrix ICA, Symantec pcAnywhere, NAI Sniffer, Microsoft SMB, Oracle SQL*Net, Sybase, Microsoft SQL

# CAVEATS

仅限经授权的安全测试。无法捕获加密协议（SSH、HTTPS）。需要 root/管理员权限。可能违反网络策略。协议检测并非完美无缺。

# HISTORY

**dsniff** 由 **Dug Song** 于 **2000 年**前后创建，是一套网络审计工具的组成部分。它揭示了明文认证的危险，推动了向加密协议的转型。dsniff 套件还包括 arpspoof 和 macof 等相关工具。

# INSTALL

```apt: sudo apt install dsniff```

```dnf: sudo dnf install dsniff```

```pacman: sudo pacman -S dsniff```

```nix: nix profile install nixpkgs#dsniff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcpdump](/man/tcpdump)(1), [wireshark](/man/wireshark)(1), [arpspoof](/man/arpspoof)(1), [ettercap](/man/ettercap)(8), [tcpreplay](/man/tcpreplay)(1)
