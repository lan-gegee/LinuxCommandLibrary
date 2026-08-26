# TAGLINE

以太网网桥帧过滤防火墙

# TLDR

**列出所有规则**

```sudo ebtables -L```

**带行号列出规则**

```sudo ebtables -L --Ln```

**封锁 MAC 地址**

```sudo ebtables -A INPUT -s [00:11:22:33:44:55] -j DROP```

**只允许特定 MAC**

```sudo ebtables -A INPUT -s ! [00:11:22:33:44:55] -j DROP```

**按协议丢弃数据包**

```sudo ebtables -A FORWARD -p IPv4 -j DROP```

**清空所有规则**

```sudo ebtables -F```

**为链设置策略**

```sudo ebtables -P FORWARD DROP```

**将规则保存到文件**

```sudo ebtables-save > [rules.txt]```

# SYNOPSIS

**ebtables** [_options_] [_command_] [_rule_]

# PARAMETERS

**-L**, **--list**
> 列出所有规则。

**-A** _chain_
> 向链追加规则。

**-D** _chain_
> 从链中删除规则。

**-I** _chain_ [_num_]
> 在指定位置插入规则。

**-F** [_chain_]
> 清空规则（全部或特定链）。

**-P** _chain_ _target_
> 设置链策略。

**-p** _protocol_
> 匹配协议（IPv4、IPv6、ARP）。

**-s** _mac_
> 源 MAC 地址。

**-d** _mac_
> 目标 MAC 地址。

**-i** _interface_
> 输入接口。

**-o** _interface_
> 输出接口。

**-j** _target_
> 跳转到目标（ACCEPT、DROP、CONTINUE、RETURN）。

**-t** _table_
> 要操作的表（filter、nat、broute）。默认为 filter。

**--Ln**
> 列出规则时显示行号。

**-N** _chain_
> 创建新的用户自定义链。

**-X** [_chain_]
> 删除一个用户自定义链。

# DESCRIPTION

**ebtables** 在 Linux 网桥的链路层（第 2 层）过滤以太网帧。它基于 MAC 地址、VLAN 标签和以太网协议控制通过网桥的流量，与工作在第 3 层的 iptables 形成互补。

ebtables 使用与 iptables 类似的链（INPUT、OUTPUT、FORWARD）和表（filter、nat、broute）。它是网桥防火墙配置和基于 MAC 的访问控制的关键工具。

# CAVEATS

只作用于经网桥转发的流量。需要内核 bridge-nf 支持。属于遗留工具；现代系统建议使用 nftables 进行统一过滤。IP 层过滤必须与 iptables 配合使用。不进行 save/restore 的话规则不会在重启后保留。

# HISTORY

ebtables 于 **21 世纪初**为 Linux 内核开发，用于为网桥提供以太网帧过滤功能。它的语法仿照 iptables 设计，便于用户上手。该项目现被视为遗留项目，新部署推荐使用 nftables。

# INSTALL

```pacman: sudo pacman -S iptables```

```apk: sudo apk add iptables```

```zypper: sudo zypper install iptables```

```brew: brew install iptables```

```nix: nix profile install nixpkgs#iptables```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [nft](/man/nft)(8), [brctl](/man/brctl)(8), [bridge](/man/bridge)(8)
