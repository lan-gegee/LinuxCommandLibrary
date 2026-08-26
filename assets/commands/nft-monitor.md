# TAGLINE

实时显示 nftables 防火墙配置的变化

# TLDR

监控**所有 nftables 事件**

```sudo nft monitor```

仅监控**规则更新**（添加、删除、替换）

```sudo nft monitor rules```

监控**集合及其元素**的更新

```sudo nft monitor sets```

监控事件并输出 **JSON 格式**

```sudo nft -j monitor```

# SYNOPSIS

**nft monitor** [_object_]

# PARAMETERS

**rules**
> 仅监控规则变化

**sets**
> 仅监控集合及元素变化

**tables**
> 仅监控表变化

**chains**
> 仅监控链变化

**-j, --json**
> 以 JSON 格式输出事件

# DESCRIPTION

**nft monitor** 实时显示 nftables 防火墙配置的变化。它订阅 netlink 通知，在规则、集合、链或表被添加、修改或删除时予以显示。

事件一旦发生就会展示，并给出可以重现该更改的确切 nftables 命令。这对调试防火墙行为、审计变更或了解其他工具如何修改防火墙非常有用。

不带过滤参数时，将显示所有 nftables 事件。指定对象类型（rules、sets 等）可将输出过滤为仅显示相应变化。

# CAVEATS

访问 netlink 通知需要 root 权限。监控会持续运行，直到用 **Ctrl+C** 中断。高频变化（如连接跟踪更新）可能产生大量输出。只显示监控期间发生的更改。

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

[nft](/man/nft)(8), [iptables](/man/iptables)(8), [conntrack](/man/conntrack)(8)
