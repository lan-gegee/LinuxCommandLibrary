# TAGLINE

管理 Redpanda 流处理主题与集群

# TLDR

**创建主题**

```rpk topic create [topic-name]```

**列出主题**

```rpk topic list```

**生产消息**

```rpk topic produce [topic] -k [key]```

**消费消息**

```rpk topic consume [topic]```

**描述集群**

```rpk cluster info```

**检查配置**

```rpk redpanda config```

# SYNOPSIS

**rpk** _command_ [_subcommand_] [_options_]

# PARAMETERS

**topic**
> 主题操作。

**cluster**
> 集群命令。

**redpanda**
> Redpanda 管理。

**acl**
> ACL 管理。

**group**
> 消费者组。

**-X** _PROP=VAL_
> 客户端属性。

**--brokers** _HOSTS_
> Broker 地址。

# DESCRIPTION

**rpk** 是 Redpanda 的命令行界面，Redpanda 是一个兼容 Kafka 的流式数据平台。它提供管理主题、生产和消费消息、管理集群以及配置 Redpanda 节点等命令，其语法对 Kafka CLI 工具的用户来说十分熟悉。

主题操作包括创建、删除、描述和列出主题，以及向主题生产消息、从主题消费消息，可用于测试和调试。集群命令提供健康检查、配置巡检和 broker 管理。该工具还负责 ACL（访问控制列表）管理和消费者组操作。

**-X** 标志用于传递客户端属性，例如身份验证凭据和 TLS 设置；**--brokers** 则指定要连接的集群端点。

# CAVEATS

需要 Redpanda/Kafka。需要网络访问。可能需要进行身份验证。

# HISTORY

**rpk** 是 **Redpanda** 的命令行界面，后者是一个用 C++ 编写、兼容 Kafka 的流处理平台。

# SEE ALSO

[kafka-topics](/man/kafka-topics)(1), [kafkacat](/man/kafkacat)(1)
