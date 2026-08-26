# TAGLINE

将 Proxmox 虚拟机迁移到远程主机或集群

# TLDR

将虚拟机**迁移**到远程主机

```qm remote-migrate [vmid] [target_vmid] 'apitoken=PVEAPIToken=[user]@[realm]![token]=[secret],host=[address],fingerprint=[fingerprint]' --target-bridge [bridge] --target-storage [storage]```

以动态迁移的方式迁移**运行中的**虚拟机

```qm remote-migrate [vmid] [target_vmid] 'apitoken=PVEAPIToken=[user]@[realm]![token]=[secret],host=[address],fingerprint=[fingerprint]' --target-bridge [bridge] --target-storage [storage] --online```

迁移成功后**删除**源虚拟机

```qm remote-migrate [vmid] [target_vmid] 'apitoken=PVEAPIToken=[user]@[realm]![token]=[secret],host=[address],fingerprint=[fingerprint]' --target-bridge [bridge] --target-storage [storage] --delete 1```

**限制**迁移带宽

```qm remote-migrate [vmid] [target_vmid] 'apitoken=PVEAPIToken=[user]@[realm]![token]=[secret],host=[address],fingerprint=[fingerprint]' --target-bridge [bridge] --target-storage [storage] --bwlimit [value]```

在目标端使用**相同的**网桥和存储名称

```qm remote-migrate [vmid] [target_vmid] 'apitoken=PVEAPIToken=[user]@[realm]![token]=[secret],host=[address],fingerprint=[fingerprint]' --target-bridge 1 --target-storage 1```

# SYNOPSIS

**qm remote-migrate** _vmid_ _target-vmid_ _target-endpoint_ [_OPTIONS_]

# PARAMETERS

**vmid**
> 本地集群上的源虚拟机 ID

**target-vmid**
> 远程集群上的目标 VM ID（可与源相同）

**target-endpoint**
> 远程连接字符串：API token、主机、TLS 指纹（端口可选）

**--target-bridge** _bridge_|_1_
> 映射网络网桥；`1` 表示保留源网桥名称

**--target-storage** _storage_|_1_
> 映射存储；`1` 表示保留源存储名称

**--online**
> 对运行中的虚拟机执行在线/动态迁移

**--delete** _0|1_
> 迁移成功后移除源虚拟机

**--bwlimit** _kbps_
> 传输的带宽限制

# DESCRIPTION

**qm remote-migrate** 通过 Proxmox API 将虚拟机从本地 Proxmox VE 集群迁移到**远程**主机或集群。与 `qm migrate`（集群内部）不同，远程迁移使用 API token 和主机指纹进行身份验证和 TLS 校验。

必须提供网桥和存储的映射，使网络和磁盘落到有效的远程资源上。当环境支持时，动态迁移（`--online`）能以更短的停机时间移动运行中的客户机。

# CAVEATS

要求远端具有具备足够权限的有效 **API token**，以及匹配的 TLS **指纹**。网络容量和存储兼容性决定传输时间。请仔细测试映射；错误的网桥/存储目标会在迁移中途失败。务必将 API token 当作机密对待。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，无需加入同一集群即可实现跨集群的虚拟机迁移。

# SEE ALSO

[qm](/man/qm)(1), [qm-migrate](/man/qm-migrate)(1), [pvecm](/man/pvecm)(1)

# RESOURCES

```[Homepage](https://www.proxmox.com)```

```[Documentation](https://pve.proxmox.com/pve-docs/qm.1.html)```

<!-- verified: 2026-07-28 -->
