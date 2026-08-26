# TAGLINE

OpenSSL 私钥生成工具

# TLDR

**生成 RSA 密钥**

```openssl genpkey -algorithm RSA -out [key.pem]```

**以指定位长生成**

```openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:[4096] -out [key.pem]```

**生成 EC 密钥**

```openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:[P-256] -out [key.pem]```

**生成 Ed25519 密钥**

```openssl genpkey -algorithm ED25519 -out [key.pem]```

**生成用口令加密的 RSA 密钥**

```openssl genpkey -algorithm RSA -aes256 -out [key.pem]```

**从 stdin 读取口令生成密钥**

```openssl genpkey -algorithm RSA -aes256 -pass stdin -out [key.pem]```

# SYNOPSIS

**openssl genpkey** [_options_]

# PARAMETERS

**-algorithm** _ALG_
> 密钥算法：RSA、EC、ED25519、ED448、X25519、X448。

**-out** _FILE_
> 输出文件（默认：stdout）。

**-pkeyopt** _OPT:VALUE_
> 算法特定的选项（例如 rsa_keygen_bits:4096、ec_paramgen_curve:P-256）。

**-aes256**
> 用 AES-256-CBC 加密输出的密钥。

**-pass** _ARG_
> 加密口令来源：pass:phrase、stdin、file:path、env:var。

**-outform** _FORMAT_
> 输出格式：PEM（默认）、DER。

**-text**
> 除编码输出外，还以人类可读形式打印密钥细节。

**-help**
> 显示帮助信息。

# DESCRIPTION

**genpkey** 是 OpenSSL 用于生成私钥的统一命令。它通过一致的接口支持 RSA、EC（NIST 曲线）、Ed25519、Ed448、X25519 和 X448 算法。

该工具为 TLS 证书、代码签名和其他加密用途创建私钥。它以单一且更灵活的接口取代了 **genrsa** 和 **gendsa** 等旧的算法专用命令。

自 OpenSSL 1.0.0 起，**genpkey** 是推荐的密钥生成方式。对于 RSA，默认密钥长度为 2048 位；若需更高安全性，建议使用 4096 位。

# CAVEATS

密钥的安全性取决于参数。请妥善保护私钥。算法支持情况因 OpenSSL 版本而异。

# HISTORY

genpkey 作为统一的密钥生成命令被加入 **OpenSSL**，以一致的接口取代了 genrsa 和 gendsa 等算法专用命令。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-genrsa](/man/openssl-genrsa)(1), [openssl-pkey](/man/openssl-pkey)(1), [openssl-req](/man/openssl-req)(1)
