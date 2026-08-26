# TAGLINE

内存数据结构存储与缓存服务器

# TLDR

以默认配置**启动 Redis 服务器**

```redis-server```

**使用配置文件启动**

```redis-server [/path/to/redis.conf]```

**在指定端口启动**

```redis-server --port [6380]```

**带密码保护启动**

```redis-server --requirepass [password]```

**以守护进程模式启动**（后台运行）

```redis-server --daemonize yes```

**使用指定数据目录启动**

```redis-server --dir [/path/to/data]```

**测试配置文件语法**

```redis-server [/path/to/redis.conf] --test-memory [megabytes]```

# SYNOPSIS

**redis-server** [_configfile_] [_options_]

# PARAMETERS

**--port** _number_
> 监听指定端口（默认：6379）

**--bind** _address_
> 绑定到指定的 IP 地址

**--daemonize** _yes|no_
> 以后台守护进程方式运行

**--requirepass** _password_
> 要求客户端连接时提供密码

**--dir** _path_
> 设置数据文件的工作目录

**--dbfilename** _file_
> 设置 RDB 快照文件名

**--appendonly** _yes|no_
> 启用仅追加文件（AOF）持久化

**--maxmemory** _bytes_
> 设置最大内存限制

**--maxmemory-policy** _policy_
> 达到 maxmemory 时的淘汰策略

**--loglevel** _level_
> 设置日志详细程度（debug、verbose、notice、warning）

**--logfile** _path_
> 将日志写入指定文件

**--replica-of** _host_ _port_
> 作为指定主节点的副本启动

# DESCRIPTION

**redis-server** 是 Redis 服务器守护进程，一个支持字符串、列表、集合、有序集合、哈希、流等结构的内存数据结构存储。它提供高性能的键值存储，并支持可选的持久化。

Redis 支持两种持久化模式：RDB 快照（按时间间隔进行的时间点快照）和 AOF（记录每次写入的仅追加文件日志）。两者可以同时启用以获得最大持久性保障。

服务器支持用于高可用的复制，副本会自动从主节点同步。Redis Sentinel 提供自动故障转移，而 Redis Cluster 支持跨多个节点的水平扩展。

配置可以通过命令行选项或配置文件指定。命令行选项优先于配置文件设置。

# CONFIGURATION

**/etc/redis/redis.conf**
> 主服务器配置文件，控制绑定地址、端口、持久化模式、内存限制、复制和安全设置。

**--save** _seconds_ _changes_
> RDB 快照触发条件：如果 N 秒内至少发生 N 次更改则保存数据集。可以指定多条 save 规则。

**--appendonly yes**
> 启用 AOF（Append Only File）持久化，记录每次写操作，比单独使用 RDB 快照具有更强的持久性。

# CAVEATS

默认情况下，Redis 绑定所有接口（0.0.0.0），可能暴露给网络。在生产环境中，请使用 **--bind** 限制为特定地址，并用 **--requirepass** 启用认证。

Redis 将数据存储在内存中。不设置 **--maxmemory** 时，它可能耗尽所有可用 RAM。生产环境请设置合适的限制和淘汰策略。

使用默认设置时，Redis 崩溃可能丢失最多 1 秒的写入（RDB 模式）。启用 AOF 并配合 **appendfsync always** 可获得更强的持久性保证，但会牺牲性能。

# HISTORY

Redis 由 **Salvatore Sanfilippo**（antirez）于 **2009 年**创建。名字最初意为 "Remote Dictionary Server"，它很快作为高性能缓存和数据结构服务器流行开来。Redis 后来成为 Redis Ltd.（前身为 Redis Labs）的一部分，同时仍以 BSD 许可证保持开源。

# INSTALL

```apt: sudo apt install redis-server```

```apk: sudo apk add valkey-compat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[redis-cli](/man/redis-cli)(1), [redis-benchmark](/man/redis-benchmark)(1), [redis-sentinel](/man/redis-sentinel)(1), [memcached](/man/memcached)(1)
