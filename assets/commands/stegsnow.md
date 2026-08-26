# TAGLINE

将消息隐藏在文本文件的空白字符中

# TLDR

从文件中**提取**消息

```stegsnow [path/to/file.txt]```

提取**经过压缩**且**有密码保护**的消息

```stegsnow -C -p [password] [path/to/file.txt]```

显示**存储容量**

```stegsnow -S -l 72 [path/to/file.txt]```

将消息**隐藏**到文本文件中

```stegsnow -m '[message]' [path/to/file.txt] [path/to/output.txt]```

以压缩方式从**消息文件**隐藏内容

```stegsnow -C -f [path/to/message.txt] [path/to/file.txt] [path/to/output.txt]```

使用**压缩和密码**进行隐藏

```stegsnow -C -p [password] -m '[message]' [path/to/file.txt] [path/to/output.txt]```

# SYNOPSIS

**stegsnow** [**-CQS**] [**-p** _passwd_] [**-l** _line-len_] [**-f** _file_ | **-m** _message_] [_infile_ [_outfile_]]

# PARAMETERS

**-C**
> 启用压缩（隐藏时）或解压（提取时）

**-Q**
> 静默模式；不显示统计信息

**-S**
> 显示近似存储容量

**-p** _password_
> 使用 ICE 加密算法的密文反馈模式以密码进行加密/解密

**-l** _line-length_
> 最大行长度（默认为 80）

**-f** _file_
> 隐藏指定文件的内容

**-m** _message_
> 隐藏指定的文本字符串

**-V, --version**
> 显示版本信息

**-h, --help**
> 显示用法信息

# DESCRIPTION

**stegsnow**（也称为 SNOW）通过在行尾追加制表符和空格，将消息隐藏在文本文件中。这些空白字符在查看文件时不可见，从而实现隐写编码。该工具使用空格和制表符序列对数据进行编码，通常每 8 列存储 3 位。

其特性包括针对英文文本优化的内置 Huffman 压缩，以及采用密文反馈模式 ICE 算法的加密。一个标记制表符指示数据起始位置，使文件头保持原样。

# CAVEATS

存储容量取决于载体文件中的行长。过短的行提供的隐藏空间较少。非文本数据应在隐藏前先使用外部压缩工具（gzip）处理。去除空白字符的工具或编辑器可能损坏隐藏数据。

# HISTORY

**SNOW**（Steganographic Nature Of Whitespace）由 **Matthew Kwan** 于 **1996 年**创建。它是最早也是最著名的基于文本的隐写术工具之一，使用在行尾空白字符中编码数据这一简单而有效的技术——普通观察者无法察觉这些空白。

# INSTALL

```apt: sudo apt install stegsnow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[steghide](/man/steghide)(1), [outguess](/man/outguess)(1), [gzip](/man/gzip)(1)
