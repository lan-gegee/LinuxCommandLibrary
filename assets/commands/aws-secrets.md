# TAGLINE

安全地存储和管理机密信息

# TLDR

**创建新机密**

```aws secretsmanager create-secret --name [secret_name] --secret-string "[secret_value]"```

**获取机密值**

```aws secretsmanager get-secret-value --secret-id [secret_name]```

**列出所有机密**

```aws secretsmanager list-secrets```

**更新机密值**

```aws secretsmanager put-secret-value --secret-id [secret_name] --secret-string "[new_value]"```

**删除机密**（带恢复窗口）

```aws secretsmanager delete-secret --secret-id [secret_name] --recovery-window-in-days [30]```

**立即删除**且不可恢复

```aws secretsmanager delete-secret --secret-id [secret_name] --force-delete-without-recovery```

**恢复已删除的机密**

```aws secretsmanager restore-secret --secret-id [secret_name]```

**轮换机密**

```aws secretsmanager rotate-secret --secret-id [secret_name]```

# SYNOPSIS

**aws secretsmanager** _command_ [_options_]

# PARAMETERS

**create-secret**
> 创建新机密。

**get-secret-value**
> 获取机密的加密值。

**list-secrets**
> 列出账户中的机密。

**put-secret-value**
> 为现有机密存储新值。

**update-secret**
> 更新机密的元数据或值。

**delete-secret**
> 将机密标记为待删除。

**restore-secret**
> 恢复先前删除的机密。

**rotate-secret**
> 触发机密轮换。

**describe-secret**
> 获取机密的元数据。

**batch-get-secret-value**
> 在单次调用中获取多个机密的值。

**tag-resource**
> 为机密添加标签。

**--secret-id** _id_
> 机密名称或 ARN。

**--secret-string** _value_
> 以字符串表示的机密值。

**--secret-binary** _blob_
> 以 base64 编码二进制表示的机密值。

**--kms-key-id** _key_
> 用于加密的 KMS 密钥（可选）。

**--recovery-window-in-days** _days_
> 永久删除前的等待期（7-30 天）。

# DESCRIPTION

**AWS Secrets Manager** 是一项用于安全存储和管理敏感信息（如数据库凭证、API 密钥和密码）的服务。**aws secretsmanager** 命令提供创建、获取、轮换和管理机密的 CLI 访问能力。

机密使用 AWS KMS 进行静态加密，可通过 Lambda 函数按计划自动轮换。访问由 IAM 策略控制，所有访问都会记录到 CloudTrail 供审计。

机密可存储最大 64KB 的字符串，支持以 JSON 表示数据库凭证等结构化数据。应用程序在运行时获取机密，从而避免在代码或配置文件中硬编码凭证。

# CAVEATS

获取机密会产生按请求计费的费用。已删除的机密默认有恢复窗口；请谨慎使用 **--force-delete-without-recovery**。自动轮换需要配置 Lambda 函数。跨区域复制需要显式配置。Secrets Manager 与 Systems Manager Parameter Store（另一种机密管理方案）相互独立。

# HISTORY

AWS Secrets Manager 于 **2018 年 4 月**上线，旨在解决安全管理工作应用机密的难题。它借鉴了 AWS Systems Manager Parameter Store 的经验，增加了自动轮换、跨区域复制以及与 RDS、Redshift 和 DocumentDB 的原生凭证管理集成等功能。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [vault](/man/vault)(1), [aws-vault](/man/aws-vault)(1)
