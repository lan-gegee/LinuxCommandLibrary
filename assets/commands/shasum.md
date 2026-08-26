# TAGLINE

计算并校验 SHA 消息摘要

# TLDR

**计算 SHA-1 哈希**

```shasum [file]```

**计算 SHA-256 哈希**

```shasum -a 256 [file]```

**计算 SHA-512 哈希**

```shasum -a 512 [file]```

**从文件校验哈希**

```shasum -c [checksums.txt]```

**从 stdin 计算哈希**

```echo -n "[text]" | shasum```

**二进制模式**

```shasum -b [file]```

**为多个文件创建校验和**

```shasum -a 256 [*.tar.gz] > [SHA256SUMS]```

# SYNOPSIS

**shasum** [_-a algorithm_] [_-b_] [_-c_] [_options_] [_files_]

# PARAMETERS

**-a** _ALG_
> 算法（1、224、256、384、512、512224、512256）。

**-b**
> 二进制模式。

**-c**, **--check**
> 从文件校验哈希。

**-t**
> 文本模式（默认）。

**-U**, **--UNIVERSAL**
> 以 Universal Newlines 模式读取（在 Windows/Unix/Mac 上产生相同摘要）。

**-0**, **--01**
> 以 BITS 模式读取（ASCII '0' 解释为 0 位，'1' 解释为 1 位）。

**-s**, **--status**
> 仅返回状态，不输出任何内容（配合 -c 使用）。

**--ignore-missing**
> 不因缺失文件而失败或报告状态（配合 -c 使用）。

**-q**, **--quiet**
> 不为每个成功校验的文件打印 OK（配合 -c 使用）。

**-w**, **--warn**
> 对格式不正确的校验和行发出警告。

**--strict**
> 对格式不正确的行以非零状态退出。

**--tag**
> BSD 风格输出，包含算法名称。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**shasum** 是一个统一的基于 Perl 的工具，用于计算和校验所有算法变体的 SHA 消息摘要。**-a** 选项选择算法：SHA-1（默认）、SHA-224、SHA-256、SHA-384、SHA-512，以及截断变体 SHA-512/224 和 SHA-512/256。SHA-256 最常用于软件分发验证和安全应用。

在校验模式（**-c**）下，shasum 读取包含先前生成校验和的文件，将每个列出的文件与其记录的哈希比对，并报告成功或失败。输出格式为哈希值加文件名，BSD 风格输出（**--tag**）还会额外包含算法名称。两种格式在校验时均可识别。

此命令是 macOS 以及安装了 Perl 的系统上的标准 SHA 工具，提供与 GNU coreutils 中独立的 **sha1sum**、**sha256sum** 和 **sha512sum** 命令等效的功能。

# CAVEATS

SHA-1 的密码学强度已被削弱——安全用途请使用 SHA-256 及以上。哈希验证要求原始哈希本身可信。

# HISTORY

**shasum** 是随 Perl 附带的 Perl 脚本。它提供 SHA 算法的统一接口，功能与 sha256sum 等类似 coreutils 程序一致。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl-utils```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sha1sum](/man/sha1sum)(1), [sha256sum](/man/sha256sum)(1), [md5sum](/man/md5sum)(1), [openssl](/man/openssl)(1), [b2sum](/man/b2sum)(1)
