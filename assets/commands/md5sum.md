# TAGLINE

计算并校验 MD5 消息摘要

# TLDR

**计算文件**的 MD5 哈希值

```md5sum [file]```

**计算多个文件**的哈希值

```md5sum [file1] [file2] [file3]```

**从 stdin 计算哈希值**

```echo "text" | md5sum```

**保存哈希值**到文件

```md5sum [*.iso] > checksums.md5```

**根据校验和验证文件**

```md5sum -c checksums.md5```

**静默验证**（只显示失败的项）

```md5sum -c --quiet checksums.md5```

**仅用状态码**验证

```md5sum -c --status checksums.md5```

**以 BSD 格式输出**

```md5sum --tag [file]```

# SYNOPSIS

**md5sum** [_options_] [_file_...]

# DESCRIPTION

**md5sum** 计算并校验 MD5 消息摘要（校验和）。MD5 生成 128 位哈希值，通常显示为 32 个字符的十六进制数。

该工具常用于在传输后验证文件完整性、检测文件变化以及为内容生成唯一标识符。可以对照先前生成的校验和文件来检查文件。

注意 MD5 在密码学上已被攻破，不应用于安全用途。对安全关键的应用请改用 SHA-256 或更强的算法。

# PARAMETERS

**-c**, **--check**
> 读取校验和并验证文件。

**--quiet**
> 验证通过的文件不打印 OK。

**--status**
> 不输出任何内容，只使用退出状态。

**-w**, **--warn**
> 对格式错误的校验和行发出警告。

**--strict**
> 对格式错误的行以非零值退出。

**--tag**
> 创建 BSD 风格的校验和输出。

**-b**, **--binary**
> 以二进制模式读取文件。

**-t**, **--text**
> 以文本模式读取文件（默认）。

**--ignore-missing**
> 校验时忽略缺失的文件。

# CAVEATS

MD5 在密码学上已被攻破，易受碰撞攻击。不适合安全用途。在某些系统上二进制模式与文本模式的结果不同。空文件的哈希恒为 d41d8cd98f00b204e9800998ecf8427e。

# HISTORY

**md5sum** 是 **GNU coreutils** 的一部分，实现了由 **Ronald Rivest** 于 **1991 年**设计的 MD5 算法。MD5 曾被广泛用于文件校验，直到 **2004-2005 年**密码学缺陷被证实。虽然它仍常用于非安全用途的校验和，但安全应用建议改用 SHA-2 家族的哈希。

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

[sha256sum](/man/sha256sum)(1), [sha1sum](/man/sha1sum)(1), [cksum](/man/cksum)(1), [b2sum](/man/b2sum)(1)
