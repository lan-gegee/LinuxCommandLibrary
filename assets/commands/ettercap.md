# TAGLINE

全面的网络中间人攻击套件

# TLDR

**启动图形**界面

```ettercap -G```

**ARP 毒化**攻击

```ettercap -Tq -M arp:remote /[target1]// /[target2]//```

在安静模式下**于指定接口嗅探**

```ettercap -Tq -i [eth0]```

**使用文本界面**

```ettercap -T```

**加载插件**

```ettercap -Tq -P [dns_spoof]```

**从 pcap 文件读取**

```ettercap -T -r [capture.pcap]```

**将捕获的数据包写入**文件

```ettercap -Tq -w [output.pcap] -M arp /[target]// /[gateway]//```

以后台守护进程方式**运行**

```ettercap -D -M arp /[target]// /[gateway]//```

# SYNOPSIS

**ettercap** [_options_] [_target1_] [_target2_]

# PARAMETERS

_TARGET_
> 目标规格（MAC/IP/PORT）。

**-G**
> 图形（GTK）界面。

**-T**
> 纯文本界面。

**-M** _METHOD_
> 中间人攻击方法。

**-i** _INTERFACE_
> 网络接口。

**-P** _PLUGIN_
> 加载插件。

**-r** _FILE_
> 从 pcap 文件读取。

**-w** _FILE_
> 写入 pcap 文件。

**-q**
> 安静模式（不显示数据包内容）。

**-D**
> 以守护进程方式运行 ettercap（在后台运行）。

**-F** _FILE_
> 加载过滤文件（由 etterfilter 编译生成）。

**-L** _FILE_
> 将所有流量记录到此文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Ettercap** 是一套针对局域网的全面中间人攻击套件。它支持主动和被动协议分析，包含网络与主机分析功能。

该工具可通过 ARP 毒化拦截流量，实现数据包嗅探、注入和过滤。插件可扩展 DNS 欺骗、操作系统指纹识别等功能。

Ettercap 用于网络安全测试、协议分析以及在授权网络上进行渗透测试。

# CONFIGURATION

**/etc/ettercap/etter.conf**
> 主配置文件，控制默认接口、数据包转发、插件路径和网络设置。

**/etc/ettercap/etter.dns**
> DNS 欺骗配置，为主机名到 IP 地址建立映射，供 dns_spoof 插件使用。

# CAVEATS

仅在授权网络上使用。可能干扰网络的正常运行。会被安全工具检测到。某些攻击需要 root 权限。

# HISTORY

Ettercap 由 **Alberto Ornaghi** 和 **Marco Valleri** 创建，作为面向网络安全研究的开源软件发布。它已成为演示中间人攻击的标准工具。

# INSTALL

```apt: sudo apt install ettercap-graphical```

```dnf: sudo dnf install ettercap```

```pacman: sudo pacman -S ettercap```

```brew: brew install ettercap```

```nix: nix profile install nixpkgs#ettercap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[arpspoof](/man/arpspoof)(8), [wireshark](/man/wireshark)(1), [tcpdump](/man/tcpdump)(1), [nmap](/man/nmap)(1), [mitmproxy](/man/mitmproxy)(1)
