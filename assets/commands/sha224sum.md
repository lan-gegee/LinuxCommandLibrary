# TAGLINE

计算并校验 SHA-224 校验和

# TLDR

**计算 SHA224 哈希**

```sha224sum [file]```

**从文件校验哈希**

```sha224sum -c [checksums.txt]```

**计算多个文件**

```sha224sum [file1] [file2]```

**从 stdin 读取**

```echo "[text]" | sha224sum```

# SYNOPSIS

**sha224sum** [_options_] [_file_...]

# PARAMETERS

**-c**, **--check**
> 从文件校验校验和。

**-b**, **--binary**
> 以二进制模式读取。

**-t**, **--text**
> 以文本模式读取。

**--quiet**
> 不为已校验的文件打印 OK。

# DESCRIPTION

**sha224sum** 计算并校验 SHA-224 加密哈希值，产生 224 位（56 个十六进制字符）的消息摘要。它是 SHA-2 哈希函数家族的一员，用法与 **sha256sum** 完全相同，区别仅在于输出长度以及对底层哈希的截断方式。

SHA-224 不如 SHA-256 常用，但在更短的哈希更受青睐的场景（例如某些证书签名方案）中可提供足够的安全性。不带 FILE 参数或 FILE 为 **-** 时，从标准输入读取。在校验模式（**-c**）下，会将先前生成的校验和与当前文件内容进行比对验证。

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

[sha256sum](/man/sha256sum)(1), [sha384sum](/man/sha384sum)(1), [sha512sum](/man/sha512sum)(1)
