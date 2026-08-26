# TAGLINE

通过 AWS CLI 管理 Amazon Aurora 关系型数据库集群

# TLDR

**创建 Aurora MySQL 集群**

```aws rds create-db-cluster --db-cluster-identifier [my-cluster] --engine aurora-mysql --master-username [admin] --master-user-password [password]```

**创建 Aurora PostgreSQL 集群**

```aws rds create-db-cluster --db-cluster-identifier [my-cluster] --engine aurora-postgresql --master-username [admin] --master-user-password [password]```

在集群中**创建数据库实例**

```aws rds create-db-instance --db-instance-identifier [my-instance] --db-cluster-identifier [my-cluster] --engine aurora-mysql --db-instance-class [db.r5.large]```

**列出 Aurora 集群**

```aws rds describe-db-clusters --query "DBClusters[?Engine=='aurora-mysql' || Engine=='aurora-postgresql']"```

**创建集群快照**

```aws rds create-db-cluster-snapshot --db-cluster-identifier [my-cluster] --db-cluster-snapshot-identifier [my-snapshot]```

**删除 Aurora 集群**

```aws rds delete-db-cluster --db-cluster-identifier [my-cluster] --skip-final-snapshot```

# SYNOPSIS

**aws rds** _command_ [_options_]

# PARAMETERS

**create-db-cluster**
> 创建新的 Aurora DB 集群

**create-db-instance**
> 在集群中创建数据库实例

**describe-db-clusters**
> 列出 DB 集群及其详情

**modify-db-cluster**
> 修改集群配置

**delete-db-cluster**
> 删除一个 Aurora 集群

**create-db-cluster-snapshot**
> 为集群创建手动快照

**restore-db-cluster-from-snapshot**
> 从快照恢复集群

**create-db-cluster-endpoint**
> 为只读副本创建自定义端点

**failover-db-cluster**
> 强制故障转移到一个副本

**--db-cluster-identifier** _name_
> 集群的唯一标识符

**--engine** _type_
> 数据库引擎：aurora-mysql、aurora-postgresql

**--engine-version** _version_
> 指定的引擎版本

**--master-username** _name_
> 主用户账户名

**--master-user-password** _password_
> 主用户密码（或使用 --manage-master-user-password）

**--db-instance-class** _class_
> 实例类型（db.r5.large、db.r6g.xlarge 等）

**--db-subnet-group-name** _name_
> 集群的子网组

**--vpc-security-group-ids** _ids_
> 用于网络访问的安全组

**--engine-mode** _mode_
> provisioned 或 serverless。

**--serverless-v2-scaling-configuration** _config_
> Aurora Serverless v2 的最小/最大 ACU 容量。

**--storage-type** _type_
> 存储类型：aurora（标准）或 aurora-iopt1（I/O 优化）。

**--manage-master-user-password**
> 让 AWS Secrets Manager 自动管理主密码。

**--skip-final-snapshot**
> 删除集群时跳过创建最终快照。

# DESCRIPTION

**aws rds** 命令管理 Amazon Aurora——一款为云构建的 MySQL 和 PostgreSQL 兼容关系型数据库。Aurora 命令在 RDS 服务命名空间下运行，而非独立的 Aurora 命名空间。

Aurora 集群由一个主写入实例和最多 15 个只读副本组成。先用 **create-db-cluster** 创建集群，再用 **create-db-instance** 添加实例。Aurora 会自动处理跨可用区的复制。

**Aurora Serverless**（engine-mode serverless）根据需求自动扩缩容量。**Aurora I/O-Optimized**（storage-type aurora-iopt1）为 I/O 密集型工作负载提供可预测的定价。

使用 **--manage-master-user-password** 可让 AWS Secrets Manager 自动管理主密码，而不必直接指定密码。

# CAVEATS

创建集群并不会自动创建实例；你必须单独添加。不带 **--skip-final-snapshot** 删除集群时需要指定最终快照标识符。VPC、子网组和安全组必须在创建集群之前配置好。

# HISTORY

**Amazon Aurora** 于 **AWS re:Invent 2014** 上发布，**2015 年 7 月**正式商用。它旨在提供 MySQL 兼容性，同时显著提升性能和可用性。Aurora PostgreSQL 于 **2017 年**推出，面向波动工作负载的 Aurora Serverless 则于 **2018 年**上线。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-rds](/man/aws-rds)(1), [mysql](/man/mysql)(1), [psql](/man/psql)(1)
