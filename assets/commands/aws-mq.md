# TAGLINE

管理 Amazon MQ 消息代理。

# TLDR

**列出所有代理**

```aws mq list-brokers```

**创建 ActiveMQ 代理**

```aws mq create-broker --broker-name [my-broker] --engine-type ACTIVEMQ --engine-version [5.17.6] --host-instance-type [mq.m5.large] --deployment-mode SINGLE_INSTANCE --users Username=[admin],Password=[password]```

**创建 RabbitMQ 代理**

```aws mq create-broker --broker-name [my-broker] --engine-type RABBITMQ --engine-version [3.13] --host-instance-type [mq.m5.large] --deployment-mode SINGLE_INSTANCE --users Username=[admin],Password=[password]```

**描述代理**并获取其详细信息

```aws mq describe-broker --broker-id [broker-id]```

**列出所有配置**

```aws mq list-configurations```

**重启代理**

```aws mq reboot-broker --broker-id [broker-id]```

**删除代理**

```aws mq delete-broker --broker-id [broker-id]```

# SYNOPSIS

**aws mq** _command_ [_options_]

# DESCRIPTION

**aws mq** 是 AWS CLI 中用于管理 Amazon MQ 的接口。Amazon MQ 是一项托管消息代理服务，支持 **Apache ActiveMQ** 和 **RabbitMQ** 引擎。Amazon MQ 负责预置、运行和维护消息代理，处理硬件预置、代理设置、软件升级和故障检测等基础设施任务。

Amazon MQ 兼容标准消息传递 API 和协议，包括 JMS、NMS、AMQP、STOMP、MQTT 和 WebSocket，无需重写应用程序代码即可将现有消息传递工作负载迁移到云端。

代理可以部署为用于开发的**单实例**模式，也可以部署为跨多个可用区的**主/备（active/standby）**模式以实现生产环境高可用。

# COMMANDS

**create-broker**
> 创建新的消息代理

**delete-broker**
> 删除现有代理

**describe-broker**
> 获取代理的配置、状态和端点

**describe-broker-engine-types**
> 列出支持的 ActiveMQ 和 RabbitMQ 引擎版本

**describe-broker-instance-options**
> 列出给定引擎和存储类型可用的代理实例类型选项

**list-brokers**
> 列出账户中的所有代理

**reboot-broker**
> 重启代理

**update-broker**
> 修改代理配置和维护设置

**promote**
> 将数据复制的副本代理提升为主代理

**create-configuration**
> 创建代理配置（ActiveMQ XML 或 RabbitMQ Cuttlefish）

**describe-configuration**
> 获取配置详情

**describe-configuration-revision**
> 获取指定的配置修订版本

**list-configurations**
> 列出所有配置

**list-configuration-revisions**
> 列出某个配置的修订版本

**update-configuration**
> 以新修订版本更新配置

**create-user**
> 在代理上创建新的 ActiveMQ 用户

**update-user**
> 更新现有 ActiveMQ 用户（组、密码、控制台访问权限）

**delete-user**
> 删除 ActiveMQ 用户

**list-users**
> 列出代理上的所有 ActiveMQ 用户

**describe-user**
> 获取 ActiveMQ 用户详情

**create-tags** / **delete-tags** / **list-tags**
> 管理代理和配置上的资源标签

# CAVEATS

代理创建需要几分钟时间。实例类型和存储无法在不停机的情况下更改。ActiveMQ 与 RabbitMQ 的配置差异很大；用户管理命令仅适用于 ActiveMQ 代理，RabbitMQ 用户需通过 RabbitMQ Web 控制台管理。最大消息大小受引擎限制（ActiveMQ 默认 100MB，RabbitMQ 为 128MB）。

# HISTORY

Amazon MQ 于 **2017 年 11 月**上线，最初支持 Apache ActiveMQ Classic。RabbitMQ 引擎支持于 **2020 年 10 月**加入。对 ActiveMQ Artemis（下一代 ActiveMQ）的支持目前尚未在 Amazon MQ 中提供。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-sqs](/man/aws-sqs)(1), [aws-sns](/man/aws-sns)(1), [aws-kafka](/man/aws-kafka)(1)
