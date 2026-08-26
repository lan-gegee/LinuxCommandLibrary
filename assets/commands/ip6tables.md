# TAGLINE

IPv6 数据包过滤管理工具

# TLDR

**列出**所有规则

```sudo ip6tables -L```

**列出**规则并显示行号

```sudo ip6tables -L --line-numbers```

**放行**端口上的流量

```sudo ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT```

**丢弃**来自某地址的流量

```sudo ip6tables -A INPUT -s 2001:db8::1 -j DROP```

按编号**删除**规则

```sudo ip6tables -D INPUT 1```

**清空**所有规则

```sudo ip6tables -F```

# SYNOPSIS

**ip6tables** [_OPTIONS_] [_chain_] [_rule-specification_]

# DESCRIPTION

**ip6tables** 是 IPv6 数据包过滤管理工具。它的语法和功能与 iptables 相同，只是处理 IPv6 流量。它管理用于过滤、NAT 和数据包修改的规则。

# PARAMETERS

**-L, --list**
> 列出所选链中的所有规则。

**-A, --append**
> 将规则追加到链的末尾。

**-D, --delete**
> 从链中删除一条规则。

**-I, --insert**
> 在指定位置插入规则。

**-R, --replace**
> 替换所选链中的一条规则。

**-F, --flush**
> 清空链（删除链中所有规则）。

**-N, --new-chain**
> 创建用户自定义链。

**-X, --delete-chain**
> 删除用户自定义链。

**-P, --policy**
> 设置链的默认策略（ACCEPT/DROP）。

**-Z, --zero**
> 将包计数器和字节计数器清零。

**-p, --protocol**
> 要匹配的协议（tcp、udp、icmpv6）。

**--dport**
> 目标端口。

**--sport**
> 源端口。

**-s, --source**
> 源地址。

**-d, --destination**
> 目标地址。

**-i, --in-interface**
> 接收数据包的接口。

**-o, --out-interface**
> 发送数据包的接口。

**-j, --jump**
> 目标动作（ACCEPT、DROP、REJECT、LOG 等）。

**-v, --verbose**
> 详细输出（显示计数器和接口）。

**-n, --numeric**
> 直接显示数字形式的地址和端口，而不解析名称。

**--line-numbers**
> 列出时显示规则编号。

# CAVEATS

IPv6 与 IPv4 规则是分开管理的。默认情况下规则不会持久保留——请使用 ip6tables-save/restore。可考虑迁移到 nftables 以统一管理 IPv4/IPv6。

# HISTORY

**ip6tables** 是 **iptables** 的 IPv6 对应物，属于 netfilter 框架的一部分。它正逐渐被 nftables 取代。

# INSTALL

```pacman: sudo pacman -S iptables```

```apk: sudo apk add iptables```

```zypper: sudo zypper install iptables```

```brew: brew install iptables```

```nix: nix profile install nixpkgs#iptables```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [ip6tables-save](/man/ip6tables-save)(8), [nft](/man/nft)(8)
