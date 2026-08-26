# TAGLINE

基于 XDP 的网络数据包过滤

# TLDR

在网卡上**加载**过滤器

```sudo xdp-filter load -p allow -m skb [network_interface]```

**卸载**过滤器

```sudo xdp-filter unload [network_interface]```

**拒绝**目标端口

```sudo xdp-filter port [destination_port]```

拒绝**源 IP**

```sudo xdp-filter ip -m src [source_ip]```

拒绝**源 MAC**

```sudo xdp-filter ether -m src [mac_address]```

显示**统计信息**

```sudo xdp-filter poll -i 10000```

# SYNOPSIS

**xdp-filter** _COMMAND_ [_OPTIONS_]

# PARAMETERS

**load** _INTERFACE_
> 在网络接口上加载过滤器

**unload** _INTERFACE_
> 从网络接口卸载过滤器

**port** _PORT_
> 按端口号过滤

**ip** _ADDRESS_
> 按 IP 地址过滤

**ether** _ADDRESS_
> 按 MAC 地址过滤

**poll**
> 显示统计信息

**-p, --policy** _POLICY_
> 设置默认策略（allow/deny）

**-m, --mode** _MODE_
> 过滤模式（src/dst 表示方向，skb/native 表示 XDP 模式）

**-i, --interval** _MS_
> 轮询间隔，以毫秒为单位

# DESCRIPTION

**xdp-filter** 加载和管理 eBPF XDP（eXpress Data Path）数据包过滤器。它在网络驱动层面、即数据包到达内核网络栈之前提供高性能的数据包过滤。

属于用于管理 XDP 程序的 xdp-tools 工具集的一部分。

# CAVEATS

需要 root 权限。并非所有网卡驱动都支持原生 XDP 模式。过滤器工作在第 2/3 层，而非应用层。

# INSTALL

```apt: sudo apt install xdp-tools```

```dnf: sudo dnf install xdp-tools```

```pacman: sudo pacman -S xdp-tools```

```apk: sudo apk add xdp-tools```

```zypper: sudo zypper install xdp-tools```

```nix: nix profile install nixpkgs#xdp-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iptables](/man/iptables)(8), [nftables](/man/nftables)(8), [tc](/man/tc)(8)
