# TAGLINE

管理 LXD 容器的网络

# TLDR

列出**所有网络**

```lxc network list```

查看网络**配置**

```lxc network show [network_name]```

将容器**附加**到网络

```lxc network attach [network_name] [container_name]```

**创建**新网络

```lxc network create [network_name]```

设置**网桥接口**

```lxc network set [network_name] bridge.external_interfaces eth0```

**禁用 NAT**

```lxc network set [network_name] ipv4.nat false```

# SYNOPSIS

**lxc network** _command_ [_options_]

# DESCRIPTION

**lxc network** 管理 LXD 容器的网络。它支持创建、配置网络并将其附加到容器，支持网桥、VLAN 以及各种网络配置。

# SUBCOMMANDS

**list**
> 列出可用的网络

**show NAME**
> 显示网络配置

**create NAME**
> 创建新的受管网络

**delete NAME**
> 删除网络

**attach NAME CONTAINER**
> 将容器附加到网络

**detach NAME CONTAINER**
> 将容器从网络分离

**set NAME KEY VALUE**
> 设置网络配置

# SEE ALSO

[lxc](/man/lxc)(1), [lxc-start](/man/lxc-start)(1)
