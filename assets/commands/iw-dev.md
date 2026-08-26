# TAGLINE

iw 的子命令，用于操作无线网络接口

# TLDR

将设备设为**监听模式**（接口必须处于 down 状态）

```sudo iw dev [wlp] set type monitor```

将设备设为**管理模式**（接口必须处于 down 状态）

```sudo iw dev [wlp] set type managed```

设置设备**信道**

```sudo iw dev [wlp] set channel [channel_number]```

以 MHz 为单位设置设备**频率**

```sudo iw dev [wlp] set freq [freq_in_mhz]```

显示所有**站点信息**

```iw dev [wlp] station dump```

创建监听模式的**虚拟接口**

```sudo iw dev [wlp] interface add "[vif_name]" type monitor addr [12:34:56:aa:bb:cc]```

**删除**虚拟接口

```sudo iw dev "[vif_name]" del```

# SYNOPSIS

**iw dev** _interface_ _command_ [_parameters_]

# PARAMETERS

**set type** _MODE_
> 设置接口模式：managed、monitor、ibss、mesh 等

**set channel** _NUM_
> 设置无线信道编号

**set freq** _MHZ_
> 以 MHz 为单位设置无线频率

**station dump**
> 显示已连接站点的信息

**interface add** _NAME_ **type** _MODE_
> 创建虚拟接口

**del**
> 删除接口

**scan**
> 触发网络扫描

# DESCRIPTION

**iw dev** 是 iw 的子命令，用于操作无线网络接口。它控制接口的模式、信道和频率，并管理虚拟接口。

监听模式允许被动抓包。管理模式用于常规客户端连接。在更改模式之前，通常必须先将接口置于 down 状态（ip link set down）。

# CAVEATS

大多数操作需要 root 权限。更改类型之前接口必须处于 down 状态。并非所有无线驱动都支持所有模式。监听模式的能力因硬件而异。

# HISTORY

iw 是已废弃的 wireless-tools（iwconfig、iwlist）的现代替代品。它的开发是为了支持 Linux 内核 2.6.22（**2007 年**）引入的 nl80211/cfg80211 无线栈。

# INSTALL

```apt: sudo apt install iw```

```dnf: sudo dnf install iw```

```pacman: sudo pacman -S iw```

```apk: sudo apk add iw```

```zypper: sudo zypper install iw```

```nix: nix profile install nixpkgs#iw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iw](/man/iw)(8), [ip-link](/man/ip-link)(8), [iwconfig](/man/iwconfig)(8)
