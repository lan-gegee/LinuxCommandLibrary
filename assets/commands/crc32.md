# TAGLINE

CRC-32 校验和计算器

# TLDR

**计算文件的 CRC32 校验和**

```crc32 [path/to/file]```

**为多个文件计算**校验和

```crc32 [file1] [file2] [file3]```

**从 stdin 计算校验和**

```echo "[text]" | crc32 /dev/stdin```

**比较两个文件的校验和**

```crc32 [file1] [file2]```

# SYNOPSIS

**crc32** [_file_...]

# PARAMETERS

_FILE_
> 要计算 CRC32 校验和的一个或多个文件。可指定多个文件。

**/dev/stdin**
> 用于从标准输入读取。

# DESCRIPTION

**crc32** 计算文件的 CRC-32 校验和，所使用的多项式与 ZIP 归档、gzip 以及 PNG 文件中的相同。它以 8 位十六进制值的形式输出校验和。

CRC-32（循环冗余校验）是一种哈希函数，主要用于检测数据的意外变动。虽然它不具备密码学安全性，但凭借速度和简洁性的优势，被广泛用于各种文件格式和网络协议的错误检测。

该命令处理在命令行上指定的文件，输出校验和及其对应的文件名。它适用于验证文件完整性、比较文件，以及处理使用 CRC-32 校验和的归档格式或协议。

# CAVEATS

CRC-32 不适合安全用途，因为它很容易被人为操纵。它能检测意外的损坏，但对蓄意修改毫无防护能力。对于安全敏感的应用，请改用 SHA-256 等加密哈希。

# HISTORY

CRC-32 于 **1975 年**首次发表，是以太网协议开发工作的一部分。它采用的特定多项式（IEEE 802.3）成为了最常见的变体。crc32 命令为这一广泛使用的校验和算法提供了便捷的命令行入口。

# INSTALL

```pacman: sudo pacman -S perl-archive-zip```

```apk: sudo apk add perl-archive-zip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cksum](/man/cksum)(1), [md5sum](/man/md5sum)(1), [sha256sum](/man/sha256sum)(1), [sha1sum](/man/sha1sum)(1), [b2sum](/man/b2sum)(1)
