# TAGLINE

分布式 SQL 数据库 CLI

# TLDR

**启动单节点集群**

```cockroach start-single-node --insecure```

**启动 SQL shell**

```cockroach sql --insecure --host=[localhost]```

**执行 SQL 语句**

```cockroach sql --insecure -e "[SELECT * FROM users]"```

**初始化集群**

```cockroach init --insecure --host=[localhost]```

**显示节点状态**

```cockroach node status --insecure```

**创建数据库**

```cockroach sql --insecure -e "CREATE DATABASE [mydb]"```

**将 CSV 数据导入表**

```cockroach sql --insecure -e "IMPORT INTO [table] CSV DATA ('[file_url]')"```

**启动临时演示集群**

```cockroach demo```

**显示集群设置**

```cockroach sql --insecure -e "SHOW CLUSTER SETTINGS"```

# SYNOPSIS

**cockroach** _command_ [_options_]

# DESCRIPTION

**cockroach** 是 CockroachDB 的命令行接口，CockroachDB 是一款为云原生应用设计的分布式 SQL 数据库。它提供全面的工具来管理多节点集群、执行 SQL 查询、执行备份和恢复，以及监控集群健康状态和性能。

CockroachDB 将 NoSQL 系统的可扩展性与传统关系型数据库的一致性保证和 SQL 接口结合在一起。该 CLI 处理集群初始化、节点管理、面向安全部署的证书生成，以及交互式或编程式的直接 SQL 执行。

该工具同时支持使用 TLS 证书的安全生产部署和不安全的开发环境。它还包含一个演示模式，无需持久化存储或集群设置即可进行实验和测试。

# COMMANDS

**start**
> 启动一个 CockroachDB 节点

**start-single-node**
> 启动单节点集群

**init**
> 初始化多节点集群

**sql**
> 打开 SQL shell 或执行语句

**node**
> 管理集群节点

**quit**
> 排空连接并关闭节点

**cert**
> 创建 CA、节点和客户端证书

**debug**
> 用于检查集群状态的调试命令

**workload**
> 数据与查询负载生成器（如基准测试）

**nodelocal upload**
> 将文件上传到节点的本地文件系统

**version**
> 显示版本

**demo**
> 启动临时演示集群

# PARAMETERS

**--insecure**
> 禁用 TLS（仅限开发）

**--host**=_address_
> 服务器地址

**--port**=_port_
> 服务器端口（默认：26257）

**--certs-dir**=_path_
> 证书目录

**--store**=_path_
> 数据存储位置

**-e**, **--execute**=_sql_
> 执行 SQL 语句

**--url**=_url_
> 连接 URL

**--log-dir**=_path_
> 日志文件目录

**--listen-addr**=_address_
> 监听的地址和端口（默认：localhost:26257）

# ENVIRONMENT

标志可通过环境变量设置：COCKROACH_HOST、COCKROACH_PORT、COCKROACH_USER、COCKROACH_INSECURE

# CAVEATS

仅在开发环境中使用 --insecure。生产环境需要 TLS 证书。兼容 PostgreSQL 线路协议。

# SEE ALSO

[psql](/man/psql)(1), [mysql](/man/mysql)(1), [sqlite3](/man/sqlite3)(1)
