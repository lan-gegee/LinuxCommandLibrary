# TAGLINE

Stolon PostgreSQL 高可用集群管理器

# TLDR

**获取集群状态**

```stolonctl --cluster-name [cluster] status```

**初始化集群**

```stolonctl --cluster-name [cluster] init```

**获取集群规格**

```stolonctl --cluster-name [cluster] spec```

**更新规格**

```stolonctl --cluster-name [cluster] update --patch '[{"key":"value"}]'```

**Failkeeper**

```stolonctl --cluster-name [cluster] failkeeper [keeper-id]```

# SYNOPSIS

**stolonctl** [_--cluster-name name_] _command_ [_options_]

# PARAMETERS

**--cluster-name** _NAME_
> 集群名称。

**status**
> 显示状态。

**init**
> 初始化集群。

**spec**
> 显示规格说明。

**update**
> 更新配置。

**--store-backend** _TYPE_
> 后端类型。

# DESCRIPTION

**stolonctl** 是 Stolon 的命令行管理界面，Stolon 是一个云原生 PostgreSQL 高可用管理器。它提供对 Stolon 集群的管理控制，包括查看集群状态、初始化新集群、更新配置规格以及触发手动故障转移。

该工具与 Stolon 的存储后端（通常是 etcd 或 Consul）通信，以读取和修改集群状态。集群规格定义了复制设置、同步复制策略、自动故障转移行为和 PostgreSQL 配置参数。通过 stolonctl 应用的更改会被集群中运行的 Stolon 组件（sentinel、keeper 和 proxy）获取并生效。

stolonctl 对于日常运维至关重要，例如查看哪个 keeper 是当前主节点、强制将故障转移到另一个 keeper，以及在不中断服务的情况下调整集群参数。它通常随基于 Kubernetes 的 Stolon 安装一起部署，但也适用于独立部署。

# CAVEATS

需要 Stolon 部署环境。依赖 Kubernetes 或 etcd。仅针对 PostgreSQL。

# HISTORY

**stolonctl** 是 **Stolon** 的 CLI，Stolon 是一个云原生 PostgreSQL 高可用管理器。

# SEE ALSO

[psql](/man/psql)(1), [pg_ctl](/man/pg_ctl)(1), [kubectl](/man/kubectl)(1)
