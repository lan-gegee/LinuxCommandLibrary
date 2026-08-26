# TAGLINE

向无线网络注入数据包用于安全测试

# TLDR

对客户端执行**去认证**攻击

```sudo aireplay-ng -0 [5] -a [AP_BSSID] -c [CLIENT_MAC] [wlan0mon]```

向接入点进行**伪认证**

```sudo aireplay-ng -1 0 -a [AP_BSSID] -e [SSID] [wlan0mon]```

针对 WEP 的 **ARP 重放**攻击

```sudo aireplay-ng -3 -b [AP_BSSID] [wlan0mon]```

交互式地**注入数据包**

```sudo aireplay-ng -2 -b [AP_BSSID] -r [capture.cap] [wlan0mon]```

**分片**攻击

```sudo aireplay-ng -5 -b [AP_BSSID] [wlan0mon]```

# SYNOPSIS

**aireplay-ng** _attack-mode_ [_-a bssid_] [_-c client_] [_-e essid_] [_options_] _interface_

# DESCRIPTION

**aireplay-ng** 是一款面向无线网络的数据包注入工具。它能够生成流量以增加 WEP 破解所需的数据捕获量、迫使客户端断开连接（从而捕获握手），并执行各种无线攻击。

该工具需要一个处于监听模式且具备注入能力的无线接口。

# PARAMETERS

**-0** _count_
> 去认证攻击（0 = 持续不断）

**-1** _delay_
> 伪认证攻击

**-2**
> 交互式数据包重放

**-3**
> ARP 请求重放攻击

**-4**
> KoreK chopchop 攻击

**-5**
> 分片攻击

**-6**
> Caffe-Latte 攻击（从客户端捕获 WEP 密钥）

**-7**
> 面向客户端的分片攻击（cfrag）

**-9**
> 注入测试

**-a** _bssid_
> 接入点 MAC 地址（用于过滤或重放）

**-b** _bssid_
> 接入点 MAC 地址（特定攻击使用，如 ARP 重放和分片攻击）

**-c** _client_
> 目标客户端 MAC

**-e** _essid_
> 目标网络名称

**-h** _mac_
> 源 MAC 地址（你的接口或某个已连接的客户端）

**-x** _pps_
> 每秒注入的数据包数量

**-D**
> 禁用接入点检测（不等待发现接入点）

**-r** _file_
> 从抓包文件读取待注入的数据包

# CAVEATS

仅限经授权的渗透测试使用。需要支持注入的接口。去认证攻击会被 WIDS 检测到。某些攻击仅对 WEP 网络有效。

# HISTORY

**aireplay-ng** 是 aircrack-ng 套件的核心组件之一，于 **2006** 年首次发布。它将各种无线攻击技术整合到了同一个工具中。

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

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [airmon-ng](/man/airmon-ng)(1), [airbase-ng](/man/airbase-ng)(1)

# RESOURCES

```[Source code](https://github.com/aircrack-ng/aircrack-ng)```

```[Homepage](https://www.aircrack-ng.org/)```

```[Documentation](https://www.aircrack-ng.org/documentation.html)```

<!-- verified: 2026-06-11 -->
