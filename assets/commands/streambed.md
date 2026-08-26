# TAGLINE

将 PostgreSQL 变更流式写入 S3 上的 Apache Iceberg 表

# TLDR

将 Postgres WAL **同步**到 Iceberg 并提供查询服务

```streambed sync --source-url=[postgres://user:pass@host:5432/db] --s3-bucket=[bucket] --s3-endpoint=[https://s3] --s3-prefix=[path] --query-addr=:5433```

以一次性快照**回填** Iceberg 表

```streambed resync --source-url=[postgres://...] --s3-bucket=[bucket] --s3-prefix=[path]```

针对现有 Iceberg 表**提供查询服务**（无需连接 Postgres）

```streambed query --s3-bucket=[bucket] --s3-prefix=[path] --query-addr=:5433```

**删除**某张表的 S3 对象和状态

```streambed cleanup --s3-bucket=[bucket] --s3-prefix=[path] --table=[name]```

**查看** sync 的标志选项

```streambed sync --help```

# SYNOPSIS

**streambed** _sync_|_resync_|_query_|_cleanup_ [_flags_]

# DESCRIPTION

**streambed** 是一个用 Go 编写的变更数据捕获（CDC）工具。它通过逻辑复制跟踪 **PostgreSQL** 预写日志（WAL），将产生的变更写成 **Parquet** 文件存入 **S3**，并提交 **Apache Iceberg** 元数据，使这些数据可以作为带版本的表进行分析查询。

`sync` 子命令作为长期运行的守护进程，可选择暴露一个兼容 **PostgreSQL 线协议**的查询端点，这样现有的 Postgres 客户端无需修改即可读取 Iceberg 表。`resync` 在一致快照下使用 `COPY` 执行一次性回填。`query` 单独运行线协议服务器，服务于已填充数据的表。`cleanup` 删除指定表的 S3 对象和追踪状态。

Streambed 的目标场景是：把分析型工作负载从生产 Postgres 实例卸载到基于 S3 的 Iceberg 湖仓，同时让讲 Postgres 协议的工具仍能查询结果。

# PARAMETERS

**sync**
> 流式处理 WAL 变更、写入 Iceberg，可选提供查询服务。

**resync**
> 在一致快照下通过 `COPY` 进行一次性回填。

**query**
> 面向现有 Iceberg 表的 Postgres 线协议查询服务器。

**cleanup**
> 删除某张表的 S3 对象和状态。

**--source-url** _URL_
> Postgres 连接字符串（或 `STREAMBED_SOURCE_URL`）。

**--s3-bucket** _NAME_
> 目标 S3 存储桶（或 `STREAMBED_S3_BUCKET`）。

**--s3-endpoint** _URL_
> S3 端点（可使用 MinIO 或其他 S3 兼容存储）。

**--s3-prefix** _PATH_
> 存储桶内的键前缀。

**--query-addr** _HOST:PORT_
> Postgres 线协议查询服务器的绑定地址。

# CONFIGURATION

每个标志都有对应的以 `STREAMBED_` 为前缀的环境变量（例如 `STREAMBED_SOURCE_URL`）。

# INSTALLATION

该项目从源码构建：

```go build -o streambed ./cmd/streambed```

# CAVEATS

Streambed 要求启用 Postgres 逻辑复制（`wal_level = logical`）并创建复制槽。与任何 CDC 管道一样，如果 WAL 增长速度快于消费速度，它就会落后，这会使 WAL 段在主库上保留到处理完成为止。

# SEE ALSO

[pg_basebackup](/man/pg_basebackup)(1), [pg_recvlogical](/man/pg_recvlogical)(1)
