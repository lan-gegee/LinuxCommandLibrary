# TAGLINE

从加密 PDF 文件中提取密码哈希以供破解

# TLDR

**从 PDF 提取哈希**

```pdf2john [encrypted.pdf] > [hash.txt]```

**多个 PDF**

```pdf2john [file1.pdf] [file2.pdf] > [hashes.txt]```

**然后用 John 破解**

```john [hash.txt]```

# SYNOPSIS

**pdf2john** _file_...

# DESCRIPTION

**pdf2john** 从加密 PDF 文件中提取密码哈希，供 John the Ripper 破解。它支持不同 Acrobat 版本所使用的 PDF 加密版本。

提取出的哈希可用于 John the Ripper 或 Hashcat。

# WORKFLOW

```bash
# 1. Extract hash
pdf2john document.pdf > pdf.hash

# 2. Crack with John
john --wordlist=/usr/share/wordlists/rockyou.txt pdf.hash

# 3. Show cracked password
john --show pdf.hash
```

# HASH FORMAT

```
document.pdf:$pdf$2*3*128*-4*1*16*abc123...
```

# SUPPORTED VERSIONS

```
PDF 1.1-1.3 (40-bit RC4)
PDF 1.4    (128-bit RC4)
PDF 1.5+   (128/256-bit AES)
```

# CAVEATS

属于 John the Ripper 套件的一部分。强密码破解可能耗时较长。请合法且合乎道德地使用。

# HISTORY

pdf2john 是 **John the Ripper** 的一部分。这款密码破解器最初由 **Solar Designer** 开发，后经扩展加入了针对各种格式的提取器。

# SEE ALSO

[john](/man/john)(1), [hashcat](/man/hashcat)(1), [rar2john](/man/rar2john)(1), [zip2john](/man/zip2john)(1)
