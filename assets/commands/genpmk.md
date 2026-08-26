# TAGLINE

WPA/WPA2 PSK 预计算工具

# TLDR

**生成哈希表**

```genpmk -f [wordlist.txt] -d [hashfile] -s [SSID]```

**显示进度**

```genpmk -f [wordlist.txt] -d [hashfile] -s [SSID] -v```

# SYNOPSIS

**genpmk** [_options_]

# DESCRIPTION

**genpmk** 生成预计算的 WPA/WPA2 PSK 哈希表，供 cowpatty 使用。由于 WPA 密钥推导依赖 SSID 且计算开销大，为常见 SSID 预计算哈希可以大幅加快密码审计速度。

该工具创建的哈希文件可供 cowpatty 在授权的安全测试中进行快速离线攻击。

# PARAMETERS

**-f** _file_
> 字典词表文件。

**-d** _file_
> 输出的哈希表文件。

**-s** _ssid_
> 目标 SSID。

**-v**
> 详细/进度输出。

# CAVEATS

哈希表与特定 SSID 绑定。大型词表会生成很大的哈希文件。仅限授权的安全测试使用。哈希表不能在不同 SSID 之间移植。

# HISTORY

**genpmk** 是 **cowpatty** 工具集的一部分，由 **Joshua Wright** 为 WPA 安全研究而创建。它通过支持预计算来解决 WPA 密钥推导的性能瓶颈。

# INSTALL

```apt: sudo apt install cowpatty```

```dnf: sudo dnf install cowpatty```

```pacman: sudo pacman -S cowpatty```

```nix: nix profile install nixpkgs#cowpatty```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cowpatty](/man/cowpatty)(1), [aircrack-ng](/man/aircrack-ng)(1), [hashcat](/man/hashcat)(1)

# RESOURCES

```[Source code](https://github.com/joswr1ght/cowpatty)```

<!-- verified: 2026-07-15 -->
