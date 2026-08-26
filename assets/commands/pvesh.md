# TAGLINE

通过命令行访问 Proxmox REST API

# TLDR

列出可用的**节点**

```pvesh get /nodes```

显示**容器或虚拟机**的详细信息

```pvesh get /nodes/[node_name]/[lxc|qemu]```

**发现** API 路径

```pvesh ls /```

显示 API 路径的**使用说明**

```pvesh usage /pools```

**添加**新的 thinpool 存储

```pvesh create /storage --storage [storage_id] --vgname [volume_group] --type lvmthin --thinpool [thinpool_name] --content [content_types]```

# SYNOPSIS

**pvesh** _command_ _path_ [_options_]

# PARAMETERS

**get**, **g**
> 从 API 路径获取数据

**ls**, **l**
> 列出可用的子路径

**usage**, **u**
> 显示 API 路径的使用信息

**create**
> 在 API 路径处创建新资源

**set**
> 修改现有资源

**delete**
> 删除 API 路径处的资源

**--output-format** _format_
> 输出格式（text、json、json-pretty）

# DESCRIPTION

**pvesh** 提供对 Proxmox VE REST API 的直接命令行访问。它允许查询和修改所有集群资源，包括节点、虚拟机、容器、存储和用户。这对脚本编写和自动化任务非常有用。

该工具与 Web 界面的功能一致，使管理员能够在命令行或脚本中执行通过 GUI 可用的任何操作。

# CAVEATS

需要 root 权限或相应的 Proxmox 权限。API 路径与 Web 界面结构对应。复杂操作可能需要多次 API 调用。

# HISTORY

**Proxmox VE** 的组成部分，提供与 Web 界面所用相同 API 的 CLI 访问。对于 Proxmox 集群的自动化、脚本编写和无头管理至关重要。

# SEE ALSO

[qm](/man/qm)(1), [pct](/man/pct)(1), [pvesm](/man/pvesm)(1), [pveum](/man/pveum)(1)
