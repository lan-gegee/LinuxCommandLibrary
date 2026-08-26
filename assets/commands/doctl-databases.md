# TAGLINE

管理 DigitalOcean 托管数据库集群

# TLDR

**列出数据库集群**

```doctl databases list```

**创建一个数据库集群**

```doctl databases create [name] --engine [pg] --region [nyc1] --size [db-s-1vcpu-1gb]```

**获取集群信息**

```doctl databases get [cluster_id]```

**删除一个集群**

```doctl databases delete [cluster_id]```

**获取连接详情**

```doctl databases connection [cluster_id]```

**调整集群规格**（规格与节点数）

```doctl databases resize [cluster_id] --size [db-s-2vcpu-4gb] --num-nodes [2]```

**下载 TLS 连接所需的 CA 证书**

```doctl databases get-ca [cluster_id]```

# SYNOPSIS

**doctl** **databases** _command_ [_arguments_] [_flags_]

# SUBCOMMANDS

**list**
> 列出你的数据库集群。

**create** _name_
> 创建一个集群。必须提供 **--engine**（`pg`、`mysql`、`redis`、`valkey`、`mongodb`、`kafka`、`opensearch`），并接受 **--region**、**--size**、**--num-nodes**、**--version** 和 **--private-network-uuid**。

**get** _id_
> 获取某个数据库集群的详情。

**delete** _id_
> 删除一个集群。**-f**, **--force** 可跳过确认提示。

**connection** _id_
> 获取连接详情（URI、主机、端口、用户、密码）。

**get-ca** _id_
> 打印用于验证到该集群 TLS 连接的 CA 证书。

**resize** _id_
> 使用 **--size** 和 **--num-nodes** 调整集群规格。

**migrate** _id_
> 将集群迁移到新的区域。

**fork** _name_
> 通过分叉现有集群创建新集群，可选择指定时间点。

**backups** _id_
> 列出集群的备份。

**events** _id_
> 列出集群事件。

**options**
> 显示可用的引擎、版本、区域和规格。

**configuration**
> 查看或更新引擎级的集群配置。

**maintenance-window**
> 安排自动维护窗口。

**storage-autoscale**
> 管理集群的存储自动扩容。

**sql-mode**
> 获取或设置 MySQL 集群的 SQL 模式。

**db**
> 管理集群内的各个数据库。

**user**
> 管理数据库用户。

**pool**
> 管理连接池（PostgreSQL）。

**replica**
> 管理只读副本。

**firewalls**
> 管理哪些资源可以连接到集群。

**indexes**
> 管理 OpenSearch 集群上的索引。

**topics**
> 管理 Kafka 集群上的主题。

# DESCRIPTION

**doctl databases** 管理 DigitalOcean 托管数据库：PostgreSQL、MySQL、Valkey（原 Redis）、MongoDB、Kafka 和 OpenSearch 集群。

该命令为集群提供完整的生命周期管理，从创建和配置到调整大小、迁移和删除。托管数据库会替你处理备份、次要版本更新、故障转移和备用节点；CLI 暴露了控制面板中可用的相同操作，使其可脚本化并可在 CI 中使用。

其他子命令用于管理集群内的各个数据库、用户、连接池、只读副本、防火墙规则和维护窗口。连接字符串、凭据和 CA 证书都可以获取，便于应用集成。

集群 ID 是 UUID，但大多数子命令也接受集群名称。给任何命令加上 **-o json** 即可获得机器可读的输出。

# CAVEATS

**delete** 会销毁集群及其所有备份；无法撤销。托管集群只接受 TLS 连接，因此客户端通常需要来自 **get-ca** 的证书。对存储而言调整大小是单向的（磁盘只能增大不能缩小），并且在节点替换期间会短暂中断连接。并非每个子命令都适用于每个引擎：**pool** 仅限 PostgreSQL，**sql-mode** 仅限 MySQL，**topics** 仅限 Kafka，**indexes** 仅限 OpenSearch。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl](/man/doctl)(1), [doctl-databases-user](/man/doctl-databases-user)(1), [doctl-databases-replica](/man/doctl-databases-replica)(1), [psql](/man/psql)(1), [mysql](/man/mysql)(1)

# RESOURCES

```[Source code](https://github.com/digitalocean/doctl)```

```[Documentation](https://docs.digitalocean.com/reference/doctl/reference/databases/)```

<!-- verified: 2026-07-14 -->
