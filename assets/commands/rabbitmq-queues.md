# TAGLINE

检查和管理 RabbitMQ 队列

# TLDR

**列出队列**

```rabbitmq-queues list```

**显示队列信息**

```rabbitmq-queues info [queue_name]```

**检查队列是否达到 quorum 临界状态**

```rabbitmq-queues check_if_node_is_quorum_critical```

**重新均衡队列主副本**

```rabbitmq-queues rebalance all```

# SYNOPSIS

**rabbitmq-queues** _command_ [_options_]

# PARAMETERS

**list**
> 列出所有队列。

**info** _queue_
> 显示队列信息。

**rebalance** _type_
> 重新均衡队列主副本（all、quorum、classic）。

**check_if_node_is_quorum_critical**
> 检查 quorum 队列健康状况。

**grow** _node_ _strategy_
> 添加队列成员。

**shrink** _node_
> 移除队列成员。

# DESCRIPTION

**rabbitmq-queues** 管理 RabbitMQ 队列。可以检查队列状态、重新均衡负载以及管理 quorum 队列成员。属于 RabbitMQ CLI 工具集。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(1), [rabbitmq-streams](/man/rabbitmq-streams)(1)
