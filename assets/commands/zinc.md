# TAGLINE

轻量级全文搜索引擎

# TLDR

**以初始管理员凭据启动 Zinc 服务器**

```ZINC_FIRST_ADMIN_USER=[admin] ZINC_FIRST_ADMIN_PASSWORD=[password] zinc```

**在指定端口启动**

```ZINC_SERVER_PORT=[4080] zinc```

**以自定义数据目录启动**

```ZINC_DATA_PATH=[/var/lib/zinc] zinc```

**通过 API 写入数据**

```curl -u [admin:password] -X POST http://localhost:4080/api/[index]/_doc -d '{"field": "value"}'```

# SYNOPSIS

**zinc** [_options_]

# PARAMETERS

注意：ZincSearch（现 OpenObserve）主要通过环境变量而非命令行标志进行配置。

# ENVIRONMENT

**ZINC_FIRST_ADMIN_USER**
> 初始管理员用户名（首次运行时必填）

**ZINC_FIRST_ADMIN_PASSWORD**
> 初始管理员密码（首次运行时必填）

**ZINC_DATA_PATH**
> 数据存储目录（默认：./data）

**ZINC_SERVER_ADDRESS**
> 服务器绑定地址（默认：0.0.0.0）

**ZINC_SERVER_PORT**
> 服务器端口（默认：4080）

**ZINC_MAX_RESULTS**
> 返回的最大搜索结果数（默认：100）

**ZINC_BATCH_SIZE**
> 批量索引时的内部批次大小（默认：1024）

**ZINC_SHARD_NUM**
> 用于提升性能的分片数量（默认：3）

**ZINC_ICE_COMPRESSOR**
> 压缩算法：snappy、s2、zstd（默认：zstd）

**ZINC_WAL_SYNC_INTERVAL**
> 预写日志同步频率（默认：1s）

**ZINC_TELEMETRY**
> 匿名使用数据（默认：true）

**ZINC_PROMETHEUS_ENABLE**
> 启用 Prometheus 指标端点（默认：false）

**GIN_MODE**
> 设为 "release" 以进入生产模式

# DESCRIPTION

**ZincSearch**（原名 Zinc）是一款轻量级全文搜索引擎，定位为 Elasticsearch 的替代方案。它提供日志搜索和分析功能，而资源需求显著更低。

ZincSearch 具有用于管理的 Web UI、兼容 Elasticsearch 搜索语法的 REST API，并支持多种数据写入方式，包括批量插入和 fluentd/fluent-bit 集成。

该搜索引擎用 Go 编写，使用 Bluge 作为索引库。它以单个二进制文件配合内嵌存储运行，无需外部依赖。

常见用例包括日志聚合、应用内搜索，以及在资源受限环境中替代 Elasticsearch。该项目后来演进为 **OpenObserve**。

# CAVEATS

Zinc 不是 Elasticsearch 的即插即用替代品。虽然支持类似的查询语法，但并非所有 Elasticsearch 功能都已实现。

高可用部署需要手动实现额外的架构（负载均衡器、复制等）。

内存占用随索引大小增长。大型部署请监控资源。

首次运行前必须通过环境变量设置初始管理员凭据。

# INSTALL

```aur: yay -S zinc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [opensearch](/man/opensearch)(1), [meilisearch](/man/meilisearch)(1)
