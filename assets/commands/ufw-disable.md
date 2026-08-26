# TAGLINE

禁用 Uncomplicated Firewall 并卸载规则

# TLDR

**卸载**并禁用 ufw

```sudo ufw disable```

**模拟**禁用操作而不实际更改

```sudo ufw --dry-run disable```

# SYNOPSIS

**ufw** [_--dry-run_] **disable**

# PARAMETERS

**disable**
> 禁用防火墙、卸载规则，并阻止其在开机时加载

**--dry-run**
> 显示将要发生的更改但不实际应用

# DESCRIPTION

**ufw disable** 关闭 Uncomplicated Firewall：当前生效的 netfilter 规则会被卸载，并且在重新用 `ufw enable` 启用之前，防火墙不会在开机时自动启动。

它是 `ufw enable` 的对应操作。如果想预览操作效果，可以先使用 dry-run。禁用后，ufw 强制执行的主机数据包过滤将被移除，直到你重新启用。

# CAVEATS

禁用防火墙后，主机将不再受 ufw 规则保护。其他防火墙工具（firewalld、ufw 之外管理的 nftables）可能仍在生效。需要 root 或 sudo。

# HISTORY

属于 **ufw**（Uncomplicated Firewall）的一部分，这是源自 Ubuntu 的 iptables/nftables 前端。

# INSTALL

```dnf: sudo dnf install ufw```

```pacman: sudo pacman -S ufw```

```apk: sudo apk add ufw```

```zypper: sudo zypper install ufw```

<!-- packages: 2026-07-28 -->

# SEE ALSO

[ufw](/man/ufw)(8), [ufw-enable](/man/ufw-enable)(8), [iptables](/man/iptables)(8)

# RESOURCES

```[Source code](https://git.launchpad.net/ufw)```

```[Documentation](https://help.ubuntu.com/community/UFW)```

<!-- verified: 2026-07-28 -->
