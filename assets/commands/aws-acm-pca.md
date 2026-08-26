# TAGLINE

管理私有证书颁发机构和证书

# TLDR

**创建**私有证书颁发机构

```aws acm-pca create-certificate-authority --certificate-authority-configuration [file://config.json] --certificate-authority-type ROOT```

**列出**账户中的所有证书颁发机构

```aws acm-pca list-certificate-authorities```

**描述**特定的证书颁发机构

```aws acm-pca describe-certificate-authority --certificate-authority-arn [arn]```

从私有 CA **签发**证书

```aws acm-pca issue-certificate --certificate-authority-arn [ca_arn] --csr [file://csr.pem] --signing-algorithm SHA256WITHRSA --validity [value]```

**吊销**证书

```aws acm-pca revoke-certificate --certificate-authority-arn [ca_arn] --certificate-serial [serial] --revocation-reason KEY_COMPROMISE```

**删除**证书颁发机构

```aws acm-pca delete-certificate-authority --certificate-authority-arn [arn]```

# SYNOPSIS

**aws acm-pca** _command_ [_options_]

# DESCRIPTION

**AWS Certificate Manager Private Certificate Authority（ACM PCA）**是一项托管服务，可为你的组织创建和管理私有证书颁发机构（CA）。它为签发和管理私有 SSL/TLS 证书提供了安全、可扩展的基础设施，免去自行运维 CA 基础设施的开销。

与来自 ACM 的公有证书不同，ACM PCA 的**私有证书**用于内部应用、微服务、VPN、IoT 设备以及私有网络中的其他资源。该服务同时支持**根 CA** 和**从属 CA**，让你能够构建完整的公钥基础设施（PKI）层级。

ACM PCA 负责加密运算和证书生命周期管理，包括证书签发、通过**证书吊销列表（CRL）**和**在线证书状态协议（OCSP）**进行的吊销，以及审计报告。它还与 **AWS CloudTrail** 集成，对所有 API 调用和证书操作进行全面的日志记录。

该服务通过 AWS SDK 提供基于 API 的访问，可实现证书签发与管理流程的自动化。它支持多种**签名算法**，包括采用不同密钥长度和哈希函数的 RSA 和 ECDSA。

# AVAILABLE COMMANDS

**create-certificate-authority**
> 创建新的根级或从属证书颁发机构

**delete-certificate-authority**
> 永久删除证书颁发机构（必须先禁用）

**describe-certificate-authority**
> 检索特定 CA 的详细信息

**issue-certificate**
> 使用 CSR 从 CA 签发私有证书

**get-certificate**
> 以 PEM 格式检索已签发的证书

**get-certificate-authority-certificate**
> 检索 CA 证书和证书链

**get-certificate-authority-csr**
> 检索 CA 的 CSR 以便对其进行签名

**import-certificate-authority-certificate**
> 导入已签名的证书以激活 CA

**revoke-certificate**
> 吊销证书并将其加入 CRL

**list-certificate-authorities**
> 列出账户中所有 CA，可选过滤条件

**create-certificate-authority-audit-report**
> 生成 CA 活动的审计报告

**create-permission**
> 授予 ACM 使用 CA 进行证书续期的权限

**put-policy**
> 为 CA 附加基于资源的策略

**tag-certificate-authority**
> 为 CA 添加元数据标签以便归类管理

**update-certificate-authority**
> 修改 CA 配置，包括 CRL 和 OCSP 设置

**wait**
> 等待 CA 状态变化（active、created、deleted）

# CAVEATS

操作受 API 速率限制；超出限制会返回 **ThrottlingException** 错误。CA 删除后在恢复期结束前无法恢复。证书签发需要有效的 CSR（证书签名请求）。私有证书不受公共浏览器信任，仅用于内部用途。

# HISTORY

**AWS Certificate Manager Private Certificate Authority** 于 **2018 年 4 月**推出，在 AWS 上提供托管的私有 CA 服务。它免除了组织自行运维证书颁发机构基础设施的需要，为私有 PKI 管理提供了可扩展且安全的替代方案。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-acm](/man/aws-acm)(1), [aws-iot](/man/aws-iot)(1), [aws-cloudtrail](/man/aws-cloudtrail)(1), [aws](/man/aws)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/acm-pca/)```

<!-- verified: 2026-06-17 -->
