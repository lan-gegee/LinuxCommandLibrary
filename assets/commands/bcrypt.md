# TAGLINE

使用 Blowfish 加密和解密文件

# TLDR

**加密**文件（生成 file.txt.bfe 并删除原文件）

```bcrypt [file.txt]```

**解密**文件（任何 .bfe 输入都会被解密）

```bcrypt [file.txt.bfe]```

**加密**但保留原文件

```bcrypt -r [file.txt]```

**加密**但不先压缩

```bcrypt -c [file.txt]```

# SYNOPSIS

**bcrypt** [_-orc_] [_-s_ _N_] _file_...

# DESCRIPTION

**bcrypt** 是一款跨平台的文件加密工具，使用 Blowfish 算法。文件用口令短语加密后保存为 **.bfe**（Blowfish Encrypted）扩展名。任何以 .bfe 结尾的文件都被视为已加密并会被解密；所有其他输入文件则被加密。

默认情况下，bcrypt 在加密前先压缩每个输入文件，处理成功后删除输入文件，并且会先用随机数据覆写原文件以阻碍数据恢复。口令短语的长度为 8 到 56 个字符；密钥在内部始终被哈希为 Blowfish 支持的最大长度 448 位。

# PARAMETERS

**-o**
> 将输出打印到标准输出（隐含 **-r**）。

**-r**
> 处理完成后不删除输入文件。

**-c**
> 加密前不压缩文件。

**-s** _N_
> 删除前用随机数据覆写输入文件 _N_ 次（默认 3 次）。

# WORKFLOW

```bash
# Encrypt (creates file.txt.bfe, removes file.txt)
bcrypt file.txt

# Decrypt (restores file.txt)
bcrypt file.txt.bfe

# Encrypt but keep the original
bcrypt -r file.txt
```

# CAVEATS

较老旧的工具，维护有限。运行期间口令短语驻留在内存中。Blowfish 已在很大程度上被 AES 取代，现代需求可考虑 **gpg** 或 **ccrypt**。忘记口令短语将导致数据无法恢复。

# HISTORY

**bcrypt** 由 **Johnny Shelley** 编写，是一款轻量、可移植的文件加密工具。它使用 Paul Kocher 的 Blowfish 算法实现，该算法由 **Bruce Schneier** 于 **1993** 年设计。此文件工具与同名的 **bcrypt** 口令哈希函数无关。

# INSTALL

```dnf: sudo dnf install bcrypt```

```brew: brew install bcrypt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[gpg](/man/gpg)(1), [openssl](/man/openssl)(1), [ccrypt](/man/ccrypt)(1), [age](/man/age)(1)

# RESOURCES

```[Homepage](https://bcrypt.sourceforge.net/)```

<!-- verified: 2026-06-19 -->
