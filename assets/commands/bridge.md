# TAGLINE

管理 Linux 网桥设备和 VLAN

# TLDR

**列出**网桥和接口

```bridge link```

显示 **VLAN** 信息

```bridge vlan```

将 VLAN **添加**到端口

```sudo bridge vlan add dev lan0 vid 100 pvid untagged```

从端口**移除** VLAN

```sudo bridge vlan delete dev lan0 vid 100```

**监视**变更

```bridge monitor```

# SYNOPSIS

**bridge** [_OPTIONS_] _OBJECT_ _COMMAND_

# DESCRIPTION

**bridge** 用于查看和操作 Linux 网桥设备及其转发表。它管理网桥端口、VLAN 和 FDB 条目，实现二层交换功能。

# PARAMETERS

**link**
> 列出网桥接口和端口。

**vlan**
> 显示或管理 VLAN 配置。

**fdb**
> 转发数据库（FDB）管理。

**mdb**
> 组播组数据库管理。

**monitor**
> 监视网桥配置的变化。

**add**
> 添加 VLAN 或 FDB 条目。

**delete**
> 移除 VLAN 或 FDB 条目。

**vid** _vlan-id_
> VLAN 标识符（1-4094）。

**pvid**
> 设为端口 VLAN ID。

**tagged/untagged**
> VLAN 打标签模式。

# CAVEATS

使用 VLAN 需要在网桥上启用 VLAN 过滤。更改可能中断现有连接。修改操作需要 root 权限。

# HISTORY

**bridge** 是 **iproute2** 的一部分，提供 Linux 网桥管理功能，是对 brctl 的补充。

# INSTALL

```apt: sudo apt install iproute2```

```pacman: sudo pacman -S iproute2```

```apk: sudo apk add iproute2```

```zypper: sudo zypper install iproute2```

```brew: brew install iproute2```

```nix: nix profile install nixpkgs#iproute2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [brctl](/man/brctl)(8), [tc](/man/tc)(8)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/network/iproute2/iproute2.git)```

```[Documentation](https://wiki.linuxfoundation.org/networking/iproute2)```

<!-- verified: 2026-06-22 -->
