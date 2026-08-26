# TAGLINE

将 scamper warts 二进制文件转换为人类可读的文本

# TLDR

**将** warts 文件**转换**为文本

```sc_warts2text [input.warts]```

**转换**多个 warts 文件

```sc_warts2text [file1.warts] [file2.warts]```

通过管道**转换**压缩的 warts 文件

```gzcat [input.warts.gz] | sc_warts2text```

带 IP 地址描述**转换**

```sc_warts2text -d [ip2descr.txt] [input.warts]```

# SYNOPSIS

**sc_warts2text** [**-d** _ip2descr-file_] [_file_ ...]

# PARAMETERS

**-d** _ip2descr-file_
> 包含 IP 地址到描述映射的文件，每行一条映射。输出中的 IP 地址将被替换为对应的描述。

# DESCRIPTION

**sc_warts2text** 将 scamper 的 warts 二进制测量文件转换为人类可读的纯文本。它是 scamper 主动互联网测量工具集的一部分。

warts 是 scamper 用于存储 traceroute、ping、路径 MTU 发现等测量结果的原生二进制格式。sc_warts2text 对该格式进行解码，并将文本形式的表示写到标准输出，便于查看或用标准文本工具进一步处理。

可以指定多个输入文件，它们会按顺序处理。输入也可以通过管道从标准输入读取，这对即时解压文件很有用。

# INSTALL

```apt: sudo apt install scamper```

```zypper: sudo zypper install scamper```

```brew: brew install scamper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scamper](/man/scamper)(1), [sc_wartsdump](/man/sc_wartsdump)(1), [sc_warts2json](/man/sc_warts2json)(1)
