# TAGLINE

现代 Linux 无线配置工具，取代 iwconfig

# TLDR

**扫描**网络

```iw dev wlan0 scan```

**连接**到开放网络

```iw dev wlan0 connect SSID```

**断开连接**

```iw dev wlan0 disconnect```

显示**连接**信息

```iw dev wlan0 link```

列出**接口**

```iw dev```

列出**能力**

```iw phy```

显示**管制域**

```iw reg get```

# SYNOPSIS

**iw** [_OPTIONS_] _object_ _command_

# DESCRIPTION

**iw** 是现代的 Linux 无线配置工具，取代 iwconfig。它通过 cfg80211/nl80211 接口来配置无线网络接口、扫描网络和管理连接。

# PARAMETERS

**dev** _interface_
> 操作指定接口

**phy** _phyN_
> 操作指定物理设备

**scan**
> 扫描无线网络

**connect** _SSID_
> 连接到开放网络

**disconnect**
> 断开当前网络的连接

**link**
> 显示当前连接状态

**reg get**
> 显示管制域信息

**set** _parameter_ _value_
> 设置接口参数

# CAVEATS

只能处理到开放网络的连接；WPA/WPA2 需使用 wpa_supplicant。部分操作需要 root 权限。取代已废弃的 iwconfig 工具。

# HISTORY

**iw** 是 **iwconfig** 的后继者，为 Linux cfg80211 无线子系统提供了现代接口。

# INSTALL

```apt: sudo apt install iw```

```dnf: sudo dnf install iw```

```pacman: sudo pacman -S iw```

```apk: sudo apk add iw```

```zypper: sudo zypper install iw```

```nix: nix profile install nixpkgs#iw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iwconfig](/man/iwconfig)(8), [wpa_supplicant](/man/wpa_supplicant)(8), [nmcli](/man/nmcli)(1)
