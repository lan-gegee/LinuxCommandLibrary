# TAGLINE

查询 OCSP 响应器

# TLDR

**检查证书状态**

```openssl ocsp -issuer [issuer.pem] -cert [cert.pem] -url [ocsp_url]```

**查询 OCSP 响应器**

```openssl ocsp -issuer [issuer.pem] -serial [serial_number] -url [ocsp_url]```

**验证响应**

```openssl ocsp -respin [response.der] -verify_other [ca.pem]```

**创建 OCSP 请求**

```openssl ocsp -issuer [issuer.pem] -cert [cert.pem] -reqout [request.der]```

# SYNOPSIS

**openssl** **ocsp** [_options_]

# PARAMETERS

**-issuer** _FILE_
> 签发者证书。

**-cert** _FILE_
> 要检查的证书。

**-serial** _NUMBER_
> 证书序列号。

**-url** _URL_
> OCSP 响应器 URL。

**-respin** _FILE_
> 读取 OCSP 响应。

**-reqout** _FILE_
> 写入 OCSP 请求。

**--help**
> 显示帮助信息。

# DESCRIPTION

**openssl ocsp** 用于查询 OCSP 响应器，检查证书的吊销状态。

该工具可在线验证证书，是 OpenSSL 套件的组成部分。

# CAVEATS

需要网络访问。属于 OpenSSL 的一部分。OCSP 响应器必须可用。

# HISTORY

OpenSSL 加入 OCSP 支持是为了实现**在线证书吊销**检查。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-verify](/man/openssl-verify)(1), [openssl-crl](/man/openssl-crl)(1)
