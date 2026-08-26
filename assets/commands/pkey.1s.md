# TAGLINE

使用 OpenSSL 处理和转换公钥与私钥

# TLDR

**从私钥中提取公钥**

```openssl pkey -in [key.pem] -pubout -out [pub.pem]```

**将 PEM 编码的密钥转换为 DER**

```openssl pkey -in [key.pem] -out [key.der] -outform DER```

**打印密钥参数而不重新编码密钥**

```openssl pkey -in [key.pem] -text -noout```

**移除加密密钥的口令**

```openssl pkey -in [encrypted.pem] -out [decrypted.pem]```

**使用 AES-256 加密私钥**

```openssl pkey -in [key.pem] -out [enc.pem] -aes-256-cbc```

**读取公钥并转换其格式**

```openssl pkey -pubin -in [pub.pem] -outform DER -out [pub.der]```

# SYNOPSIS

**openssl** **pkey** [_options_]

# PARAMETERS

**-in** _FILE_
> 输入密钥文件（省略时为 stdin）。

**-out** _FILE_
> 输出文件（省略时为 stdout）。

**-inform** _FORMAT_
> 输入格式：**PEM**、**DER** 或 **ENGINE**。

**-outform** _FORMAT_
> 输出格式：**PEM** 或 **DER**。

**-passin** _arg_
> 输入口令来源（如 **pass:**、**env:**、**file:**）。

**-passout** _arg_
> 用于加密的输出口令来源。

**-pubin**
> 输入文件是公钥。

**-pubout**
> 仅输出公钥。

**-text**
> 以人类可读的形式打印密钥细节。

**-text_pub**
> 仅以文本形式打印公钥部分。

**-noout**
> 不输出编码后的密钥（配合 **-text** 使用）。

**-traditional**
> 使用旧式"传统"格式写入私钥（例如 RSA 使用 PKCS#1）。

**-_cipher_**
> 任意的 OpenSSL 密码算法（如 **-aes-256-cbc**、**-des-ede3**），用于加密输出的密钥。

# DESCRIPTION

**openssl pkey** 是一个统一的密钥处理工具，可处理任何受支持算法（RSA、DSA、EC、Ed25519、Ed448、X25519、X448）的公钥和私钥。它取代了较旧的特定算法命令 **openssl rsa**、**openssl dsa** 和 **openssl ec**。

该工具可以用 **-pubout** 提取公钥、在 PEM 和 DER 编码之间转换、用 **-text** 显示参数，以及添加或移除口令加密。提供密码算法选项时，生成的私钥将以加密的 PKCS#8 形式写出。

# CAVEATS

写入未加密的私钥文件会移除已有的口令。确保文件系统权限足够严格（例如 **chmod 600**）。某些无法读取现代 PKCS#8 编码密钥的工具需要 **-traditional** 标志。

# HISTORY

**openssl pkey** 随通用的 **EVP_PKEY** 接口一同推出，为所有密钥算法提供单一工具，取代了特定算法的 **rsa**、**dsa** 和 **ec** 子命令。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-genpkey](/man/openssl-genpkey)(1), [openssl-rsa](/man/openssl-rsa)(1)
