# TAGLINE

处理 PKCS#7 证书链结构

# TLDR

**查看 PKCS#7 结构**

```openssl pkcs7 -in [file.p7b] -print_certs```

**转换为 PEM**

```openssl pkcs7 -in [file.p7b] -out [certs.pem] -print_certs```

**查看结构信息**

```openssl pkcs7 -in [file.p7b] -text -noout```

**将 DER 转换为 PEM**

```openssl pkcs7 -in [file.der] -inform DER -out [file.pem]```

# SYNOPSIS

**openssl** **pkcs7** [_options_]

# PARAMETERS

**-in** _FILE_
> 输入文件。

**-out** _FILE_
> 输出文件。

**-print_certs**
> 打印证书。

**-text**
> 以文本形式打印。

**-inform** _FORMAT_
> 输入格式（PEM、DER）。

**-noout**
> 无输出。

# DESCRIPTION

**openssl pkcs7** 处理 PKCS#7 结构（.p7b 文件），其中包含不含私钥的证书链。该格式常用于分发 CA 证书包和中间证书。

**-print_certs** 选项从链中提取单个 PEM 证书。通过 **-inform** 和 **-outform** 可在 PEM 与 DER 编码之间转换格式。**-text** 选项以人类可读的形式显示结构。

# CAVEATS

属于 OpenSSL 的组成部分。仅处理证书链。不含私钥。

# HISTORY

OpenSSL 对 PKCS#7 的支持用于处理**证书链**结构。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-pkcs12](/man/openssl-pkcs12)(1)
