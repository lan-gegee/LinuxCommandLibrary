# TAGLINE

现代的 Sequoia OpenPGP 命令行工具

# TLDR

**生成密钥**

```sq key generate --userid "[Name <email>]"```

**加密文件**

```sq encrypt --recipient-file [key.pgp] [file]```

**解密文件**

```sq decrypt [file.pgp]```

**签名文件**

```sq sign [file]```

**验证签名**

```sq verify --signer-file [key.pgp] [file.sig]```

**检查数据包**

```sq inspect [file.pgp]```

# SYNOPSIS

**sq** _command_ [_options_] [_args_]

# SUBCOMMANDS

**key**
> 生成、修改和检查 OpenPGP 密钥。

**encrypt**
> 为一个或多个接收者加密数据。

**decrypt**
> 使用私钥解密数据。

**sign**
> 创建 OpenPGP 签名（内联、分离或 cleartext）。

**verify**
> 验证 OpenPGP 签名。

**inspect**
> 在不解密的情况下查看 OpenPGP 数据包结构。

**cert**
> 管理 TPK（可传输公钥 / 证书）。

**pki**
> 通过信任网络（Web of Trust）认证和担保密钥。

# COMMON OPTIONS

**--recipient-file** _FILE_
> 为 _FILE_ 中的证书加密。

**--signer-file** _FILE_
> 使用 _FILE_ 中的私钥进行签名或验证。

**--output** _FILE_, **-o** _FILE_
> 将输出写入 _FILE_ 而不是 stdout。

**--binary**
> 输出二进制 OpenPGP 数据而不是 ASCII 封装格式。

**--force**
> 覆盖已存在的输出文件。

# DESCRIPTION

**sq** 是 Sequoia PGP 的命令行界面，后者是一个用 Rust 编写的现代 OpenPGP 实现。它遵循 OpenPGP 标准，提供密钥生成、加密、解密、签名和签名验证功能。

该工具支持标准的 PGP 工作流，包括带用户 ID 的密钥对生成、使用公钥为接收者加密文件，以及分离或内联签名。**inspect** 子命令可用于查看 OpenPGP 数据包结构，便于调试和验证。

Sequoia PGP 由前 GnuPG 贡献者开发，是传统 PGP 实现的内存安全、模块化替代方案。sq 致力于提供更简洁的命令行界面，同时保持与 OpenPGP 的完全兼容。

# CAVEATS

与 GPG 不同。属于 Sequoia 特有实现。部分功能存在差异。

# HISTORY

**sq** 是 **Sequoia PGP** 的 CLI，后者是由前 GnuPG 开发者用 Rust 编写的现代 OpenPGP 实现。

# INSTALL

```apt: sudo apt install sq```

```dnf: sudo dnf install sequoia-sq```

```pacman: sudo pacman -S sequoia-sq```

```apk: sudo apk add sequoia-sq```

```zypper: sudo zypper install sequoia-sq```

```brew: brew install sq```

```nix: nix profile install nixpkgs#sq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [age](/man/age)(1), [rage](/man/rage)(1)
