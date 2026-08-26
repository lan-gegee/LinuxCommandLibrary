# TAGLINE

在 Dropbear 与 OpenSSH 格式之间转换 SSH 密钥

# TLDR

将 **OpenSSH 转换为 Dropbear** 格式

```dropbearconvert openssh dropbear ~/.ssh/id_rsa output_key```

将 **Dropbear 转换为 OpenSSH** 格式

```dropbearconvert dropbear openssh input_key ~/.ssh/id_rsa```

# SYNOPSIS

**dropbearconvert** _input_type_ _output_type_ _input_file_ _output_file_

# DESCRIPTION

**dropbearconvert** 在 Dropbear 和 OpenSSH 格式之间转换私钥。Dropbear 与 OpenSSH 使用不同的私钥格式，该实用工具在两种实现之间架起桥梁。

# PARAMETERS

**input_type**
> 输入密钥的格式："dropbear" 或 "openssh"

**output_type**
> 输出密钥的格式："dropbear" 或 "openssh"

**input_file**
> 输入私钥文件的路径

**output_file**
> 转换后输出密钥文件的路径

# CAVEATS

**受口令保护的密钥无法转换。**dropbearconvert 无法提示输入口令，因此加密的 OpenSSH 密钥必须先解密，例如用 `ssh-keygen -p -N "" -f key`，并小心处理得到的明文密钥。另请注意，Dropbear 自己的格式根本没有加密变体：转换*为* Dropbear 格式时，磁盘上得到的一定是未受保护的私钥。

只转换私钥。公钥无需转换，因为两种实现使用相同的单行 `authorized_keys` 格式。

该工具会不加询问地覆盖输出文件，而且方向转错时会静默生成对端无法读取的文件，所以请保留原文件的副本。

# HISTORY

**dropbearconvert** 的存在源于历史：Dropbear 早于 OpenSSH 现行的密钥格式出现，选择了自己的紧凑编码，以适应那些解析 PEM 成本过高的设备。这一决定导致两种实现互相无法读取，这个小巧的转换器便是桥梁。它随 Dropbear 本体一起发布，而在空间受限的固件上往往最先被裁掉——这就是为什么密钥转换通常在工作站上完成、再将结果拷贝过去。

# INSTALL

```apt: sudo apt install dropbear-bin```

```apk: sudo apk add dropbear-convert```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dropbear](/man/dropbear)(8), [dropbearkey](/man/dropbearkey)(1), [dbclient](/man/dbclient)(1), [ssh-keygen](/man/ssh-keygen)(1)

# RESOURCES

```[Source code](https://github.com/mkj/dropbear)```

```[Homepage](https://matt.ucc.asn.au/dropbear/dropbear.html)```

<!-- verified: 2026-07-14 -->
