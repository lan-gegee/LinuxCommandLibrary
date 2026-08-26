# TAGLINE

处理证书吊销列表

# TLDR

**查看 CRL 内容**

```openssl crl -in [crl.pem] -text -noout```

**将 PEM 转换为 DER**

```openssl crl -in [crl.pem] -outform DER -out [crl.der]```

**将 DER 转换为 PEM**

```openssl crl -in [crl.der] -inform DER -out [crl.pem]```

用 CA 证书**校验** CRL 签名

```openssl crl -in [crl.pem] -CAfile [ca.crt] -verify```

**获取 CRL 颁发者名称哈希**

```openssl crl -in [crl.pem] -hash -noout```

显示 CRL **指纹**

```openssl crl -in [crl.pem] -fingerprint -noout```

显示 CRL **颁发者**及更新日期

```openssl crl -in [crl.pem] -issuer -lastupdate -nextupdate -noout```

# SYNOPSIS

**openssl crl** [_options_] [-in _file_] [-out _file_]

# PARAMETERS

**-in** _file_
> 输入的 CRL。

**-out** _file_
> 输出文件。

**-inform** _format_
> 输入格式（PEM、DER）。

**-outform** _format_
> 输出格式。

**-text**
> 以人类可读的文本形式打印 CRL。

**-noout**
> 不输出 CRL 的编码版本。

**-verify**
> 校验 CRL 签名。指定了 -CApath、-CAfile 或 -CAstore 时会隐式启用。

**-hash**
> 输出颁发者名称的哈希，用于按颁发者名称在目录中查找 CRL。

**-fingerprint**
> 输出 CRL 的指纹。

**-issuer**
> 输出颁发者名称。

**-lastupdate**
> 输出 lastUpdate 字段。

**-nextupdate**
> 输出 nextUpdate 字段。

**-crlnumber**
> 输出 CRL 编号。

**-nameopt** _option_
> 指定主题或颁发者名称的显示方式。

**-CAfile** _file_
> 用于校验的 CA 证书文件。

**-CApath** _dir_
> 用于校验的 CA 证书目录。

**-gendelta** _file_
> 输出主 CRL 与指定 CRL 之间的比较结果。

**-badsig**
> 写出之前破坏签名；用于测试。

# DESCRIPTION

**openssl crl** 用于处理证书吊销列表（CRL）。CRL 列出了在到期日之前已被吊销的证书。

该命令可以显示、转换和校验 CRL 文件。

# CRL CONTENTS

```
Issuer            - CA that issued CRL
Last Update       - When CRL was issued
Next Update       - When next CRL expected
Revoked Certs     - List of serial numbers
```

# CAVEATS

CRL 可能会变得很大。实时检查请考虑改用 OCSP。CRL 必须保持最新。

# HISTORY

CRL 由 X.509 标准定义，是 PKI 基础设施的一部分，自早期版本起就在 OpenSSL 中得到实现。

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

[openssl-ca](/man/openssl-ca)(1), [openssl-verify](/man/openssl-verify)(1)
