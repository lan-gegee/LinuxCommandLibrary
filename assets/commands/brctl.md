# TAGLINE

管理以太网网桥接口

# TLDR

**显示**所有网桥

```sudo brctl show```

**创建**网桥

```sudo brctl addbr [bridge]```

**删除**网桥

```sudo brctl delbr [bridge]```

将接口**添加**到网桥

```sudo brctl addif [bridge] [eth0]```

从网桥**移除**接口

```sudo brctl delif [bridge] [eth0]```

在网桥上**启用**生成树协议（STP）

```sudo brctl stp [bridge] on```

# SYNOPSIS

**brctl** _command_ [_bridge_] [_interface_]

# DESCRIPTION

**brctl** 用于管理 Linux 上的以太网网桥接口。网桥在二层连接多个网络段，使它们表现得像单一网络。这常用于虚拟化、容器和网络基础设施场景。

它属于旧版的 **bridge-utils** 软件包，不再添加新功能；现代配置应改用 iproute2 的 **ip link** 和 **bridge** 命令。例如，**brctl addbr br0** 等价于 **ip link add br0 type bridge**，而 **brctl addif br0 eth0** 等价于 **ip link set eth0 master br0**。

# PARAMETERS

**show**
> 显示现有网桥的信息。

**addbr** _bridge_
> 创建新网桥。

**delbr** _bridge_
> 删除网桥。

**addif** _bridge_ _interface_
> 将接口加入网桥。

**delif** _bridge_ _interface_
> 将接口移出网桥。

**stp** _bridge_ _on|off_
> 启用/禁用生成树协议。

**setageing** _bridge_ _time_
> 设置 MAC 地址老化时间。

**setfd** _bridge_ _time_
> 设置转发延迟。

# CAVEATS

brctl 已被弃用，建议使用 iproute2 的 ip 和 bridge 命令。接口必须处于启用（up）状态才能参与桥接。在复杂拓扑中应启用 STP 以防止环路。

# HISTORY

**brctl** 是 **bridge-utils** 软件包的一部分，正被 iproute2 的 bridge 命令取代。

# INSTALL

```apt: sudo apt install bridge-utils```

```dnf: sudo dnf install bridge-utils```

```apk: sudo apk add bridge-utils```

```zypper: sudo zypper install bridge-utils```

```nix: nix profile install nixpkgs#bridge-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bridge](/man/bridge)(8), [ip](/man/ip)(8), [ifconfig](/man/ifconfig)(8), [iptables](/man/iptables)(8)

# RESOURCES

```[Source code](https://kernel.googlesource.com/pub/scm/network/bridge/bridge-utils/)```

```[Documentation](https://www.man7.org/linux/man-pages/man8/brctl.8.html)```

<!-- verified: 2026-06-19 -->
