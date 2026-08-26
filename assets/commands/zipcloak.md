# TAGLINE

加密或解密 ZIP 归档

# TLDR

**加密 ZIP 文件**

```zipcloak [archive.zip]```

**解密 ZIP 文件**

```zipcloak -d [archive.zip]```

**加密并输出到新文件**

```zipcloak -O [encrypted.zip] [archive.zip]```

**安静模式**

```zipcloak -q [archive.zip]```

# SYNOPSIS

**zipcloak** [_-d_] [_-O output_] [_options_] _zipfile_

# PARAMETERS

**-d**, **--decrypt**
> 解密归档。

**-O** _FILE_
> 输出到新文件。

**-q**, **--quiet**
> 安静模式。

**-b** _PATH_
> 临时文件路径。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本。

# DESCRIPTION

**zipcloak** 通过添加或移除密码保护来加密或解密 ZIP 归档。加密时会提示输入密码，并对归档内的所有文件应用加密。使用 **-d** 标志解密时，会在验证原始密码后移除加密。

默认情况下，zipcloak 原地修改归档并替换原始文件。**-O** 选项可将加密或解密的结果写入新文件，保持原始归档不变。

zipcloak 使用标准 ZIP 加密（PKZIP），与大多数 ZIP 工具和操作系统广泛兼容。它是 Info-ZIP 工具集的一部分。

# CAVEATS

标准 ZIP 加密（PKZIP/ZipCrypto）以现代标准衡量已被视为较弱，可通过已知明文攻击破解。要更强的加密，考虑使用支持 AES-256 的 **7z**。想保留未加密的原始归档时应使用 **-O** 选项。加密只作用于文件内容；文件名和元数据仍然可见。

# HISTORY

**zipcloak** 是 **Info-ZIP** 工具集的一部分，该工具集最初于 20 世纪 90 年代初开发，是 ZIP 归档格式工具的自由、可移植实现。它提供了一种便捷方式，为现有 ZIP 归档添加或移除密码保护而无需重新创建归档。

# INSTALL

```apt: sudo apt install zip```

```dnf: sudo dnf install zip```

```pacman: sudo pacman -S zip```

```apk: sudo apk add zip```

```zypper: sudo zypper install zip```

```brew: brew install zip```

```nix: nix profile install nixpkgs#zip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zip](/man/zip)(1), [unzip](/man/unzip)(1), [7z](/man/7z)(1), [zipinfo](/man/zipinfo)(1), [zipnote](/man/zipnote)(1)
