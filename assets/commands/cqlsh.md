# TAGLINE

交互式 Cassandra 查询语言 Shell

# TLDR

**启动 CQL shell**

```cqlsh```

**连接远程主机**

```cqlsh [hostname] [9042]```

**带身份验证连接**

```cqlsh -u [username] -p [password]```

**从文件执行 CQL**

```cqlsh -f [script.cql]```

**执行单条语句**

```cqlsh -e "SELECT * FROM [keyspace].[table]"```

**检查节点状态**

```nodetool status```

**查看集群信息**

```nodetool info```

**修复节点**

```nodetool repair```

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

**--connect-timeout** _secs_
> 连接超时时间。

**--request-timeout** _secs_
> 查询超时时间。

# NODETOOL COMMANDS

**status**
> 显示集群节点状态。

**info**
> 节点信息。

**ring**
> 令牌环信息。

**repair** [_keyspace_]
> 执行反熵修复。

**cleanup** [_keyspace_]
> 清除不属于本节点的数据。

**compact** [_keyspace_]
> 强制执行压缩（compaction）。

**flush** [_keyspace_]
> 将 memtable 刷写入 SSTable。

**snapshot** [_name_]
> 进行快照备份。

**decommission**
> 停用该节点。

**drain**
> 排空节点以备关机。

**describecluster**
> 集群信息。

# CONFIGURATION

**~/.cassandra/cqlshrc**
> 用户级 cqlsh 设置，包括连接默认值、显示格式和身份验证凭据。

**/etc/cassandra/cassandra.yaml**
> Cassandra 主配置文件，控制集群行为、数据目录、网络设置和数据复制。

# DESCRIPTION

**cqlsh** 是 Cassandra 查询语言 Shell，用于以交互方式或脚本方式执行 CQL 语句。**nodetool** 用于管理 Cassandra 节点操作。

CQL 类似 SQL 但存在一些差异。keyspace 相当于数据库；表具有分区键和聚簇列。查询必须包含分区键才能进行高效查找。

**nodetool status** 以 Up/Down/Normal/Leaving/Joining 状态及令牌所有权展示集群健康状况。**nodetool repair** 确保各副本之间的数据一致性。

快照通过创建 SSTable 的硬链接备份来实现时间点恢复。**cleanup** 在拓扑变更后清除多余数据。**compact** 强制执行 SSTable 压缩。

节点生命周期操作：**drain** 为关机做准备，**decommission** 将节点移出集群并把数据流式传输到其他节点。

# CAVEATS

CQL 不是 SQL；应避免联接和复杂查询。过宽的分区会影响性能。repair 非常消耗资源；应合理安排计划。移除节点前先执行 decommission。身份验证默认关闭。

# HISTORY

Apache Cassandra 最初由 **Facebook** 为收件箱搜索功能开发，并于 **2008 年**开源。它在 **2009 年**成为 Apache 项目，**2010 年**成为顶级项目。Cassandra 结合了 Dynamo 的分布式模型与 Bigtable 的数据模型。DataStax 成立于 **2010 年**，旨在提供商业支持。经过大规模测试后，4.0 版本（2021 年）带来了重大改进。

# SEE ALSO

[scylladb](/man/scylladb)(1), [cockroach](/man/cockroach)(1), [mongo](/man/mongo)(1)

# RESOURCES

```[Source code](https://github.com/apache/cassandra)```

```[Homepage](https://cassandra.apache.org)```

```[Documentation](https://cassandra.apache.org/doc/latest/cassandra/managing/tools/cqlsh.html)```

<!-- verified: 2026-06-23 -->
