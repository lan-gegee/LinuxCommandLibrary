# TAGLINE

Apache Kafka 命令行界面

# TLDR

**列出主题**

```kafkactl get topics```

**描述主题**

```kafkactl describe topic [my-topic]```

**创建带分区的主题**

```kafkactl create topic [my-topic] --partitions [32]```

从主题开头开始**消费**

```kafkactl consume [my-topic] --from-beginning```

**消费**最后 N 条消息

```kafkactl consume [my-topic] --tail=[5]```

**生产**带键和值的消息

```kafkactl produce [my-topic] --key=[my-key] --value=[my-value]```

以自定义分隔符从 stdin **生产**

```echo "[key]#[value]" | kafkactl produce [my-topic] --separator=#```

**列出消费者组**

```kafkactl get consumer-groups```

**描述消费者组**

```kafkactl describe consumer-group [my-group]```

# SYNOPSIS

**kafkactl** [*global-options*] *command* [*args*]

# DESCRIPTION

**kafkactl** 是一个与 Apache Kafka 集群交互的命令行界面。它涵盖常见的日常任务：列出和管理主题、消费和生产消息、检查消费者组，以及处理 schema registry 编码（Avro、JSON Schema、Protobuf）。

配置文件中的 context 可以让你在多个集群之间切换。可选的 Kubernetes 集成可以在集群内部运行 kafkactl，从而访问只能通过 kubectl 到达的 broker。它支持 bash、zsh 和 fish 的 Shell 补全，包括主题和消费者组的动态补全。

默认配置路径为 **$HOME/.config/kafkactl/config.yml**（也会在 **$HOME/.kafkactl/**、**$APPDATA/kafkactl/** 和 **/etc/kafkactl/** 下查找）。支持 git 根目录附近的项目级配置文件。凭据可以通过交互式提示输入并存储在操作系统钥匙串中，也可以通过配置文件和环境变量提供。

# PARAMETERS

**get topics**

> 列出当前 context 上的主题。

**describe topic** *topic*

> 显示主题详情；**--all-configs** 包含所有主题配置；**--skip-empty** 省略空分区。

**create topic** *topic*

> 创建主题。选项包括 **--partitions**、**--replication-factor**、**--config** *key=value*，以及用于从导出的 JSON 克隆配置的 **--file**。

**alter topic** *topic*

> 修改分区数、副本因子或主题配置。

**consume** *topic*

> 消费消息。常用标志：**--from-beginning**、**--tail=**_N_、**--exit**、**--group**、**--print-keys**、**--print-timestamps**、**--print-headers**、**--print-partitions**、**--from-timestamp**、**--to-timestamp**、**--max-messages**、**--filter-key**、**--filter-value**、**-o** yaml|json。

**produce** *topic*

> 通过 **--key** / **--value**、stdin 或 **--file** 生产消息。支持 **--separator**、**--input-format=json**、**--header**、编码方式、protobuf 类型和 **--rate**。

**get consumer-groups**

> 列出消费者组；可用 **--topic** 过滤。

**describe consumer-group** *group*

> 显示消费者组详情和滞后量；**--only-with-lag** 用于过滤。

**completion** bash|zsh|fish

> 生成 shell 补全脚本。

**--config-file=**_path_

> 使用备用配置文件。

完整命令树和标志请参见 **kafkactl --help** 及在线命令文档。

# CONFIGURATION

创建包含一个或多个命名 context（brokers、TLS、SASL、schema registry、可选的 kubernetes）的 **$HOME/.config/kafkactl/config.yml**。若该文件不存在，会生成适用于本地单节点集群的默认配置。每个配置键都可以被环境变量覆盖。完整的配置结构请参见上游文档。

# CAVEATS

**--from-timestamp** / **--to-timestamp** 在消费者启动时计算 offset；它们不是针对未来时间的按钟表调度的工具。使用错误的编码或 schema 版本生产数据，可能导致消费者无法解码。使用 Kubernetes 模式时，kubectl 访问权限和 RBAC 必须允许所配置的操作。

# INSTALL

```brew: brew install kafkactl```

```nix: nix profile install nixpkgs#kafkactl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kcat](/man/kcat)(1), [kafka-console-consumer](/man/kafka-console-consumer)(1), [kafka-console-producer](/man/kafka-console-producer)(1), [kubectl](/man/kubectl)(1)

# RESOURCES

```[Source code](https://github.com/deviceinsight/kafkactl)```

```[Documentation](https://deviceinsight.github.io/kafkactl/)```

<!-- verified: 2026-07-19 -->
