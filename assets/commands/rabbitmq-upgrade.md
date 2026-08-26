# TAGLINE

检查并为 RabbitMQ 升级做准备

# TLDR

**检查升级就绪状态**

```rabbitmq-upgrade await_online_quorum_plus_one```

**排空节点以便升级**

```rabbitmq-upgrade drain```

**升级后恢复节点**

```rabbitmq-upgrade revive```

# SYNOPSIS

**rabbitmq-upgrade** _command_ [_options_]

# PARAMETERS

**await_online_quorum_plus_one**
> 等待足够数量的在线副本。

**drain**
> 为停机/升级准备节点。

**revive**
> 升级后恢复节点。

**post_upgrade**
> 执行升级后任务。

**-n** _node_
> 目标节点。

# DESCRIPTION

**rabbitmq-upgrade** 协助进行 RabbitMQ 集群升级。它通过管理节点状态和检查 quorum 健康状况来确保安全的滚动升级。属于 RabbitMQ CLI 工具集。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(1), [rabbitmq-queues](/man/rabbitmq-queues)(1)
