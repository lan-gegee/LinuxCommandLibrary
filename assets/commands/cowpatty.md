# TAGLINE

WPA/WPA2 PSK 离线审计工具

# TLDR

对抓包文件进行**字典攻击**

```cowpatty -f [wordlist.txt] -r [capture.cap] -s [SSID]```

**使用预计算的哈希表**

```cowpatty -d [hashfile] -r [capture.cap] -s [SSID]```

**生成哈希表**

```genpmk -f [wordlist.txt] -d [hashfile] -s [SSID]```

**检查单个口令**

```cowpatty -r [capture.cap] -s [SSID] -p "[passphrase]"```

# SYNOPSIS

**cowpatty** [_options_]

# DESCRIPTION

**cowpatty** 是一个 WPA/WPA2 PSK 审计工具，针对捕获的身份验证握手执行离线字典攻击。它用于经授权的无线安全测试。

该工具处理四次握手的抓包数据，并对照捕获的身份验证交换过程逐一测试口令。预计算哈希表可以大幅加快对常见 SSID 的测试速度。

# PARAMETERS

**-f** _file_
> 含候选口令的字典文件。

**-d** _file_
> 预计算哈希表文件。

**-r** _file_
> 数据包抓包文件。

**-s** _ssid_
> 网络 SSID（必需）。

**-p** _pass_
> 要测试的单个口令。

**-c**
> 仅检查是否存在有效握手。

**-v**
> 详细输出。

**-2**
> 使用第 1、2 帧或第 2、3 帧。

# CAVEATS

需要有效的握手抓包数据。仅用于经授权的安全测试。每个网络都需要其 SSID 专属的哈希表。字典攻击的效果受限于字典质量。

# HISTORY

**cowpatty** 由 **Joshua Wright** 于约 **2004** 年创建，用于 WPA 安全研究。它是最早公开的 WPA PSK 审计工具之一，证明了强口令的重要性。该工具影响了 aircrack-ng 等后来的无线安全工具。

# INSTALL

```apt: sudo apt install cowpatty```

```dnf: sudo dnf install cowpatty```

```pacman: sudo pacman -S cowpatty```

```nix: nix profile install nixpkgs#cowpatty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aircrack-ng](/man/aircrack-ng)(1), [genpmk](/man/genpmk)(1), [hashcat](/man/hashcat)(1), [wifite](/man/wifite)(1)

# RESOURCES

```[Source code](https://github.com/joswr1ght/cowpatty)```

<!-- verified: 2026-06-23 -->
