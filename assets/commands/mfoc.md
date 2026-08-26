# TAGLINE

破解 MIFARE Classic 卡

# TLDR

**恢复密钥并转储卡内容**

```mfoc -O [output.mfd]```

**尝试额外的候选密钥**（可重复使用）

```mfoc -k [FFFFFFFFFFFF] -O [output.mfd]```

**增加扇区探测次数**

```mfoc -P [50] -O [output.mfd]```

**设置距离容差**（半程；总范围为 2 x NUM）

```mfoc -T [40] -O [output.mfd]```

**显示帮助**

```mfoc -h```

# SYNOPSIS

**mfoc** [**-h**] [**-k** _KEY_]... [**-P** _NUM_] [**-T** _NUM_] [**-O** _FILE_]

# PARAMETERS

**-O** _FILE_
> 将卡内容转储到 FILE（MFD 格式）。

**-k** _KEY_
> 除默认密钥外，首先尝试 KEY（12 个十六进制数字）。可多次指定。

**-P** _NUM_
> 每个扇区最多探测 NUM 次。默认为 20。

**-T** _NUM_
> 将距离容差的半程设为 NUM。默认为 20（总范围 40）。

**-h**
> 显示选项摘要。

# DESCRIPTION

**mfoc** 是 Nethemba 最初提出的"离线嵌套"攻击的开源实现。它利用 MIFARE Classic 卡 Crypto1 密码算法的弱点来恢复扇区认证密钥，然后将完整的卡内容转储到文件中。

至少需要一个已知的扇区密钥（默认密钥或用 **-k** 提供的密钥）；mfoc 以它为起点，通过嵌套认证恢复其余密钥。得到的 .mfd 转储文件可以用 **nfc-mfclassic** 等工具写回空白卡。

# CAVEATS

需要兼容 libnfc 的 NFC 读卡器（如 ACR122U、PN532）。对带有加固随机数（hardened nonce）的 MIFARE Classic 卡（EV1、SL1 模式的 Plus）无效；这类卡请使用 mfcuk 或 mfoc-hardnested。仅限对你拥有的卡进行经授权的安全研究。

# HISTORY

mfoc（MIFARE Classic Offline Cracker）通过 nfc-tools 项目发布，实现了 Nethemba 在 2009 年提出的针对 Crypto1 的嵌套攻击。它通常与 **libnfc** 和 **mfcuk** 一同分发。

# INSTALL

```apt: sudo apt install mfoc```

```pacman: sudo pacman -S mfoc```

```zypper: sudo zypper install mfoc```

```brew: brew install mfoc```

```nix: nix profile install nixpkgs#mfoc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mfterm](/man/mfterm)(1)
