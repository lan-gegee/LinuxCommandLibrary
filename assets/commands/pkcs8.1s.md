# TAGLINE

将私钥转换为 PKCS#8 格式

# TLDR

**转换为 PKCS#8**

```openssl pkcs8 -topk8 -in [key.pem] -out [key-pkcs8.pem]```

**加密转换**

```openssl pkcs8 -topk8 -in [key.pem] -out [key.p8] -v2 aes256```

**转换为未加密形式**

```openssl pkcs8 -topk8 -in [key.pem] -out [key.p8] -nocrypt```

**从 PKCS#8 转换回来**

```openssl pkcs8 -in [key.p8] -out [key.pem]```

# SYNOPSIS

**openssl** **pkcs8** [_options_]

# PARAMETERS

**-topk8**
> 转换为 PKCS#8 格式。

**-in** _FILE_
> 输入的密钥文件。

**-out** _FILE_
> 输出文件。

**-nocrypt**
> 不加密。

**-v2** _CIPHER_
> 加密密码算法。

**-inform** _FORMAT_
> 输入格式。

# DESCRIPTION

**openssl pkcs8** 在传统 OpenSSL 格式与标准化的 PKCS#8 格式之间转换私钥。PKCS#8 是一种被广泛支持的私钥容器格式，可在不同的加密库和编程语言之间通用。

**-topk8** 标志将传统格式转换为 PKCS#8 格式。可以使用 **-v2** 以各种密码算法加密密钥，或使用 **-nocrypt** 保持不加密。不带 **-topk8** 时，该工具读取 PKCS#8 输入并输出传统格式。

# CAVEATS

属于 OpenSSL 的组成部分。用于密钥格式转换。加密可选。

# HISTORY

OpenSSL 对 PKCS#8 的支持实现了**私钥格式**转换。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-rsa](/man/openssl-rsa)(1)
