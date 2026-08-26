# TAGLINE

管理 Proxmox VE 高可用服务

# TLDR

**显示 HA 状态**

```ha-manager status```

**为 VM 启用 HA**

```ha-manager add [vm:100]```

**移出 HA**

```ha-manager remove [vm:100]```

**设置 HA 组**

```ha-manager set [vm:100] --group [hagroup1]```

**迁移服务**

```ha-manager migrate [vm:100] [target-node]```

# SYNOPSIS

**ha-manager** _command_ [_options_]

# PARAMETERS

**status**
> 显示 HA 管理器状态。

**add** _sid_
> 将服务加入 HA。

**remove** _sid_
> 将服务移出 HA。

**set** _sid_ [_options_]
> 配置服务选项。

**migrate** _sid_ _node_
> 将服务迁移到节点。

**relocate** _sid_ _node_
> 请求重新定位。

**--group** _name_
> HA 组分配。

**--state** _state_
> 期望的状态（started、stopped、disabled）。

**--max_restart** _n_
> 最大重启尝试次数。

**--max_relocate** _n_
> 最大重新定位尝试次数。

# DESCRIPTION

**ha-manager** 管理 Proxmox VE 高可用服务。它控制哪些虚拟机和容器受 HA 保护，确保节点故障时它们能被自动重启或迁移。

HA 需要至少三个节点的集群才能形成正确的法定票数（quorum）。服务会受到监视，并根据配置的策略自动恢复。

# SERVICE ID FORMAT

```
vm:100        Virtual machine ID 100
ct:101        Container ID 101
```

# CAVEATS

需要 Proxmox 集群。法定票数要求至少 3 个节点。VM 迁移需要共享存储。建议配置网络隔离（fencing）。HA manager 必须处于运行状态。

# HISTORY

ha-manager 是开源虚拟化平台 **Proxmox VE** 的一部分。Proxmox HA 使用 Corosync 集群引擎提供自动故障转移。

# SEE ALSO

[pvecm](/man/pvecm)(1), [qm](/man/qm)(1)
