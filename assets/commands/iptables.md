# TAGLINE

Linux 内核中 IPv4 数据包过滤和 NAT 的管理工具

# TLDR

带行号**查看**链、规则和计数器

```sudo iptables -vnL --line-numbers```

设置链的**策略**规则

```sudo iptables -P [chain] [rule]```

为某个 IP 向链中**追加**规则

```sudo iptables -A [chain] -s [ip_address] -j [rule]```

为 IP 追加带**协议和端口**的规则

```sudo iptables -A [chain] -s [ip_address] -p tcp --dport [port] -j [rule]```

添加 **NAT 伪装（masquerade）**规则

```sudo iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -j MASQUERADE```

按行号**删除**链中的规则

```sudo iptables -D [chain] [rule_line_number]```

**清空**所有规则

```sudo iptables -F```

# SYNOPSIS

**iptables** [_-t table_] _command_ [_chain_] [_options_] [_-j target_]

# DESCRIPTION

**iptables** 是 Linux 内核防火墙（netfilter）中 IPv4 数据包过滤和 NAT 的管理工具。它允许配置表、链和规则以控制网络流量。

# PARAMETERS

**-L, --list**
> 列出所选链中的所有规则

**-A, --append chain**
> 将规则追加到链

**-D, --delete chain**
> 从链中删除规则

**-I, --insert chain [rulenum]**
> 在链中的指定位置插入规则（默认位置 1）

**-P, --policy chain target**
> 设置链的默认策略

**-F, --flush**
> 清空所有规则

**-N, --new-chain chain**
> 创建新的用户自定义链

**-X, --delete-chain [chain]**
> 删除用户自定义链（必须为空）

**-E, --rename-chain old new**
> 重命名用户自定义链

**-t, --table table**
> 指定表（filter、nat、mangle、raw、security）

**-s, --source address**
> 源地址规格

**-d, --destination address**
> 目标地址规格

**-p, --protocol protocol**
> 协议（tcp、udp、icmp、all）

**--dport port**
> 目标端口

**--sport port**
> 源端口

**-j, --jump target**
> 规则的目标动作（ACCEPT、DROP、REJECT、MASQUERADE 等）

**-v, --verbose**
> 详细输出

**-n, --numeric**
> 数字形式输出（不解析名称）

**-x, --exact**
> 展开数字（显示精确的包计数器和字节计数器）

**-i, --in-interface name**
> 入站接口名称

**-o, --out-interface name**
> 出站接口名称

**-m, --match match**
> 加载扩展匹配模块（如 state、conntrack、multiport）

**--line-numbers**
> 显示行号

# CAVEATS

默认情况下规则不会持久保留；要持久化请使用 **iptables-save** 和 **iptables-restore**。IPv6 流量请使用 **ip6tables**。现代系统可能改用 **nftables**。

# HISTORY

属于 **netfilter** 项目。在 **Linux 2.4**（2001 年）中引入，用于取代 ipchains。目前正逐渐被 **nftables** 取代。

# INSTALL

```pacman: sudo pacman -S iptables```

```apk: sudo apk add iptables```

```zypper: sudo zypper install iptables```

```brew: brew install iptables```

```nix: nix profile install nixpkgs#iptables```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip6tables](/man/ip6tables)(8), [iptables-save](/man/iptables-save)(8), [iptables-restore](/man/iptables-restore)(8), [nft](/man/nft)(8), [firewall-cmd](/man/firewall-cmd)(1), [ufw](/man/ufw)(8)
