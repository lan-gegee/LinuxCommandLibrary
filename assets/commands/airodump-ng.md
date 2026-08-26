# TAGLINE

捕获无线数据包并发现附近网络

# TLDR

**扫描**所有无线网络

```sudo airodump-ng [wlan0mon]```

在**指定信道**上捕获数据包

```sudo airodump-ng -c [6] --bssid [00:11:22:33:44:55] -w [capture] [wlan0mon]```

只扫描 **5GHz** 网络

```sudo airodump-ng --band a [wlan0mon]```

显示**厂商信息**进行扫描

```sudo airodump-ng --manufacturer [wlan0mon]```

扫描并显示 **WPS** 信息

```sudo airodump-ng --wps [wlan0mon]```

# SYNOPSIS

**airodump-ng** [_-c channel_] [_--bssid mac_] [_-w prefix_] [_--band band_] [_options_] _interface_

# DESCRIPTION

**airodump-ng** 是一款无线数据包捕获和网络发现工具。它实时显示检测到的接入点和客户端，并将数据包捕获到文件中，供之后使用 aircrack-ng 分析。

该工具显示网络名称、加密类型、信号强度、信道、MAC 地址和关联的客户端，是无线侦察的必备工具。

# PARAMETERS

**-c** _channel_
> 锁定到特定信道

**--bssid** _mac_
> 按接入点 MAC 过滤

**-w** _prefix_
> 输出文件前缀（生成 .cap、.csv、.kismet.csv、.kismet.netxml）

**--band** _band_
> 要扫描的频段：a（5GHz）、b 和 g（2.4GHz）。字母可以组合，例如 abg

**-a**
> 过滤掉（隐藏）未关联的客户端

**--encrypt** _suite_
> 按加密方式过滤接入点（如 WEP、WPA、WPA2、OPN）

**--essid** _essid_
> 按 ESSID 过滤接入点

**--write-interval** _seconds_
> 两次文件写入之间的时间间隔

**--manufacturer**
> 显示来自 OUI 的厂商信息

**--wps**
> 显示 WPS 信息

**--output-format** _formats_
> 输出格式：pcap、ivs、csv、gps、kismet、netxml

**-r** _file_
> 从抓包文件读取而不是实时捕获

# CAVEATS

仅限经授权的安全测试使用。需要监听模式的接口。抓包文件可能变得非常大。某些信息要求停留在正确的信道上。

# HISTORY

**airodump-ng** 是 aircrack-ng 套件的核心组件之一，于 **2006** 年首次发布。它取代了最初的 airodump，功能更完善且稳定性更好。

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

[aircrack-ng](/man/aircrack-ng)(1), [aireplay-ng](/man/aireplay-ng)(1), [airmon-ng](/man/airmon-ng)(1), [airodump-ng-oui-update](/man/airodump-ng-oui-update)(1), [wireshark](/man/wireshark)(1)

# RESOURCES

```[Source code](https://github.com/aircrack-ng/aircrack-ng)```

```[Homepage](https://www.aircrack-ng.org/)```

```[Documentation](https://www.aircrack-ng.org/documentation.html)```

<!-- verified: 2026-06-11 -->
