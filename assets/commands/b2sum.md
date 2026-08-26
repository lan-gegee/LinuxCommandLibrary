# TAGLINE

计算并校验 BLAKE2 加密校验和。

# TLDR

**计算** BLAKE2 校验和

```b2sum [file]```

**校验**校验和

```b2sum -c [checksums.b2]```

使用**指定长度**

```b2sum -l [256] [file]```

计算**多个文件**的校验和

```b2sum [file1] [file2] [file3]```

# SYNOPSIS

**b2sum** [_options_] [_file_...]

# DESCRIPTION

**b2sum** 计算并校验 BLAKE2b 加密校验和。BLAKE2 是一种快速、安全的哈希函数，在软件实现中性能优于 MD5、SHA-1 和 SHA-2，同时提供不低于 SHA-3 的安全性。

该工具是 GNU coreutils 的一部分，提供与 md5sum 和 sha256sum 类似的功能。

# PARAMETERS

**-c**, **--check**
> 从文件读取校验和并进行校验。

**-l**, **--length** _bits_
> 摘要长度（位），必须为 8 的倍数（默认：512）。校验时忽略。

**-b**, **--binary**
> 以二进制模式读取。

**-t**, **--text**
> 以文本模式读取（默认）。

**--tag**
> 创建 BSD 风格的校验和行。

**-z**, **--zero**
> 每行输出以 NUL 结尾，而不是换行符。

**--ignore-missing**
> 校验时，不对缺失的文件报错或报告状态。

**--quiet**
> 校验时，不为每个成功校验的文件打印 OK。

**--status**
> 校验时不打印任何内容；仅通过退出码表示结果。

**-w**, **--warn**
> 校验时，对格式不当的校验和行发出警告。

**--strict**
> 校验时，只要出现格式不当的校验和行就以非零状态退出。

# FEATURES

- 性能快
- 可配置输出长度（8 位的倍数）
- 校验模式
- 与 md5sum 和 sha256sum 相同的接口

# WORKFLOW

```bash
# Create checksums
b2sum file1 file2 > checksums.b2

# Verify
b2sum -c checksums.b2

# Use 256-bit digest
b2sum -l 256 file
```

# CAVEATS

支持范围不如 SHA-256 广泛。不同工具可能分别使用 BLAKE2b 或 BLAKE2s。长度参数会影响兼容性。相比 SHA 家族属于较新的算法。

# HISTORY

**b2sum** 在 GNU coreutils **8.26** 版本（2016 年）中加入，在该算法于 **2012** 年发表后提供了 BLAKE2 哈希支持。

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

[sha256sum](/man/sha256sum)(1), [md5sum](/man/md5sum)(1), [b3sum](/man/b3sum)(1), [cksum](/man/cksum)(1)

# RESOURCES

```[Source code](https://github.com/coreutils/coreutils)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html)```

<!-- verified: 2026-06-19 -->
