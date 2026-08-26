# TAGLINE

计算并校验 BLAKE3 加密校验和。

# TLDR

**计算** BLAKE3 校验和

```b3sum [file]```

**校验**校验和

```b3sum -c [checksums.b3]```

从 **stdin** 计算

```echo "data" | b3sum```

**多个文件**

```b3sum [file1] [file2] [file3]```

生成**带密钥的哈希**（从 stdin 读取 32 字节密钥）

```b3sum --keyed [file] < [keyfile]```

从上下文字符串**派生密钥**

```b3sum --derive-key "[app 2026-06-19 context]" [file]```

# SYNOPSIS

**b3sum** [_options_] [_file_...]

# DESCRIPTION

**b3sum** 计算 BLAKE3 加密校验和。BLAKE3 明显快于 BLAKE2、MD5、SHA-1 和 SHA-2，同时保持很高的安全性。它针对并行化做了优化，能够充分利用现代 CPU 的能力。

该工具提供与 md5sum 和 sha256sum 类似的接口，但性能要好得多。

# PARAMETERS

**-c**, **--check**
> 从文件读取 BLAKE3 校验和并进行校验。

**--keyed**
> 带密钥哈希模式；从 stdin 读取 32 字节密钥。

**--derive-key** _context_
> 密钥派生模式，使用给定的上下文字符串。

**-l**, **--length** _bytes_
> 十六进制编码之前的输出长度（字节）（默认：32）。

**--seek** _offset_
> 从给定的字节偏移开始输出（默认：0）。

**--num-threads** _n_
> 可使用的最大线程数。

**--no-mmap**
> 禁用对输入文件的内存映射。

**--no-names**
> 省略文件名，仅输出哈希值。

**--raw**
> 将原始哈希字节而不是十六进制写入 stdout（仅限单个输入）。

**--tag**
> 输出 BSD 风格的校验和行。

**--quiet**
> 校验时，不为每个成功校验的文件打印 OK。

# FEATURES

- 极快（每秒可达数 GB）
- 并行处理
- 输出长度不受限制
- 用于完整性校验的树形哈希
- 用于身份验证的带密钥模式
- 输出具有确定性

# WORKFLOW

```bash
# Hash files
b3sum *.tar.gz > checksums.b3

# Verify
b3sum -c checksums.b3

# Hash stdin
cat largefile | b3sum

# Use multiple threads
b3sum --num-threads 8 hugefile.bin
```

# CAVEATS

算法相对较新（2020 年）。采用程度不如 SHA-256 广泛。不适合用于密码哈希（请改用 argon2）。需要较新的软件版本。

# HISTORY

**b3sum** 于 **2020** 年随 BLAKE3 规范一同发布，由 Jack O'Connor 和 Samuel Neves 开发，是 BLAKE2 的演进版本，针对速度和并行化做了优化。

# INSTALL

```apt: sudo apt install b3sum```

```dnf: sudo dnf install b3sum```

```pacman: sudo pacman -S b3sum```

```apk: sudo apk add b3sum```

```zypper: sudo zypper install b3sum```

```brew: brew install b3sum```

```nix: nix profile install nixpkgs#b3sum```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[b2sum](/man/b2sum)(1), [sha256sum](/man/sha256sum)(1), [md5sum](/man/md5sum)(1), [xxhsum](/man/xxhsum)(1)

# RESOURCES

```[Source code](https://github.com/BLAKE3-team/BLAKE3)```

```[Documentation](https://github.com/BLAKE3-team/BLAKE3/blob/master/b3sum/README.md)```

<!-- verified: 2026-06-19 -->
