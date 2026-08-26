# TAGLINE

创建和管理用于防火墙规则的 IP 地址集合

# TLDR

**创建**一个空的 IP 集

```ipset create [set_name] hash:ip```

向集合中**添加**一个 IP 地址

```ipset add [set_name] [192.168.1.25]```

从集合中**删除**一个 IP 地址

```ipset del [set_name] [192.168.1.25]```

**销毁**一个 IP 集

```ipset destroy [set_name]```

将 IP 集**保存**到文件

```ipset save [set_name] > [path/to/ip_set]```

**列出**所有 IP 集

```ipset list```

**测试**某个 IP 是否在集合中

```ipset test [set_name] [192.168.1.25]```

从文件**恢复** IP 集

```ipset restore < [path/to/ip_set]```

# SYNOPSIS

**ipset** _command_ [_options_]

# PARAMETERS

**create** _NAME_ _TYPE_
> 创建新的 IP 集（类型：hash:ip、hash:net、hash:ip,port 等）

**add** _NAME_ _ENTRY_
> 向集合添加条目

**del** _NAME_ _ENTRY_
> 从集合移除条目

**destroy** _NAME_
> 删除集合

**list** [_NAME_]
> 列出集合内容

**save** [_NAME_]
> 以可恢复格式输出集合

**restore**
> 从保存的输出恢复集合

**test** _NAME_ _ENTRY_
> 测试条目是否在集合中

**flush** [_NAME_]
> 清空集合中的所有条目

**-exist**
> 添加已存在的条目或删除不存在的条目时不报错

**-quiet**
> 抑制输出

# DESCRIPTION

**ipset** 创建和管理 IP 集——一种用于存储 IP 地址、网络、端口及其组合的框架。iptables/nftables 规则可以引用这些集合，从而高效地匹配大列表。

不同的集合类型支持不同的条目格式：hash:ip 用于单个地址，hash:net 用于 CIDR 段，hash:ip,port 用于地址-端口组合。集合使用哈希表实现 O(1) 的查找性能。

# CAVEATS

需要 root 权限。必须先创建集合才能在防火墙规则中引用。若无显式的保存/恢复操作，集合内容在重启后不会保留。

# HISTORY

ipset 由 Jozsef Kadlecsik 开发，为 Linux 防火墙提供高效的基于集合的匹配。它已成为标准 Linux 网络工具集的一部分，被广泛用于实现黑名单和白名单。

# INSTALL

```apt: sudo apt install ipset```

```dnf: sudo dnf install ipset```

```pacman: sudo pacman -S ipset```

```apk: sudo apk add ipset```

```zypper: sudo zypper install ipset```

```nix: nix profile install nixpkgs#ipset```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [nft](/man/nft)(8), [firewall-cmd](/man/firewall-cmd)(1)
