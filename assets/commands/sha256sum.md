# TAGLINE

计算并校验 SHA-256 校验和

# TLDR

**计算文件的 SHA256 校验和**

```sha256sum [file]```

**计算多个文件**的校验和

```sha256sum [file1] [file2]```

**从 stdin 读取**并计算校验和

```echo "text" | sha256sum```

**生成校验和文件**以便日后验证

```sha256sum [file1] [file2] > [checksums.sha256]```

**对照校验和文件校验**文件

```sha256sum -c [checksums.sha256]```

**静默校验**（只显示失败项）

```sha256sum -c --quiet [checksums.sha256]```

# SYNOPSIS

**sha256sum** [_OPTION_]... [_FILE_]...

# PARAMETERS

**-b**, **--binary**
> 以二进制模式读取

**-c**, **--check**
> 从文件读取校验和并进行校验

**-t**, **--text**
> 以文本模式读取（默认）

**--tag**
> 创建 BSD 风格的校验和输出

**-z**, **--zero**
> 用 NUL 而不是换行符结束每个输出行，并禁用文件名转义

**--quiet**
> 不为每个已校验的文件打印 OK

**--status**
> 不输出任何内容，用退出代码表示成功与否

**-w**, **--warn**
> 对格式不正确的校验和行发出警告

**--strict**
> 对格式不正确的校验和行以非零状态退出

**--ignore-missing**
> 校验时不因缺失文件而失败

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**sha256sum** 计算并校验 SHA-256 加密哈希值。SHA-256（安全散列算法 256 位）属于 SHA-2 家族，产生 256 位（32 字节）的哈希值，通常以 64 个十六进制字符表示。

该命令常用于验证文件的完整性和真实性。软件分发者通常在下载旁提供 SHA256 校验和，让用户能够确认文件在传输过程中没有损坏或被篡改。

使用 **-c** 校验文件时，输入文件应包含 sha256sum 输出格式的行：哈希值、两个空格（二进制模式为一个空格加星号），以及文件名。

# CAVEATS

SHA-256 并非为密码哈希设计；该用途请使用 **bcrypt** 或 **argon2**。在 GNU 系统上，二进制模式和文本模式产生相同的校验和。在 macOS 上，等效命令是 **shasum -a 256**。

# HISTORY

SHA-256 由 **NSA** 设计，作为 SHA-2 哈希函数家族的一部分由 **NIST** 于 **2001 年**发布。**sha256sum** 命令被加入 **GNU Coreutils**，用于提供计算这些哈希的标准 Unix 工具。它已成为软件分发验证的重要手段，取代了存在已知弱点的 MD5 和 SHA-1。SHA-256 广泛用于安全领域，包括比特币的工作量证明系统。

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

[md5sum](/man/md5sum)(1), [sha1sum](/man/sha1sum)(1), [sha512sum](/man/sha512sum)(1), [b2sum](/man/b2sum)(1), [cksum](/man/cksum)(1)
