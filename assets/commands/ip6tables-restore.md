# TAGLINE

从文件恢复 IPv6 防火墙规则

# TLDR

此命令是 IPv6 防火墙场景下 **iptables-restore** 的别名

```tldr iptables-restore```

# SYNOPSIS

**ip6tables-restore** [_options_] [_file_]

# DESCRIPTION

**ip6tables-restore** 恢复之前由 **ip6tables-save** 保存的 IPv6 防火墙规则。它在功能上与 **iptables-restore** 完全相同，只是作用于 IPv6 的 **ip6tables** 规则集而非 IPv4 的 **iptables** 规则集。

# INSTALL

```pacman: sudo pacman -S iptables```

```apk: sudo apk add iptables```

```zypper: sudo zypper install iptables```

```brew: brew install iptables```

```nix: nix profile install nixpkgs#iptables```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables-restore](/man/iptables-restore)(8), [ip6tables](/man/ip6tables)(8), [ip6tables-save](/man/ip6tables-save)(8), [iptables](/man/iptables)(8)
