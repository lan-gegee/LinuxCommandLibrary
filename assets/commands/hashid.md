# TAGLINE

通过分析长度和字符特征识别哈希类型的 Python 工具

# TLDR

**识别哈希类型**

```hashid '[hash]'```

**从文件识别**

```hashid [hashes.txt]```

**显示扩展的哈希类型**

```hashid -e '[hash]'```

**显示 Hashcat 模式编号**

```hashid -m '[hash]'```

**显示 John the Ripper 格式**

```hashid -j '[hash]'```

**输出到文件**

```hashid -o [output.txt] '[hash]'```

# SYNOPSIS

**hashid** [_options_] _hash_|_file_

# PARAMETERS

**-e**, **--extended**
> 列出所有可能的哈希类型，包括加盐类型。

**-m**, **--mode**
> 显示 Hashcat 模式编号。

**-j**, **--john**
> 显示 John the Ripper 格式。

**-o**, **--outfile** _file_
> 将输出写入文件。

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示程序版本。

# DESCRIPTION

**hashID** 是一个 Python 3 工具，它用正则表达式分析哈希值的长度和字符模式来识别哈希类型。它支持 220 多种不同的哈希类型，包括 MD5、SHA 变体、NTLM、bcrypt 和加盐哈希。它可以分析单个哈希、一个哈希文件或整个目录。在渗透测试和安全分析中，可用于确定应该使用哪种破解工具及其模式。

# CAVEATS

识别基于模式匹配（长度和字符集），因此结果是概率性的而非确定性的；许多哈希类型共享相同的格式（例如 MD5 和 NTLM 都是 32 位十六进制字符）。

# INSTALL

```nix: nix profile install nixpkgs#hashid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hashcat](/man/hashcat)(1), [john](/man/john)(1)

# RESOURCES

```[Source code](https://github.com/psypanda/hashID)```
```[Homepage](https://psypanda.github.io/hashID/)```

<!-- verified: 2026-07-17 -->
