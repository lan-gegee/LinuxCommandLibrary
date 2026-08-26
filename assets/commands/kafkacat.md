# TAGLINE

命令行 Kafka 生产者和消费者

# TLDR

**生产消息**

```echo "[message]" | kafkacat -P -b [localhost:9092] -t [topic]```

**消费消息**

```kafkacat -C -b [localhost:9092] -t [topic]```

**从头开始消费**

```kafkacat -C -b [localhost:9092] -t [topic] -o beginning```

**列出主题**

```kafkacat -L -b [localhost:9092]```

**从文件生产消息**

```kafkacat -P -b [localhost:9092] -t [topic] [file.txt]```

**按格式消费**

```kafkacat -C -b [localhost:9092] -t [topic] -f '[%T] %k: %s\n'```

**使用分隔符生产带键的消息**

```echo "[key]:[value]" | kafkacat -P -b [localhost:9092] -t [topic] -K ":"```

**消费 N 条消息**后退出

```kafkacat -C -b [localhost:9092] -t [topic] -c [10]```

# SYNOPSIS

**kafkacat** [_options_]

# PARAMETERS

**-P**
> 生产者模式。

**-C**
> 消费者模式。

**-L**
> 元数据列表模式。

**-b** _brokers_
> broker 列表。

**-t** _topic_
> 主题名称。

**-p** _partition_
> 分区编号。

**-o** _offset_
> Offset：beginning、end、stored 或数字。

**-K** _delim_
> 键分隔符。

**-f** _format_
> 输出格式字符串。

**-c** _count_
> 消费 count 条消息后退出。

**-e**
> 到达主题末尾时退出。

**-G** _group_ _topic_
> 消费者组模式（高层均衡消费者）。

**-X** _property=value_
> 设置 librdkafka 属性（如 security.protocol=SSL）。

# DESCRIPTION

**kafkacat**（也称 kcat）是一个命令行 Kafka 生产者和消费者。它比 Kafka 内置的 shell 脚本更快更简单，适合测试和调试。

# FORMAT STRINGS

```
%T  - Timestamp
%k  - Key
%s  - Message (payload)
%p  - Partition
%o  - Offset
%t  - Topic
```

# CAVEATS

较新版本已更名为 kcat。需要 librdkafka。不随 Kafka 发行版附带。部分功能需要特定版本的 librdkafka。

# HISTORY

kafkacat 由 **Magnus Edenhill** 创建，他也是 librdkafka 的作者。它已更名为 **kcat**，但 kafkacat 这个名字仍被广泛使用。

# INSTALL

```brew: brew install kafkacat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kcat](/man/kcat)(1), [kafka](/man/kafka)(1), [kafka-topics](/man/kafka-topics)(1)
