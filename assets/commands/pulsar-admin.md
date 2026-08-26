# TAGLINE

Apache Pulsar 集群管理工具

# TLDR

**列出**租户

```pulsar-admin tenants list```

**列出**租户中的命名空间

```pulsar-admin namespaces list [tenant]```

**列出**命名空间中的主题

```pulsar-admin topics list [tenant/namespace]```

**创建**主题

```pulsar-admin topics create persistent://[tenant]/[namespace]/[topic]```

查看主题统计信息

```pulsar-admin topics stats [topic]```

检查 broker 状态

```pulsar-admin brokers list [cluster]```

**创建**租户

```pulsar-admin tenants create [tenant]```

设置命名空间保留策略

```pulsar-admin namespaces set-retention [tenant/namespace] --size [10G] --time [3d]```

# SYNOPSIS

**pulsar-admin** _command_ [_options_]

# ADMIN COMMANDS

**tenants** list|create|delete|get|update
> 管理租户（多租户机制）。

**namespaces** list|create|delete|policies
> 管理命名空间。

**topics** list|create|delete|stats|subscriptions
> 管理主题和订阅。

**brokers** list|leader|namespaces
> Broker 信息。

**clusters** list|create|delete|update
> 集群管理。

**functions** create|delete|list|status
> 管理 Pulsar Functions。

**sources**/**sinks** create|delete|list
> 管理 IO 连接器。

# PARAMETERS

**--admin-url** _url_
> Pulsar 管理服务 URL。

**--auth-plugin** _class_
> 身份验证插件类。

**--auth-params** _params_
> 身份验证参数。

**--tls-trust-certs-filepath** _path_
> TLS 信任证书文件的路径。

# DESCRIPTION

**pulsar-admin** 用于管理 Apache Pulsar 集群，处理租户、命名空间、主题和集群配置。它提供对整个 Pulsar 基础设施的管理控制。

Pulsar 的多租户模型按层级组织资源：集群包含租户，租户包含命名空间，命名空间包含主题。每一层都有可配置的策略。

主题使用 **persistent://tenant/namespace/topic** 格式（或 **non-persistent://**）。订阅定义消费者接收消息的方式：exclusive（独占）、shared（共享）、failover（故障转移）或 key_shared（按键共享）。

**pulsar-admin topics stats** 显示消息速率、存储大小、订阅以及生产者/消费者连接。这有助于监控主题的健康状况。

Pulsar Functions 可直接在 broker 上运行轻量级流处理。Sources 和 sinks 连接外部系统，实现数据的导入和导出。

# CAVEATS

受保护的集群需要正确配置身份验证。根据 broker 设置，主题创建可能是自动的。命名空间策略影响其中的所有主题。Functions 需要启用 function worker。

# HISTORY

Apache Pulsar 最初由 **Yahoo!** 开发，于 **2016 年**开源，并在 **2018 年**成为 Apache 顶级项目。Pulsar 为多租户和地理复制而设计，将存储（BookKeeper）与服务（broker）分离。它提供主题压缩、分层存储和内置 schema registry 等特性。StreamNative 提供商业支持。

# SEE ALSO

[nats](/man/nats)(1), [rabbitmqctl](/man/rabbitmqctl)(1)
