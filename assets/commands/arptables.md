# TAGLINE

管理 ARP 数据包过滤规则。

# TLDR

**列出** ARP 规则

```sudo arptables -L```

**丢弃**来自某 IP 的数据包

```sudo arptables -A INPUT -s 192.168.0.1 -j DROP```

**按编号删除**规则

```sudo arptables -D INPUT rule_number```

**清空**所有规则

```sudo arptables -F```

设置**默认策略**

```sudo arptables -P OUTPUT ACCEPT```

将规则**保存**到文件

```sudo arptables-save > path/to/file```

# SYNOPSIS

**arptables** [_OPTIONS_] _chain_ _rule-specification_

# DESCRIPTION

**arptables** 用于管理 ARP（地址解析协议）数据包过滤规则。它与 iptables 类似，但工作在 ARP 层面，可以控制接受或丢弃哪些 ARP 请求和应答。

# PARAMETERS

**-L, --list**
> 列出所选链或所有链中的全部规则

**-A, --append**
> 将规则追加到链的末尾

**-I, --insert** _chain_ [_rulenum_]
> 在给定位置插入规则（默认：链的顶部）

**-R, --replace** _chain_ _rulenum_
> 按编号替换一条已有规则

**-D, --delete**
> 删除匹配的规则或按编号删除规则

**-F, --flush**
> 清空所有规则

**-Z, --zero**
> 将链中的数据包和字节计数器归零

**-P, --policy**
> 为链设置默认策略

**-N, --new-chain** _name_
> 创建新的用户自定义链

**-X, --delete-chain** [_name_]
> 删除用户自定义链

**-s, --source-ip** _address_
> 匹配源 IP 地址

**-d, --destination-ip** _address_
> 匹配目标 IP 地址

**--source-mac** _address_
> 匹配源 MAC 地址

**--destination-mac** _address_
> 匹配目标 MAC 地址

**-i, --in-interface** _name_
> 匹配入站接口（INPUT、FORWARD）

**-o, --out-interface** _name_
> 匹配出站接口（OUTPUT、FORWARD）

**--opcode** _code_
> 匹配 ARP 操作码（如 Request、Reply）

**-j, --jump** _target_
> 规则的目标动作（ACCEPT、DROP 等）

# CAVEATS

需要 root 权限。在现代系统上使用 nftables 后端。基于 nft 的 **arptables** 只提供 **INPUT** 和 **OUTPUT** 链；**FORWARD** 链仅存在于旧版实现中。ARP 过滤工作在二层/三层的交界处，配置不当可能影响网络连通性。使用 **arptables-save** 和 **arptables-restore** 来持久化和重新加载规则集。

# HISTORY

**arptables** 是 **xtables-nft** 套件的一部分，提供与 netfilter 框架集成的 ARP 数据包过滤。

# INSTALL

```pacman: sudo pacman -S iptables```

```apk: sudo apk add iptables```

```zypper: sudo zypper install iptables```

```brew: brew install iptables```

```nix: nix profile install nixpkgs#iptables```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[iptables](/man/iptables)(8), [nft](/man/nft)(8), [arp](/man/arp)(8), [ebtables](/man/ebtables)(8)

# RESOURCES

```[Source code](https://git.netfilter.org/arptables/)```

```[Homepage](https://www.netfilter.org/)```

```[Documentation](https://man7.org/linux/man-pages/man8/arptables-nft.8.html)```

<!-- verified: 2026-06-16 -->
