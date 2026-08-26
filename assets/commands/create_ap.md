# TAGLINE

WiFi 接入点创建工具

# TLDR

创建无密码的**开放网络**

```create_ap [wlan0] [eth0] [access_point_ssid]```

创建带 **WPA/WPA2 密码**的接入点

```create_ap [wlan0] [eth0] [access_point_ssid] [passphrase]```

创建**不共享互联网**的接入点

```create_ap -n [wlan0] [access_point_ssid] [passphrase]```

创建共享互联网的**桥接网络**

```create_ap -m bridge [wlan0] [eth0] [access_point_ssid] [passphrase]```

使用**预先配置好的桥接**接口

```create_ap -m bridge [wlan0] [br0] [access_point_ssid] [passphrase]```

从**同一块 WiFi 接口**共享互联网

```create_ap [wlan0] [wlan0] [access_point_ssid] [passphrase]```

使用**其他 WiFi 驱动**

```create_ap --driver [wifi_adapter] [wlan0] [eth0] [access_point_ssid] [passphrase]```

# SYNOPSIS

**create_ap** [_options_] _wifi_interface_ [_internet_interface_] [_ssid_] [_passphrase_]

# DESCRIPTION

**create_ap** 使用 hostapd 创建 WiFi 接入点。它会自动处理 hostapd、dnsmasq、iptables 和网络接口的复杂配置，把通常必需的繁琐手动设置抽象掉。

该工具配置 hostapd 来创建接入点，设置 dnsmasq 以提供 DHCP 与 DNS 服务，通过 iptables 建立 NAT 路由（或在指定时改用桥接），并管理网络接口配置。它支持用于共享互联网连接的 NAT 模式（默认）、用于透明网桥的 bridge 模式，以及不共享互联网的隔离模式。

# PARAMETERS

**-n**
> 不共享互联网（隔离接入点）

**-m** _mode_
> 模式：nat（默认）、bridge、none

**--driver** _driver_
> WiFi 驱动（nl80211、rtl871xdrv 等）

**-c** _channel_
> WiFi 信道

**--hidden**
> 隐藏 SSID

**--ieee80211n**
> 启用 802.11n

**--ieee80211ac**
> 启用 802.11ac

# CAVEATS

需要 hostapd 和 dnsmasq。WiFi 网卡必须支持 AP 模式。部分网卡可能因驱动限制而无法工作。需要 root 权限。最初的 create_ap 项目（作者 oblique）已归档且不再维护；目前积极开发的后继者是 **linux-router**（即 lnxrouter 命令），它保持了兼容的命令行接口。

# INSTALL

```aur: yay -S create_ap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hostapd](/man/hostapd)(8), [dnsmasq](/man/dnsmasq)(8), [iw](/man/iw)(8)

# RESOURCES

```[Source code](https://github.com/oblique/create_ap)```

<!-- verified: 2026-06-26 -->
