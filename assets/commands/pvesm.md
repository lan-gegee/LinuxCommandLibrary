# TAGLINE

配置 Proxmox 存储后端

# TLDR

获取所有存储的**状态**

```pvesm status```

**列出**存储内容

```pvesm list [storage_name]```

**添加**目录存储

```pvesm add dir [storage_name] --path [path/to/directory]```

**设置**存储包含特定内容类型

```pvesm set [storage_name] --content [iso,images,backup,vztmpl]```

从存储中**删除**文件

```pvesm free local:iso/[filename.iso]```

**移除**存储

```pvesm remove [storage_name]```

# SYNOPSIS

**pvesm** _command_ [_storage_] [_options_]

# PARAMETERS

**status**, **st**
> 显示所有存储的状态

**list**, **l** _storage_
> 列出指定存储的内容

**add** _type_ _storage_ _options_
> 添加新的存储定义

**set** _storage_ _options_
> 修改存储配置

**remove**, **r** _storage_
> 移除存储定义

**free** _volume_
> 从存储中删除卷/文件

**--content** _types_
> 允许的内容类型（iso、images、rootdir、vztmpl、backup）

**--path** _path_
> 目录路径（用于 dir 类型）

# DESCRIPTION

**pvesm** 管理 Proxmox VE 的存储定义。它为虚拟机磁盘映像、ISO 文件、容器模板和备份配置存储后端。支持的存储类型包括本地目录、NFS、CIFS、LVM、ZFS、Ceph 和 iSCSI。

存储配置是集群范围的；更改会传播到所有节点。每个存储都可以限制为特定的内容类型，并且可以只在选定的节点上启用。

# CAVEATS

移除存储定义不会删除数据。存储必须从启用了它的所有节点都能访问。某些存储类型需要额外的软件包或配置。

# HISTORY

**Proxmox VE** 的组成部分，为虚拟化提供统一的存储管理。它将不同的存储后端抽象为一个一致的接口，供 qm 和 pct 用于虚拟机和容器的存储。

# SEE ALSO

[qm](/man/qm)(1), [pct](/man/pct)(1), [pvesh](/man/pvesh)(1)
