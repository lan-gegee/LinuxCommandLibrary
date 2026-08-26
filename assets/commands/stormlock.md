# TAGLINE

带租约过期的简单集中式锁

# TLDR

**获取**资源的租约

```stormlock acquire [resource]```

**以显式 TTL 获取**租约

```stormlock acquire --ttl [60s] [resource]```

使用 id **释放租约**

```stormlock release [resource] [lease-id]```

**续订现有租约**

```stormlock renew [resource] [lease-id]```

**显示资源当前的租约**

```stormlock current [resource]```

**仅打印租约 id**

```stormlock current --id-only [resource]```

**检查租约是否仍被持有**

```stormlock is-held [resource] [lease-id]```

# SYNOPSIS

**stormlock** _subcommand_ [_options_] _resource_ [_lease-id_]

# PARAMETERS

**acquire** _RESOURCE_ [**--ttl** _DUR_]
> 尝试获取租约。成功时打印租约 id。

**release** _RESOURCE_ _LEASE_ID_
> 释放指定资源上的指定租约。

**renew** _RESOURCE_ _LEASE_ID_ [**--ttl** _DUR_]
> 延长租约时长。

**current** _RESOURCE_ [**--id-only**]
> 显示当前租约持有者及其 id。`--id-only` 仅打印 id。

**is-held** _RESOURCE_ _LEASE_ID_
> 若给定租约仍处于活跃状态则以状态码 0 退出，否则以非零值退出。

**-c**, **--config** _FILE_
> 配置文件路径。覆盖 `STORMLOCK_CONFIG`。

**--ttl** _DURATION_
> 租约的存活时间（例如 `30s`、`5m`、`1h`）。默认值来自配置文件。

**--help**
> 显示帮助。

# CONFIGURATION

**~/.config/stormlock/config.toml**
> 默认配置文件位置。采用 INI/TOML 语法，包含 `[default]`、按资源配置和 `[backend.<name>]` 区段。常见键：`ttl`、`principal`、`backend`。

**STORMLOCK_CONFIG**
> 覆盖配置文件路径。

# BACKENDS

支持的存储后端：

- **etcd** — 使用 etcd 租约。
- **redis** — 使用带 TTL 的 Redis 键。
- **dynamodb** — 使用支持条件写入的 AWS DynamoDB 表。
- **postgresql** — 使用带过期时间列的 PostgreSQL 行。

自定义后端可通过实现 `stormlock.Backend` 接口并经由 Python entry points 注册的方式添加。

# DESCRIPTION

**stormlock** 是一个简单的集中式锁管理器，面向需要偶尔协调（部署、迁移、cron 任务）的人类操作者和脚本。每个锁都关联一个主体（即持有者）以及一个会自动过期的带 TTL 租约，因此持有者崩溃不会导致资源死锁。

典型流程：`stormlock acquire <resource>` 打印一个租约 id；执行受保护的工作；完成后运行 `stormlock release <resource> <lease-id>`。对于长时间运行的任务，定期调用 `stormlock renew` 以延长租约。

# CAVEATS

需要可达的后端。锁只是建议性的——所有协作客户端都必须在操作前检查锁。TTL 必须调整为长于最坏情况下的工作单元时长（或在工作期间续订）。该工具用 Python 编写；通过 `pip install stormlock[etcd,redis,...]` 安装并附带所需的后端 extras。

# HISTORY

**stormlock** 由 **Thayne McCombs**（tmccombs）在 GitHub 上维护。它以 Apache 2.0 许可证发布。

# SEE ALSO

[flock](/man/flock)(1), [redis-cli](/man/redis-cli)(1), [etcdctl](/man/etcdctl)(1), [consul](/man/consul)(1)
