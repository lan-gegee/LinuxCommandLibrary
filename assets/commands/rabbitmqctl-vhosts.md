# TAGLINE

管理 RabbitMQ 虚拟主机

# TLDR

**列出虚拟主机**

```rabbitmqctl list_vhosts```

**添加虚拟主机**

```rabbitmqctl add_vhost [vhost_name]```

**删除虚拟主机**

```rabbitmqctl delete_vhost [vhost_name]```

**设置 vhost 限制**

```rabbitmqctl set_vhost_limits -p [vhost] '{"max-queues":100}'```

# SYNOPSIS

**rabbitmqctl** _vhost_command_ [_options_]

# PARAMETERS

**list_vhosts**
> 列出所有虚拟主机。

**add_vhost** _name_
> 创建虚拟主机。

**delete_vhost** _name_
> 移除虚拟主机。

**set_vhost_limits** _json_
> 设置资源限制。

**clear_vhost_limits**
> 移除限制。

**-p** _vhost_
> 目标虚拟主机。

# DESCRIPTION

**rabbitmqctl** 的 vhost 命令管理 RabbitMQ 虚拟主机。虚拟主机为队列、交换机和权限提供逻辑隔离。属于 RabbitMQ 服务器管理的组成部分。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(1), [rabbitmqctl-users](/man/rabbitmqctl-users)(1)
