# TAGLINE

证书吊销列表处理工具

# TLDR

以文本格式**显示 CRL 信息**

```openssl crl -in [crl.pem] -text -noout```

将 CRL 从 **PEM 转换**为 DER 格式

```openssl crl -in [crl.pem] -outform DER -out [crl.der]```

将 CRL 从 **DER 转换**为 PEM 格式

```openssl crl -in [crl.der] -inform DER -out [crl.pem]```

使用 CA 证书**验证 CRL 签名**

```openssl crl -in [crl.pem] -CAfile [ca.pem] -verify```

**打印 CRL 的颁发者**

```openssl crl -in [crl.pem] -issuer -noout```

**打印上次更新和下次更新**时间

```openssl crl -in [crl.pem] -lastupdate -nextupdate -noout```

# SYNOPSIS

**openssl crl** [_options_] [_-in file_] [_-out file_]

# PARAMETERS

**-in** _FILE_
> 要处理的输入 CRL 文件。

**-out** _FILE_
> 保存转换后 CRL 的输出文件。

**-inform** _FORMAT_
> 输入格式：PEM 或 DER。

**-outform** _FORMAT_
> 输出格式：PEM 或 DER。

**-text**
> 以人类可读的文本格式打印 CRL。

**-noout**
> 不输出编码后的 CRL。

**-verify**
> 验证 CRL 上的签名。

**-CAfile** _FILE_
> 用于验证的 CA 证书文件。

**-issuer**
> 打印颁发者名称。

**-lastupdate**
> 打印上次更新时间。

**-nextupdate**
> 打印下次更新时间。

**-hash**
> 打印 CRL 颁发者名称的哈希值。

# DESCRIPTION

**openssl crl** 是 OpenSSL 中用于处理证书吊销列表（CRL）的命令。CRL 是由颁发证书的证书权威机构（CA）在证书计划到期日之前吊销的数字证书清单。

该命令可以解析、转换和验证 CRL。它同时支持 PEM（Base64 编码）和 DER（二进制）两种格式。CRL 验证可确保该列表确实由声称的 CA 签名，且未被篡改。

CRL 是 PKI（公钥基础设施）安全的关键组成部分，让系统能够检查某张证书是否已被吊销。该命令可以提供关于被吊销证书、吊销日期以及 CRL 有效期的详细信息。

# CAVEATS

CRL 可能变得很大，从而影响性能。现代系统通常更倾向于使用 OCSP（在线证书状态协议）进行实时吊销检查。CRL 验证需要签署该 CRL 的 CA 证书。

# HISTORY

证书吊销列表定义于 **X.509** 标准中，自早期版本起就在 OpenSSL 中实现。CRL 格式规范见 **RFC 5280**。OpenSSL 的 crl 命令为处理这一关键的 PKI 组件提供了全面的工具。

# SEE ALSO

[x509](/man/x509)(1), [verify](/man/verify)(1), [openssl](/man/openssl)(1)
