# TAGLINE

创建和解析 PKCS#12 证书包

# TLDR

**创建 PKCS#12 文件**

```openssl pkcs12 -export -out [cert.p12] -inkey [key.pem] -in [cert.pem]```

**提取证书**

```openssl pkcs12 -in [cert.p12] -clcerts -nokeys -out [cert.pem]```

**提取私钥**

```openssl pkcs12 -in [cert.p12] -nocerts -out [key.pem]```

**查看 PKCS#12 信息**

```openssl pkcs12 -in [cert.p12] -info -noout```

# SYNOPSIS

**openssl** **pkcs12** [_options_]

# PARAMETERS

**-export**
> 创建 PKCS#12 文件。

**-in** _FILE_
> 输入文件。

**-out** _FILE_
> 输出文件。

**-inkey** _FILE_
> 私钥文件。

**-clcerts**
> 仅输出客户端证书。

**-nocerts**
> 不包含证书。

**-nokeys**
> 不包含私钥。

# DESCRIPTION

**openssl pkcs12** 用于创建和解析 PKCS#12（.p12/.pfx）文件。这种格式将私钥与其对应的证书以及可选的 CA 链打包进一个受密码保护的单个文件中，广泛用于在系统之间传输凭据。

在导出模式（**-export**）下，它将 PEM 密钥和证书组合为 PKCS#12 归档。在解析模式（默认）下，它从现有归档中提取证书和密钥。**-clcerts**、**-cacerts**、**-nocerts** 和 **-nokeys** 等过滤器控制提取哪些组件。

# CAVEATS

属于 OpenSSL 的组成部分。受密码保护。跨平台格式。

# HISTORY

OpenSSL 对 PKCS#12 的支持提供了**证书包**操作能力。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-x509](/man/openssl-x509)(1)
