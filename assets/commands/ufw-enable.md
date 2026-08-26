# TAGLINE

启用 Uncomplicated Firewall 并在开机时加载规则

# TLDR

**重载**并启用 ufw

```sudo ufw enable```

**模拟**启用操作而不实际更改

```sudo ufw --dry-run enable```

# SYNOPSIS

**ufw** [_--dry-run_] **enable**

# PARAMETERS

**enable**
> 启用防火墙、加载已配置的规则，并在开机时激活它们

**--dry-run**
> 显示将要发生的更改但不实际应用

# DESCRIPTION

**ufw enable** 开启 Uncomplicated Firewall：已配置的规则被加载到 netfilter 中，并且该服务会被设置成开机自启。在远程主机上启用之前，先配合 `ufw allow`/`deny`（或应用配置）使用，以免把自己 SSH 锁在外面。

它是 `ufw disable` 的对应操作。启用后，`ufw status` 会报告当前生效的策略和规则。

# CAVEATS

在远程系统上，应**先**放行 SSH（例如 `ufw allow OpenSSH` 或 22 端口）再启用。启用 ufw 会替换或叠加到其他主机防火墙配置上，具体取决于发行版的默认行为。需要 root 或 sudo。

# HISTORY

属于 **ufw**（Uncomplicated Firewall）的一部分，这是源自 Ubuntu 的 iptables/nftables 前端。

# INSTALL

```dnf: sudo dnf install ufw```

```pacman: sudo pacman -S ufw```

```apk: sudo apk add ufw```

```zypper: sudo zypper install ufw```

<!-- packages: 2026-07-28 -->

# SEE ALSO

[ufw](/man/ufw)(8), [ufw-disable](/man/ufw-disable)(8), [iptables](/man/iptables)(8)

# RESOURCES

```[Source code](https://git.launchpad.net/ufw)```

```[Documentation](https://help.ubuntu.com/community/UFW)```

<!-- verified: 2026-07-28 -->
