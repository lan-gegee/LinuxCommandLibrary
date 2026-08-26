# TAGLINE

内存键值数据存储服务器

# TLDR

**以默认配置启动服务器**

```valkey-server```

**使用配置文件启动**

```valkey-server [/etc/valkey/valkey.conf]```

**在指定端口启动**

```valkey-server --port [6379]```

**以密码启动**

```valkey-server --requirepass [password]```

**以最大内存限制启动**

```valkey-server --maxmemory [256mb]```

**以禁用保护模式启动**

```valkey-server --protected-mode no```

**以守护进程方式启动**

```valkey-server --daemonize yes```

**启用 AOF 持久化启动**

```valkey-server --appendonly yes```

作为另一台服务器的**副本启动**

```valkey-server --replicaof [127.0.0.1] [6379]```

**以 Sentinel 模式启动**

```valkey-server --sentinel```

# SYNOPSIS

**valkey-server** [_config-file_] [_options_]

# PARAMETERS

**--port** _port_
> 监听端口（默认：6379）。

**--bind** _address_
> 绑定地址（默认：127.0.0.1）。

**--requirepass** _password_
> 要求连接时提供密码。

**--maxmemory** _bytes_
> 最大内存限制。

**--maxclients** _n_
> 最大客户端连接数。

**--daemonize** _yes|no_
> 以守护进程方式运行。

**--pidfile** _file_
> PID 文件位置。

**--logfile** _file_
> 日志文件位置。

**--loglevel** _level_
> 日志级别：debug、verbose、notice、warning。

**--appendonly** _yes|no_
> 启用 AOF（追加文件）持久化。

**--save** _seconds_ _changes_
> 快照保存规则。

**--protected-mode** _yes|no_
> 启用保护模式。

**--dir** _directory_
> 持久化所用的工作目录。

**--replicaof** _host_ _port_
> 作为指定服务器的副本启动。

**--sentinel**
> 以 Sentinel 模式启动，用于高可用性监控。

**--tls-port** _port_
> 在指定端口监听 TLS 连接。

**--io-threads** _n_
> 用于提升性能的 I/O 线程数（默认：1，即禁用）。

**--cluster-enabled** _yes|no_
> 启用集群模式。

**--dbfilename** _file_
> RDB 快照的文件名（默认：dump.rdb）。

# DESCRIPTION

**valkey-server** 是 Valkey 的服务器组件。Valkey 是一个从 Redis 分支而来的开源内存数据存储，提供高性能键值存储，支持字符串、哈希、列表、集合、有序集合等多种结构。

Valkey 与 Redis OSS 7.2 及更早版本完全兼容。现有的 Redis 客户端、应用和工具只需更改连接端点即可与 Valkey 配合使用。

服务器通过 RDB 快照和 AOF（Append Only File，追加文件）支持持久化。集群与复制功能可提供高可用性和水平扩展能力。

Valkey 8.0+ 相比 Redis 增强了多线程 I/O 并改进了内存效率。

# CAVEATS

默认受内存限制；生产环境应配置 maxmemory。除非禁用保护模式，否则远程访问会被限制。持久化需要磁盘空间。可能存在兼容用的符号链接（redis-server）。

# HISTORY

在 Redis Labs 将许可证改为源码可用（source-available）之后，**Valkey** 于 2024 年从 Redis 分支而来。Linux 基金会将 Valkey 作为开源 Redis 的社区驱动延续项目托管。主要贡献者包括 AWS、Google、Oracle 和 Ericsson。

# INSTALL

```apt: sudo apt install valkey-server```

```dnf: sudo dnf install valkey```

```pacman: sudo pacman -S valkey```

```apk: sudo apk add valkey```

```zypper: sudo zypper install valkey```

```brew: brew install valkey```

```nix: nix profile install nixpkgs#valkey```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[valkey-cli](/man/valkey-cli)(1), [redis-server](/man/redis-server)(1), [memcached](/man/memcached)(1)
