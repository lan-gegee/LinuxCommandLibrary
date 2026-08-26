# TAGLINE

计算并校验 SHA-384 校验和

# TLDR

**计算文件的 SHA-384 哈希**

```sha384sum [file]```

**计算多个文件的 SHA-384 哈希**

```sha384sum [file1] [file2]```

**校验存储在文件中的校验和**

```sha384sum -c [checksums.txt]```

**校验校验和，只显示失败项**

```sha384sum -c --quiet [checksums.txt]```

**从 stdin 读取**

```echo "[text]" | sha384sum```

**生成校验和并保存到文件**

```sha384sum [file] > [checksums.sha384]```

# SYNOPSIS

**sha384sum** [_options_] [_file_...]

# PARAMETERS

**-c**, **--check**
> 从文件校验校验和。

**-b**, **--binary**
> 以二进制模式读取。

**-t**, **--text**
> 以文本模式读取。

**--quiet**
> 不为已校验的文件打印 OK。

**--status**
> 不输出任何内容；用退出状态表示结果（0 = 成功，1 = 失败）。

**--strict**
> 对格式不正确的校验和行以非零状态退出。

**-w**, **--warn**
> 对格式不正确的校验和行发出警告。

**--tag**
> 输出 BSD 风格的校验和。

# DESCRIPTION

**sha384sum** 计算并校验 SHA-384 加密哈希值，产生 384 位（96 个十六进制字符）的消息摘要。它属于 SHA-2 家族，由 SHA-512 截断输出而来，安全强度介于 SHA-256 和 SHA-512 之间。

SHA-384 常用于 TLS/SSL 证书和数字签名等需要比 SHA-256 更强安全性、但又不需要 SHA-512 完整 128 字符输出的场景。不带 FILE 参数或 FILE 为 **-** 时，从标准输入读取。在校验模式（**-c**）下，会将先前生成的校验和与当前文件内容进行比对验证。

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

[sha256sum](/man/sha256sum)(1), [sha512sum](/man/sha512sum)(1), [sha224sum](/man/sha224sum)(1), [sha1sum](/man/sha1sum)(1), [md5sum](/man/md5sum)(1), [b2sum](/man/b2sum)(1)
