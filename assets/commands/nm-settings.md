# TAGLINE

描述 NetworkManager 连接可用的属性

# TLDR

**查看连接设置**

```nmcli connection show [connection_name]```

**设置 IPv4 地址**

```nmcli connection modify [conn] ipv4.addresses "[192.168.1.10/24]"```

**设置 DNS 服务器**

```nmcli connection modify [conn] ipv4.dns "[8.8.8.8 8.8.4.4]"```

**设置网关**

```nmcli connection modify [conn] ipv4.gateway "[192.168.1.1]"```

**设置为静态 IP**

```nmcli connection modify [conn] ipv4.method manual```

# SYNOPSIS

**nm-settings** - NetworkManager 连接设置参考

# PARAMETERS

**connection.id**
> 连接名称。

**connection.type**
> 连接类型。

**ipv4.method**
> auto、manual、disabled。

**ipv4.addresses**
> IP 地址。

**ipv4.dns**
> DNS 服务器。

**802-11-wireless.ssid**
> WiFi 网络名称。

# DESCRIPTION

**nm-settings** 描述 NetworkManager 连接可用的属性。这些设置可通过 nmcli、nm-connection-editor 配置，也可直接写在 keyfile 中。

设置按类别组织（connection、ipv4、ipv6、wifi 等）。

# COMMON SETTINGS

```
connection.autoconnect=yes
ipv4.method=auto|manual
ipv4.addresses=192.168.1.10/24
ipv4.gateway=192.168.1.1
ipv4.dns=8.8.8.8
802-11-wireless.ssid=MyNetwork
```

# KEYFILE FORMAT

```ini
# /etc/NetworkManager/system-connections/MyConn.nmconnection
[connection]
id=MyConn
type=ethernet

[ipv4]
method=manual
addresses=192.168.1.10/24
gateway=192.168.1.1
dns=8.8.8.8;
```

# CAVEATS

设置的名称因连接类型而异。某些设置要求特定的类型。keyfile 格式与 D-Bus 名称不同。

# SEE ALSO

[nmcli](/man/nmcli)(1), [nm-connection-editor](/man/nm-connection-editor)(1), [NetworkManager.conf](/man/NetworkManager.conf)(5)
