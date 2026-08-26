# TAGLINE

Elasticsearch TLS 证书生成器

# TLDR

**生成 CA 证书**

```elasticsearch-certutil ca```

**生成节点证书**

```elasticsearch-certutil cert --ca [elastic-stack-ca.p12]```

**生成 CSR**

```elasticsearch-certutil csr```

**生成 HTTP 证书**

```elasticsearch-certutil http```

**以 PEM 格式输出**

```elasticsearch-certutil ca --pem```

# SYNOPSIS

**elasticsearch-certutil** _mode_ [_options_]

# SUBCOMMANDS

**ca**
> 生成证书颁发机构。

**cert**
> 生成 X.509 证书。

**csr**
> 生成证书签名请求。

**http**
> 生成 HTTP 层证书。

# PARAMETERS

**--ca** _file_
> PKCS#12 格式现有 CA 的路径（cert 模式）。

**--ca-cert** _file_
> PEM 格式 CA 证书的路径。

**--ca-key** _file_
> PEM 格式 CA 私钥的路径。

**--ca-pass** _password_
> CA 私钥的密码。

**--out** _file_
> 输出文件路径。

**--pem**
> 以 PEM 格式而非 PKCS#12 格式输出。

**--dns** _names_
> 证书的 DNS 名称列表，逗号分隔。

**--ip** _addresses_
> 证书的 IP 地址列表，逗号分隔。

**--name** _name_
> 生成的证书的文件名（不含扩展名）。

**--pass** _password_
> 生成的私钥的密码。

**--days** _n_
> 证书有效期（天）（默认：1095）。

**--keysize** _bits_
> RSA 密钥长度（位）（默认：2048）。

**--multiple**
> 为多个实例生成证书。

**--in** _file_
> 描述待生成证书实例的 YAML 文件。

**--self-signed**
> 创建自签名证书（cert 模式）。

**-s**, **--silent**
> 最少输出。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**elasticsearch-certutil** 为保护 Elasticsearch 集群生成证书和证书颁发机构。它通过自动创建自签名证书、证书颁发机构和证书签名请求来简化证书管理流程。

该工具是在传输层（节点间通信）和 HTTP 层（客户端 API 访问）上启用 TLS/SSL 加密的必备手段。它以 PKCS#12 或 PEM 格式生成证书，并可为集群部署包含多个 DNS 名称和 IP 地址。

elasticsearch-certutil 简化了生产环境 Elasticsearch 部署所需的安全配置，并支持 Elastic Stack 安全特性等功能。

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [elasticsearch-keystore](/man/elasticsearch-keystore)(1), [elasticsearch-users](/man/elasticsearch-users)(1)
