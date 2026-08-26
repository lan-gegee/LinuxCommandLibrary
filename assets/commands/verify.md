# TAGLINE

校验 X.509 证书链

# TLDR

**针对系统 CA 存储验证证书**

```openssl verify [certificate.pem]```

**使用指定的 CA 文件验证**

```openssl verify -CAfile [ca-bundle.pem] [certificate.pem]```

**使用中间证书验证**

```openssl verify -untrusted [intermediate.pem] [certificate.pem]```

**验证并显示证书链**

```openssl verify -show_chain [certificate.pem]```

**验证主机名是否与证书匹配**

```openssl verify -verify_hostname [example.com] [certificate.pem]```

**以详细输出进行验证**

```openssl verify -verbose [certificate.pem]```

**启用 CRL 检查的验证**

```openssl verify -crl_check -CRLfile [crl.pem] [certificate.pem]```

# SYNOPSIS

**openssl verify** [**-CAfile** _file_] [**-CApath** _dir_] [**-untrusted** _file_] [**-show_chain**] [**-verbose**] [**-verify_hostname** _host_] [_certificate_...]

# PARAMETERS

**-CAfile** _file_
> 包含受信任 CA 证书的 PEM 格式文件。

**-CApath** _dir_
> 包含受信任 CA 证书的目录（哈希文件名）。

**-untrusted** _file_
> 包含不受信任的中间证书的文件，用于构建证书链。

**-trusted** _file_
> 包含显式受信任证书的文件。

**-show_chain**
> 显示构建出的完整证书链。

**-verbose**
> 打印有关验证过程的额外信息。

**-verify_hostname** _hostname_
> 验证证书是否与指定的主机名匹配。

**-verify_email** _email_
> 验证证书是否与指定的电子邮箱地址匹配。

**-verify_ip** _ip_
> 验证证书是否与指定的 IP 地址匹配。

**-verify_depth** _num_
> 要验证的证书链最大深度。

**-crl_check**
> 用 CRL 检查终端实体证书。

**-crl_check_all**
> 用 CRL 检查整条证书链。

**-CRLfile** _file_
> 包含证书吊销列表（CRL）的文件。

**-partial_chain**
> 接受由中间证书锚定的证书链。

**-purpose** _purpose_
> 预期用途：sslclient、sslserver、smimesign、smimeencrypt 等。

**-no_check_time**
> 不对照当前时间检查证书有效期。

**-attime** _timestamp_
> 在指定的 UNIX 时间戳而非当前时间下验证证书链。

**-policy** _oid_
> 要求证书链中包含指定的证书策略 OID。

**-CAstore** _uri_
> 指向受信任 CA 证书存储的 URI（例如 file: 或 store:）。

# DESCRIPTION

**openssl verify** 通过检查签名、有效期和信任锚点来校验 X.509 证书链。它从目标证书向上构建一条到达受信任根 CA 的链，并逐级验证。

该命令首先通过查找签发者证书来构建证书链，然后验证每个证书的签名、过期日期和约束条件。证书链必须终止于 CA 文件、CA 目录或系统信任存储中找到的受信任根 CA。

验证成功时返回 0。失败时会产生指示问题的错误码：证书过期、签名失败、缺少签发者或违反约束。常见错误包括 "unable to get local issuer certificate"（缺少中间证书）和 "certificate has expired"。

该命令通常以 **openssl verify** 的形式调用，而非独立的 **verify**。

# CAVEATS

证书路径必须是 PEM 编码的文件。一个文件中包含多个证书时都会被处理，但默认只验证第一个。主机名验证需要显式指定 **-verify_hostname** 选项。自签名证书需要 **-partial_chain** 或将其纳入信任存储。

# HISTORY

**verify** 命令自 **20 世纪 90 年代**末 OpenSSL 早期版本起就是其组成部分。它实现了 RFC 5280（X.509 PKI）定义的证书路径验证。该命令不断演进，以支持主机名验证、多信任锚点和高级策略检查等现代需求。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-verify](/man/openssl-verify)(1), [openssl-x509](/man/openssl-x509)(1), [openssl-s_client](/man/openssl-s_client)(1), [openssl-req](/man/openssl-req)(1), [openssl-ca](/man/openssl-ca)(1)
