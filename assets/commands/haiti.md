# TAGLINE

命令行哈希类型识别工具

# TLDR

**识别哈希的类型**

```haiti [hash_string]```

**识别哈希类型**并包含加盐变体在内的扩展算法

```haiti -e [hash_string]```

**从标准输入识别哈希**

```echo "[hash_string]" | haiti -```

**显示简短输出**，不带 hashcat/john 参考

```haiti --short [hash_string]```

**禁用彩色输出**

```haiti --no-color [hash_string]```

# SYNOPSIS

**haiti** [**-e**|**--extended**] [**--short**] [**--no-color**] _hash_

# PARAMETERS

**-e**, **--extended**
> 列出所有可能的哈希算法，包括使用盐值的算法

**--short**
> 以简短格式显示，不带 hashcat 和 John the Ripper 参考

**--no-color**
> 禁用彩色输出

**--hashcat-only**
> 只显示 hashcat 参考

**--john-only**
> 只显示 John the Ripper 参考

**-h**, **--help**
> 打印帮助信息

**-V**, **--version**
> 打印版本号

# DESCRIPTION

**HAITI**（HAsh IdenTifIer）是一款用于识别给定哈希类型的命令行工具和库。它可检测超过 **675 种哈希类型**，包括 SHA3、Keccak、Blake2 等现代算法以及众多应用专用格式。对于每种识别出的哈希类型，它会提供对应的 **Hashcat** 模式编号和 **John the Ripper** 格式名称，便于后续进行哈希破解。

HAITI 分析哈希的长度、字符集和格式来缩小候选算法范围，并按可能性排序呈现结果。

# CAVEATS

哈希识别是概率性的——许多哈希类型的长度和字符集完全相同，因此 HAITI 通常会返回多个可能的匹配项。没有额外上下文时，它无法确切判断具体算法。安装需要 Ruby 运行环境。

# HISTORY

**HAITI** 由 **Alexandre ZANNI**（noraj）创建，使用 **Ruby** 编写。它被开发为旧式哈希识别工具的现代替代品，重点是支持最新算法并提供破解工具的直接参考。它收录于 **Kali Linux** 及其他注重安全的发行版中。

# INSTALL

```brew: brew install haiti```

```nix: nix profile install nixpkgs#haiti```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hashcat](/man/hashcat)(1), [john](/man/john)(1)
