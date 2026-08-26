# TAGLINE

Apache Kafka TUI 客户端

# TLDR

**启动 Kafka TUI**

```ktea```

**连接到指定集群**

```ktea -c [cluster_name]```

# SYNOPSIS

**ktea** [_options_]

# DESCRIPTION

**ktea** 是一款 Apache Kafka TUI 客户端，旨在简化和加速与 Kafka 集群的交互。它提供多集群支持、topic 管理、文本/JSON/Avro 格式的记录消费、消费者组监控以及 schema registry 集成。

表格可以使用类 vi 的按键导航（**j**/**k** 上下移动，**d**/**u** 下翻/上翻页）。该工具适合快速查看 topic、读取事件和管理 Kafka 资源，而无需 GUI 客户端的开销。

# CAVEATS

需要能访问正在运行的 Kafka 集群。Schema registry 集成需要兼容的 schema registry 服务。

# HISTORY

**ktea** 由 **Jonas Geiregat** (jonas-grgt) 创建，使用 **Go** 编写。它的设计目标是让用户从终端快速远程访问 Kafka 集群。

# INSTALL

```brew: brew install ktea```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kplay](/man/kplay)(1), [kaskade](/man/kaskade)(1)
