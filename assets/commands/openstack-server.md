# TAGLINE

管理 OpenStack 云中的计算实例

# TLDR

**列出服务器**

```openstack server list```

**创建服务器**

```openstack server create --flavor [m1.small] --image [ubuntu] --network [private] [server_name]```

**查看服务器详情**

```openstack server show [server_name]```

**删除服务器**

```openstack server delete [server_name]```

**启动已停止的服务器**

```openstack server start [server_name]```

**停止运行中的服务器**

```openstack server stop [server_name]```

**重启服务器**

```openstack server reboot [server_name]```

**SSH 登录服务器**

```openstack server ssh [server_name] -- -l [username]```

# SYNOPSIS

**openstack server** _command_ [_options_]

# PARAMETERS

**list**
> 列出服务器。

**create** _name_
> 创建新服务器。

**delete** _name_
> 删除服务器。

**show** _name_
> 显示服务器详情。

**start** _name_
> 启动服务器。

**stop** _name_
> 停止服务器。

**reboot** _name_
> 重启服务器。

**--flavor** _flavor_
> 实例规格/尺寸。

**--image** _image_
> 启动镜像。

**--network** _network_
> 要附加的网络。

**--key-name** _key_
> SSH 密钥对。

**--security-group** _group_
> 要分配的安全组（可重复）。

**--availability-zone** _zone_
> 服务器所在的可用区。

**resize** _name_ **--flavor** _flavor_
> 将服务器调整为其他规格。

**ssh** _name_
> SSH 登录该服务器。

**migrate** _name_
> 将服务器迁移到其他主机。

# DESCRIPTION

**openstack server** 管理 OpenStack 云中的计算实例（虚拟机）。它是统一 OpenStack 命令行客户端（python-openstackclient）的组成部分。命令遵循 `openstack server <action>` 的模式，并支持通过 `-f` 设置输出格式（json、table、csv、yaml），通过 `-c` 选择列。

# CAVEATS

需要有效的 OpenStack 凭据（通常来自 openrc 文件或 OS_* 环境变量）。某些操作（如 resize）需要确认。服务器名称可能不唯一；脚本化操作请使用 ID。

# SEE ALSO

[openstack](/man/openstack)(1), [openstack-flavor](/man/openstack-flavor)(1), [openstack-image](/man/openstack-image)(1), [openstack-network](/man/openstack-network)(1), [openstack-volume](/man/openstack-volume)(1)
