# TAGLINE

发送 Wake-on-LAN 魔术包

# TLDR

发送 **WoL** 数据包

```wol [mac_address]```

通过 IP 发送到不同**子网**

```wol -i [ip_address] [mac_address]```

通过主机名发送到不同**子网**

```wol -h [hostname] [mac_address]```

指定**端口**

```wol -p [port_number] [mac_address]```

从**文件**读取

```wol -f [path/to/file]```

**详细**输出

```wol -v [mac_address]```

# SYNOPSIS

**wol** [_OPTIONS_] _MAC_ADDRESS_

# PARAMETERS

**-i, --ipaddr** _IP_
> 发送到指定的 IP 地址

**-h, --host** _HOSTNAME_
> 发送到指定的主机名

**-p, --port** _PORT_
> 使用指定端口

**-f, --file** _FILE_
> 从文件读取地址

**-v, --verbose**
> 详细输出

# DESCRIPTION

**wol** 发送 Wake-on-LAN 魔术包以远程唤醒计算机。目标计算机必须在 BIOS 和网络接口配置中启用 WoL。

魔术包默认在本地网络中广播。对于远程网络，需指定目标的 IP 或主机名。

# CAVEATS

目标机器必须支持并已启用 WoL。没有特殊配置时可能无法跨路由器工作。必须知道目标的 MAC 地址。

# INSTALL

```dnf: sudo dnf install wol```

```pacman: sudo pacman -S wol```

```zypper: sudo zypper install wol```

```nix: nix profile install nixpkgs#wol```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[etherwake](/man/etherwake)(8), [wakeonlan](/man/wakeonlan)(1)
