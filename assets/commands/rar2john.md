# TAGLINE

从 RAR 归档中提取密码哈希

# TLDR

**从 RAR 文件提取哈希**

```rar2john [archive.rar] > [hash.txt]```

**处理多个归档**

```rar2john [file1.rar] [file2.rar] > [hashes.txt]```

**然后用 John 破解**

```john [hash.txt]```

# SYNOPSIS

**rar2john** _file_...

# DESCRIPTION

**rar2john** 从加密的 RAR 归档中提取密码哈希，转换为适合用 John the Ripper 或 Hashcat 进行离线密码恢复的格式。它读取归档的加密元数据并输出一个哈希字符串，其中包含验证密码猜测所需的密码学参数，从而无需反复访问原始归档文件。

该工具同时支持 RAR3 和 RAR5 加密格式，两者使用不同的密钥派生算法。单次调用可处理多个归档，每行哈希都以源文件名为前缀。它是 John the Ripper jumbo 套件的一部分，通常用于经授权的安全审计和密码恢复场景。

# EXAMPLES

```bash
# Extract hash
rar2john encrypted.rar > rar.hash

# Crack with wordlist
john --wordlist=/usr/share/wordlists/rockyou.txt rar.hash

# Show cracked password
john --show rar.hash

# Use hashcat instead (RAR5 mode 13000, RAR3 mode 12500)
rar2john archive.rar | cut -d: -f2 > hash.txt
hashcat -m 13000 hash.txt wordlist.txt
```

# HASH FORMAT

```
archive.rar:$rar5$16$abc123...$15$...
```

# RAR VERSIONS

```
RAR3 - Older format, faster to crack
RAR5 - Modern format, stronger encryption
```

# CAVEATS

属于 John the Ripper jumbo 的一部分。强密码可能耗时极长。请合法且合乎道德地使用。

# HISTORY

rar2john 是 **Solar Designer** 和 Openwall 社区开发的 **John the Ripper** 的一部分，提供 RAR 哈希提取功能。

# INSTALL

```dnf: sudo dnf install john```

```pacman: sudo pacman -S john```

```apk: sudo apk add john```

```zypper: sudo zypper install john```

```brew: brew install john```

```nix: nix profile install nixpkgs#john```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[john](/man/john)(1), [zip2john](/man/zip2john)(1), [pdf2john](/man/pdf2john)(1), [hashcat](/man/hashcat)(1)
