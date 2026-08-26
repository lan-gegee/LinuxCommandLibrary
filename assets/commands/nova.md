# TAGLINE

OpenStack Compute 的命令行客户端，用于管理虚拟机

# TLDR

列出**当前项目/租户**中的服务器

```nova list```

列出**所有租户**的服务器（需管理员权限）

```nova list --all-tenants```

使用网络、镜像和规格**启动**实例

```nova boot --nic net-id=[net_id] --image [image_id] --flavor [flavor] --availability-zone nova:[host_name] [vm_name]```

**开启**服务器电源

```nova start [server]```

**关闭**服务器电源

```nova stop [server]```

为服务器**附加**网络接口

```nova interface-attach --net-id [net_id] [server]```

# SYNOPSIS

**nova** _command_ [_options_] [_arguments_]

# PARAMETERS

**list**
> 列出虚拟机

**boot**
> 创建并启动新的虚拟机

**start**
> 启动已停止的虚拟机

**stop**
> 停止运行中的虚拟机

**delete**
> 删除虚拟机

**show**
> 显示虚拟机详情

**interface-attach**
> 为虚拟机附加网络接口

**--nic net-id=_id_**
> 要附加的网络

**--image _id_**
> 用于启动的镜像 ID

**--flavor _name_**
> 实例类型/规格

**--availability-zone _zone:host_**
> 放置位置说明

**--all-tenants**
> 显示所有租户的虚拟机（需管理员权限）

# DESCRIPTION

**nova** 是 OpenStack Compute（Nova）的命令行客户端，用于管理 OpenStack 云中的虚拟机实例。它处理虚拟机的生命周期操作：创建、启动、停止和删除实例。

Nova 与其他 OpenStack 服务集成：Glance 提供镜像、Neutron 负责网络、Cinder 提供块存储、Keystone 处理认证。认证凭据通常通过环境变量提供（OS_USERNAME、OS_PASSWORD 等）。

该客户端与 Nova API 通信，按照指定的配置（规格、镜像、网络）来分配计算资源。

# CAVEATS

需要配置 OpenStack 凭据（通常通过 source 一个 openrc 文件）。旧版 nova 客户端正被 **openstack** 统一客户端取代。创建虚拟机前必须先存在网络和存储配置。跨租户操作需要管理员权限。

# INSTALL

```zypper: sudo zypper install nova```

```brew: brew install nova```

```nix: nix profile install nixpkgs#nova```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openstack](/man/openstack)(1), [neutron](/man/neutron)(1), [glance](/man/glance)(1)
