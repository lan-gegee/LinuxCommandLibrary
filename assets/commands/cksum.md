# TAGLINE

文件校验和与字节数计算器

# TLDR

**计算文件的校验和**

```cksum [file.txt]```

**计算多个文件的校验和**

```cksum [file1] [file2]```

**从 stdin 计算**

```echo "data" | cksum```

**使用 SHA256 算法**

```cksum --algorithm sha256 [file.txt]```

**从文件验证校验和**

```cksum -c [checksums.txt]```

**以 base64 输出**

```cksum --base64 [file.txt]```

# SYNOPSIS

**cksum** [_option_]... [_file_]...

# DESCRIPTION

**cksum** 为每个指定的文件计算循环冗余校验（CRC）校验和与字节数，若未给出文件则处理标准输入。它是 GNU coreutils 的一部分，常用于在传输或复制后验证文件完整性。

默认情况下，cksum 使用 POSIX 标准的 32 位 CRC 算法。较新版本的 cksum（GNU coreutils 9.0+）通过 **--algorithm** 选项支持包括 MD5、SHA1、SHA256 和 SHA512 在内的更多算法，使其成为各种独立校验和工具的多功能替代品。

输出格式包含校验和值、字节数和文件名。使用 **--check** 选项时，cksum 可以读取之前生成的校验和文件，并验证其中列出的文件未被修改。

# PARAMETERS

**-a**, **--algorithm** _name_
> 选择算法（crc、md5、sha1、sha256、sha512 等）

**-c**, **--check**
> 读取校验和并进行验证

**-l**, **--length** _bits_
> 摘要长度（位）

**--base64**
> 输出 base64 编码的摘要

**--raw**
> 输出原始二进制摘要

**--tag**
> BSD 风格校验和（默认）

**--untagged**
> 反向格式，不含摘要类型

**-z**, **--zero**
> 行结尾用 NUL 而非换行符

**--ignore-missing**
> 校验时不因文件缺失而失败

**--quiet**
> 不为验证通过的文件打印 OK

**--status**
> 安静模式，用退出码表示结果

**-w**, **--warn**
> 对格式错误的校验和行发出警告

# OUTPUT FORMAT

```
checksum byte_count filename
```

# CAVEATS

CRC32 不具备密码学安全性。安全关键的校验请使用 SHA256 或更强的算法。未给出文件或文件为 - 时从 stdin 读取。

# HISTORY

**cksum** 在 **POSIX.2**（1992 年）中被标准化。它是 GNU coreutils 的一部分。用于 SHA/MD5 的 **--algorithm** 选项在 GNU coreutils **9.0**（2021 年）中加入。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[md5sum](/man/md5sum)(1), [sha256sum](/man/sha256sum)(1), [sum](/man/sum)(1)
