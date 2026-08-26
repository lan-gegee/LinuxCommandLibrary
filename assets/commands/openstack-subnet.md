# TAGLINE

管理 OpenStack 网络中的 IP 子网

# TLDR

**列出子网**

```openstack subnet list```

**创建子网**

```openstack subnet create --network [network] --subnet-range [192.168.1.0/24] [subnet_name]```

**查看子网详情**

```openstack subnet show [subnet_name]```

**删除子网**

```openstack subnet delete [subnet_name]```

# SYNOPSIS

**openstack subnet** _command_ [_options_]

# PARAMETERS

**list**
> 列出子网。

**create** _name_
> 创建子网。

**delete** _name_
> 删除子网。

**show** _name_
> 显示子网详情。

**--network** _network_
> 父网络。

**--subnet-range** _cidr_
> CIDR 表示的 IP 地址范围。

**--gateway** _ip_
> 网关 IP 地址。

**--dhcp** / **--no-dhcp**
> 在子网上启用或禁用 DHCP（默认：_enabled_）。

**--dns-nameserver** _ip_
> DNS 服务器地址（多个 DNS 需重复此选项）。

**--allocation-pool** _start=IP,end=IP_
> 将 DHCP 分配限制在子网内的某个范围（可重复）。

**--ip-version** _4|6_
> 子网的 IP 版本（默认：_4_）。

**--ipv6-address-mode** _MODE_
> IPv6 地址模式：_slaac_、_dhcpv6-stateful_ 或 _dhcpv6-stateless_。

**--ipv6-ra-mode** _MODE_
> IPv6 路由通告模式（取值与 **--ipv6-address-mode** 相同）。

**--host-route** _destination=CIDR,gateway=IP_
> 添加静态主机路由（可重复）。

**--subnet-pool** _NAME_
> 从子网池分配范围，而不是直接指定 **--subnet-range**。

# DESCRIPTION

**openstack subnet** 管理 OpenStack 网络中的 IP 子网。可为虚拟网络配置 IP 范围、DHCP、DNS 和路由。属于 OpenStack 统一 CLI。

# SEE ALSO

[openstack-network](/man/openstack-network)(1), [openstack-port](/man/openstack-port)(1)
