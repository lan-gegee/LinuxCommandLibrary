# TAGLINE

配置和管理 SSL/TLS 证书

# TLDR

**申请**新的 SSL/TLS 证书

```aws acm request-certificate --domain-name [example.com] --validation-method DNS```

**列出**账户中的所有证书

```aws acm list-certificates```

**详细描述**特定证书

```aws acm describe-certificate --certificate-arn [arn]```

将证书**导入** ACM

```aws acm import-certificate --certificate [file://cert.pem] --private-key [file://key.pem]```

**导出**私有证书及其私钥

```aws acm export-certificate --certificate-arn [arn] --passphrase [file://pass.txt]```

**删除**证书

```aws acm delete-certificate --certificate-arn [arn]```

# SYNOPSIS

**aws acm** _command_ [_options_]

# DESCRIPTION

**AWS Certificate Manager（ACM）**是一项用于配置、管理、部署和续期 SSL/TLS 证书的服务，面向基于 AWS 的网站和应用。它负责处理证书创建、验证、续期和部署等复杂任务，简化了证书生命周期管理。

ACM 免费提供**公有证书**，供 **Elastic Load Balancing**、**Amazon CloudFront**、**Amazon API Gateway** 及其他集成的 AWS 服务使用。它还支持通过 AWS Certificate Manager Private Certificate Authority（PCA）为内部资源提供**私有证书**。

该服务自动续期 ACM 签发的证书，省去手动续期流程，降低了证书过期的风险。证书可通过 **DNS 验证**（推荐）或**电子邮件验证**完成验证。

ACM 与 AWS 服务无缝集成，可在无需人工干预的情况下自动部署和续期证书。由 ACM 管理的证书无法下载，但如果是导入的或属于私有证书则可以导出。

# AVAILABLE COMMANDS

**add-tags-to-certificate**
> 为 ACM 证书添加元数据标签，便于组织和计费

**delete-certificate**
> 永久删除证书（必须未被使用）

**describe-certificate**
> 检索证书的详细信息，包括状态、域名和验证详情

**export-certificate**
> 导出私有证书及其私钥（需要口令）

**get-account-configuration**
> 检索账户级别的 ACM 配置设置

**get-certificate**
> 以 PEM 格式检索证书和证书链

**import-certificate**
> 将第三方证书导入 ACM 进行管理

**list-certificates**
> 列出所有证书，可按状态过滤

**list-tags-for-certificate**
> 列出附加到特定证书的所有标签

**put-account-configuration**
> 配置账户级别的 ACM 设置，例如到期事件

**remove-tags-from-certificate**
> 移除证书上的元数据标签

**renew-certificate**
> 手动续期符合条件的证书

**request-certificate**
> 向 ACM 申请新的公有 SSL/TLS 证书

**resend-validation-email**
> 为基于电子邮件的验证重新发送域名验证邮件

**revoke-certificate**
> 吊销通过 ACM-PCA 签发的私有证书

**search-certificates**
> 按域名、密钥类型或其他条件搜索和过滤证书

**update-certificate-options**
> 更新证书配置，例如证书透明度日志

**wait**
> 等待证书状态变化（issued、validated）

# CAVEATS

除非是导入的或属于私有证书，否则 ACM 管理的证书无法导出。删除证书是永久性的，无法撤销。删除前证书不得关联任何 AWS 资源。DNS 验证要求你具备修改该域名 DNS 记录的能力。

# HISTORY

**AWS Certificate Manager** 于 **2016 年 1 月**推出，旨在简化 AWS 上的 SSL/TLS 证书管理。最初只支持 Elastic Load Balancing，随后扩展到 CloudFront、API Gateway 和其他服务。**2018 年 4 月**加入了对私有 CA 的支持，DNS 验证的引入也进一步简化了验证流程。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-acm-pca](/man/aws-acm-pca)(1), [aws-elbv2](/man/aws-elbv2)(1), [aws-cloudfront](/man/aws-cloudfront)(1), [aws-apigateway](/man/aws-apigateway)(1), [aws](/man/aws)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/acm/)```

<!-- verified: 2026-06-17 -->
