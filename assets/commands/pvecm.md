# TAGLINE

Proxmox 集群成员管理

# TLDR

将当前节点**加入**已有集群

```pvecm add [hostname_or_ip]```

将节点添加到**集群配置**

```pvecm addnode [node]```

显示此节点可用的 **API 版本**

```pvecm apiver```

生成**新的集群**配置

```pvecm create [clustername]```

从集群中**移除**节点

```pvecm delnode [node]```

显示集群中的**节点**

```pvecm nodes```

显示集群**状态**

```pvecm status```

# SYNOPSIS

**pvecm** _command_ [_options_]

# PARAMETERS

**add** _host_
> 将本节点加入已有集群

**addnode**, **addn** _node_
> 将节点添加到集群配置（内部使用）

**apiver**, **ap**
> 显示集群加入 API 版本

**create**, **c** _name_
> 以给定名称创建新集群

**delnode**, **d** _node_
> 从集群配置中移除节点

**nodes**, **n**
> 列出集群节点

**status**, **s**
> 显示集群状态

**expected** _votes_
> 设置法定人数所需的期望票数

# DESCRIPTION

**pvecm** 管理 Proxmox VE 集群成员。它处理集群的创建、节点加入已有集群以及节点的移除。集群提供高可用、实时迁移和共享存储能力。

Proxmox 集群使用 corosync 进行集群通信，使用 pmxcfs 进行分布式配置存储。所有集群节点共享相同的配置。

# CAVEATS

创建集群后不可逆，除非重装系统。移除节点要求该节点离线并执行干净的关闭流程。网络配置必须允许集群通信（默认端口 5405-5412）。

# HISTORY

属于 **Proxmox VE**，支持多节点部署和统一管理。基于 corosync 集群引擎构建，为高可用特性提供基础。

# SEE ALSO

[pvesh](/man/pvesh)(1), [qm](/man/qm)(1), [pct](/man/pct)(1), [ha-manager](/man/ha-manager)(1)
