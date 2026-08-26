# TAGLINE

安全地存储和管理机密信息

# TLDR

**创建新机密**

```aws secretsmanager create-secret --name [secret-name] --secret-string "[secret-value]"```

**获取机密的值**

```aws secretsmanager get-secret-value --secret-id [secret-name]```

**列出所有机密**

```aws secretsmanager list-secrets```

**更新机密值**

```aws secretsmanager put-secret-value --secret-id [secret-name] --secret-string "[new-value]"```

**删除机密**（带恢复窗口）

```aws secretsmanager delete-secret --secret-id [secret-name] --recovery-window-in-days [7]```

**立即删除机密**（不可恢复）

```aws secretsmanager delete-secret --secret-id [secret-name] --force-delete-without-recovery```

**轮换机密**

```aws secretsmanager rotate-secret --secret-id [secret-name]```

**生成随机密码**

```aws secretsmanager get-random-password --password-length [32]```

# SYNOPSIS

**aws secretsmanager** _subcommand_ [_options_]

# DESCRIPTION

**aws secretsmanager** 是 AWS CLI 中用于管理 Amazon Secrets Manager 的接口。Secrets Manager 是一项用于安全存储、管理和检索机密的服务，可保存数据库凭证、API 密钥和其他敏感信息。

Secrets Manager 支持自动轮换机密、通过 IAM 策略进行细粒度访问控制，以及通过 CloudTrail 记录审计日志。它还支持跨区域复制以实现灾难恢复。

# SUBCOMMANDS

**Secret Management**
> create-secret, delete-secret, describe-secret, get-secret-value, put-secret-value, update-secret, restore-secret

**Listing**
> list-secrets, list-secret-version-ids

**Rotation**
> rotate-secret, cancel-rotate-secret

**Replication**
> replicate-secret-to-regions, remove-regions-from-replication, stop-replication-to-replica

**Access Control**
> get-resource-policy, put-resource-policy, delete-resource-policy, validate-resource-policy

**Tagging**
> tag-resource, untag-resource

**Utilities**
> get-random-password, batch-get-secret-value, update-secret-version-stage

# CAVEATS

已删除的机密会进入恢复窗口（默认 30 天），之后才被永久删除；使用 **--force-delete-without-recovery** 可跳过这一步。机密值大小上限为 64KB。自动轮换需要 Lambda 函数。Secrets Manager 按每个机密每月收费，另加每次 API 调用的费用。

# HISTORY

AWS Secrets Manager 于 **2018 年 4 月**上线，提供带内置轮换功能的集中式机密管理服务。它取代了将机密存放在环境变量、配置文件或 Parameter Store 中的临时性方案。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ssm](/man/aws-ssm)(1), [vault](/man/vault)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/index.html)```

<!-- verified: 2026-06-18 -->
