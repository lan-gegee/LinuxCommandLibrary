# TAGLINE

解密 WEP 和 WPA/WPA2 加密的抓包文件

# TLDR

**解密 WEP** 抓包文件

```airdecap-ng -w [hex_key] [capture.cap]```

**解密 WPA/WPA2** 抓包文件

```airdecap-ng -p [passphrase] -e [SSID] [capture.cap]```

**保留 802.11 头部**（不剥离无线头部）

```airdecap-ng -l -w [hex_key] [capture.cap]```

使用 **BSSID 过滤器**解密

```airdecap-ng -p [passphrase] -e [SSID] -b [00:11:22:33:44:55] [capture.cap]```

使用**成对主密钥**（PMK）解密

```airdecap-ng -k [pmk_hex] -e [SSID] [capture.cap]```

# SYNOPSIS

**airdecap-ng** [_-l_] [_-w key_] [_-p pass -e essid_] [_-b bssid_] _capture-file_

# DESCRIPTION

**airdecap-ng** 在你已知密钥的情况下解密 WEP 和 WPA/WPA2 加密的抓包文件。它会生成一个未加密的抓包文件（默认后缀为 **-dec.cap**），可用 Wireshark 等工具进行分析。

默认情况下会剥离 802.11 无线头部，使输出看起来像标准的以太网抓包。使用 **-l** 可保留原始的 802.11 帧。

# PARAMETERS

**-w** _key_
> 十六进制形式的 WEP 密钥

**-p** _passphrase_
> WPA/WPA2 口令

**-e** _essid_
> 网络名称（WPA 必需）

**-b** _bssid_
> 接入点 MAC 地址过滤器

**-l**
> 不从解密输出中移除 802.11 头部（保留无线帧）。

**-k** _pmk_
> 使用指定的 WPA/WPA2 成对主密钥（十六进制）而不是口令。

# CAVEATS

要解密 WPA，你需要口令和 SSID 两者。抓包文件必须包含有效的四次握手，且只有握手成功之后的数据包才会被解密。输出文件默认命名为 _input_-dec.cap。建议使用单个文件名而不是 shell 通配符。

# HISTORY

**airdecap-ng** 是 aircrack-ng 套件的一部分，开发于 **2000 年代中期**。它提供与 aircrack-ng 互补的功能：一旦恢复了密钥，就可以用 airdecap-ng 解密流量以便分析。

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

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [wireshark](/man/wireshark)(1), [tcpdump](/man/tcpdump)(1)
