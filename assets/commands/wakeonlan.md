# TAGLINE

发送 Wake-on-LAN 魔术包

# TLDR

**唤醒计算机**

```wakeonlan [00:11:22:33:44:55]```

**指定广播地址唤醒**

```wakeonlan -i [192.168.1.255] [00:11:22:33:44:55]```

**通过特定端口唤醒**

```wakeonlan -p [9] [00:11:22:33:44:55]```

**从文件读取并唤醒**

```wakeonlan -f [hosts.txt]```

输出详细信息

```wakeonlan -v [00:11:22:33:44:55]```

# SYNOPSIS

**wakeonlan** [_-i address_] [_-p port_] [_-f file_] [_options_] _mac_

# PARAMETERS

**-i** _ADDRESS_
> 广播地址。

**-p** _PORT_
> UDP 端口（默认 9）。

**-f** _FILE_
> 从文件读取 MAC 地址。

**-v**
> 输出详细信息。

# DESCRIPTION

**wakeonlan** 发送 Wake-on-LAN（WoL）魔术包，通过网络远程开启计算机。魔术包是一种特殊格式的 UDP 广播，其中目标机器的 MAC 地址重复 16 次，即使系统已关机，网卡也能识别它。

该工具默认向网络广播地址的 UDP 端口 9 发送数据包，可到达本地子网中处于休眠状态的主机。可以指定自定义广播地址以实现跨子网的定向广播，对于配置在端口 7 的系统也可以改用其他端口。

通过从文件读取 MAC 地址（每行一个），可以一次唤醒多台机器。目标计算机必须在 BIOS/UEFI 设置和网卡驱动中启用 WoL 支持，并且必须保持物理连接到网络。

# REQUIREMENTS

- 目标网卡支持 WoL
- BIOS/UEFI 中已启用 WoL
- 操作系统中已启用 WoL
- 计算机已连接到网络

# CAVEATS

仅适用于本地网络（除非经过转发）。需要 BIOS 设置。部分网卡需要配置驱动。

# HISTORY

**Wake-on-LAN** 由 AMD 和 HP 于 **1996 年**开发。wakeonlan 为这一电源管理功能提供了命令行入口。

# INSTALL

```pacman: sudo pacman -S wakeonlan```

```apk: sudo apk add wakeonlan```

```brew: brew install wakeonlan```

```nix: nix profile install nixpkgs#wakeonlan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[etherwake](/man/etherwake)(1), [ethtool](/man/ethtool)(8)
