# TAGLINE

从 ZIP 文件中提取密码哈希

# TLDR

**从 ZIP 提取哈希**

```zip2john [archive.zip] > [hash.txt]```

**提取指定文件**

```zip2john [archive.zip]::[file.txt] > [hash.txt]```

**然后用 John 破解**

```john [hash.txt]```

**显示破解出的密码**

```john --show [hash.txt]```

# SYNOPSIS

**zip2john** [_options_] _archive.zip_ [> _hash.txt_]

# DESCRIPTION

**zip2john** 从 ZIP 文件中提取密码哈希。它为 John the Ripper 准备哈希。

哈希提取适用于加密的 ZIP 文件。同时支持 PKZIP 和 AES 加密。

输出为 John 兼容格式。重定向到文件即可进行破解。

可处理归档中的多个文件。每个文件都会产生一个哈希条目。

与 John the Ripper 配合用于恢复密码。支持字典攻击和暴力破解。

# USAGE WORKFLOW

1. 提取哈希：`zip2john archive.zip > hash.txt`
2. 破解哈希：`john hash.txt`
3. 查看结果：`john --show hash.txt`

# CAVEATS

仅限授权的密码恢复。强密码需要较长时间。是 John the Ripper 工具集的一部分。

# HISTORY

**zip2john** 是 **John the Ripper** 密码破解工具的一部分。它使 ZIP 密码恢复成为可能。

# INSTALL

```dnf: sudo dnf install john```

```pacman: sudo pacman -S john```

```apk: sudo apk add john```

```zypper: sudo zypper install john```

```brew: brew install john```

```nix: nix profile install nixpkgs#john```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[john](/man/john)(1), [rar2john](/man/rar2john)(1), [pdf2john](/man/pdf2john)(1)
