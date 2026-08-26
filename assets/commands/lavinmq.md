# TAGLINE

轻量级高性能 AMQP 消息代理

# TLDR

以默认设置**启动消息代理**

```lavinmq```

**使用指定的配置文件启动**

```lavinmq --config=[path/to/lavinmq.ini]```

**指定持久化存储的数据目录**

```lavinmq --data-dir=[path/to/data]```

**绑定到指定地址**和 AMQP 端口

```lavinmq --bind=[0.0.0.0] --amqp-port=[5672]```

**显示版本**信息

```lavinmq -v```

通过配套 CLI **管理代理**（队列、策略、定义）

```lavinmqctl list_queues```

**将代理定义导出**为 JSON

```lavinmqctl export_definitions > [definitions.json]```

# SYNOPSIS

**lavinmq** [_options_]

**lavinmqctl** [_options_] _command_ [_arguments_]

# PARAMETERS

**-c** _file_, **--config**=_file_
> 从指定的 INI 配置文件加载代理设置。

**-D** _dir_, **--data-dir**=_dir_
> 存放持久化数据（队列、消息、定义）的目录。

**-b** _address_, **--bind**=_address_
> 要监听的 IP 或主机名（默认 127.0.0.1）。

**--amqp-port**=_port_
> AMQP 监听端口（默认 5672）。

**--amqps-port**=_port_
> AMQPS（TLS）监听端口（默认 5671）。

**--http-port**=_port_
> HTTP 管理 UI 端口（默认 15672）。

**--https-port**=_port_
> HTTPS 管理 UI 端口（默认 15671）。

**--guest-only-loopback**=_bool_
> 将默认用户 _guest_ 限制为仅允许环回连接。

**--log-level**=_level_
> 日志详细程度（debug、info、warn、error、fatal）。

**-h**, **--help**
> 显示用法信息并退出。

**-v**, **--version**
> 打印 LavinMQ 版本并退出。

# DESCRIPTION

**LavinMQ** 是一个实现 **AMQP 0-9-1** 协议的开源消息代理，与现有的 RabbitMQ 客户端库在线协议兼容。它还支持 **MQTT** 以及一种原生的流（streams）协议。它用 **Crystal** 编写，设计目标是在单节点上处理极高的吞吐量，同时借助操作系统页缓存和内存映射文件保持较低的内存占用。

该代理包含两个可执行程序。**lavinmq** 是长期运行的服务器进程，负责接受客户端连接、在交换器与队列之间路由消息，并提供内置的 HTTP 管理 UI。**lavinmqctl** 是管理用途的命令行工具，用于在服务器运行期间检查和管理虚拟主机、用户、队列、交换器、绑定、策略以及代理定义。

LavinMQ 支持面向高可用性的集群、副本队列、federation、shovel，以及面向日志式消费的流（streams）特性。配置可以通过 INI 文件提供，也可以在命令行上覆盖；安装方式则包括原生软件包、从源码构建，或直接运行官方的 **cloudamqp/lavinmq** Docker 镜像。

# CONFIGURATION

LavinMQ 从 INI 文件（通常为 **/etc/lavinmq/lavinmq.ini**）读取设置，文件被划分为 **[main]**、**[mgmt]**、**[amqp]**、**[mqtt]** 等小节。一个最简示例：

```
[main]
data_dir = /var/lib/lavinmq
guest_only_loopback = true
log_level = info

[mgmt]
bind = 0.0.0.0
port = 15672
tls_port = 15671

[amqp]
bind = 0.0.0.0
port = 5672
tls_port = 5671
```

命令行传入的任何标志都会覆盖配置文件中的对应值。默认用户 **guest**（密码 **guest**）被限制为本地连接，除非禁用 **guest_only_loopback**。

# CAVEATS

默认的 **guest/guest** 账户仅供本地测试使用，在将代理暴露到网络之前应当予以更换。尽管 LavinMQ 与 RabbitMQ 客户端在很大程度上兼容，但部分高级的 RabbitMQ 特性及插件尚未实现。持久化数据按节点存放在磁盘上，因此非集群部署的代理若发生非正常关闭，下次启动时可能需要恢复操作。

# HISTORY

**LavinMQ** 由 **CloudAMQP**（84codes）创建，并于 **2022 年**首次开源。它源自该公司运营大型 RabbitMQ 集群的经验，目标是提供一个更轻、更快且采用相同线上协议的消息代理。项目以 **Crystal** 编写，采用 **Apache 2.0** 许可证，此后陆续加入了集群、MQTT 支持和流协议。

# INSTALL

```brew: brew install lavinmq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmq-server](/man/rabbitmq-server)(1), [rabbitmqctl](/man/rabbitmqctl)(1), [mosquitto](/man/mosquitto)(8)
