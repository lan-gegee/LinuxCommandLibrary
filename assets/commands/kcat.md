# TAGLINE

Apache Kafka 的通用非 JVM 生产者和消费者

# TLDR

**从主题消费消息**

```kcat -b [localhost:9092] -t [topic] -C```

**向主题生产消息**

```echo "[message]" | kcat -b [localhost:9092] -t [topic] -P```

**列出元数据**

```kcat -b [localhost:9092] -L```

**以自定义格式消费**

```kcat -b [localhost:9092] -t [topic] -C -f '%k: %s\n'```

**从头开始消费**

```kcat -b [localhost:9092] -t [topic] -C -o beginning```

**查询水位线**

```kcat -b [localhost:9092] -t [topic] -Q```

# SYNOPSIS

**kcat** [_options_] _mode_

# PARAMETERS

**-b** _brokers_
> 逗号分隔的 Kafka broker 列表（host[:port]）。

**-t** _topic_
> 要生产到或从中消费的主题。

**-p** _partition_
> 要生产到或从中消费的分区。

**-C**
> 消费者模式。

**-P**
> 生产者模式。

**-L**
> 元数据列表模式。

**-Q**
> 按时间戳查询 offset。

**-G** _group_
> 高层消费者组（要求 broker >= 0.9.0）。

**-o** _offset_
> 起始 offset（beginning、end、stored 或数字；负数表示从末尾倒数）。

**-e**
> 消费完最后一条消息后退出。

**-q**
> 静默模式，无信息性输出。

**-f** _format_
> 输出格式字符串（如 `%t %p %o %k %s\n`）。

**-J**
> 以 JSON 封装输出消息。

**-K** _sep_
> 生产/消费时的键分隔符。

**-D** _sep_
> 消息分隔符（默认换行符）。

**-X** _prop=val_
> 设置一个 librdkafka 配置属性。

**-F** _file_
> 从文件读取 librdkafka 配置。

# DESCRIPTION

**kcat**（原名 kafkacat）是 Apache Kafka 的通用非 JVM 生产者和消费者。它用 C 语言基于 **librdkafka** 编写，提供一个与 Kafka 集群交互的轻量级 CLI。它支持生产、消费、列出元数据、查询 offset，以及通过 Schema Registry 处理 Avro/JSON 载荷。

# HISTORY

该工具最初名为 **kafkacat**，2021 年更名为 **kcat** 以与上游品牌保持一致。根据发行版的打包方式，两个名称可能都存在。

# INSTALL

```apt: sudo apt install kcat```

```dnf: sudo dnf install kcat```

```apk: sudo apk add kcat```

```brew: brew install kcat```

```nix: nix profile install nixpkgs#kcat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kafka](/man/kafka)(1), [kafkacat](/man/kafkacat)(1), [kafka-topics](/man/kafka-topics)(1)
