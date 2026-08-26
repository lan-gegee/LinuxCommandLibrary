# TAGLINE

诊断 RabbitMQ 节点与集群健康状态

# TLDR

**检查本地节点是否在运行**

```rabbitmq-diagnostics check_running```

**打印集群状态**

```rabbitmq-diagnostics cluster_status```

**检查资源告警**（内存、磁盘）

```rabbitmq-diagnostics check_alarms```

**内存占用明细**

```rabbitmq-diagnostics memory_breakdown```

**检查监听端口**是否可达

```rabbitmq-diagnostics check_port_connectivity```

**检查虚拟主机**是否正常

```rabbitmq-diagnostics check_virtual_hosts```

**以 JSON 输出**便于解析

```rabbitmq-diagnostics status --formatter json```

# SYNOPSIS

**rabbitmq-diagnostics** [_options_] _command_ [_command_options_]

# PARAMETERS

**-n** _node_
> 目标节点名（默认：**rabbit@$(hostname)**）。

**-l**, **--longnames**
> 使用完全限定节点名（FQDN）。

**-t** _timeout_
> 操作超时时间，单位为秒。

**--formatter** _format_
> 输出格式：**table**（默认）、**json**、**csv**、**erlang**。

**-q**, **--quiet**
> 隐藏信息性标头和状态行。

**-s**, **--silent**
> 检查成功时不输出任何内容（适用于监控场景）。

# HEALTH CHECK COMMANDS

**check_running**
> 节点正在运行且 rabbit 应用已启动。

**check_local_alarms**
> 本地节点上没有生效的资源告警。

**check_alarms**
> 整个集群中没有任何资源告警。

**check_port_connectivity**
> 所有监听端口都能接受 TCP 连接。

**check_port_listener** _port_
> 特定端口存在活动监听器。

**check_protocol_listener** _proto_
> 特定协议（amqp、mqtt、stomp）存在活动监听器。

**check_virtual_hosts**
> 所有虚拟主机都在目标节点上运行。

**check_node_is_mirror_sync_critical**
> 没有 classic 镜像队列处于同步临界状态。

# OBSERVABILITY COMMANDS

**status**
> 高层节点状态（版本、监听器、内存）。

**cluster_status**
> 成员关系、分区以及各节点的监听器信息。

**memory_breakdown**
> 详细的内存统计（队列、二进制数据、ETS、进程……）。

**environment**
> 所有 RabbitMQ 应用的生效应用环境。

**listeners**
> 列出所有已配置的网络监听器。

**runtime_thread_stats**
> BEAM 调度器/线程统计信息。

# DESCRIPTION

**rabbitmq-diagnostics** 提供 RabbitMQ 节点和集群的健康检查与可观测性命令。它是监控脚本和 Kubernetes 探针的推荐工具，取代了以往许多对 **rabbitmqctl** 的临时用法。

健康检查失败时返回非零退出码，因此很容易接入存活/就绪探针和 CI 门禁。"更深层的"检查（如 **check_alarms**）耗时更长，对节点的检验也更全面，所以高频探针请使用 **check_running**，把更重的检查留给低频监控。

# CAVEATS

需要有正在运行的 RabbitMQ 节点，且 Erlang cookie 与节点一致。某些检查需要管理插件或特定 RabbitMQ 版本。机器处理建议使用 **--formatter json**——table 输出格式不稳定。

# HISTORY

于 **RabbitMQ 3.8**（2019 年）作为专用诊断 CLI 推出，接管了此前归属于 **rabbitmqctl** 的健康检查职责。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(8), [rabbitmq-plugins](/man/rabbitmq-plugins)(8), [rabbitmq-server](/man/rabbitmq-server)(8)
