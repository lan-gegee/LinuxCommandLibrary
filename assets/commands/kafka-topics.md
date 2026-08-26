# TAGLINE

管理 Kafka 主题

# TLDR

**创建主题**

```kafka-topics.sh --create --topic [name] --partitions [3] --replication-factor [1] --bootstrap-server [localhost:9092]```

**列出所有主题**

```kafka-topics.sh --list --bootstrap-server [localhost:9092]```

**描述主题**

```kafka-topics.sh --describe --topic [name] --bootstrap-server [localhost:9092]```

**删除主题**

```kafka-topics.sh --delete --topic [name] --bootstrap-server [localhost:9092]```

**修改分区数**

```kafka-topics.sh --alter --topic [name] --partitions [6] --bootstrap-server [localhost:9092]```

# SYNOPSIS

**kafka-topics.sh** [_options_]

# PARAMETERS

**--create**
> 创建新主题。

**--list**
> 列出所有主题。

**--describe**
> 显示主题详情。

**--delete**
> 删除主题。

**--alter**
> 修改主题配置。

**--topic** _name_
> 主题名称。

**--partitions** _n_
> 分区数量。

**--replication-factor** _n_
> 副本因子。

**--bootstrap-server** _servers_
> Kafka broker 地址。

**--config** _key=value_
> 主题配置。

**--if-exists**
> 仅当主题存在时执行。

**--if-not-exists**
> 仅当主题不存在时执行。

# DESCRIPTION

**kafka-topics.sh** 用于管理 Kafka 主题。主题是 Kafka 中组织消息的核心抽象，通过分区实现并行处理，通过副本保证持久性。

# TOPIC CONFIGURATIONS

```bash
# Set retention
--config retention.ms=86400000

# Set cleanup policy
--config cleanup.policy=compact

# Set max message size
--config max.message.bytes=1048576
```

# CAVEATS

分区只能增加不能减少。副本因子受 broker 数量限制。删除操作可能需要在配置中启用。ZooKeeper 连接已弃用。

# INSTALL

```pacman: sudo pacman -S kafka```

```brew: brew install kafka```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kafka](/man/kafka)(1), [kafkacat](/man/kafkacat)(1)
