# TAGLINE

管理 RabbitMQ 集群成员关系与状态

# TLDR

**显示集群状态**

```rabbitmqctl cluster_status```

**加入集群**

```rabbitmqctl join_cluster [rabbit@node1]```

**离开集群**

```rabbitmqctl reset```

**更改节点类型**

```rabbitmqctl change_cluster_node_type [disc]```

# SYNOPSIS

**rabbitmqctl** _cluster_command_ [_options_]

# PARAMETERS

**cluster_status**
> 显示集群状态。

**join_cluster** _node_
> 加入现有集群。

**forget_cluster_node** _node_
> 从集群中移除离线节点。

**change_cluster_node_type** _type_
> 更改为 disc 或 ram 节点。

**rename_cluster_node** _old_ _new_
> 重命名集群节点。

**force_boot**
> 当节点是最后关机的节点时强制其启动。

# DESCRIPTION

**rabbitmqctl** 的集群命令管理 RabbitMQ 集群成员关系。可以组建集群、添加/移除节点以及监控集群健康状况。属于 RabbitMQ 服务器管理的组成部分。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(1), [rabbitmq-queues](/man/rabbitmq-queues)(1)
