# TAGLINE

通过 OpenSSL 执行密码消息语法（CMS）操作

# TLDR

使用证书**签署文件**并以 S/MIME 格式输出

```openssl cms -sign -in [file.txt] -out [signed.p7m] -signer [cert.pem] -inkey [key.pem]```

**验证已签署的消息**

```openssl cms -verify -in [signed.p7m] -CAfile [ca-cert.pem]```

为接收方**加密文件**

```openssl cms -encrypt -in [file.txt] -out [encrypted.p7m] -recip [recipient.pem]```

**解密 CMS 消息**

```openssl cms -decrypt -in [encrypted.p7m] -recip [cert.pem] -inkey [key.pem]```

**创建分离签名**

```openssl cms -sign -in [file.txt] -out [signature.p7s] -signer [cert.pem] -inkey [key.pem] -nodetach```

**从已签署的消息中提取内容**

```openssl cms -verify -in [signed.p7m] -out [content.txt] -noverify```

# SYNOPSIS

**openssl cms** [_operation_] [_options_]

# PARAMETERS

**-sign**
> 使用证书和私钥签署输入数据。

**-verify**
> 验证已签署的 CMS 消息。

**-encrypt**
> 为一个或多个接收方加密输入数据。

**-decrypt**
> 解密 CMS 加密消息。

**-in** _FILE_
> 要处理的输入文件。

**-out** _FILE_
> 结果的输出文件。

**-signer** _FILE_
> 用于签署的证书文件。

**-recip** _FILE_
> 用于加密或解密的接收方证书。

**-inkey** _FILE_
> 用于签署或解密的私钥文件。

**-CAfile** _FILE_
> 包含受信任 CA 证书、用于验证的文件。

**-nodetach**
> 将被签署的内容包含在 CMS 消息中（非分离式）。

**-noverify**
> 不验证签署者的证书。

**-text**
> 为 S/MIME 邮件添加 text/plain MIME 头。

# DESCRIPTION

**openssl cms** 是 OpenSSL 中用于处理密码消息语法（CMS）数据的工具。CMS 是一种数据密码保护标准，定义于 RFC 5652，是 PKCS#7 的后继者。

该命令提供数据的签名、验证、加密和解密操作。它支持多种内容类型，允许分离签名，并能处理 S/MIME 电子邮件格式。CMS 广泛应用于安全电子邮件（S/MIME）、数字签名和加密数据容器。

关键操作包括：创建可集成时间戳机构的签名消息；使用不同证书为多个接收方加密数据；以及依据证书链并结合适当的信任校验来验证签名。

# CAVEATS

必须正确配置证书信任链才能进行验证。自签名证书需要显式的信任设置。**-noverify** 选项会绕过证书验证，仅应用于测试。默认加密算法可能因 OpenSSL 版本而异。

# HISTORY

CMS 于 **2009 年**被标准化为 **RFC 5652**，在 RSA Laboratories 的 PKCS#7 基础上发展而来。OpenSSL 添加了 **cms** 命令，作为对较旧的 **smime** 命令的改进，更好地支持了 CMS 特有的功能和更现代的加密选项。

# SEE ALSO

[x509](/man/x509)(1), [openssl](/man/openssl)(1)
