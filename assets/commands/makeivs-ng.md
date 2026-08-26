# TAGLINE

生成用于测试 WEP 破解的 IVs 文件

# TLDR

**生成 IVs 文件**

```makeivs-ng -b [00:11:22:33:44:55] -w [key] -o [output.ivs]```

**以指定数量生成**

```makeivs-ng -b [BSSID] -k [128] -n [100000] -w [key] -o [output.ivs]```

**创建用于测试的 IVs**

```makeivs-ng -b [00:11:22:33:44:55] -w [0102030405] -o [test.ivs]```

# SYNOPSIS

**makeivs-ng** [_options_]

# PARAMETERS

**-b** _BSSID_
> 接入点的 BSSID。

**-w** _KEY_
> WEP 密钥。

**-k** _BITS_
> 密钥长度（64/128）。

**-n** _COUNT_
> 要生成的 IV 数量。

**-f** _IV_
> 首个 IV 值。

**-s** _SEED_
> 用于初始化随机数生成器的种子。

**-o** _FILE_
> 输出文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**makeivs-ng** 生成用于测试 WEP 破解的 IVs 文件。它为 aircrack-ng 创建示例数据。

该工具是 aircrack-ng 套件的一部分，用于测试和教学目的。

# CAVEATS

属于安全研究工具。仅限合法用途。是 aircrack-ng 套件的一部分。

# HISTORY

makeivs-ng 是用于无线安全审计与测试的 **aircrack-ng** 套件的组成部分。

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

[aircrack-ng](/man/aircrack-ng)(1), [airodump-ng](/man/airodump-ng)(1), [aireplay-ng](/man/aireplay-ng)(1)
