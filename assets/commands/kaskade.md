# TAGLINE

Apache Kafka 的文本用户界面

# TLDR

以默认连接**启动 kaskade**

```kaskade```

**连接到指定的 broker**

```kaskade -b [localhost:9092]```

# SYNOPSIS

**kaskade** [**-b** _broker_] [_options_]

# DESCRIPTION

**kaskade** 是一个面向 **Apache Kafka** 的 TUI，让你可以直接在终端中与主题交互并消费消息。它提供列出主题、分区、消费者组和组成员的功能，还可以查看主题信息，包括滞后量、副本和记录数。

该工具支持创建、编辑和删除主题，按名称过滤主题，以及消费消息，反序列化支持 JSON、string、integer、long、float、boolean、double、**Avro**、**Protobuf** 和 **Schema Registry** 格式。消息可以按键、值、header 或分区过滤。

# CAVEATS

需要运行中的 Kafka 集群。Schema Registry 集成需要运行中的 Schema Registry 实例。复杂的 Avro/Protobuf schema 在反序列化上可能存在限制。

# HISTORY

**kaskade** 由 **Saul Jabin**（sauljabin）创建，用 **Python** 编写，基于 **Textual** 框架。它的设计目标是为终端带来现代化的交互式 Kafka 浏览体验。

# INSTALL

```brew: brew install kaskade```

<!-- packages: 2026-07-22 -->

# SEE ALSO
