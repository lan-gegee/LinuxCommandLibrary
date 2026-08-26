# TAGLINE

Wake-on-LAN 魔术包发送工具

# TLDR

**通过 MAC 地址唤醒计算机**

```sudo etherwake [00:11:22:33:44:55]```

**通过指定网卡唤醒**

```sudo etherwake -i [eth0] [00:11:22:33:44:55]```

**以广播方式唤醒**

```sudo etherwake -b [00:11:22:33:44:55]```

**带密码唤醒**

```sudo etherwake -p [password] [00:11:22:33:44:55]```

**调试模式**

```sudo etherwake -D [00:11:22:33:44:55]```

# SYNOPSIS

**etherwake** [_options_] _mac-address_

# PARAMETERS

**-i** _interface_
> 要使用的网络接口。

**-b**
> 使用广播地址。

**-D**
> 提高调试级别；显示数据包内容（重复使用可查看更多信息）。

**-p** _password_
> SecureOn 密码（6 字节）。

**-V**
> 显示版本。

_mac-address_
> 目标 MAC 地址（XX:XX:XX:XX:XX:XX）。

# DESCRIPTION

**etherwake** 发送 Wake-on-LAN（WoL）魔术包，将计算机从睡眠、休眠或关机状态唤醒。目标计算机必须在 BIOS/UEFI 和网络接口上启用 WoL。

魔术包包含一个同步流，随后是重复 16 次的目标 MAC 地址。当网卡检测到这一模式时，就会发出信号让计算机开机。

# REQUIREMENTS

- 目标必须在 BIOS/UEFI 中启用 WoL
- 网络接口必须支持 WoL
- 目标必须位于同一网段（或使用定向广播）
- 目标网卡在待机时必须保持供电

# CAVEATS

需要 root 权限或 CAP_NET_RAW 能力。仅适用于局域网；跨互联网的 WoL 需要端口转发或 VPN。某些网卡需要特定的驱动配置。无线网络通常不支持 WoL。

# HISTORY

Wake-on-LAN 由 AMD 和惠普于 **1996 年**作为 Advanced Manageability Alliance 的一部分开发。etherwake 是 Linux 上多个 WoL 发送工具实现之一。

# INSTALL

```apt: sudo apt install etherwake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wol](/man/wol)(1), [wakeonlan](/man/wakeonlan)(1), [ethtool](/man/ethtool)(8)

# RESOURCES

```[Documentation](https://manpages.debian.org/etherwake)```

<!-- verified: 2026-07-15 -->
