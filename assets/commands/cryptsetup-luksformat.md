# TAGLINE

初始化 LUKS 加密分区

# TLDR

使用**密码短语**初始化 LUKS 卷

```cryptsetup luksFormat [/dev/sdXY]```

使用**密钥文件**初始化 LUKS 卷

```cryptsetup luksFormat [/dev/sdXY] [path/to/keyfile]```

初始化并**设置标签**

```cryptsetup luksFormat --label [label] [/dev/sdXY]```

# SYNOPSIS

**cryptsetup luksFormat** [_options_] _device_ [_keyfile_]

# DESCRIPTION

**cryptsetup luksFormat** 初始化 LUKS（Linux 统一密钥设置）加密分区。它会创建 LUKS 头，并使用密码短语或密钥文件设置初始密钥槽。

LUKS 提供标准化的磁盘加密方案，具有多个密钥槽、安全的密钥管理，并在各发行版之间保持兼容。

# PARAMETERS

**--type** _type_
> LUKS 类型：luks1 或 luks2。默认为 luks2。

**-c**, **--cipher** _cipher_
> 加密算法规范。默认为编译时内置值（通常是 aes-xts-plain64）。

**-s**, **--key-size** _bits_
> 密钥长度（位），必须是 8 的倍数。对于 XTS 模式，卷密钥会在两个加密器之间拆分，因此 512 对应 AES-256。

**-h**, **--hash** _hash_
> LUKS 密钥设置和卷密钥摘要所用的哈希算法。

**-i**, **--iter-time** _ms_
> PBKDF 处理密码短语所花的毫秒数。数值越高，抗暴力破解能力越强。

**--pbkdf** _algo_
> LUKS2 的 PBKDF 算法：pbkdf2、argon2i 或 argon2id（默认）。

**-d**, **--key-file** _file_
> 从文件读取密码短语。用 - 表示从标准输入读取。

**-l**, **--keyfile-size** _bytes_
> 从密钥文件最多读取这么多字节。

**-y**, **--verify-passphrase**
> 要求输入密码短语两次，若两次不一致则失败。

**-q**, **--batch-mode**
> 抑制所有确认询问。适用于脚本场景。

**--use-urandom**, **--use-random**
> 选择生成卷密钥所用的内核随机数源（/dev/urandom 或 /dev/random）。

**--sector-size** _bytes_
> LUKS2 的加密扇区大小：512 到 4096 之间的 2 的幂。

**--label** _label_
> 设置 LUKS2 设备标签。

**--integrity** _algo_
> 使用给定的完整性算法启用认证磁盘加密（仅限 LUKS2）。

# CAVEATS

会销毁分区上的所有数据，且无法撤销。务必先备份数据。LUKS1 兼容性更好；LUKS2 支持更新的特性。需要 root 权限。

# INSTALL

```apt: sudo apt install cryptsetup-bin```

```dnf: sudo dnf install cryptsetup```

```pacman: sudo pacman -S cryptsetup```

```apk: sudo apk add cryptsetup```

```zypper: sudo zypper install cryptsetup```

```nix: nix profile install nixpkgs#cryptsetup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8), [cryptsetup-open](/man/cryptsetup-open)(8), [lsblk](/man/lsblk)(8)
