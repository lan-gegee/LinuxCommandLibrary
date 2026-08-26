# TAGLINE

Kafka topic 工具，支持生产、消费和基础管理操作

# TLDR

从 topic **消费**

```kt consume -topic [my-topic]```

**生产**消息

```echo "[hello]" | kt produce -topic [my-topic]```

**列出** topic

```kt topic -filter [my-]```

**打印**消息键/值的模式

```kt consume -topic [t] -value-as-string```

# SYNOPSIS

**kt** *command* [*options*]

# DESCRIPTION

**kt** 是一款轻量级 Kafka CLI，可用于生产和消费消息、列出 topic 以及执行简单的管理任务，无需面对完整的 JVM **kafka-console-*** 工具集。通过命令行标志或环境变量（**KT_BROKERS** 等）配置 broker。安装方式：**go install github.com/fgeller/kt/v14@latest**（模块路径可能随主版本变化）。

# PARAMETERS

**consume** **-topic** *name*

> 读取消息。

**produce** **-topic** *name*

> 从 stdin 写入消息。

**topic** / **group** / **admin** 子命令

> 元数据和消费者组操作——参见 **kt -h**。

**-brokers** *list*

> 引导服务器。

# CAVEATS

认证模式（SASL/SSL）需要匹配的标志/配置。大型集群需要谨慎设置过滤条件。用 Go 安装时请确认模块版本。

# INSTALL

```nix: nix profile install nixpkgs#kt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kcat](/man/kcat)(1), [kafkacat](/man/kafkacat)(1), [kafka-console-consumer](/man/kafka-console-consumer)(1)

# RESOURCES

```[Source code](https://github.com/fgeller/kt)```

<!-- verified: 2026-07-19 -->
