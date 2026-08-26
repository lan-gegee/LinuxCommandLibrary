# TAGLINE

网络连接跟踪管理

# TLDR

**列出**所有连接

```conntrack -L```

显示**实时**事件

```conntrack -E```

带**时间戳**的事件

```conntrack -E -o timestamp```

特定 **IP** 的事件

```conntrack -E -s ip_address```

按源 IP **删除**流

```conntrack -D -s ip_address```

# SYNOPSIS

**conntrack** [_OPTIONS_]

# DESCRIPTION

**conntrack** 与 Linux 内核的连接跟踪系统（conntrack）交互。它可以查看、搜索和修改供有状态防火墙使用的被跟踪网络连接。

# PARAMETERS

**-L, --dump**
> 列出当前所有被跟踪的连接

**-E, --event**
> 显示实时连接事件

**-D, --delete**
> 删除符合条件的连接

**-U, --update**
> 更新符合条件的连接

**-s, --orig-src** _address_
> 按原始源地址过滤

**-d, --orig-dst** _address_
> 按原始目标地址过滤

**-p, --proto** _protocol_
> 按协议过滤（tcp、udp、icmp）

**-o, --output** _type_
> 输出格式（extended、timestamp、xml）

**--src-nat**
> 过滤 SNAT 连接

**--dst-nat**
> 过滤 DNAT 连接

# CAVEATS

需要 root 权限以及 nf_conntrack 内核模块。删除连接可能中断活动的会话。高流量系统中可能存在数千条被跟踪的连接。

# HISTORY

**conntrack** 是 **conntrack-tools** 软件包的一部分，该软件包用于管理 Linux 连接跟踪系统。

# INSTALL

```apt: sudo apt install conntrack```

```dnf: sudo dnf install conntrack-tools```

```pacman: sudo pacman -S conntrack-tools```

```apk: sudo apk add conntrack-tools```

```zypper: sudo zypper install conntrack-tools```

```nix: nix profile install nixpkgs#conntrack-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [nft](/man/nft)(8), [ss](/man/ss)(8)

# RESOURCES

```[Source code](https://git.netfilter.org/conntrack-tools/)```

```[Homepage](https://conntrack-tools.netfilter.org/)```

```[Documentation](https://www.netfilter.org/projects/conntrack-tools/)```

<!-- verified: 2026-06-23 -->
