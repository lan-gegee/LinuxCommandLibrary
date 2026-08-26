# TAGLINE

在网络接口之间中继 PPPoE 流量

# TLDR

**启动 PPPoE 中继**

```pppoe-relay -S [eth0] -C [eth1]```

**跨多个接口中继**

```pppoe-relay -S [eth0] -C [eth1] -C [eth2]```

**在前台运行**

```pppoe-relay -n -S [eth0] -C [eth1]```

# SYNOPSIS

**pppoe-relay** [_options_]

# PARAMETERS

**-S** _INTERFACE_
> 服务器侧接口。

**-C** _INTERFACE_
> 客户端侧接口。

**-n**
> 不派生到后台。

**-i**
> 无可用 AC 时忽略 PADI。

# DESCRIPTION

**pppoe-relay** 在网络接口之间转发 PPPoE 发现包和会话包，充当不同网段上 PPPoE 客户端与接入集中器之间的中继代理。这使一个子网中的客户端能够连接到另一个子网上的 PPPoE 服务器。

该中继同时在服务器侧和客户端侧接口上监听，透明地转发 PPPoE 控制流量和数据流量。可以指定多个客户端接口，让单个接入集中器服务于多个网段。

# CAVEATS

需要多个网络接口。属于特殊用途场景。

# HISTORY

pppoe-relay 提供网段之间的 **PPPoE 数据包中继**功能。

# INSTALL

```apt: sudo apt install pppoe```

```dnf: sudo dnf install rp-pppoe```

```pacman: sudo pacman -S rp-pppoe```

```apk: sudo apk add rp-pppoe```

```zypper: sudo zypper install rp-pppoe```

```nix: nix profile install nixpkgs#rp-pppoe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pppoe](/man/pppoe)(8), [pppoe-server](/man/pppoe-server)(8)
