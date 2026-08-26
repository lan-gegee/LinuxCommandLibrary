# TAGLINE

管理 RabbitMQ 流队列

# TLDR

**列出**流协议**连接**

```rabbitmq-streams list_stream_connections```

**显示**流的**状态**

```rabbitmq-streams stream_status --vhost [vhost] --stream [stream_name]```

在给定节点上**添加**流**副本**

```rabbitmq-streams add_replica --vhost [vhost] [stream_name] [node]```

从给定节点**删除**流**副本**

```rabbitmq-streams delete_replica --vhost [vhost] [stream_name] [node]```

**重启**流及其所有**副本**

```rabbitmq-streams restart_stream --vhost [vhost] [stream_name]```

以**首选主节点**重启流

```rabbitmq-streams restart_stream --vhost [vhost] --preferred-leader-node [node] [stream_name]```

# SYNOPSIS

**rabbitmq-streams** [**-n** _node_] [**-t** _timeout_] [**-l**|**-q**] _command_ [_command options_]

# PARAMETERS

**-n** _node_
> 执行命令的目标节点。默认为本地主机对应的节点。

**-t** _timeout_
> 操作超时时间（秒）。默认值因命令而异。

**-l**, **--longnames**
> 使用长节点名（FQDN）。必须与 broker 的配置一致。

**-q**, **--quiet**
> 隐藏信息性消息，只输出必要数据。

**--formatter** _formatter_
> 输出格式：csv、erlang、json、pretty_table、table。

# SUBCOMMANDS

**add_replica** _stream_ _node_
> 在给定节点上添加流副本。

**delete_replica** _stream_ _node_
> 从给定节点移除流副本。

**stream_status** **--stream** _stream_
> 显示流的状态，包括主副本和其他副本。

**restart_stream** _stream_
> 重启流及其所有副本。可接受 **--preferred-leader-node** 将主副本放到特定节点上。

**list_stream_connections** [_connectioninfoitem_...]
> 返回流协议连接统计信息。

**list_stream_consumers** [**-p** _vhost_] [_consumerinfoitem_...]
> 返回附着到流的消费者。

**list_stream_publishers** [**-p** _vhost_] [_publisherinfoitem_...]
> 返回附着到流的发布者。

**list_stream_consumer_groups** [**-p** _vhost_]
> 列出流的单活跃消费者组。

# DESCRIPTION

**rabbitmq-streams** 是用于管理 RabbitMQ 流的命令行工具。流是一种持久化、可复制、只追加的日志数据结构，专为高吞吐量消息场景设计。该工具管理流副本、监控流状态并列出流连接与消费者。属于 RabbitMQ CLI 工具套件。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(1), [rabbitmq-queues](/man/rabbitmq-queues)(1), [rabbitmq-diagnostics](/man/rabbitmq-diagnostics)(1)
