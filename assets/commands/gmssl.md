# TAGLINE

中国国密算法工具集

# TLDR

**生成 SM2 密钥对**

```gmssl sm2keygen -pass [password] -out [key.pem]```

**计算文件的 SM3 哈希**

```gmssl sm3 < [file]```

**用 SM4 加密**

```gmssl sm4 -encrypt -in [plaintext.txt] -out [ciphertext.bin]```

**用 SM4 解密**

```gmssl sm4 -decrypt -in [ciphertext.bin] -out [plaintext.txt]```

**生成随机字节**

```gmssl rand -hex [32]```

**用 SM2 签名**

```gmssl sm2sign -key [key.pem] -pass [password] -in [file] -out [sig]```

# SYNOPSIS

**gmssl** _command_ [_options_]

# SUBCOMMANDS

**sm2keygen**
> 生成 SM2 密钥对。

**sm2sign**
> 用 SM2 签名。

**sm2verify**
> 验证 SM2 签名。

**sm2encrypt**
> 用 SM2 公钥加密。

**sm2decrypt**
> 用 SM2 私钥解密。

**sm3**
> 计算 SM3 哈希。

**sm4**
> SM4 加密/解密。

**rand**
> 生成随机数据。

**version**
> 显示版本。

# PARAMETERS

**-in** _file_
> 输入文件。

**-out** _file_
> 输出文件。

**-pass** _password_
> 密钥口令。

**-pubout** _file_
> 将导出的公钥写入文件（与 **sm2keygen** 配合使用）。

**-encrypt**
> 加密模式。

**-decrypt**
> 解密模式。

**-hex**
> 以十六进制输出。

# DESCRIPTION

**GmSSL** 是一个支持中国国家标准密码算法（国密/GM）的开源密码学工具集。它提供 SM2（椭圆曲线密码）、SM3（哈希函数）、SM4（分组密码）、SM9（标识密码）和 ZUC（流密码）的实现。其命令行界面与 OpenSSL 类似。

# HISTORY

GmSSL 的开发是为了支持中国的密码标准，这些标准在中国政府和金融系统中被强制要求使用。该项目由北京大学和开源社区维护。

# INSTALL

```brew: brew install gmssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [gpg](/man/gpg)(1)

# RESOURCES

```[Source code](https://github.com/guanzhi/GmSSL)```

```[Homepage](http://guanzhi.github.io/GmSSL/)```

<!-- verified: 2026-07-17 -->
