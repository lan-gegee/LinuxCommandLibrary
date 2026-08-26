# TAGLINE

将当前 iptables IPv4 配置转储到 stdout 或文件

# TLDR

**打印**所有规则

```sudo iptables-save```

打印**特定表**

```sudo iptables-save -t filter```

**保存**到文件

```sudo iptables-save -f /etc/iptables.rules```

# SYNOPSIS

**iptables-save** [_OPTIONS_]

# DESCRIPTION

**iptables-save** 将当前 iptables IPv4 配置转储到 stdout 或文件。输出可通过 iptables-restore 恢复。IPv6 规则请使用 ip6tables-save。

# PARAMETERS

**-t, --table** _table_
> 仅输出指定表的规则（filter、nat、mangle、raw、security）

**-f, --file** _filename_
> 将输出写入文件而非 stdout

**-c, --counters**
> 在输出中包含包计数器和字节计数器

# CAVEATS

此命令只保存 IPv4 规则。IPv6 请使用 ip6tables-save。规则的输出格式适用于 iptables-restore。在繁忙的系统上计数器值会不断变化。

# HISTORY

**iptables-save** 是用于管理 Linux 内核防火墙的 **iptables** 软件包的一部分。

# INSTALL

```pacman: sudo pacman -S iptables```

```apk: sudo apk add iptables```

```zypper: sudo zypper install iptables```

```brew: brew install iptables```

```nix: nix profile install nixpkgs#iptables```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [iptables-restore](/man/iptables-restore)(8), [ip6tables-save](/man/ip6tables-save)(8)
