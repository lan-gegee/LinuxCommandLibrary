# TAGLINE

管理关系数据库实例

# TLDR

**创建 MySQL 数据库实例**

```aws rds create-db-instance --db-instance-identifier [my-db] --db-instance-class db.t3.micro --engine mysql --master-username admin --master-user-password [password] --allocated-storage 20```

**列出所有数据库实例**

```aws rds describe-db-instances```

**描述特定实例**

```aws rds describe-db-instances --db-instance-identifier [my-db]```

**创建手动快照**

```aws rds create-db-snapshot --db-instance-identifier [my-db] --db-snapshot-identifier [my-snapshot]```

**从快照恢复**

```aws rds restore-db-instance-from-db-snapshot --db-instance-identifier [new-db] --db-snapshot-identifier [my-snapshot]```

**修改实例**（调整大小、更改设置）

```aws rds modify-db-instance --db-instance-identifier [my-db] --db-instance-class db.t3.small --apply-immediately```

**创建只读副本**

```aws rds create-db-instance-read-replica --db-instance-identifier [my-replica] --source-db-instance-identifier [my-db]```

**删除实例**（跳过最终快照）

```aws rds delete-db-instance --db-instance-identifier [my-db] --skip-final-snapshot```

# SYNOPSIS

**aws rds** _command_ [_options_]

# DESCRIPTION

**aws rds** 是 AWS CLI 中用于管理 Amazon Relational Database Service（RDS）的接口。这是一项托管关系数据库服务，为 MySQL、PostgreSQL、MariaDB、Oracle、SQL Server 和 Amazon Aurora 处理预置、修补、备份和恢复。

RDS 提供自动备份、时间点恢复、用于扩展的只读副本、面向高可用性的 Multi-AZ 部署以及静态加密。Aurora 在 RDS 基础上扩展出兼容 MySQL 和 PostgreSQL 的数据库，并具备更强的性能。

# COMMANDS

**create-db-instance**
> 创建新的数据库实例

**delete-db-instance**
> 终止数据库实例

**describe-db-instances**
> 列出并描述实例

**modify-db-instance**
> 更改实例配置

**reboot-db-instance**
> 重启数据库实例

**start-db-instance**
> 启动已停止的实例

**stop-db-instance**
> 停止运行中的实例

**create-db-snapshot**
> 创建手动备份

**restore-db-instance-from-db-snapshot**
> 从备份恢复

**create-db-instance-read-replica**
> 创建只读副本

**create-db-cluster**
> 创建 Aurora 集群

**describe-db-snapshots**
> 列出并描述快照

**delete-db-snapshot**
> 删除手动快照

**failover-db-cluster**
> 触发 Aurora 故障转移

**add-tags-to-resource**
> 为 RDS 资源打标签

# CAVEATS

除非启用了 Multi-AZ，否则修改实例可能导致短暂停机。存储只能增加，不能减少。某些引擎版本无法降级。建议在删除前创建最终快照，但这会产生存储费用。

# HISTORY

Amazon RDS 于 **2009 年 10 月**上线，最初支持 MySQL。PostgreSQL 于 **2013 年**加入，Aurora 于 **2014 年**加入。Multi-AZ 部署、只读副本和加密选项随时间不断扩展。支持零停机升级的蓝/绿部署于 **2022 年**推出。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-aurora](/man/aws-aurora)(1), [mysql](/man/mysql)(1), [psql](/man/psql)(1)
