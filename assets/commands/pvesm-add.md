# TAGLINE

在 Proxmox VE 中添加存储后端定义

# TLDR

添加**目录（directory）**存储

```pvesm add dir [storage_name] --path [path/to/directory]```

添加 **LVM** 存储

```pvesm add lvm [storage_name] --vgname [volume_group_name]```

添加 **LVM-Thin** 存储

```pvesm add lvmthin [storage_name] --vgname [volume_group_name] --thinpool [logical_volume_name]```

# SYNOPSIS

**pvesm add** _type_ _storage_ [_OPTIONS_]

# PARAMETERS

**type**
> 存储类型（如 `dir`、`lvm`、`lvmthin`、`nfs`、`cifs`、`zfspool`、`rbd`、`iscsi`）

**storage**
> 唯一的存储标识符（集群范围的名称）

**--path** _path_
> 目录路径（用于 `dir` 类型）

**--vgname** _name_
> 卷组名称（用于 LVM 类型）

**--thinpool** _name_
> 精简池逻辑卷名称（用于 `lvmthin`）

**--content** _types_
> 允许的内容类型（如 `images`、`iso`、`backup`、`vztmpl`、`rootdir`）

**--nodes** _list_
> 将存储限制为所列出的集群节点

# DESCRIPTION

**pvesm add** 在 Proxmox VE 集群中注册新的存储定义。存储后端用于保存虚拟机磁盘、容器卷、ISO 文件、模板和备份。定义存储在整个集群范围内，一旦某个节点可以访问该存储，`qm` 和 `pct` 即可使用它。

支持的类型包括本地目录、NFS、CIFS、LVM、LVM-thin、ZFS 池、Ceph RBD 和 iSCSI 等。选项因类型而异；完整对照表见 `man pvesm`。

# CAVEATS

如果底层存储不存在，添加定义并不会创建它（例如 LVM 卷组必须已经存在）。路径和网络共享必须从启用了该存储的每个节点都可以访问。重复的存储 ID 会被拒绝。

# HISTORY

**Proxmox VE** 存储管理工具（`pvesm`）的一部分。

# SEE ALSO

[pvesm](/man/pvesm)(1), [qm](/man/qm)(1), [pct](/man/pct)(1)

# RESOURCES

```[Homepage](https://www.proxmox.com)```

```[Documentation](https://pve.proxmox.com/pve-docs/pvesm.1.html)```

<!-- verified: 2026-07-28 -->
