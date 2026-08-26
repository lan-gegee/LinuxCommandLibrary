# TAGLINE

分布式变更数据捕获平台

# TLDR

**启动 Debezium Server**

```debezium-server```

**用 Docker 运行 Debezium Server**

```docker run -it --name debezium -p 8080:8080 -v $PWD/conf:/debezium/conf debezium/server```

**在 Kafka Connect 中运行 MySQL 连接器**

```curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d @[mysql-connector.json]```

**检查连接器状态**

```curl http://localhost:8083/connectors/[connector-name]/status```

**列出正在运行的连接器**

```curl http://localhost:8083/connectors```

# SYNOPSIS

**debezium-server**（独立运行）

Kafka Connect REST API 位于 **http://localhost:8083/connectors**

# CONFIGURATION

**application.properties**（Debezium Server）：
```properties
debezium.source.connector.class=io.debezium.connector.mysql.MySqlConnector
debezium.source.offset.storage.file.filename=data/offsets.dat
debezium.source.database.hostname=localhost
debezium.source.database.port=3306
debezium.source.database.user=debezium
debezium.source.database.password=dbz
debezium.source.database.server.id=1
debezium.source.database.server.name=mydb
debezium.sink.type=kafka
debezium.sink.kafka.producer.bootstrap.servers=localhost:9092
```

# CONNECTORS

**MySQL**：读取 MySQL/MariaDB binlog
**PostgreSQL**：使用逻辑复制
**MongoDB**：读取 oplog
**SQL Server**：使用 CDC 表
**Oracle**：使用 LogMiner 或 XStream
**Cassandra**：读取 commit log

# DESCRIPTION

**Debezium** 是一个开源的分布式变更数据捕获（CDC）平台。它监控数据库并为每一行级变更生成事件，从而实现实时数据流与数据同步。

Debezium 连接器读取数据库事务日志（MySQL binlog、PostgreSQL WAL 等），并将变更转换为事件。这些事件可以发送到 Apache Kafka、Amazon Kinesis、Google Pub/Sub 或其他接收端，供下游应用处理。

该平台既可以作为 Kafka Connect 连接器运行（分布式、可扩展），也可以作为 Debezium Server 运行（独立部署、更简单）。它能捕获插入、更新和删除操作，附带前后值和元数据。

# CAVEATS

需要修改数据库配置以启用日志读取。大型数据库的初始快照可能耗时显著。Kafka Connect 模式需要 Kafka 基础设施。模式变更需要谨慎处理。访问日志所需的数据库权限因平台而异。

# HISTORY

Debezium 由 **Red Hat** 的 **Randall Hauch** 创建，首次发布于 **2016 年**。其开发目标是为微服务架构提供可靠的开源 CDC 方案。这个采用 Apache 许可证的项目吸引了庞大而多元的贡献者社区。**2024 年 12 月**，Debezium 加入 **Commonhaus Foundation**，在保持既有社区和流程的同时确立了厂商中立的治理结构。

# SEE ALSO

[kafka](/man/kafka)(1), [docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1)
