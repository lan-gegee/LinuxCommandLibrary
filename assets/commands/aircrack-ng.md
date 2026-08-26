# TAGLINE

破解 WEP 和 WPA/WPA2 无线加密密钥

# TLDR

使用字典文件**破解 WPA/WPA2**

```aircrack-ng -w [wordlist.txt] [capture.cap]```

用**捕获的 IV** 破解 WEP

```aircrack-ng [capture.cap]```

指定**目标 BSSID**

```aircrack-ng -b [00:11:22:33:44:55] [capture.cap]```

使用**多个字典文件**

```aircrack-ng -w [list1.txt],[list2.txt] [capture.cap]```

显示**破解统计信息**

```aircrack-ng -S [capture.cap]```

# SYNOPSIS

**aircrack-ng** [_-w wordlist_] [_-b bssid_] [_-e essid_] [_options_] _capture-file_

# DESCRIPTION

**aircrack-ng** 是一款 WiFi 安全审计工具，可破解 WEP 和 WPA/WPA2-PSK 加密密钥。对于 WPA/WPA2，它对捕获的四次握手进行字典攻击。对于 WEP，它利用统计方法攻击其密码学弱点。

该工具读取包含无线流量的抓包文件，识别加密类型和捕获到的握手，然后尝试恢复口令。

# PARAMETERS

**-w** _file_
> 用于 WPA/WPA2 破解的字典文件

**-b** _bssid_
> 目标接入点的 MAC 地址

**-e** _essid_
> 目标网络名称

**-a** _mode_
> 攻击模式（1：WEP，2：WPA/WPA2）

**-l** _file_
> 将找到的密钥写入文件

**-q**
> 静默模式（不显示状态）

**-S**
> WPA 破解速度测试（基准测试）

**-p** _threads_
> 要使用的 CPU 线程数

**-K**
> WEP 破解时使用 KoreK 攻击而非 PTW（PTW 是更快的现代默认方式）

**-x**
> 禁用最后一个密钥字节的暴力破解（WEP）。-x1 表示启用（默认），-x2 表示暴力破解最后两个密钥字节

**-y**
> 实验性单一暴力破解攻击，在标准攻击在超过 100 万个 IV 时仍然失败时使用

**-z**
> WEP 破解使用 PTW 攻击（默认）

**-D**, **--wep-decloak**
> WEP decloak 模式，跳过损坏的密钥流

**-M** _num_
> WEP 破解可使用的最大 IV 数量

**-1**, **--oneshot**
> 仅运行一次 PTW 密钥破解尝试

# CAVEATS

仅限经授权的安全测试使用。WPA/WPA2 破解需要捕获到四次握手。成功与否取决于字典文件的质量；复杂密码可能无法破解。对于 WPA，hashcat 等 GPU 加速工具速度更快。

# HISTORY

**aircrack-ng** 由最初的 aircrack 工具演化而来，"-ng"（next generation，下一代）版本于 **2006** 年首次发布。它已成为开源 WiFi 安全评估的标准工具集。

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

[airodump-ng](/man/airodump-ng)(1), [aireplay-ng](/man/aireplay-ng)(1), [hashcat](/man/hashcat)(1)
