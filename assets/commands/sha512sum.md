# TAGLINE

计算并校验 SHA-512 校验和

# TLDR

**计算文件的 SHA512 校验和**

```sha512sum [path/to/file]```

**计算多个文件的校验和**

```sha512sum [file1] [file2] [file3]```

**计算校验和并保存**到文件

```sha512sum [*.iso] > [checksums.sha512]```

**从文件校验校验和**

```sha512sum -c [checksums.sha512]```

**静默校验**（只显示失败项）

```sha512sum -c --quiet [checksums.sha512]```

**从 stdin 读取**

```echo -n "[text]" | sha512sum```

# SYNOPSIS

**sha512sum** [_OPTION_]... [_FILE_]...

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

**sha512sum** 按 FIPS-180-2 的描述计算并校验 SHA512（512 位）消息摘要。它为文件内容生成 128 个十六进制字符的哈希，提供强大的完整性验证。

不带 FILE 参数或 FILE 为 **-** 时，sha512sum 从标准输入读取。输出格式为：校验和、空格、模式指示符（二进制为 *，文本为空格）以及文件名。

SHA512 比 SHA1 或 MD5 提供更强的安全性，适合加密应用。在 GNU 系统上，二进制模式和文本模式没有区别。

# CAVEATS

与 SHA256（64 字符）或 SHA1（40 字符）相比，SHA512 生成的哈希明显更长（128 个十六进制字符）。虽然更安全，但在处理大量文件时校验速度可能比较弱的算法慢。

# HISTORY

sha512sum 属于 **GNU coreutils**，由 Ulrich Drepper、Scott Miller 和 David Madore 编写。SHA-512 由 NIST 于 **2001 年**作为 SHA-2 家族的一部分发布，旨在取代老旧的 SHA-1 算法。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils-sha512sum```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sha256sum](/man/sha256sum)(1), [sha384sum](/man/sha384sum)(1), [sha224sum](/man/sha224sum)(1), [sha1sum](/man/sha1sum)(1), [md5sum](/man/md5sum)(1), [b2sum](/man/b2sum)(1), [shasum](/man/shasum)(1)
