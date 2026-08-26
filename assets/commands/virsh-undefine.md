# TAGLINE

移除 libvirt 域定义

# TLDR

**取消定义域**

```virsh undefine [domain]```

**取消定义并移除存储**

```virsh undefine [domain] --remove-all-storage```

**取消定义 NVRAM 域**

```virsh undefine [domain] --nvram```

# SYNOPSIS

**virsh** **undefine** _domain_ [_options_]

# PARAMETERS

**--remove-all-storage**
> 删除关联的卷。

**--nvram**
> 移除 NVRAM 文件。

**--keep-nvram**
> 保留 NVRAM 文件。

**--snapshots-metadata**
> 移除与该域关联的所有快照元数据。

**--managed-save**
> 移除该域的所有托管保存镜像。

**--storage** _volumes_
> 要移除的卷目标名或源路径的逗号分隔列表。

**--checkpoints-metadata**
> 移除该域的所有检查点元数据。

# DESCRIPTION

**virsh undefine** 从 libvirt 中移除持久化的域定义。如果该域正在运行，它会变为瞬态（仍在运行但不再持久化）；否则会被完全移除。默认保留磁盘镜像；使用 **--remove-all-storage** 可同时删除关联的托管卷。

对于使用 UEFI/NVRAM 的域，NVRAM 文件默认被移除；传入 **--keep-nvram** 可保留它。

# CAVEATS

使用 **--remove-all-storage** 移除存储的操作不可逆。带有快照的域无法取消定义，除非提供 **--snapshots-metadata**。在 libvirt 存储池之外管理的存储卷需要手动清理。

# INSTALL

```apt: sudo apt install libvirt-clients```

```dnf: sudo dnf install libvirt-client```

```apk: sudo apk add libvirt-client```

```zypper: sudo zypper install libvirt-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-list](/man/virsh-list)(1), [virsh-pool-undefine](/man/virsh-pool-undefine)(1)

