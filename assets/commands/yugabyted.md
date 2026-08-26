# TAGLINE

管理 YugabyteDB 分布式 SQL 集群

# TLDR

**启动本地集群**

```yugabyted start```

**以指定数据目录启动**

```yugabyted start --base_dir=[/data/yb]```

**检查集群状态**

```yugabyted status```

**停止集群**

```yugabyted stop```

**使用 PostgreSQL 客户端连接**

```ysqlsh```

**使用 Cassandra 客户端连接**

```ycqlsh```

**向集群添加节点**

```yugabyted start --join=[existing-node]```

**销毁集群数据**

```yugabyted destroy```

# SYNOPSIS

**yugabyted** _command_ [_options_]

**ysqlsh** [_options_]

**ycqlsh** [_options_] [_host_] [_port_]

# YUGABYTED COMMANDS

**start**
> 启动 YugabyteDB 节点。

**stop**
> 停止 YugabyteDB 节点。

**status**
> 显示集群状态。

**destroy**
> 删除集群数据。

**configure**
> 配置集群设置。

**collect_logs**
> 收集日志用于排障。

**version**
> 显示版本信息。

# YUGABYTED OPTIONS

**--base_dir** _path_
> 数据目录。

**--listen** _address_
> 节点的监听地址。

**--join** _host_
> 要加入的集群中的现有节点。

**--cloud_location** _region.zone_
> 云端放置信息。

**--fault_tolerance** _level_
> 容错级别：none、zone、region。

**--ui** _bool_
> 启用管理界面。默认：true。

# YSQLSH PARAMETERS

**-h**, **--host** _host_
> 数据库服务器主机。

**-p**, **--port** _port_
> 数据库端口。默认：5433。

**-U**, **--username** _user_
> 数据库用户名。

**-d**, **--dbname** _database_
> 数据库名称。

**-c** _command_
> 执行单条命令。

**-f** _file_
> 从文件执行命令。

# DESCRIPTION

**yugabyted** 管理 YugabyteDB 集群——一种与 PostgreSQL 兼容的分布式 SQL 数据库。它简化了单节点和多节点部署。

YugabyteDB 提供两种 API：YSQL（兼容 PostgreSQL）和 YCQL（兼容 Cassandra）。SQL 工作负载使用 **ysqlsh**，宽列工作负载使用 **ycqlsh**。

**yugabyted start** 运行 YB-Master 和 YB-TServer 进程。管理界面（默认端口 15433）显示集群健康状况、表和指标。YSQL 通过端口 5433 连接。

对于多节点集群，先正常启动第一个节点，然后在其他节点上使用 **--join**。**--fault_tolerance** 配置复制策略，以在可用区或区域故障时继续存活。

YSQL 支持大多数 PostgreSQL 特性，包括扩展、存储过程和常见 ORM。连接字符串遵循 PostgreSQL 格式。

# CAVEATS

部分 PostgreSQL 特性在分布式环境下不受支持或行为不同。容错至少需要 3 个节点。RF3 复制会使存储需求增至三倍。时钟同步对一致性至关重要。

# HISTORY

YugabyteDB 由 **Yugabyte, Inc.** 创建，该公司由前 Facebook 工程师 **Kannan Muthukkaruppan** 和 **Karthik Ranganathan** 于 **2016 年**创立。它于 **2017 年**首次发布，设计目标是 Google Spanner 的开源替代品。该数据库将类 Spanner 架构与 PostgreSQL 和 Cassandra 兼容性相结合。YugabyteDB 采用 Apache 许可证，企业版功能单独提供。

# SEE ALSO

[psql](/man/psql)(1), [cqlsh](/man/cqlsh)(1), [cockroach](/man/cockroach)(1)
