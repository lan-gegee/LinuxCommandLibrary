# TAGLINE

对照受信任的 CA 验证证书链

# TLDR

**验证证书**

```openssl verify [certificate.crt]```

**使用 CA 文件验证**

```openssl verify -CAfile [ca.crt] [certificate.crt]```

**使用 CA 目录验证**

```openssl verify -CApath [/etc/ssl/certs/] [certificate.crt]```

**验证证书链**

```openssl verify -CAfile [ca.crt] -untrusted [intermediate.crt] [leaf.crt]```

**显示验证详情**

```openssl verify -verbose [certificate.crt]```

**显示构建出的证书链**

```openssl verify -show_chain -CAfile [ca.crt] [certificate.crt]```

**启用 CRL 检查进行验证**

```openssl verify -crl_download -crl_check -CAfile [ca.crt] [certificate.crt]```

# SYNOPSIS

**openssl verify** [_options_] _cert_...

# PARAMETERS

**-CAfile** _file_
> 受信任根证书所在的 CA 证书文件。

**-CApath** _dir_
> CA 证书目录（哈希文件名）。

**-CAstore** _uri_
> 受信任 CA 证书存储的 URI。

**-untrusted** _file_
> 包含非受信中间证书的文件。

**-partial_chain**
> 允许在链中任一证书受信任时，即使证书链不完整也算验证成功。

**-verbose**
> 打印有关验证操作的额外信息。

**-show_chain**
> 显示验证期间构建的证书链信息。

**-x509_strict**
> 严格的 X.509 合规性检查（禁用对不合规情况的变通处理）。

**-attime** _timestamp_
> 在指定时间（自纪元起的秒数）而非当前时间进行验证。

**-no_check_time**
> 不检查证书和 CRL 的有效期。

**-purpose** _purpose_
> 证书用途（sslclient、sslserver、smimesign、smimeencrypt 等）。

**-CRLfile** _file_
> 包含 PEM 格式 CRL 的文件，用于吊销检查。

**-crl_download**
> 尝试下载证书的 CRL 信息。

**-crl_check**
> 用 CRL 检查终端实体证书。

**-crl_check_all**
> 用 CRL 检查链中所有证书。

**-check_ss_sig**
> 验证自签名根 CA 上的签名（默认禁用）。

# DESCRIPTION

**openssl verify** 对照受信任的 CA 验证证书链。它检查签名、有效期限和信任链。验证成功时返回退出状态码 0。

# CAVEATS

默认不检查吊销状态；请使用 -crl_check 或 -crl_download。系统 CA 存储位置因发行版而异。验证失败时可用 -verbose 获取诊断信息。

# HISTORY

证书验证是 PKI 的基础，openssl verify 提供了对 OpenSSL 验证函数的命令行访问。-show_chain 选项在 OpenSSL 1.1.0 中加入。

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

[openssl-x509](/man/openssl-x509)(1), [openssl-s_client](/man/openssl-s_client)(1), [openssl-crl](/man/openssl-crl)(1)
