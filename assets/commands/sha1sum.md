# TAGLINE

计算并校验 SHA-1 校验和

# TLDR

**计算文件的 SHA1 校验和**

```sha1sum [path/to/file]```

**计算多个文件的校验和**

```sha1sum [file1] [file2] [file3]```

**计算校验和并保存**到文件

```sha1sum [*.iso] > [checksums.sha1]```

**从文件校验校验和**

```sha1sum -c [checksums.sha1]```

**静默校验**（只显示失败项）

```sha1sum -c --quiet [checksums.sha1]```

**从 stdin 读取**

```echo -n "[text]" | sha1sum```

# SYNOPSIS

**sha1sum** [_OPTION_]... [_FILE_]...

# PARAMETERS

**-b**, **--binary**
> 以二进制模式读取

**-c**, **--check**
> 从 FILE 中读取校验和并进行校验

**-t**, **--text**
> 以文本模式读取（默认）

**--tag**
> 创建 BSD 风格的校验和输出

**-z**, **--zero**
> 用 NUL 而不是换行符结束每个输出行

**--ignore-missing**
> 校验时不因缺失文件而失败

**--quiet**
> 不为每个成功校验的文件打印 OK

**--status**
> 不输出任何内容；用退出状态表示结果

**--strict**
> 对格式不正确的校验和行以非零状态退出

**-w**, **--warn**
> 对格式不正确的校验和行发出警告

# DESCRIPTION

**sha1sum** 按 FIPS-180-1 的描述计算并校验 SHA1（160 位）消息摘要。它为文件内容生成唯一的 40 字符十六进制哈希，可用于验证文件完整性和检测修改。

不带 FILE 参数或 FILE 为 **-** 时，sha1sum 从标准输入读取。输出格式为：校验和、空格、模式指示符（二进制为 *，文本为空格）以及文件名。

使用 **-c** 校验时，输入应是先前 sha1sum 的输出。每一行都会被校验并报告为 OK 或 FAILED。

# CAVEATS

SHA-1 在密码学上已被攻破，容易受到碰撞攻击。不应再用于数字签名等安全敏感应用。如需更强的安全性，请改用 **sha256sum** 或 **sha512sum**。

# HISTORY

sha1sum 属于 **GNU coreutils**，由 Ulrich Drepper、Scott Miller 和 David Madore 编写。SHA-1 由 NSA 设计，于 **1995 年**由 NIST 发布。**2017 年**碰撞漏洞得到实证，导致其在密码学用途上被弃用。

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

[sha256sum](/man/sha256sum)(1), [sha512sum](/man/sha512sum)(1), [md5sum](/man/md5sum)(1), [cksum](/man/cksum)(1)
