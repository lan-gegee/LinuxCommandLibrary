# TAGLINE

nftables 数据包过滤的命令行界面

# TLDR

**列出当前规则集**

```sudo nft list ruleset```

**添加表**

```sudo nft add table inet [filter]```

**添加带钩子的链**

```sudo nft add chain inet [filter] [input] \{ type filter hook input priority 0 \; policy accept \; \}```

**添加接受特定端口的规则**

```sudo nft add rule inet [filter] [input] tcp dport \{ ssh, http, https \} accept```

**按句柄删除规则**

```sudo nft delete rule inet [filter] [input] handle [3]```

**清空所有规则**

```sudo nft flush ruleset```

**将规则集保存到文件**

```sudo nft list ruleset > /etc/nftables.conf```

# SYNOPSIS

**nft** [_OPTIONS_] [_commands_]

# DESCRIPTION

**nft** 是 nftables 的命令行界面。nftables 是现代 Linux 内核数据包过滤框架，以统一的语法和更好的性能取代了 iptables、ip6tables、arptables 和 ebtables。

nftables 采用表、链、规则的层级结构。地址族包括 **inet**（IPv4+IPv6）、**ip**（仅 IPv4）、**ip6**（仅 IPv6）、**bridge**、**arp** 和 **netdev**。规则可以通过 `nft -f /etc/nftables.conf` 从文件加载。

# PARAMETERS

**list ruleset**
> 显示当前完整的规则集

**add table** _family_ _name_
> 创建新表

**add chain** _family_ _table_ _chain_ _specification_
> 创建新链

**add rule** _family_ _table_ _chain_ _statement_
> 向链中添加规则

**delete rule** _family_ _table_ _chain_ **handle** _n_
> 按句柄删除规则

**flush ruleset**
> 移除所有规则和表

**--handle**
> 显示规则的句柄以便删除

**--numeric**
> 显示数字输出（不做名称解析）

# CAVEATS

nftables 语法与 iptables 差别很大。必须先创建表才能创建链，先有链才能添加规则。更改立即生效，但默认不持久——请保存到 /etc/nftables.conf 以实现持久化。

# HISTORY

**nft** 是 **nftables** 项目的组成部分，该项目是 iptables 的后继者，在 Linux 内核中提供统一的数据包分类框架。

# INSTALL

```apt: sudo apt install nftables```

```dnf: sudo dnf install nftables```

```pacman: sudo pacman -S nftables```

```apk: sudo apk add nftables```

```zypper: sudo zypper install nftables```

```brew: brew install nftables```

```nix: nix profile install nixpkgs#nftables```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [firewall-cmd](/man/firewall-cmd)(1)
