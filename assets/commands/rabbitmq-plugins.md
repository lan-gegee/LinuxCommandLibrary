# TAGLINE

管理 RabbitMQ 服务器插件

# TLDR

**列出插件**

```rabbitmq-plugins list```

**启用插件**

```rabbitmq-plugins enable [rabbitmq_management]```

**禁用插件**

```rabbitmq-plugins disable [rabbitmq_management]```

**启用多个插件**

```rabbitmq-plugins enable [plugin1] [plugin2]```

**显示已启用的插件**

```rabbitmq-plugins list --enabled```

# SYNOPSIS

**rabbitmq-plugins** [_options_] _command_ [_command_options_]

# PARAMETERS

**-n** _node_
> 目标节点。

**--offline**
> 在节点未运行时修改。

**--online**
> 要求节点处于运行状态。

# COMMANDS

**list**
> 列出所有插件。

**enable** _plugins_
> 启用插件。

**disable** _plugins_
> 禁用插件。

**set** _plugins_
> 设置确切的插件列表。

# DESCRIPTION

**rabbitmq-plugins** 管理 RabbitMQ 插件。插件可扩展 RabbitMQ 的功能，例如管理界面、MQTT 支持和 LDAP 身份验证。

# EXAMPLES

```bash
# List all plugins
rabbitmq-plugins list

# Enable management UI
rabbitmq-plugins enable rabbitmq_management

# Enable MQTT
rabbitmq-plugins enable rabbitmq_mqtt

# Disable plugin
rabbitmq-plugins disable rabbitmq_stomp

# Offline enable
rabbitmq-plugins enable --offline rabbitmq_management
```

# COMMON PLUGINS

```
rabbitmq_management      - Web UI and API
rabbitmq_mqtt            - MQTT protocol
rabbitmq_stomp           - STOMP protocol
rabbitmq_shovel          - Message transfer
rabbitmq_federation      - Federation
rabbitmq_prometheus      - Metrics export
```

# CAVEATS

部分插件需要重启节点。依赖项会自动启用。管理界面位于端口 15672。

# HISTORY

RabbitMQ 插件系统由 **Pivotal**（现为 VMware）开发，是 RabbitMQ 可扩展架构的一部分。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(8), [rabbitmq-diagnostics](/man/rabbitmq-diagnostics)(8), [rabbitmq-server](/man/rabbitmq-server)(8)
