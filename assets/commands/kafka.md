# TAGLINE

分布式事件流平台

# TLDR

**启动 Kafka 服务器**

```kafka-server-start.sh [config/server.properties]```

**停止 Kafka 服务器**

```kafka-server-stop.sh```

**创建带分区和副本的主题**

```kafka-topics.sh --create --topic [mytopic] --partitions [3] --replication-factor [1] --bootstrap-server [localhost:9092]```

**列出所有主题**

```kafka-topics.sh --list --bootstrap-server [localhost:9092]```

**描述主题**

```kafka-topics.sh --describe --topic [mytopic] --bootstrap-server [localhost:9092]```

**向主题生产消息**

```kafka-console-producer.sh --topic [mytopic] --bootstrap-server [localhost:9092]```

**从头开始消费消息**

```kafka-console-consumer.sh --topic [mytopic] --from-beginning --bootstrap-server [localhost:9092]```

# SYNOPSIS

**kafka-server-start.sh** _config_

# DESCRIPTION

**Apache Kafka** 是一个分布式事件流平台。它为实时数据管道和流应用提供高吞吐、低延迟的消息处理。

Kafka 将消息组织成主题，通过分区实现并行处理，通过副本实现容错。生产者发送消息；消费者读取消息。

# KEY CONCEPTS

- **Topic**：消息的类别
- **Partition**：有序且不可变的序列
- **Producer**：向主题发送消息
- **Consumer**：从主题读取消息
- **Broker**：Kafka 服务器节点
- **Consumer Group**：协同工作的消费者集合

# CONFIGURATION

```properties
# server.properties (KRaft mode, Kafka 3.3+)
node.id=1
process.roles=broker,controller
controller.quorum.voters=1@localhost:9093
listeners=PLAINTEXT://:9092,CONTROLLER://:9093
log.dirs=/var/kafka-logs
```

```properties
# server.properties (legacy ZooKeeper mode)
broker.id=0
listeners=PLAINTEXT://:9092
log.dirs=/var/kafka-logs
zookeeper.connect=localhost:2181
```

# CAVEATS

Kafka 4.0 移除了 ZooKeeper 支持；新部署必须使用 KRaft 模式。内存和磁盘占用高。主题配置会影响保留策略和存储。消费者组重平衡可能导致临时处理延迟。

# HISTORY

Kafka 由 **LinkedIn** 开发并于 **2011** 年开源。它以作家 Franz Kafka 命名，后来成为 Apache 项目，如今已是事件驱动架构的基础设施。

# INSTALL

```pacman: sudo pacman -S kafka```

```brew: brew install kafka```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kafka-topics](/man/kafka-topics)(1), [kafkacat](/man/kafkacat)(1)
