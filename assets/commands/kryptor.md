# TAGLINE

现代文件加密与签名工具

# TLDR

用口令**加密**文件

```kryptor -e [file]```

**解密**文件

```kryptor -d [file.kryptor]```

**生成**密钥对

```kryptor -g```

**签名**文件

```kryptor -s [file]```

**验证**签名

```kryptor -v [file]```

# SYNOPSIS

**kryptor** [*options*] [*files*...]

# DESCRIPTION

**kryptor** 使用现代加密原语加密和签名文件，可调选项很少——定位为 **age** + **minisign** 更友好的替代品。它支持口令、对称密钥和非对称多接收者加密；私钥在静态存储时会被加密。这是面向 Windows、Linux 和 macOS 的跨平台 CLI。

# PARAMETERS

**-e**, **--encrypt**

> 加密文件/目录。

**-d**, **--decrypt**

> 解密。

**-g**, **--generate**

> 创建密钥对。

**-s**, **--sign** / **-v**, **--verify**

> 分离式签名，可附加注释。

完整的长选项和接收者标志请见：**kryptor --help** 或 https://www.kryptor.co.uk/

# CAVEATS

请妥善保管口令和私钥；密钥丢失即意味着数据丢失。请确认你使用的是官方二进制文件。加密不能替代备份。

# INSTALL

```nix: nix profile install nixpkgs#kryptor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[age](/man/age)(1), [minisign](/man/minisign)(1), [gpg](/man/gpg)(1)

# RESOURCES

```[Source code](https://github.com/samuel-lucas6/Kryptor)```

```[Homepage](https://www.kryptor.co.uk/)```

<!-- verified: 2026-07-19 -->
