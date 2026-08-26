# TAGLINE

从 iptables-save 创建的文件恢复 iptables IPv4 规则

# TLDR

从文件**恢复**

```sudo iptables-restore /etc/iptables.rules```

从文件**恢复**但不清空现有规则

```sudo iptables-restore -n /etc/iptables.rules```

**测试**规则而不实际应用

```sudo iptables-restore -t /etc/iptables.rules```

配合 iptables-save 从 stdin **恢复**

```sudo iptables-save | sudo iptables-restore```

# SYNOPSIS

**iptables-restore** [_OPTIONS_] [_file_]

# DESCRIPTION

**iptables-restore** 从 iptables-save 创建的文件恢复 iptables IPv4 规则。IPv6 规则请使用 ip6tables-restore。输入可以来自文件或 stdin。

# PARAMETERS

**-c, --counters**
> 恢复包计数器和字节计数器的值

**-n, --noflush**
> 恢复前不清空现有规则

**-T, --table** _name_
> 仅恢复指定的表

**-t, --test**
> 测试模式——解析规则但不应用

**-v, --verbose**
> 在处理规则集期间输出额外的调试信息

**-w, --wait** [_seconds_]
> 等待 xtables 锁

**-V, --version**
> 输出程序版本号

**-M, --modprobe** _modprobe_
> 指定 modprobe 程序的路径

# CAVEATS

默认情况下，恢复前会清空所有现有规则。使用 -n 可在不清空的情况下追加规则。此命令只恢复 IPv4 规则；IPv6 请使用 ip6tables-restore。

# HISTORY

**iptables-restore** 是用于管理 Linux 内核防火墙的 **iptables** 软件包的一部分。

# INSTALL

```pacman: sudo pacman -S iptables```

```apk: sudo apk add iptables```

```zypper: sudo zypper install iptables```

```brew: brew install iptables```

```nix: nix profile install nixpkgs#iptables```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [iptables-save](/man/iptables-save)(8), [ip6tables-restore](/man/ip6tables-restore)(8)
