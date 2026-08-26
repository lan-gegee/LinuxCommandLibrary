# TAGLINE

开源消息代理服务器

# TLDR

在前台**启动 RabbitMQ 服务器**

```rabbitmq-server```

**在后台启动**（分离模式）

```rabbitmq-server -detached```

**以指定节点名启动**

```RABBITMQ_NODENAME=[rabbit@hostname] rabbitmq-server```

**通过 systemd 启动**

```sudo systemctl start rabbitmq-server```

**启用管理插件**以获得 Web 界面

```rabbitmq-plugins enable rabbitmq_management```

**检查服务器状态**

```rabbitmqctl status```

# SYNOPSIS

**rabbitmq-server** [_options_]

# PARAMETERS

**-detached**
> 在后台运行服务器（守护进程化）。

**-n** _NODE_
> 指定节点名（RABBITMQ_NODENAME 的替代方式）。

# DESCRIPTION

**rabbitmq-server** 启动 RabbitMQ 消息代理——一个广泛使用的开源消息队列系统。RabbitMQ 实现 AMQP 0-9-1（高级消息队列协议），并可通过插件支持 MQTT、STOMP 和 AMQP 1.0。

生产环境中服务器通常通过 systemd 或 init 脚本管理。默认监听端口 **5672** 接受 AMQP 连接。管理插件在端口 **15672** 提供 Web 界面，用于监控队列、交换机和连接。

RabbitMQ 支持集群以实现高可用、虚拟主机实现多租户，以及多种交换机类型（direct、topic、fanout、headers）以实现灵活的消息路由。

# CONFIGURATION

**/etc/rabbitmq/rabbitmq.conf**
> 主配置文件（新的 sysctl 风格格式）。控制监听器、用户、资源限制和集群设置。

**/etc/rabbitmq/advanced.config**
> 高级 Erlang 项配置，用于 rabbitmq.conf 不支持的选项。

**/etc/rabbitmq/rabbitmq-env.conf**
> 用于覆盖节点名、端口、配置路径和日志位置的环境变量文件。

**RABBITMQ_NODENAME**
> 节点名（默认：rabbit@hostname）。

**RABBITMQ_NODE_PORT**
> AMQP 端口（默认：5672）。

**RABBITMQ_CONFIG_FILE**
> 配置文件的路径（不带扩展名）。

**RABBITMQ_LOG_BASE**
> 日志文件目录（默认：/var/log/rabbitmq）。

# CAVEATS

需要 Erlang/OTP 运行时。出于安全考虑，默认的 **guest** 用户只能从 localhost 连接。启用管理插件（**rabbitmq-plugins enable rabbitmq_management**）可获得 Web 界面。生产负载可能需要调高文件描述符限制。

# HISTORY

RabbitMQ 由 **Rabbit Technologies Ltd** 使用 Erlang 开发，于 **2007 年**首次发布。该公司于 2010 年被 **SpringSource**（后并入 VMware）收购。现由 **Broadcom**（通过 VMware）维护，仍是最广泛部署的消息代理之一。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(8), [rabbitmq-plugins](/man/rabbitmq-plugins)(8), [rabbitmq-diagnostics](/man/rabbitmq-diagnostics)(8)
