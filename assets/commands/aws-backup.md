# TAGLINE

集中管理跨 AWS 服务的备份

# TLDR

**创建**备份保管库

```aws backup create-backup-vault --backup-vault-name [vault_name]```

**创建**备份计划

```aws backup create-backup-plan --backup-plan [file://plan.json]```

**启动**按需备份作业

```aws backup start-backup-job --backup-vault-name [vault] --resource-arn [arn] --iam-role-arn [role_arn]```

**列出**所有备份保管库

```aws backup list-backup-vaults```

**列出**保管库中的恢复点

```aws backup list-recovery-points-by-backup-vault --backup-vault-name [vault]```

从恢复点**启动**恢复作业

```aws backup start-restore-job --recovery-point-arn [arn] --iam-role-arn [role_arn] --metadata file://[metadata.json]```

**描述**备份作业的状态

```aws backup describe-backup-job --backup-job-id [job_id]```

# SYNOPSIS

**aws backup** _command_ [_options_]

# DESCRIPTION

**AWS Backup** 是一项统一的、完全托管的备份服务，旨在保护多个 AWS 服务中的资源及其关联数据。它将备份操作集中化并自动化，免去为每个 AWS 服务单独编写自定义脚本和手动流程的需要。

该服务通过以下方式简化备份管理：

> **集中式备份管理** - 创建带有保留策略和计划的备份计划，适用于 Amazon EBS、Amazon RDS、Amazon DynamoDB、Amazon EFS、Amazon FSx、AWS Storage Gateway、Amazon EC2 等多种 AWS 服务

> **基于策略的备份计划** - 定义指定频率、保留期限和生命周期规则的备份策略，并通过标签或资源 ID 自动应用到资源上

> **跨区域与跨账户备份** - 将备份复制到不同的 AWS 区域或账户，以满足灾难恢复和合规要求

> **备份保管库** - 在带访问策略和基于资源权限的加密保管库中组织和保护恢复点

> **合规与审计** - 通过 AWS Backup Audit Manager 框架监控备份活动、生成合规报告，并跟踪整个组织的备份覆盖情况

该服务与 **AWS Organizations** 集成实现集中式备份策略，与 **AWS CloudTrail** 集成实现审计日志，与 **Amazon EventBridge** 集成实现事件驱动的工作流。它支持持续备份服务的**时间点恢复**以及最小化存储成本的**增量备份**。

# AVAILABLE COMMANDS

**create-backup-vault**
> 创建用于存储恢复点的保管库

**delete-backup-vault**
> 删除空的备份保管库

**list-backup-vaults**
> 列出账户中的所有备份保管库

**create-backup-plan**
> 创建包含规则和计划的备份计划

**update-backup-plan**
> 修改现有的备份计划

**delete-backup-plan**
> 移除一个备份计划

**list-backup-plans**
> 列出所有备份计划

**create-backup-selection**
> 定义备份计划应用于哪些资源

**start-backup-job**
> 为资源启动按需备份

**stop-backup-job**
> 取消正在运行的备份作业

**list-backup-jobs**
> 查看备份作业的历史和状态

**describe-backup-job**
> 获取备份作业的状态和详情

**list-protected-resources**
> 列出由 AWS Backup 备份的资源

**start-restore-job**
> 从恢复点恢复资源

**list-restore-jobs**
> 查看恢复作业的历史和状态

**list-recovery-points-by-backup-vault**
> 列出保管库中的所有恢复点

**delete-recovery-point**
> 删除特定的恢复点

**start-copy-job**
> 将恢复点复制到另一个保管库或区域

**create-framework**
> 创建用于备份审计的合规框架

**create-report-plan**
> 生成关于备份活动和合规性的报告

**create-legal-hold**
> 应用法定保全，防止恢复点被删除

**put-backup-vault-access-policy**
> 配置保管库访问权限

**tag-resource**
> 为备份资源添加标签以便归类管理

# CAVEATS

备份和恢复操作需要具备相应权限的 IAM 角色。某些服务需要特定的备份配置，或对恢复选项有限制。跨区域复制会产生数据传输费用。删除保管库前必须清空其中所有恢复点。

# HISTORY

**AWS Backup** 在 **AWS re:Invent 2018** 上发布，于 **2019 年 1 月**作为集中式备份服务上线。此后它逐步扩展支持更多 AWS 服务，并增加了跨账户备份、审计框架和法定保全等功能。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-s3](/man/aws-s3)(1), [aws-rds](/man/aws-rds)(1), [aws-dynamodb](/man/aws-dynamodb)(1), [aws-efs](/man/aws-efs)(1), [aws](/man/aws)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/backup/)```

<!-- verified: 2026-06-17 -->
