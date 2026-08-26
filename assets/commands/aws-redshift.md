# TAGLINE

管理数据仓库集群

# TLDR

**列出所有集群**

```aws redshift describe-clusters```

**描述特定集群**

```aws redshift describe-clusters --cluster-identifier [cluster_name]```

**创建新集群**

```aws redshift create-cluster --cluster-identifier [cluster_name] --node-type dc2.large --master-username [admin] --master-user-password [password] --number-of-nodes [2]```

**创建单节点集群**

```aws redshift create-cluster --cluster-identifier [cluster_name] --node-type dc2.large --master-username [admin] --master-user-password [password] --cluster-type single-node```

**调整集群大小**

```aws redshift resize-cluster --cluster-identifier [cluster_name] --cluster-type multi-node --node-type ra3.xlplus --number-of-nodes [4]```

**创建快照**

```aws redshift create-cluster-snapshot --cluster-identifier [cluster_name] --snapshot-identifier [snapshot_name]```

**删除集群**（跳过最终快照）

```aws redshift delete-cluster --cluster-identifier [cluster_name] --skip-final-cluster-snapshot```

**暂停集群**以节省成本

```aws redshift pause-cluster --cluster-identifier [cluster_name]```

# SYNOPSIS

**aws redshift** _subcommand_ [_options_]

# DESCRIPTION

**aws redshift** 是 AWS CLI 的一个子命令，用于管理 Amazon Redshift。这是一项全托管的 PB 级数据仓库服务，采用列式存储和并行查询执行，可在大型数据集上实现快速分析。

集群由领导节点和计算节点组成。领导节点负责管理连接和查询规划，计算节点则存储数据并执行查询。Redshift 可通过标准 PostgreSQL 驱动执行 SQL 查询。

Redshift Serverless 提供按用量付费的选项，无需管理集群。数据可以从 S3、DynamoDB、EMR 加载，或通过 Firehose 流式传入。

# PARAMETERS

**describe-clusters**
> 列出集群及其详情。

**create-cluster**
> 启动新集群。

**delete-cluster**
> 终止集群。

**modify-cluster**
> 更改集群设置。

**resize-cluster**
> 更改节点类型或数量。

**pause-cluster**
> 暂停集群以停止计费。

**resume-cluster**
> 恢复已暂停的集群。

**reboot-cluster**
> 重启集群。

**create-cluster-snapshot**
> 创建手动快照。

**restore-from-cluster-snapshot**
> 从快照创建集群。

**describe-cluster-snapshots**
> 列出快照。

**--cluster-identifier** _name_
> 唯一的集群名称。

**--node-type** _type_
> 实例类型（dc2.large、ra3.xlplus 等）。

**--number-of-nodes** _count_
> 计算节点数量。

**--cluster-type** _type_
> single-node 或 multi-node。

**--master-username** _name_
> 管理员用户名。

**--master-user-password** _password_
> 管理员密码。

**--db-name** _name_
> 默认数据库名称。

# CAVEATS

集群创建需要几分钟时间。经典调整大小（classic resize）会创建新集群并迁移数据；弹性调整大小（elastic resize）更快但有限制。**pause-cluster** / **resume-cluster** 仅适用于 **RA3** 节点类型（DC2 集群无法暂停）。已暂停的集群仍会产生备份存储费用。多节点集群至少需要 2 个节点。主密码必须满足复杂度要求。公开访问需要正确的安全组和 VPC 设置。

# HISTORY

**Amazon Redshift** 于 **2013 年 2 月**上线，是 AWS 的第一个数据仓库服务，名称取自一种天文现象。**Redshift Spectrum** 于 **2017 年**推出，可直接在 S3 中查询数据。带托管存储的 **RA3 节点**于 **2019 年**推出，将计算与存储分离。**Redshift Serverless** 于 **2022 年 7 月**正式可用。该服务还陆续增加了 AQUA（Advanced Query Accelerator）、机器学习集成和数据共享等功能。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [psql](/man/psql)(1), [aws-s3](/man/aws-s3)(1)
