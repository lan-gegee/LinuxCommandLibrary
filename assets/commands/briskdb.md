# TAGLINE

带 HTTP 与 PostgreSQL 监听器的分片 SQLite 引擎

# TLDR

用四个分片文件**启动服务器**

```briskdb --data-dir [./briskdb-data] --shards [4]```

在自定义 HTTP 地址上**监听**

```briskdb --listen [127.0.0.1:7654] --data-dir [./briskdb-data]```

启用 PostgreSQL 监听器（环回地址、无身份验证）

```briskdb --data-dir [./briskdb-data] --postgres-listen [127.0.0.1:5433]```

用 psql **连接**本地监听器

```psql -h [127.0.0.1] -p [5433] -d [default]```

检查运行中实例的**健康状况**

```curl http://127.0.0.1:7654/health```

通过 HTTP **查询已注册的表**

```curl -X POST http://127.0.0.1:7654/v1/query -H 'content-type: application/json' -d '{"sql":"SELECT id, name FROM widgets WHERE id = ?1","params":["widget-1"]}'```

显示版本

```briskdb --version```

# SYNOPSIS

**briskdb** [_options_]

# DESCRIPTION

**briskdb** 是 **BriskDB** 的独立服务器。BriskDB 是一个 Rust 引擎，将许多普通的 SQLite WAL 文件呈现为一个逻辑数据库。对不同分片的写入使用独立的 WAL 锁，因此可以并行进行。虚拟桶路由器（4,096 个桶）将行分配到各个分片；每个分片仍是普通 SQLite 文件，现有工具即可查看。

同一引擎还提供 Rust crate 和 Python 扩展形式。**briskdb** 二进制程序启动 HTTP 监听器（默认 **127.0.0.1:7654**），并可选启动 PostgreSQL 线路协议监听器。HTTP 提供 **/health**、**/metrics**、**/admin**（只读数据浏览器）以及 JSON 查询/写入端点。PostgreSQL 监听器默认关闭（`--postgres-listen disabled`）；未启用身份验证时只允许绑定环回地址。任何远程 PostgreSQL 绑定都必须使用 TLS 加单身份 SCRAM-SHA-256。

配套的离线工具 **briskdb-import** 可将一个只读 SQLite 数据库转换为新的 BriskDB 数据目录。它不是在线服务端点，也不会覆盖已有目标目录。

BriskDB 目前处于 **alpha** 阶段。跨分片文件没有通用的原子事务。存储格式和公共 API 在 1.0 之前可能变化。

# PARAMETERS

**--data-dir** _path_
> 清单文件和分片文件所在目录（默认 **./briskdb-data**；环境变量 **BRISKDB_DATA_DIR**）。

**--shards** _n_
> 创建新数据库时的分片数量，2–64（默认 **4**；环境变量 **BRISKDB_SHARDS**）。后续打开时会从清单读取分片数，不匹配则拒绝。

**--listen** _addr_
> HTTP 监听地址（默认 **127.0.0.1:7654**；环境变量 **BRISKDB_LISTEN**）。未验证身份的 HTTP 仅允许绑定环回地址。

**--postgres-listen** _addr_|**disabled**
> PostgreSQL TCP 监听地址，或 **disabled**（默认；环境变量 **BRISKDB_POSTGRES_LISTEN**）。

**--postgres-tls-cert** _path_
> PostgreSQL 监听器 TLS 所用的 PEM 证书链（环境变量 **BRISKDB_POSTGRES_TLS_CERT**）。必须与 **--postgres-tls-key** 和 **--postgres-password-file** 一起设置。

**--postgres-tls-key** _path_
> PostgreSQL 监听器的 PEM 私钥（环境变量 **BRISKDB_POSTGRES_TLS_KEY**）。

**--postgres-user** _name_
> SCRAM-SHA-256 身份（默认 **briskdb**；环境变量 **BRISKDB_POSTGRES_USER**）。

**--postgres-password-file** _path_
> 保存 PostgreSQL SCRAM 密码的文件；不要在命令行传递密码（环境变量 **BRISKDB_POSTGRES_PASSWORD_FILE**）。

**--connections-per-shard** _n_
> 每个分片的最大活动 SQLite 连接数，1–16（环境变量 **BRISKDB_CONNECTIONS_PER_SHARD**）。

**--queue-capacity-per-shard** _n_
> 每个分片的最大排队操作数，1–1024（环境变量 **BRISKDB_QUEUE_CAPACITY_PER_SHARD**）。

**--max-result-rows** _n_
> 单次查询可物化的最大行数（环境变量 **BRISKDB_MAX_RESULT_ROWS**）。

**--max-result-bytes** _n_
> 单次查询可物化的最大逻辑字节数（环境变量 **BRISKDB_MAX_RESULT_BYTES**）。

**--request-timeout-ms** _n_
> 引擎请求超时时间（毫秒）；**0** 表示禁用默认截止时间（环境变量 **BRISKDB_REQUEST_TIMEOUT_MS**）。

**--shutdown-grace-ms** _n_
> 优雅关机的排空等待时长（毫秒）（环境变量 **BRISKDB_SHUTDOWN_GRACE_MS**）。

**-h**, **--help**
> 显示用法后退出。

**-V**, **--version**
> 打印版本号后退出。

# CAVEATS

这是 1.0 之前的软件：磁盘布局和库 API 可能在版本之间变化。HTTP 无身份验证且拒绝非环回地址。PostgreSQL TLS/SCRAM 只有单一身份，不支持角色。跨分片写入不是单个原子事务。受支持的备份方式是：在每个服务器和嵌入式实例退出后，停止服务并对整个数据目录做副本。多进程访问仅限同主机和本地文件系统；模式变更和恢复操作要求独占进程所有权。

# HISTORY

**BriskDB** 是 **schapman1974** 于 2026 年发布的 alpha 项目，使用 **Rust** 编写。它以 SQLite 作为存储引擎，增加了分片路由、分片安全的生成式 ID、HTTP 和 PostgreSQL 协议适配器，以及 Debian/systemd 安装包。MongoDB 和 MySQL 监听器已在计划中。

# SEE ALSO

[sqlite3](/man/sqlite3)(1), [psql](/man/psql)(1), [duckdb](/man/duckdb)(1)

# RESOURCES

```[Source code](https://github.com/schapman1974/briskdb)```

```[Documentation](https://github.com/schapman1974/briskdb/blob/main/docs/ARCHITECTURE.md)```

<!-- verified: 2026-08-16 -->
