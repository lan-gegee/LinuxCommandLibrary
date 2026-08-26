# TAGLINE

从无线抓包文件中移除 WEP 隐匿（cloaking）

# TLDR

**移除隐匿**，按 BSSID 过滤抓包文件

```airdecloak-ng -i [capture.cap] --bssid [00:11:22:33:44:55]```

**按 ESSID 过滤**（网络名称）

```airdecloak-ng -i [capture.cap] --ssid [MyNetwork]```

**为清洗后的数据包指定输出**文件

```airdecloak-ng -i [capture.cap] -o [output.pcap] --bssid [00:11:22:33:44:55]```

**将空数据包视为**可能被隐匿的数据包

```airdecloak-ng -i [capture.cap] --bssid [00:11:22:33:44:55] --null-packets```

# SYNOPSIS

**airdecloak-ng** -i _input_ [--bssid _bssid_ | --ssid _essid_] [_options_]

# DESCRIPTION

**airdecloak-ng** 从无线抓包文件中过滤掉 WEP 隐匿技术产生的数据包。某些接入点通过注入伪造或损坏的数据包来实现隐匿，以干扰 WEP 破解工具。

该工具识别并移除这些隐匿数据包，生成一个更干净的抓包文件，便于更有效地分析或破解。

# PARAMETERS

**-i** _file_
> 输入抓包文件（pcap 格式）。

**-o** _file_
> 存放有效（已清洗）数据包的输出文件。默认：_<src>_-filtered.pcap。

**-c** _file_
> 存放隐匿数据包的输出文件。默认：_<src>_-cloaked.pcap。

**-u** _file_
> 存放未知/被忽略数据包的输出文件。默认：invalid_status.pcap。

**--bssid** _mac_
> 按接入点 MAC 地址过滤。

**--ssid** _essid_
> 按网络 ESSID 过滤。

**--filters** _list_
> 按顺序应用过滤方法（signal、duplicate_sn、duplicate_sn_ap、duplicate_sn_client、consecutive_sn、duplicate_iv、signal_dup_consec_sn）。

**--null-packets**
> 将空数据包视为可能被隐匿的数据包。

**--disable-base-filter**
> 跳过基础过滤逻辑。

**--drop-frag**
> 移除分片数据包。

# CAVEATS

只对来自使用 WEP 隐匿技术的接入点的抓包有用。使用 WPA/WPA2 的现代网络不采用这些隐匿技术。如果隐匿检测过于激进，可能会误删合法数据包。

# HISTORY

**airdecloak-ng** 被加入 aircrack-ng 套件，是为了应对 **2000 年代后期**某些接入点厂商实施的特定 WEP 保护机制。

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

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1)
