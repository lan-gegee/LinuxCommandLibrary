# TAGLINE

计算并校验文件校验和

# TLDR

**计算 SHA256 哈希**

```rhash --sha256 [file]```

**计算多种哈希**

```rhash --md5 --sha1 --sha256 [file]```

**计算所有支持的哈希**

```rhash --all [file]```

**从文件校验哈希**

```rhash -c [hashfile.sha256]```

**创建哈希文件**

```rhash --sha256 [file] -o [file.sha256]```

**递归计算所有文件的哈希**

```rhash -r --sha256 [directory]```

**以 BSD 格式输出**

```rhash --bsd --sha256 [file]```

**计算 CRC32**

```rhash --crc32 [file]```

# SYNOPSIS

**rhash** [_--algorithm_] [_-c_] [_-r_] [_-o file_] [_options_] _files_

# PARAMETERS

**-C**, **--crc32**
> 计算 CRC32 校验和。

**-M**, **--md5**
> 计算 MD5 哈希。

**-H**, **--sha1**
> 计算 SHA1 哈希。

**--sha256**
> 计算 SHA-256 哈希。

**--sha512**
> 计算 SHA-512 哈希。

**--sha3-256**
> 计算 SHA3-256 哈希。

**--blake2b**
> 计算 BLAKE2b 哈希。

**-a**, **--all**
> 计算所有支持的哈希。

**--list-hashes**
> 显示支持的哈希函数名称。

**-c**, **--check**
> 从文件校验哈希。

**-u**, **--update** _FILE_
> 向已有的哈希文件中添加新的摘要。

**-k**, **--check-embedded**
> 通过文件名中内嵌的 CRC32 校验文件。

**-B**, **--benchmark**
> 对选定的哈希算法运行基准测试。

**-r**, **--recursive**
> 递归处理目录。

**--follow**
> 递归处理时跟随符号链接。

**-m**, **--message** _TEXT_
> 计算文本消息的哈希而不是文件的哈希。

**-o**, **--output** _FILE_
> 输出到文件。

**--bsd**
> 使用 BSD 输出格式。

**--sfv**
> 使用 SFV 输出格式（默认）。

**--simple**
> 使用简单格式（哈希后跟文件名）。

**-g**, **--magnet**
> 输出磁力链接。

**-e**, **--embed-crc**
> 重命名文件，将 CRC32 嵌入文件名。

**-v**, **--verbose**
> 显示更详细的输出。

**-P**, **--percents**
> 处理过程中显示进度百分比。

**--speed**
> 显示处理速度。

**-p** _FMT_, **--printf** _FMT_
> 使用格式化指令自定义输出格式。

**--template** _FILE_
> 从文件读取输出格式。

**-b**, **--base64**
> 以 Base64 编码输出哈希。

**--hex**
> 以十六进制输出哈希（默认）。

**--uppercase**
> 以大写十六进制输出哈希。

# DESCRIPTION

**rhash**（Recursive Hasher）用于计算和校验文件的消息摘要与校验和。它支持大量哈希算法，包括 CRC32、MD5、SHA 系列、SHA3、BLAKE2、BLAKE3、Tiger、TTH、AICH、ed2k、Whirlpool、GOST 和 RIPEMD-160。

可以在单次遍历中同时计算多个哈希，非常适合生成完整的哈希清单。默认输出格式为带 CRC32 的 SFV，可通过 **--bsd**、**--simple**、**--magnet** 或 **--printf** 更改。

校验模式（-c）会读取哈希文件并核对文件与存储值是否一致，报告不匹配和缺失的文件。更新模式则向已有的哈希文件追加新条目。

磁力链接输出会生成可供 BitTorrent 客户端使用的链接，其中包含文件哈希、大小，还可包含文件名。

--embed-crc 选项会重命名文件，将 CRC32 嵌入文件名中（常见于动漫/视频文件），从而可以一眼检查完整性。

通过 --printf 自定义输出格式便于与其他工具集成。模板使用占位标记表示文件名、哈希、大小等。

# CAVEATS

大文件的哈希计算耗时较长。部分算法（MD5、SHA1）在密码学上已不够安全。并非所有平台都支持全部算法。不同工具的哈希文件格式各不相同。CRC32 不具备抗碰撞性。

# HISTORY

**rhash** 由 **Aleksey Kravchenko** 于 **2005 年**前后创建，是一款快速而全面的哈希计算工具。它以 C 语言编写，注重性能，支持的算法比大多数同类工具更多。该项目持续开发，定期更新以支持新的哈希函数。

# INSTALL

```apt: sudo apt install rhash```

```dnf: sudo dnf install rhash```

```pacman: sudo pacman -S rhash```

```apk: sudo apk add rhash```

```zypper: sudo zypper install rhash```

```brew: brew install rhash```

```nix: nix profile install nixpkgs#rhash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sha256sum](/man/sha256sum)(1), [sha512sum](/man/sha512sum)(1), [sha1sum](/man/sha1sum)(1), [md5sum](/man/md5sum)(1), [shasum](/man/shasum)(1), [cksum](/man/cksum)(1), [b3sum](/man/b3sum)(1)
