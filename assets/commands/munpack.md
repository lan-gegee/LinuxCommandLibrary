# TAGLINE

从 MIME 编码的消息中提取文件

# TLDR

**提取 MIME 附件**

```munpack [message.mime]```

**从标准输入提取**

```cat [email.eml] | munpack```

**提取到指定目录**

```munpack -C [output_dir] [message.mime]```

**安静模式**

```munpack -q [message.mime]```

**强制覆盖**

```munpack -f [message.mime]```

# SYNOPSIS

**munpack** [_options_] [_files_...]

# PARAMETERS

**-f**
> 强制覆盖已有文件。

**-q**
> 安静模式。

**-t**
> 文本模式（转换换行符）。

**-C** _dir_
> 提取到指定目录。

# DESCRIPTION

**munpack** 从 MIME 编码的消息中提取文件。它解码 base64 和 quoted-printable 内容，并将附件保存为独立文件。

munpack 是 mpack 的配套工具，用于处理 multipart MIME 消息。

# EXAMPLE

```bash
# Extract from email
munpack saved_email.eml

# Extract from mailbox
formail -s munpack < mbox

# Extract to specific folder
munpack -C ~/attachments email.mime
```

# SUPPORTED ENCODINGS

```
- Base64
- Quoted-printable
- Uuencode (legacy)
- BinHex (legacy)
```

# CAVEATS

文件名可能会被清理。嵌套 MIME 可能需要多次处理。部分传统编码未获完整支持。

# HISTORY

munpack 由卡内基梅隆大学的 **John G. Myers** 编写，是处理电子邮件附件的 MIME 工具集的一部分。

# INSTALL

```apt: sudo apt install mpack```

```brew: brew install mpack```

```nix: nix profile install nixpkgs#mpack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpack](/man/mpack)(1), [uudecode](/man/uudecode)(1), [base64](/man/base64)(1), [ripmime](/man/ripmime)(1)
