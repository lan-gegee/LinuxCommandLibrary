# TAGLINE

自动化 WEP 密钥恢复工具

# TLDR

**指定接口**和 buddy 服务器启动

```sudo easside-ng -f [wlan0] -s [buddy_ip]```

**针对特定 BSSID**

```sudo easside-ng -f [wlan0] -s [buddy_ip] -v [00:11:22:33:44:55]```

**锁定特定信道**

```sudo easside-ng -f [wlan0] -s [buddy_ip] -c [6]```

仅**确定 Internet IP**

```sudo easside-ng -f [wlan0] -s [buddy_ip] -n```

# SYNOPSIS

**easside-ng** [_options_] **-f** _interface_ **-s** _buddy_ip_

# PARAMETERS

**-f** _interface_
> 要使用的无线接口（必填）。

**-s** _ip_
> Buddy-ng 服务器 IP 地址（必填）。

**-v** _mac_
> 受害者 BSSID（目标接入点的 MAC 地址）。

**-m** _mac_
> 源 MAC 地址。

**-i** _ip_
> 源 IP 地址。

**-r** _ip_
> 路由器 IP 地址。

**-c** _channel_
> 将网卡锁定到该信道。

**-n**
> 仅确定 Internet IP。

**-h**
> 显示帮助。

# DESCRIPTION

**easside-ng** 是 Aircrack-ng 套件中的一款工具，用于自动化的 WEP 密钥恢复。它与外部的 "buddy" 服务器通信，无需 WEP 密钥即可解密数据包，从而获得网络访问能力。

该工具针对 WEP 加密网络将攻击过程自动化，利用了 WEP 协议的已知漏洞。

# CAVEATS

需要支持监听模式和包注入的无线网卡。WEP 已被弃用且很少使用。仅用于经授权的安全测试。需要在互联网上运行 buddy-ng 服务器。未经适当授权可能违法。

# HISTORY

easside-ng 是 **Aircrack-ng** 套件的一部分，由最初的 Aircrack 项目发展而来。该工具旨在演示 WEP 的漏洞并用于正当的安全测试。对 WEP 的攻击推动了 WPA/WPA2 的普及。

# INSTALL

```apt: sudo apt install aircrack-ng```

```dnf: sudo dnf install aircrack-ng```

```pacman: sudo pacman -S aircrack-ng```

```apk: sudo apk add aircrack-ng```

```zypper: sudo zypper install aircrack-ng```

```brew: brew install aircrack-ng```

```nix: nix profile install nixpkgs#aircrack-ng```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [aireplay-ng](/man/aireplay-ng)(1), [buddy-ng](/man/buddy-ng)(1)
