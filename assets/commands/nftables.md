# TAGLINE

取代 iptables 的现代 Linux 防火墙框架

# TLDR

**列出所有规则**

```sudo nft list ruleset```

**添加表**

```sudo nft add table inet [filter]```

**添加链**

```sudo nft add chain inet [filter] [input] '{ type filter hook input priority 0; }'```

**添加规则**

```sudo nft add rule inet [filter] [input] tcp dport [22] accept```

**删除规则**

```sudo nft delete rule inet [filter] [input] handle [5]```

**从文件加载规则**

```sudo nft -f [/etc/nftables.conf]```

**清空所有规则**

```sudo nft flush ruleset```

# SYNOPSIS

**nft** [_options_] [_commands_]

# PARAMETERS

**list**
> 列出对象。

**add**
> 添加对象。

**delete**
> 删除对象。

**flush**
> 清空对象。

**-f** _file_
> 从文件读取命令。

**-i**
> 交互模式。

**-n**
> 数字输出。

# DESCRIPTION

**nftables** 是取代 iptables 的现代 Linux 防火墙框架。它为 IPv4、IPv6、ARP 和网桥过滤提供单一统一的接口。

nftables 采用全新语法，并在性能和功能上对 iptables 有所改进。

# RULE EXAMPLE

```
table inet filter {
    chain input {
        type filter hook input priority 0;
        ct state established,related accept
        tcp dport 22 accept
        tcp dport 80 accept
        drop
    }
}
```

# CAVEATS

语法与 iptables 不同。它取代 iptables、ip6tables、arptables、ebtables。需要内核支持。

# HISTORY

nftables 由 **Netfilter** 项目开发，主要作者为 **Patrick McHardy** 和 **Pablo Neira Ayuso**，随 Linux 内核 **3.13**（2014 年）发布。

# INSTALL

```dnf: sudo dnf install nftables```

```pacman: sudo pacman -S nftables```

```zypper: sudo zypper install nftables```

```brew: brew install nftables```

```nix: nix profile install nixpkgs#nftables```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [firewalld](/man/firewalld)(1), [ufw](/man/ufw)(8)
