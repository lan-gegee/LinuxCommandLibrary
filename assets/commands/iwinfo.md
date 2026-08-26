# TAGLINE

OpenWrt 中获取无线接口信息的工具

# TLDR

**列出**所有无线接口

```iwinfo```

显示某个接口的**详细信息**

```iwinfo [interface] info```

**扫描**附近的网络

```iwinfo [interface] scan```

列出**已连接设备**

```iwinfo [interface] assoclist```

列出支持的**信道**

```iwinfo [interface] freqlist```

列出可用的**发射功率**级别

```iwinfo [interface] txpowerlist```

# SYNOPSIS

**iwinfo** [_interface_] [_command_]

# PARAMETERS

**info**
> 显示详细的接口信息

**scan**
> 扫描附近的无线网络

**assoclist**
> 列出已关联（连接）的客户端

**freqlist**
> 列出支持的频率/信道

**txpowerlist**
> 列出可用的发射功率级别

**countrylist**
> 列出支持的国家代码

# DESCRIPTION

**iwinfo** 是 OpenWrt 中获取无线接口信息的工具。它提供统一的接口来查询无线驱动的能力和状态，屏蔽了各种无线驱动之间的差异。

该工具显示连接状态、信号强度、加密类型和其他无线参数。它在监控接入点客户端和扫描网络方面特别有用。

# CAVEATS

仅适用于 OpenWrt/LEDE 系统。输出格式可能因无线驱动而异。某些功能需要特定驱动的支持。

# HISTORY

iwinfo 为 OpenWrt 而开发，旨在为路由器固件中使用的不同硬件和驱动提供一致的无线信息接口。

# INSTALL

```aur: yay -S iwinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iw](/man/iw)(8), [uci](/man/uci)(1)
