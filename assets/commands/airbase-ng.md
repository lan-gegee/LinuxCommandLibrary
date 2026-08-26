# TAGLINE

创建基于软件的无线接入点用于渗透测试

# TLDR

**创建**一个虚假接入点

```sudo airbase-ng -e "[FakeSSID]" -c [6] [wlan0mon]```

创建带 **WPA1/TKIP** 的 AP

```sudo airbase-ng -e "[SSID]" -c [6] -z 2 [wlan0mon]```

创建带 **WPA2/CCMP** 的 AP

```sudo airbase-ng -e "[SSID]" -c [6] -Z 4 [wlan0mon]```

响应**所有探测请求**

```sudo airbase-ng -e "[SSID]" -P -c [6] [wlan0mon]```

# SYNOPSIS

**airbase-ng** [_-e essid_] [_-c channel_] [_-a bssid_] [_options_] _interface_

# DESCRIPTION

**airbase-ng** 是 aircrack-ng 套件中的一个工具，用于为渗透测试创建软件接入点。它可以模拟接入点、捕获 WPA 握手、执行中间人攻击以及测试客户端安全性。

该工具会创建可用于路由流量的虚拟接口（at0），从而对已连接的客户端进行网络分析。

# PARAMETERS

**-e** _essid_
> 接入点的 ESSID（网络名称）

**-c** _channel_
> 工作信道

**-a** _bssid_
> 设置接入点的 BSSID（MAC 地址）

**-W** _0|1_
> 设置信标中广播的 WEP 标志（0 = 关，1 = 开；默认 0）

**-z** _type_
> 设置 WPA1 加密套件：1 = WEP40，2 = TKIP，4 = CCMP，5 = WEP104

**-Z** _type_
> 与 **-z** 相同，但针对 WPA2

**-P**
> 响应所有探测请求，包括针对其他 ESSID 的请求

**-C** _seconds_
> 以此间隔启用对被探测 ESSID 的信标广播（与 **-P** 配合使用）

**-v**
> 详细输出

**-F** _prefix_
> 将所有收发的帧写入以此前缀命名的 pcap 文件

**-I** _interval_
> 设置以毫秒为单位的信标间隔

**--caffe-latte**
> Caffe-Latte 攻击模式

**--cfrag**
> 利用分片的 PRGA 攻击

# CAVEATS

仅限经授权的安全测试使用。要求接口处于监听模式。未经许可创建虚假接入点可能违反当地法律。客户端可能连接并暴露其流量。

# HISTORY

**airbase-ng** 是 aircrack-ng 套件的一部分，该套件于 **2000 年代中期**由 aircrack 演化而来。它的开发目的是通过模拟各种接入点场景来测试无线安全。

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

[aircrack-ng](/man/aircrack-ng)(1), [airmon-ng](/man/airmon-ng)(1), [aireplay-ng](/man/aireplay-ng)(1), [airodump-ng](/man/airodump-ng)(1), [airtun-ng](/man/airtun-ng)(1), [airdecap-ng](/man/airdecap-ng)(1)

# RESOURCES

```[Source code](https://github.com/aircrack-ng/aircrack-ng)```

```[Homepage](https://www.aircrack-ng.org/)```

```[Documentation](https://www.aircrack-ng.org/documentation.html)```

<!-- verified: 2026-06-11 -->
