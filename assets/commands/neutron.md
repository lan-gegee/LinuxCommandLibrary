# TAGLINE

OpenStack 网络服务

# TLDR

**列出网络**

```openstack network list```

**创建网络**

```openstack network create [network_name]```

**创建子网**

```openstack subnet create --network [network] --subnet-range [192.168.1.0/24] [subnet_name]```

**创建路由器**

```openstack router create [router_name]```

**列出端口**

```openstack port list```

**查看网络详情**

```openstack network show [network_name]```

# SYNOPSIS

**openstack network** _command_ [_options_]

# PARAMETERS

**list**
> 列出网络。

**create**
> 创建网络。

**delete**
> 删除网络。

**show**
> 查看网络详情。

**set**
> 修改网络。

# DESCRIPTION

**Neutron** 是 OpenStack 的网络服务（现在通过统一的 openstack 客户端访问）。它将网络连接作为一种服务提供，管理网络、子网、路由器和端口。

# NETWORK TYPES

```
flat       - Untagged network
vlan       - VLAN segmentation
vxlan      - Virtual overlay
gre        - GRE tunnels
geneve     - Geneve encapsulation
```

# COMPONENTS

```
neutron-server      - API server
neutron-l2-agent    - L2 connectivity
neutron-l3-agent    - L3 routing
neutron-dhcp-agent  - DHCP service
```

# CAVEATS

需要 OpenStack 凭据。具体能力由插件决定。多租户网络较为复杂。

# HISTORY

Neutron 原名 Quantum，于 **2013 年**更名。它是 OpenStack 软件定义网络核心服务的组成部分。

# INSTALL

```aur: yay -S neutron```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openstack](/man/openstack)(1), [nova](/man/nova)(1)
