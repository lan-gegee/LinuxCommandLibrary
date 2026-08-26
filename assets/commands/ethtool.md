# TAGLINE

网络接口配置与诊断工具

# TLDR

显示**设置**

```ethtool eth0```

显示**驱动**信息

```ethtool -i eth0```

显示**特性**

```ethtool -k eth0```

显示**统计信息**

```ethtool -S eth0```

**闪烁** LED

```ethtool -p eth0 10```

设置**速率**和双工模式

```ethtool -s eth0 speed 1000 duplex full autoneg off```

# SYNOPSIS

**ethtool** [_OPTIONS_] _device_

# DESCRIPTION

**ethtool** 显示和修改网络接口控制器（NIC）参数。它对以太网设备设置提供全面控制，让管理员能够查询驱动信息、链路状态和硬件能力，并配置速率、双工模式以及各种卸载（offload）特性等参数。

该工具是网络故障排查、性能调优和硬件诊断的必备利器。它可以启用或禁用校验和卸载、分散-聚集 I/O、分段卸载等影响网络吞吐量和 CPU 占用的特性。

ethtool 直接与网络设备驱动交互，可以暴露标准网络工具无法获取的硬件特定能力和统计信息。

# PARAMETERS

**-i, --driver**
> 显示驱动信息

**-k, --show-features**
> 显示卸载及其他特性

**-K, --features**
> 更改卸载及其他特性

**-S, --statistics**
> 显示 NIC 和驱动统计信息

**-p, --identify** _seconds_
> 让设备 LED 闪烁以便识别

**-s, --change**
> 更改设备设置

**speed** _10|100|1000|10000_
> 设置链路速率，单位 Mbps

**duplex** _half|full_
> 设置双工模式

**autoneg** _on|off_
> 启用/禁用自动协商

# CAVEATS

并非所有驱动都支持所有选项。更改设置可能暂时中断连接。某些设置要求接口处于关闭状态。

# HISTORY

**ethtool** 是检查和调优以太网网络接口的标准 Linux 工具。

# INSTALL

```apt: sudo apt install ethtool```

```dnf: sudo dnf install ethtool```

```pacman: sudo pacman -S ethtool```

```apk: sudo apk add ethtool```

```zypper: sudo zypper install ethtool```

```nix: nix profile install nixpkgs#ethtool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ip](/man/ip)(8), [mii-tool](/man/mii-tool)(8), [tc](/man/tc)(8)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/network/ethtool/ethtool.git/)```

```[Homepage](https://www.kernel.org/pub/software/network/ethtool/)```

<!-- verified: 2026-07-15 -->
