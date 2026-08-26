# TAGLINE

为加密 WiFi 流量创建虚拟隧道接口

# TLDR

**创建**虚拟隧道接口

```sudo airtun-ng -a [AP_BSSID] [wlan0mon]```

用 **WEP 密钥**创建隧道

```sudo airtun-ng -a [AP_BSSID] -w [hex_key] [wlan0mon]```

用 **WPA 口令**创建隧道

```sudo airtun-ng -a [AP_BSSID] -p [passphrase] -e [SSID] [wlan0mon]```

双向隧道（**收发兼备**）

```sudo airtun-ng -a [AP_BSSID] -w [hex_key] -b [wlan0mon]```

# SYNOPSIS

**airtun-ng** [_-a bssid_] [_-w wep_key_] [_-p wpa_pass -e essid_] [_options_] _interface_

# DESCRIPTION

**airtun-ng** 创建虚拟隧道接口（at0、at1 等），允许与无线网络之间收发已解密的流量。这样，当你知道密钥时，就可以在加密 WiFi 网络上使用标准网络工具。

该工具可在 WEP 或 WPA 模式下工作，创建一个透明处理加密/解密的虚拟以太网接口。

# PARAMETERS

**-a** _bssid_
> 接入点 MAC 地址

**-w** _key_
> 十六进制形式的 WEP 密钥（加密发出的数据包）

**-y** _file_
> 从文件读取 PRGA（密钥流）而不是 WEP 密钥

**-p** _passphrase_
> WPA 口令（解密数据包；与 **-a** 和 **-e** 配合使用）

**-e** _essid_
> 网络名称（WPA 必需）

**-i** _iface_
> 从这个附加接口捕获数据包

**-t** _tods_
> 帧目的地：0 = 发往客户端，1 = 发往 AP，2 = WDS/桥接

**-b**
> 双向模式（收发兼备）

**-r** _file_
> 从 pcap 文件读取待注入的帧

**-h** _mac_
> 源 MAC 地址

# CAVEATS

仅限经授权的测试使用。接口必须处于监听模式。WPA 模式要求已完成四次握手。虚拟接口创建后还需进行配置（IP 等）。

# HISTORY

**airtun-ng** 被加入 aircrack-ng 套件，是为了支持后渗透场景：利用已获取的密钥，通过标准工具与目标网络交互。

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

[aircrack-ng](/man/aircrack-ng)(1), [airbase-ng](/man/airbase-ng)(1), [airdecap-ng](/man/airdecap-ng)(1), [airodump-ng](/man/airodump-ng)(1), [aireplay-ng](/man/aireplay-ng)(1)

# RESOURCES

```[Source code](https://github.com/aircrack-ng/aircrack-ng)```

```[Homepage](https://www.aircrack-ng.org/)```

```[Documentation](https://www.aircrack-ng.org/documentation.html)```

<!-- verified: 2026-06-11 -->
