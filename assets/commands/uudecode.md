# TAGLINE

解码经 uuencode 编码的二进制文件

# TLDR

**解码 uuencode 编码的文件**

```uudecode [encoded.txt]```

**解码到指定的输出文件**

```uudecode -o [output] [encoded.txt]```

**从 stdin 解码**

```cat [encoded.txt] | uudecode```

**解码多个文件**

```uudecode [file1.txt] [file2.txt]```

# SYNOPSIS

**uudecode** [_-o outfile_] [_file ..._]

# PARAMETERS

**-o** _outfile_
> 把输出写入指定的文件，而不使用编码数据中的文件名。

_file_
> 待解码的输入文件（省略时读取 stdin）。

# DESCRIPTION

**uudecode** 把经过 uuencode 编码的文件还原为原始的二进制形式。它能自动识别输入采用的是传统 UU 编码还是 base64 编码，两种格式均可处理。

默认情况下，输出文件名取自编码文件的头行；**-o** 选项可以覆盖这一行为。文件权限会依据编码头部恢复，但出于安全考虑，setuid 位和执行位不会被保留。

当指定多个文件时，它们会被逐一单独解码。

# CAVEATS

为保障安全，原始文件的 setuid 位和执行位会被剥离。解码不可信的文件时，编码头部携带的输出文件名可能带来安全风险；请使用 **-o** 指定安全的输出路径。另外要确认编码文件使用的是同一种编码方法（UU 或 base64）。

# HISTORY

uudecode 由贝尔实验室开发，于 1980 年代初随 **BSD 4.0** 首次亮相，是 uuencode 的配套解码工具。两者共同解决了在纯文本的 UUCP 网络上传输二进制文件的问题。虽然邮件附件领域已被 MIME 全面取代，这些命令仍保留在类 Unix 系统上，用于向后兼容及简单的编码任务。

# INSTALL

```apt: sudo apt install sharutils```

```dnf: sudo dnf install sharutils```

```pacman: sudo pacman -S sharutils```

```apk: sudo apk add sharutils```

```zypper: sudo zypper install sharutils```

```nix: nix profile install nixpkgs#sharutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uuencode](/man/uuencode)(1), [base64](/man/base64)(1), [mail](/man/mail)(1)
