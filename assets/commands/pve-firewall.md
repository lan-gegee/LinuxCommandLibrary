# TAGLINE

Proxmox 分布式防火墙管理器

# TLDR

**编译**并打印所有防火墙规则

```pve-firewall compile```

显示关于**本地网络**的信息

```pve-firewall localnet```

**重启** Proxmox VE 防火墙服务

```pve-firewall restart```

**启动** Proxmox VE 防火墙服务

```pve-firewall start```

**停止** Proxmox VE 防火墙服务

```pve-firewall stop```

**模拟**所有防火墙规则

```pve-firewall simulate```

显示 Proxmox VE 防火墙的**状态**

```pve-firewall status```

# SYNOPSIS

**pve-firewall** _command_ [_options_]

# PARAMETERS

**compile**, **c**
> 编译并打印所有防火墙规则

**localnet**, **l**
> 显示本地网络信息

**restart**, **r**
> 重启防火墙服务

**start**
> 启动防火墙服务

**stop**
> 停止防火墙服务

**simulate**, **si**
> 模拟防火墙规则而不应用

**status**
> 显示防火墙服务状态

# DESCRIPTION

**pve-firewall** 管理 Proxmox VE 分布式防火墙。它基于集群范围和每 VM/容器的配置生成 iptables 规则。防火墙可以在数据中心、节点、VM 和容器层级进行配置。

compile 和 simulate 命令有助于在应用前调试防火墙配置。防火墙支持规则集、IP 集、别名和安全组，便于有序的配置管理。

# CAVEATS

防火墙规则是存储在 pmxcfs 中的集群级配置。更改可能影响所有集群节点。配置错误可能锁定管理访问；在进行重大更改前请确保有可用的控制台连接。

# HISTORY

属于 **Proxmox VE**，为虚拟化环境提供集成的防火墙管理。构建于 iptables/nftables 之上，并与 Proxmox 的集群文件系统集成以实现分布式配置。

# SEE ALSO

[qm](/man/qm)(1), [pct](/man/pct)(1), [pvesh](/man/pvesh)(1)
