# TAGLINE

在多种编码之间转换 Ed25519 公钥

# TLDR

**列出**支持的公钥编码格式

```edky list```

**将** Iroh 密钥**转换为** libp2p/multibase 密钥

```edky convert -f iroh -t libp2p [key]```

**将** libp2p 密钥**转换回** Iroh（base32z）

```edky convert -f libp2p -t iroh [key]```

**将** NEAR 密钥**转换为**原始十六进制

```edky convert -f near -t hex [key]```

**将**十六进制**转换为** NEAR 风格密钥

```edky convert -f hex -t near [key]```

**解析**指定编码的密钥

```edky parse -f openssh [key]```

# SYNOPSIS

**edky** [_options_] [_command_] [_args_]

# DESCRIPTION

**edky**（读作 "ed-key"）在密码学和点对点技术栈中常用的编码格式之间转换 **Ed25519** 公钥。它既可以作为命令行工具使用，也提供 Rust、TypeScript/JavaScript、Dart、Python 和 Ruby 的库。

**--from** / **--to** 支持的编码包括 **hex** / **base16**、**base32z**、**base58**、**base64**、**base64url**、**multibase**，以及生态别名如 **iroh**、**libp2p**、**ipfs**、**near**、**openssh** 和 **asimov**。子命令有 **list**（枚举格式）、**convert**（重新编码密钥）和 **parse**（校验并检查密钥）。

可通过 Cargo 的 **cli** feature 安装 CLI（**cargo install edky --locked --features=cli**），或使用 **cargo binstall edky**。convert/parse 在未指定时默认的输入和输出编码为 **hex**。

# PARAMETERS

**list**
> 打印支持的公钥编码格式名称。

**convert** [**-f** _FROM_] [**-t** _TO_] [_INPUTS_…]
> 将每个输入密钥从编码 _FROM_ 转换为编码 _TO_。默认值：**hex** → **hex**。

**parse** [**-f** _FROM_] [_INPUTS_…]
> 以编码 _FROM_ 解析密钥（默认 **hex**）。

**-f**, **--from** _FORMAT_
> 输入编码格式。

**-t**, **--to** _FORMAT_
> 输出编码格式（仅限 **convert**）。

**-d**, **--debug**
> 启用调试输出。

**-v**, **--verbose**
> 提高输出详细程度（可重复使用）。

**-V**, **--version**
> 打印版本信息。

**--license**
> 显示许可证信息。

**--color** _auto|always|never_
> 控制彩色输出（默认 **auto**）。

**-h**, **--help**
> 打印帮助。

# CAVEATS

仅处理**公**钥；不能转换私钥或对数据进行签名。编码别名可能映射到相同的传输格式（例如 **iroh** 与 **base32z**，或 multibase 编码 DID 密钥时的 **libp2p** / **ipfs** / **multibase**）。所选格式的输入长度或字母表无效时会报错。

# HISTORY

**edky** 是 Arto Bendiken 开发的公有领域（Unlicense）软件，旨在促进 ASIMOV、IPFS、Iroh、libp2p、NEAR、OpenSSH 及相关 Ed25519 编码之间的互操作。

# SEE ALSO

[ssh-keygen](/man/ssh-keygen)(1), [age-keygen](/man/age-keygen)(1), [openssl](/man/openssl)(1)

# RESOURCES

```[Source code](https://github.com/artob/edky)```

```[Homepage](https://edky.dev)```

<!-- verified: 2026-07-22 -->
