# TAGLINE

Redis 集群的高可用监控

# TLDR

用配置文件**启动** Sentinel

```redis-sentinel [/etc/redis/sentinel.conf]```

以哨兵模式通过 redis-server **启动**

```redis-server [sentinel.conf] --sentinel```

**列出**所有受监控的主节点

```redis-cli -p [26379] sentinel masters```

**按名称获取**当前主节点地址

```redis-cli -p [26379] sentinel get-master-addr-by-name [mymaster]```

**触发**手动故障转移

```redis-cli -p [26379] sentinel failover [mymaster]```

# SYNOPSIS

**redis-sentinel** _config_file_

**redis-server** _config_file_ **--sentinel**

# DESCRIPTION

**Redis Sentinel** 通过持续监控、自动故障转移和通知为 Redis 部署提供高可用性。它监视主节点和副本节点，当主节点不可达且达到法定数量的 Sentinel 进程一致认定其宕机时，它会自动将一个副本提升为主节点，并重新配置其余副本使用新的主节点。

Sentinel 还充当配置提供者，让客户端能够发现指定服务当前的主节点地址。多个 Sentinel 实例（建议至少三个）组成一个分布式系统，对故障转移决策达成共识，从而防止脑裂场景。

配置文件是必需的；Sentinel 会在故障转移时重写它以持久化新拓扑。

# PARAMETERS

**--sentinel**
> 传给 `redis-server` 时，使用提供的配置文件以 Sentinel 模式启动。

# CAVEATS

建议至少部署三个 Sentinel 实例以确保稳健的法定数量。Sentinel 默认端口是 26379。Sentinel 会在故障转移时修改自己的配置文件。Sentinel 不做数据分片——它只负责监控和引导客户端。

# HISTORY

Redis Sentinel 由 **Salvatore Sanfilippo** 在 **Redis 2.4** 中引入（**2.8** 版起稳定），用于在无需人工干预的情况下提供高可用性。

# INSTALL

```apt: sudo apt install redis-sentinel```

```apk: sudo apk add valkey-compat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redis-server](/man/redis-server)(1), [redis-cli](/man/redis-cli)(1)
