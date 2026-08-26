# TAGLINE

管理数据库只读副本

# TLDR

**列出副本**

```doctl databases replica list [cluster_id]```

**在其他区域创建只读副本**

```doctl databases replica create [cluster_id] [replica_name] --region [fra1] --size [db-s-1vcpu-1gb]```

**获取副本信息**

```doctl databases replica get [cluster_id] [replica_name]```

**获取副本的连接详情**

```doctl databases replica connection [cluster_id] [replica_name]```

**删除一个副本**

```doctl databases replica delete [cluster_id] [replica_name]```

**将副本提升为独立的主集群**

```doctl databases replica promote [cluster_id] [replica_name]```

# SYNOPSIS

**doctl** **databases** **replica** _command_ _database-cluster-id_ [_replica-name_] [_flags_]

# SUBCOMMANDS

**list** _cluster-id_
> 获取某个集群的只读副本列表。

**create** _cluster-id_ _name_
> 创建一个只读副本。接受 **--region**、**--size** 和 **--private-network-uuid**。

**get** _cluster-id_ _name_
> 获取某个只读副本的信息。

**delete** _cluster-id_ _name_
> 删除一个只读副本。**-f**, **--force** 可跳过确认提示。

**connection** _cluster-id_ _name_
> 获取副本的连接字符串、主机、端口、用户和密码。

**promote** _cluster-id_ _name_
> 将一个只读副本提升为独立的主集群。

# OPTIONS

**--region** _SLUG_
> 副本所在区域，例如 `nyc1` 或 `fra1`。默认与主集群相同区域。

**--size** _SLUG_
> 副本的机器规格，例如 `db-s-1vcpu-1gb`。

**--private-network-uuid** _UUID_
> 要将副本接入的 VPC。

**-o**, **--output** _FORMAT_
> 输出格式：`text`（默认）或 `json`。

**--format** _FIELDS_
> 以逗号分隔的要显示的列。

# DESCRIPTION

**doctl databases replica** 管理 DigitalOcean 托管数据库集群的只读副本。只读副本是主数据库的只读拷贝，为读取密集型工作负载提供横向扩展能力，并支持数据的地理分布。

副本从主集群异步复制数据，使应用可以把读取查询分散到多个数据库实例上。这可以减轻主集群的负载并提高查询性能。副本还可以部署在不同区域，让地理上分散的用户获得更低的延迟。

在灾难恢复场景中，可以将副本提升为独立的集群，即基于该副本创建一个全新的数据库集群。这提供了故障转移能力和数据迁移选项。

# CAVEATS

复制是异步的，副本可能落后于主集群并提供略微过期的数据。**promote** 操作不可逆：副本将成为独立集群，不再跟随主集群，并从那时起按完整集群计费。并非所有引擎或套餐都提供只读副本（最小的共享 CPU 档位和某些引擎不支持），每个副本按其自身规格的价格单独计费。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl](/man/doctl)(1), [doctl-databases](/man/doctl-databases)(1), [doctl-databases-user](/man/doctl-databases-user)(1)

# RESOURCES

```[Source code](https://github.com/digitalocean/doctl)```

```[Documentation](https://docs.digitalocean.com/reference/doctl/reference/databases/replica/)```

<!-- verified: 2026-07-14 -->
