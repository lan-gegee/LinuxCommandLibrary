# TAGLINE

Proxmox VE 的 LXC 容器管理工具

# TLDR

**列出**容器

```pct list```

**启动/停止**容器

```pct start 100```

**进入**容器 shell

```pct enter 100```

**创建**容器

```pct create 100 local:vztmpl/distro.tar.zst --rootfs local-lvm:4```

**调整**磁盘大小

```pct resize 100 rootfs 20G```

**显示**配置

```pct config 100```

创建容器**快照**

```pct snapshot 100 my-snapshot --description "description"```

**销毁**容器

```pct destroy 100 --purge```

# SYNOPSIS

**pct** _command_ [_OPTIONS_] [_vmid_]

# DESCRIPTION

**pct** 是 Proxmox VE 的 LXC 容器管理工具。它提供完整的命令行界面，用于创建、配置、启动、停止和管理 Linux 容器。

# PARAMETERS

**list**
> 列出所有容器

**create** _vmid_ _template_
> 从模板创建新容器

**config** _vmid_
> 显示容器配置

**set** _vmid_
> 修改容器配置

**start** _vmid_
> 启动容器

**stop** _vmid_
> 停止容器

**enter** _vmid_
> 访问容器 shell

**exec** _vmid_ _command_
> 在容器中执行命令

**snapshot** _vmid_ _name_
> 创建快照

**destroy** _vmid_
> 移除容器

**resize** _vmid_ _disk_ _size_
> 调整容器磁盘大小

**--purge**
> 销毁时移除所有相关资源

# CAVEATS

容器 ID 在整个 Proxmox 集群内必须唯一。某些操作要求容器处于停止状态。对于在内部运行 Docker 或 LXC 的容器，必须启用 nesting 特性。

# HISTORY

**pct** 是 **Proxmox VE** 虚拟化平台的一部分，基于 LXC 技术提供轻量级容器化能力。

# SEE ALSO

[pct-create](/man/pct-create)(1), [pct-exec](/man/pct-exec)(1), [qm](/man/qm)(1)
