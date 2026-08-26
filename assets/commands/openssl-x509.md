# TAGLINE

多用途证书工具

# TLDR

**查看证书详情**

```openssl x509 -in [certificate.crt] -text -noout```

**获取证书指纹**

```openssl x509 -in [certificate.crt] -fingerprint -sha256 -noout```

**将 PEM 转换为 DER**

```openssl x509 -in [cert.pem] -outform DER -out [cert.der]```

**查看过期日期**

```openssl x509 -in [certificate.crt] -enddate -noout```

**提取公钥**

```openssl x509 -in [certificate.crt] -pubkey -noout```

**用密钥创建自签名证书**

```openssl x509 -req -in [csr.pem] -signkey [key.pem] -out [cert.pem] -days [365]```

# SYNOPSIS

**openssl x509** [_options_] [-in _file_] [-out _file_]

# PARAMETERS

**-in** _file_
> 输入证书。

**-out** _file_
> 输出文件。

**-text**
> 以文本形式打印。

**-noout**
> 不输出证书。

**-fingerprint**
> 打印指纹。

**-subject**, **-issuer**
> 打印主题/颁发者。

**-dates**
> 打印有效期限。

**-pubkey**
> 输出公钥。

**-req**
> 输入为 CSR。

**-signkey** _file_
> 用密钥进行自签名。

# DESCRIPTION

**openssl x509** 是一个多用途证书工具。它可以显示信息、转换格式、签署证书以及修改证书属性。

它是 OpenSSL 中最常用的证书管理命令之一。

# COMMON QUERIES

```bash
# Subject
openssl x509 -in cert.pem -subject -noout

# Validity dates
openssl x509 -in cert.pem -dates -noout

# Serial number
openssl x509 -in cert.pem -serial -noout
```

# CAVEATS

注意与创建证书的 openssl req 区分。使用信息查询类命令时请配合 -noout 以抑制 PEM 输出。

# HISTORY

X.509 是 ITU-T 制定的 PKI 标准，OpenSSL 自早期版本起就为此提供了全面的工具支持。

# INSTALL

```apt: sudo apt install openssl```

```dnf: sudo dnf install openssl```

```pacman: sudo pacman -S openssl```

```apk: sudo apk add openssl```

```zypper: sudo zypper install openssl```

```brew: brew install openssl```

```nix: nix profile install nixpkgs#openssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl-req](/man/openssl-req)(1), [openssl-ca](/man/openssl-ca)(1), [openssl-verify](/man/openssl-verify)(1)
