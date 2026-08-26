# TAGLINE

二层网络协议攻击框架

# TLDR

**启动交互式 ncurses 模式**

```sudo yersinia -I```

**启动 GTK 图形界面**

```sudo yersinia -G```

**发起 DHCP 饥饿攻击**

```sudo yersinia dhcp -attack 1 -i [eth0]```

发送 STP BPDU 以**夺取根网桥**

```sudo yersinia stp -attack 4 -i [eth0]```

**发起 DTP 攻击**以启用干道（trunking）

```sudo yersinia dtp -attack 1 -i [eth0]```

**泛洪 CDP 表**

```sudo yersinia cdp -attack 1 -i [eth0]```

在端口 12000 上**启动网络守护进程**

```sudo yersinia -D```

# SYNOPSIS

**yersinia** [_-hVGID_] [_protocol_] [_-attack attack_] [_options_]

# PARAMETERS

**-h**, **--help**
> 显示帮助

**-V**, **--Version**
> 显示版本

**-G**
> 启动 GTK 图形界面

**-I**
> 启动 ncurses 交互模式

**-D**
> 作为网络守护进程启动（端口 12000 上的 telnet 服务器）

**-d**
> 启用调试模式。

**-e**
> 不进入交互模式直接执行攻击。

**-i** _INTERFACE_
> 要使用的网络接口。

**-l** _FILE_
> 将输出记录到文件。

**-c** _FILE_
> 从文件读取配置。

**-r** _FILE_
> 从 pcap 文件读取数据包。

**-w** _FILE_
> 将数据包写入 pcap 文件。

**-attack** _NUM_
> 要执行的攻击编号。

# PROTOCOLS

**stp**
> 生成树协议攻击

**vtp**
> VLAN 干道协议攻击

**dtp**
> 动态干道协议攻击

**hsrp**
> 热备份路由协议攻击

**dhcp**
> DHCP 饥饿攻击与伪造服务器攻击

**cdp**
> Cisco 发现协议攻击

**dot1q**
> 802.1Q VLAN 跳跃攻击

**dot1x**
> 802.1X 基于端口的认证攻击

**mpls**
> MPLS 标签交换攻击

**isl**
> 交换机间链路协议攻击

# DESCRIPTION

**yersinia** 是一个用于执行二层网络攻击的框架。它利用的是工作在数据链路层的网络协议中的弱点，这些协议在安全评估中往往被忽视。

该工具支持多种攻击模式：交互式 ncurses 控制台（**-I**）、GTK 图形界面（**-G**）、网络守护进程（**-D**）以及直接的命令行执行。交互模式会显示协议字段和可用攻击，并用指示器标明哪些属于 DoS 攻击。

常见攻击包括 DHCP 饥饿（耗尽 IP 地址池）、STP 夺取根网桥（拦截流量）、DTP 干道协商（获取 VLAN 访问权）以及 CDP 泛洪（使交换机表溢出）。这些攻击可以破坏网络正常运行或形成中间人位置。

# CAVEATS

二层攻击可能严重破坏网络运行。某些攻击属于拒绝服务攻击，会导致网络不稳定。只能在你拥有所有权或获得明确授权测试的网络上使用。需要 root 权限。许多攻击只在本地网段内有效。现代交换机可能对某些攻击具备防护措施。

# HISTORY

Yersinia 由 **David Barroso** 和 **Alfredo Andres** 开发，是用于演示二层漏洞的研究工具。名字源自引起鼠疫的细菌 *Yersinia pestis*，暗喻这些攻击可以在网络中蔓延。该工具表明网络安全必须覆盖所有 OSI 层，而不仅仅是应用层威胁。它已成为网络渗透测试的标准工具之一。

# INSTALL

```apk: sudo apk add yersinia```

```nix: nix profile install nixpkgs#yersinia```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ettercap](/man/ettercap)(8), [arpspoof](/man/arpspoof)(8), [macchanger](/man/macchanger)(1), [tcpdump](/man/tcpdump)(8)
