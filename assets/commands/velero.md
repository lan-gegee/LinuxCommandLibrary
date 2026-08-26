# TAGLINE

Kubernetes 集群备份与恢复

# TLDR

**创建备份**

```velero backup create [backup-name]```

**列出备份**

```velero backup get```

**从备份恢复**

```velero restore create --from-backup [backup-name]```

**创建定时备份**

```velero schedule create [daily] --schedule="0 1 * * *"```

**查看备份详情**

```velero backup describe [backup-name]```

**删除备份**

```velero backup delete [backup-name]```

**列出恢复任务**

```velero restore get```

**安装 Velero**

```velero install --provider [aws] --bucket [bucket-name]```

# SYNOPSIS

**velero** _command_ [_options_]

# PARAMETERS

**backup create** _NAME_
> 创建备份。

**backup get**
> 列出备份。

**restore create**
> 从备份恢复。

**schedule create** _NAME_
> 创建计划任务。

**--from-backup** _NAME_
> 来源备份。

**--schedule** _CRON_
> Cron 计划表达式。

**--include-namespaces** _NS_
> 限定命名空间。

**--provider** _PROVIDER_
> 存储提供商。

# DESCRIPTION

**velero** 为 Kubernetes 集群提供备份和恢复能力。它捕获集群资源定义和持久卷快照，并将其存储在 S3、GCS 或 Azure Blob Storage 等云对象存储中。

备份可以按需创建，也可以通过基于 cron 的计划自动执行。恢复操作会从备份重建资源，既支持完整集群恢复，也支持按命名空间或资源类型的选择性恢复。该工具常用于灾难恢复、集群迁移和升级前快照。

# CAVEATS

需要对象存储。卷快照取决于提供商。部分资源默认被排除在外。

# HISTORY

**Velero**（原名 Heptio Ark）为 Kubernetes 备份而创建，现由 VMware 维护，是 Tanzu 产品组合的一部分。

# INSTALL

```pacman: sudo pacman -S velero```

```zypper: sudo zypper install velero```

```brew: brew install velero```

```nix: nix profile install nixpkgs#velero```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [restic](/man/restic)(1)
