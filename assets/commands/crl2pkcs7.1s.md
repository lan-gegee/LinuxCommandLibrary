# TAGLINE

CRL 到 PKCS#7 格式的转换器

# TLDR

**从 CRL 和证书创建 PKCS#7**

```openssl crl2pkcs7 -in [crl.pem] -certfile [cert.pem] -out [result.p7b]```

**仅由 CRL 创建 PKCS#7**（不含证书）

```openssl crl2pkcs7 -in [crl.pem] -nocrl -out [result.p7b]```

**从多个 CRL 创建 PKCS#7**

```openssl crl2pkcs7 -in [crl1.pem] -in [crl2.pem] -out [result.p7b]```

**以 DER 格式输出**

```openssl crl2pkcs7 -in [crl.pem] -outform DER -out [result.p7b]```

**包含证书链**

```openssl crl2pkcs7 -nocrl -certfile [chain.pem] -out [certs.p7b]```

# SYNOPSIS

**openssl crl2pkcs7** [_options_] [_-in file_] [_-out file_]

# PARAMETERS

**-in** _FILE_
> 输入的 CRL 文件（可多次指定）。

**-out** _FILE_
> 输出的 PKCS#7 文件。

**-certfile** _FILE_
> 包含待纳入证书的文件。

**-nocrl**
> 不在输出中包含 CRL（仅含证书）。

**-inform** _FORMAT_
> 输入 CRL 格式：PEM 或 DER。

**-outform** _FORMAT_
> 输出 PKCS#7 格式：PEM 或 DER。

# DESCRIPTION

**openssl crl2pkcs7** 将证书吊销列表（CRL）和 X.509 证书转换为 PKCS#7 格式。PKCS#7 是一种存储密码学数据的标准格式，常用于证书捆绑包和已签名的数据。

该命令适合用来创建将 CRL 与相关 CA 证书组合在一起的 PKCS#7 结构。某些应用和协议在分发吊销信息时要求同时附带证书链，此时就需要这种格式。

借助 **-nocrl** 选项还可以创建只含证书的 PKCS#7 文件，这对于以广泛受支持的格式分发证书捆绑包很有用。

# CAVEATS

PKCS#7 输出是一种"退化"形式，只包含证书和/或 CRL，不含有签名的数据。有些应用要求此类文件使用 .p7b 或 .p7c 扩展名。输出中的证书不会经过校验；certfile 里的所有 PEM 证书都会被原样包含。

# HISTORY

PKCS#7 由 RSA Security 定义，属于公钥密码学标准（Public-Key Cryptography Standards）的一部分。OpenSSL 的 crl2pkcs7 命令提供了 X.509 CRL 格式与 PKCS#7 之间的转换能力，从而与使用 PKCS#7 容器格式的系统实现互操作。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-crl](/man/openssl-crl)(1), [openssl-x509](/man/openssl-x509)(1), [x509](/man/x509)(1)
