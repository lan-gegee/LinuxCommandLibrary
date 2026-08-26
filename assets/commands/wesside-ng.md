# TAGLINE

自动化 WEP 密钥破解工具

# TLDR

在接口上**开始自动化 WEP 密钥破解**

```sudo wesside-ng -i [wlan0mon]```

**针对特定网络**（BSSID）

```sudo wesside-ng -i [wlan0mon] -v [00:11:22:33:44:55]```

**指定网络的 IP 地址**

```sudo wesside-ng -i [wlan0mon] -n [192.168.1.0]```

**设置扫描的最大信道**

```sudo wesside-ng -i [wlan0mon] -f [13]```

**只收集 PRGA 而不破解**

```sudo wesside-ng -i [wlan0mon] -c```

# SYNOPSIS

**wesside-ng** **-i** _interface_ [**-v** _bssid_] [**-n** _netip_] [**-m** _myip_] [**-a** _mymac_] [**-c**] [**-p** _minprga_] [**-t** _threshold_] [**-f** _maxchan_]

# PARAMETERS

**-i** _interface_
> 要使用的无线接口（必需）。必须处于监听模式。

**-v** _bssid_
> 目标受害者的 BSSID（接入点的 MAC 地址）。

**-n** _netip_
> 要使用的网络 IP 地址。

**-m** _myip_
> 注入数据包时使用的源 IP 地址。

**-a** _mymac_
> 要使用的源 MAC 地址。

**-c**
> 收集 PRGA 数据但不破解密钥。

**-p** _minprga_
> 要收集的 PRGA（伪随机生成算法）数据的最小字节数。

**-t** _threshold_
> 破解阈值。

**-f** _maxchan_
> 扫描的最高信道。默认为 11。

**-k** _txnum_
> 忽略确认帧并发送 txnum 次。

**-h**
> 显示帮助信息。

# DESCRIPTION

**wesside-ng** 是 Aircrack-ng 套件中的自动化 WEP 密钥破解工具。它在无需人工干预的情况下执行完整的攻击流程：识别网络、建立关联、收集 PRGA 数据、推断 IP 规划、注入 ARP 请求以及破解 WEP 密钥。

该工具利用 WEP 加密的弱点，通过注入数据包产生包含 IV（初始化向量）的流量，这些 IV 是密钥恢复所必需的。它先使用 fragmentation attack 技术获取 PRGA 数据，然后重放 ARP 请求以加速 IV 收集。

wesside-ng 需要一块支持监听模式下数据包注入的无线网卡。运行工具前必须先将接口设为监听模式（通常使用 airmon-ng）。

# CAVEATS

WEP 已经过时，不应再用于无线安全。此工具仅用于经授权的安全测试和教育目的。未经授权访问网络属于违法行为。需要支持注入功能的兼容无线硬件。并非在所有网络或所有硬件上都能可靠工作。

# HISTORY

**wesside-ng** 最初由 **Andrea Bittau** 编写，作为研究论文 "The Fragmentation Attack in Practice" 和 "The Final Nail in WEP's Coffin"（与 Mark Handley、Joshua Lockey 合著）的概念验证。它被并入 **Aircrack-ng** 套件，用以演示 WEP 的实际漏洞。随着网络迁移到 WPA/WPA2/WPA3，该工具的重要性已大幅下降。

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

[aircrack-ng](/man/aircrack-ng)(1), [airmon-ng](/man/airmon-ng)(8), [aireplay-ng](/man/aireplay-ng)(8), [airodump-ng](/man/airodump-ng)(8), [easside-ng](/man/easside-ng)(8)
