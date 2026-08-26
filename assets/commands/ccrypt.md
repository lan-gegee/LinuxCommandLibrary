# TAGLINE

基于 AES 的文件加密与解密

# TLDR

**加密文件**

```ccrypt [file.txt]```

**解密文件**

```ccrypt -d [file.txt.cpt]```

**解密到 stdout**

```ccat [file.txt.cpt]```

**更换加密密钥**

```ccrypt -x [file.cpt]```

**使用文件中的密钥加密**

```ccrypt -k [keyfile] [file.txt]```

**强制覆盖**

```ccrypt -f [file.txt]```

# SYNOPSIS

**ccrypt** [_options_] [_file_...]

**ccencrypt** [_options_] [_file_...]

**ccdecrypt** [_options_] [_file_...]

**ccat** [_options_] [_file_...]

# DESCRIPTION

**ccrypt** 使用 Rijndael 密码（AES）和 256 位密钥对文件和数据流进行加解密。它会用带 `.cpt` 扩展名的加密版本替换原文件，并且原文件会被安全覆写而不是简单删除。

该工具通过独立的命令名提供三种操作模式：**ccencrypt** 用于加密，**ccdecrypt** 用于解密，**ccat** 用于解密到标准输出而不修改文件。这三者与调用 ccrypt 加上相应标志在功能上完全等价。

默认情况下密钥以交互方式提示输入，加密时必须输入两次以防打错。对于自动化流程，可以使用 `-k` 选项从文件读取密钥。

# PARAMETERS

**-e**, **--encrypt**
> 加密模式

**-d**, **--decrypt**
> 解密模式

**-c**, **--cat**
> 解密到 stdout

**-x**, **--keychange**
> 更换加密密钥

**-k** _file_, **--keyfile** _file_
> 从文件读取密钥

**-K** _key_, **--key** _key_
> 在命令行指定密钥（不安全）

**-f**, **--force**
> 不询问直接覆盖

**-v**, **--verbose**
> 打印进度信息

**-q**, **--quiet**
> 抑制警告

**-b**, **--brave**
> 只要求输入一次密钥

**-S** _suf_, **--suffix** _suf_
> 使用指定后缀而不是 .cpt

**-l**, **--symlinks**
> 处理符号链接

# COMMANDS

**ccencrypt**：等价于 ccrypt -e

**ccdecrypt**：等价于 ccrypt -d

**ccat**：等价于 ccrypt -c

# CAVEATS

在命令行使用 -K 会让密钥暴露在进程列表中。出于安全考虑请使用 -k 配合密钥文件或标准输入。基于 AES/Rijndael 密码算法。

# INSTALL

```apt: sudo apt install ccrypt```

```brew: brew install ccrypt```

```nix: nix profile install nixpkgs#ccrypt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [openssl](/man/openssl)(1), [age](/man/age)(1)

# RESOURCES

```[Homepage](https://ccrypt.sourceforge.net)```

<!-- verified: 2026-06-22 -->
