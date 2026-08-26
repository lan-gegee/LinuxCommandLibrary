# TAGLINE

高性能的 Cassandra 兼容 NoSQL 数据库

# TLDR

**启动 CQL shell**

```cqlsh```

**连接到 ScyllaDB 节点**

```cqlsh [hostname] [9042]```

**使用身份验证连接**

```cqlsh -u [username] -p [password]```

**从文件执行 CQL**

```cqlsh -f [script.cql]```

**检查节点状态**

```nodetool status```

**查看 ScyllaDB 信息**

```scylla --version```

**检查集群状态**

```nodetool describecluster```

**刷新 memtable**

```nodetool flush```

# SYNOPSIS

**cqlsh** [_options_] [_host_] [_port_]

**nodetool** [_options_] _command_ [_args_]

# CQLSH PARAMETERS

**-u**, **--username** _user_
> 身份验证用户名。

**-p**, **--password** _pass_
> 身份验证密码。

**-k**, **--keyspace** _keyspace_
> 初始 keyspace。

**-f** _file_
> 执行 CQL 文件。

**-e** _statement_
> 执行单条 CQL 语句。

**--ssl**
> 使用 SSL 连接。

**--request-timeout** _secs_
> 查询超时时间。

# NODETOOL COMMANDS

**status**
> 显示集群节点状态。

**info**
> 节点信息和指标。

**ring**
> 令牌环信息。

**repair** [_keyspace_]
> 运行修复操作。

**compact** [_keyspace_]
> 强制压缩。

**flush** [_keyspace_]
> 将 memtable 刷新到 SSTable。

**snapshot** [_name_]
> 创建快照备份。

**drain**
> 排空节点以备关机。

**version**
> 显示 ScyllaDB 版本。

**describecluster**
> 集群信息。

**toppartitions**
> 显示热点分区。

# SCYLLADB-SPECIFIC

**nodetool toppartitions** _keyspace_ _table_ _duration_
> 识别造成负载的热点分区。

**nodetool setlogginglevel** _logger_ _level_
> 动态调整日志级别。

**scylla --developer-mode** _mode_
> 开发模式标志。

**scylla --smp** _cores_
> 要使用的 CPU 核心数量。

**scylla --memory** _amount_
> 内存分配量。

# DESCRIPTION

**ScyllaDB** 使用与 Cassandra 兼容的工具（**cqlsh** 和 **nodetool**），命令和 CQL 语法完全相同。ScyllaDB 是 Cassandra 的 C++ 重写版本，旨在实现更低的延迟和更高的吞吐量。

**cqlsh** 用于执行 CQL 语句。keyspace、表和查询语法与 Cassandra 一致。ScyllaDB 改进了轻量级事务（LWT）并支持物化视图。

**nodetool** 用于管理集群操作。ScyllaDB 为其扩展了 **toppartitions**，用于识别导致负载不均衡的热点。

ScyllaDB 的每核心分片（shard-per-core）架构消除了 CPU 核心之间的锁竞争。**--smp** 标志控制核心分配。其配置与 Cassandra 不同，使用 scylla.yaml。

ScyllaDB Alternator 提供 DynamoDB 兼容 API，需通过 AWS SDK 工具而非 cqlsh 访问。

# CONFIGURATION

**/etc/scylla/scylla.yaml**
> ScyllaDB 主配置文件，包含集群设置、网络、存储和调优参数。

**/etc/scylla/cassandra-rackdc.properties**
> 数据中心和机架配置，用于拓扑感知副本放置。

**~/.cassandra/cqlshrc**
> CQL shell 配置文件，包含连接默认值、格式设置和身份验证信息。

# CAVEATS

虽然兼容 CQL，但某些 Cassandra 特性有所不同或不受支持。配置文件也与 Cassandra 不同。修复操作更快但仍消耗大量资源。驱动程序请查阅兼容性矩阵。

# HISTORY

ScyllaDB 由 **Avi Kivity**（KVM 作者）和 **Dor Laor** 于 **2015 年**创立。首个版本于 **2015 年**发布，是使用 Seastar 框架以 C++ 编写的 Cassandra 直接替代品。2.0 版本（2017 年）增加了物化视图。ScyllaDB 开源版采用 Apache 许可证；企业版额外提供加密和 LDAP 等功能。

# SEE ALSO

[cqlsh](/man/cqlsh)(1)
