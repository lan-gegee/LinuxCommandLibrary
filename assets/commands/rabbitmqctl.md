# TAGLINE

管理 RabbitMQ 的命令行工具

# TLDR

**列出队列**

```rabbitmqctl list_queues```

**列出队列及详细信息**

```rabbitmqctl list_queues name messages consumers```

**列出交换机**

```rabbitmqctl list_exchanges```

**列出连接**

```rabbitmqctl list_connections```

**添加用户**

```rabbitmqctl add_user [username] [password]```

**设置用户权限**

```rabbitmqctl set_permissions [username] ".*" ".*" ".*"```

**删除队列**

```rabbitmqctl delete_queue [queue_name]```

**集群状态**

```rabbitmqctl cluster_status```

# SYNOPSIS

**rabbitmqctl** [_-n node_] [_-t timeout_] _command_ [_args_]

# PARAMETERS

**list_queues** [_COLUMNS_]
> 列出队列及其所选信息。

**list_exchanges** [_COLUMNS_]
> 列出交换机。

**list_bindings**
> 列出绑定关系。

**list_connections** [_COLUMNS_]
> 列出连接。

**list_channels** [_COLUMNS_]
> 列出通道。

**list_users**
> 列出用户。

**add_user** _USER_ _PASS_
> 添加用户。

**delete_user** _USER_
> 删除用户。

**set_permissions** _USER_ _CONF_ _WRITE_ _READ_
> 设置权限。

**delete_queue** _QUEUE_
> 删除队列。

**purge_queue** _QUEUE_
> 清空队列。

**cluster_status**
> 显示集群状态。

**-n** _NODE_
> 目标节点。

**-t** _TIMEOUT_
> 命令超时时间。

# DESCRIPTION

**rabbitmqctl** 管理 RabbitMQ 消息代理。它控制服务器操作、进行用户管理，并提供监控信息。

队列列表会显示消息数、消费者连接和内存占用。列选择可自定义输出，方便监控脚本使用。

用户管理负责身份验证。权限模式（configure、write、read）控制对虚拟主机和资源的访问。

集群命令管理分布式部署。状态信息展示节点成员和同步情况。

该工具通过 Erlang distribution 进行控制。在集群环境中，节点名用于标识目标。

监控命令支持与外部系统集成。JSON 输出便于自动化处理。

# CAVEATS

需要访问 Erlang cookie。部分命令需要管理员权限。集群操作需要谨慎协调。

# HISTORY

自 **Rabbit Technologies**（后被 VMware 收购，现为 Broadcom 一部分）于 **2007 年**前后发布 broker 以来，**rabbitmqctl** 一直是 RabbitMQ 的管理 CLI。它至今仍是主要的管理接口。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmq-server](/man/rabbitmq-server)(8), [rabbitmq-plugins](/man/rabbitmq-plugins)(8), [rabbitmq-diagnostics](/man/rabbitmq-diagnostics)(8)
