# TAGLINE

GnuTLS 证书与密钥生成工具

# TLDR

生成**私钥**

```certtool -p --outfile [path/to/private.key]```

生成**自签名证书**

```certtool -s --load-privkey [path/to/private.key] --template [path/to/info.template] --outfile [path/to/certificate.crt]```

生成**证书签名请求**（CSR）

```certtool -q --load-privkey [path/to/private.key] --template [path/to/info.template] --outfile [path/to/request.csr]```

生成 **CA 证书**

```certtool -s --load-privkey [path/to/ca.key] --template [path/to/ca.template] --outfile [path/to/ca.crt]```

对照 CA **校验**证书

```certtool --verify --infile [path/to/certificate.crt] --load-ca-certificate [path/to/ca.crt]```

# SYNOPSIS

**certtool** [_options_]

# DESCRIPTION

**certtool** 基于 GnuTLS 库生成和管理 X.509 证书、私钥、证书签名请求及其他 PKI 结构。它是 OpenSSL 证书工具的替代品，拥有独特的命令行界面和基于模板的工作流程。

组织名、通用名（common name）、有效期、密钥用途和扩展项等证书属性在模板文件中定义，而不是作为命令行参数传入。这使得复杂的证书配置可复现、可脚本化。模板语法采用简单的键值对。

该工具支持完整的 PKI 工作流程：生成私钥、创建自签名 CA 证书、签发证书签名请求、用 CA 签署证书以及验证证书链。

# PARAMETERS

**-p, --generate-privkey**
> 生成私钥

**-s, --generate-self-signed**
> 生成自签名证书

**-q, --generate-request**
> 生成证书签名请求

**--generate-certificate**
> 从 CSR 生成证书

**--load-privkey** _file_
> 从文件加载私钥

**--template** _file_
> 使用模板文件提供证书信息

**--outfile** _file_
> 输出文件路径

**--verify**
> 验证证书链

**-i, --certificate-info**
> 显示证书信息

# CAVEATS

模板文件格式与 OpenSSL 配置不同。某些功能可能需要特定的 GnuTLS 版本。证书模板必须指定所有必填字段。

# INSTALL

```apt: sudo apt install gnutls-bin```

```dnf: sudo dnf install gnutls-utils```

```apk: sudo apk add gnutls-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [gnutls-cli](/man/gnutls-cli)(1)

# RESOURCES

```[Source code](https://gitlab.com/gnutls/gnutls)```

```[Documentation](https://gnutls.org/manual/html_node/certtool-Invocation.html)```

<!-- verified: 2026-06-22 -->
