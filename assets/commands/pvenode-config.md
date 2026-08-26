# TAGLINE

获取或设置 Proxmox VE 节点配置选项

# TLDR

**获取**所有节点配置选项

```pvenode config get```

获取**特定属性**

```pvenode config get --property description```

设置节点**描述**（备注面板）

```pvenode config set --description "primary cluster node"```

为 TLS 证书配置 **ACME** 域

```pvenode config set --acme domains=pve.example.com```

设置 **Wake-on-LAN** MAC 地址

```pvenode config set --wakeonlan XX:XX:XX:XX:XX:XX```

设置第一个客户机在主机启动后的**开机延迟**（秒）

```pvenode config set --startall-onboot-delay 10```

设置内存 **ballooning 目标**百分比

```pvenode config set --ballooning-target 90```

# SYNOPSIS

**pvenode config get** [_OPTIONS_]

**pvenode config set** [_OPTIONS_]

# PARAMETERS

**--property** _name_
> (get) 仅返回指定属性：acme、acmedomain0–5、ballooning-target、description、location、startall-onboot-delay、wakeonlan（默认：全部）

**--description** _text_
> (set) 显示在 Web UI 备注面板中的节点描述

**--acme** _settings_
> (set) 节点专属的 ACME 设置（账户、域）

**--acmedomain**_n_ _settings_
> (set) 域索引 n 的 ACME 域和验证插件

**--ballooning-target** _percent_
> (set) ballooning 的内存使用目标，0–100（默认 80）

**--startall-onboot-delay** _seconds_
> (set) 主机启动后延迟启动开机自启客户机的时间，0–300（默认 0）

**--wakeonlan** _settings_
> (set) Wake-on-LAN MAC 以及可选的绑定网卡 / 广播地址

**--location** _settings_
> (set) 节点位置（纬度、经度、可选名称）

**--delete** _list_
> (set) 要移除的设置

**--digest** _hash_
> (set) 如果配置摘要不一致则阻止并发修改

# DESCRIPTION

**pvenode config** 读取和写入 Proxmox VE 主机的节点级配置。设置包括备注/描述、ACME 证书域名、Wake-on-LAN、客户机自动启动延迟、内存 ballooning 目标以及地理位置元数据。

这些选项只影响本地节点（而非集群级的数据中心配置）。与证书相关的 ACME 域设置需配合 **pvenode acme** 命令使用，以订购和续订 API 和 Web UI 所用的 TLS 证书。

# CAVEATS

更改 ACME 域本身并不会签发证书；仍需要执行 **pvenode acme cert order**（通常还需重启 **pveproxy**）。并发编辑可能产生竞争；脚本化操作时请使用 **--digest**。错误的 Wake-on-LAN 设置将导致无法远程唤醒处于休眠状态的节点。

# HISTORY

**pvenode config** 是 **Proxmox VE** **pvenode** 节点管理工具的一部分。

# SEE ALSO

[pvesubscription](/man/pvesubscription)(1), [pveversion](/man/pveversion)(1), [pvesh](/man/pvesh)(1)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pvenode.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-16 -->
