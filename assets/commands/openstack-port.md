# TAGLINE

管理 OpenStack Neutron 中的网络端口

# TLDR

**列出端口**

```openstack port list```

**创建端口**

```openstack port create --network [network] [port_name]```

**查看端口详情**

```openstack port show [port_name]```

**删除端口**

```openstack port delete [port_name]```

# SYNOPSIS

**openstack port** _command_ [_options_]

# PARAMETERS

**list**
> 列出端口。

**create** _name_
> 创建端口。

**delete** _name_
> 删除端口。

**show** _name_
> 显示端口详情。

**--network** _network_
> 端口所属的网络。

**--fixed-ip** _ip_
> 固定 IP 地址。

**--security-group** _group_
> 安全组。

**--mac-address** _mac_
> MAC 地址。

# DESCRIPTION

**openstack port** 管理 OpenStack Neutron 中的网络端口。端口表示附加到实例上的虚拟网络接口。属于 OpenStack 统一 CLI。

# SEE ALSO

[openstack-network](/man/openstack-network)(1), [openstack-server](/man/openstack-server)(1)
