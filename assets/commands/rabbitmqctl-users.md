# TAGLINE

管理 RabbitMQ 用户和权限

# TLDR

**列出用户**

```rabbitmqctl list_users```

**添加用户**

```rabbitmqctl add_user [username] [password]```

**删除用户**

```rabbitmqctl delete_user [username]```

**更改用户密码**

```rabbitmqctl change_password [username] [new_password]```

**设置用户标签**

```rabbitmqctl set_user_tags [username] [administrator]```

为用户在某个 vhost 上**设置权限**

```rabbitmqctl set_permissions -p [vhost] [username] ".*" ".*" ".*"```

**列出**特定用户在所有 vhost 上的权限

```rabbitmqctl list_user_permissions [username]```

**校验**用户的凭据

```rabbitmqctl authenticate_user [username] [password]```

# SYNOPSIS

**rabbitmqctl** _user_command_ [_options_]

# PARAMETERS

**list_users**
> 列出所有用户。

**add_user** _user_ _pass_
> 创建用户。

**delete_user** _user_
> 移除用户。

**change_password** _user_ _pass_
> 更改密码。

**clear_password** _user_
> 清除用户的密码，禁止基于密码登录。

**authenticate_user** _user_ _pass_
> 校验凭据是否与用户存储的身份验证信息匹配。

**set_user_tags** _user_ _tags ..._
> 设置角色标签（administrator、monitoring、management、policymaker）。会替换所有现有标签。

**set_permissions** [**-p** _vhost_] _user_ _conf_ _write_ _read_
> 使用正则表达式模式设置 vhost 的 configure、write 和 read 权限。

**clear_permissions** [**-p** _vhost_] _user_
> 撤销用户在某 vhost 上的所有权限。

**list_permissions** [**-p** _vhost_]
> 列出可访问某 vhost 的所有用户及其权限。

**list_user_permissions** _user_
> 列出某用户可访问的所有 vhost 及其权限。

**-p** _vhost_
> 目标虚拟主机（默认："/"）。

# DESCRIPTION

**rabbitmqctl** 的用户命令管理 RabbitMQ 用户和权限。可以创建用户、设置密码、分配角色以及配置 vhost 访问。属于 RabbitMQ 服务器管理的组成部分。这些命令仅管理内部 RabbitMQ 数据库中的用户；来自其他身份验证后端（如 LDAP）的用户无法用这些命令管理。

# INSTALL

```dnf: sudo dnf install rabbitmq-server```

```apk: sudo apk add rabbitmq-server```

```zypper: sudo zypper install rabbitmq-server```

```nix: nix profile install nixpkgs#rabbitmq-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rabbitmqctl](/man/rabbitmqctl)(1), [rabbitmqctl-vhosts](/man/rabbitmqctl-vhosts)(1)
