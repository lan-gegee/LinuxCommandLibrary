# TAGLINE

管理 OpenStack Neutron 中的虚拟网络

# TLDR

**列出网络**

```openstack network list```

**创建网络**

```openstack network create [network_name]```

**查看网络详情**

```openstack network show [network_name]```

**删除网络**

```openstack network delete [network_name]```

# SYNOPSIS

**openstack network** _command_ [_options_]

# PARAMETERS

**list**
> 列出网络。

**create** _name_
> 创建网络。

**delete** _name_
> 删除网络。

**show** _name_
> 显示网络详情。

**--external**
> 创建为外部网络。

**--share**
> 跨项目共享网络。

**--provider-network-type** _type_
> 提供商网络类型（flat、vlan、vxlan）。

# DESCRIPTION

**openstack network** 管理 OpenStack Neutron 中的虚拟网络。可创建隔离网络、配置外部连接并管理网络基础设施。属于 OpenStack 统一 CLI。

# SEE ALSO

[openstack-subnet](/man/openstack-subnet)(1), [openstack-port](/man/openstack-port)(1), [openstack-server](/man/openstack-server)(1)
