# TAGLINE

将独立的 VDO 卷转换为 LVM 管理的 VDO 逻辑卷

# TLDR

导入 VDO 卷，VG/LV 使用**自动命名**

```lvm_import_vdo [/dev/mapper/vdo_volume]```

导入并设置**目标 VG/LV 名称**

```lvm_import_vdo -n [vg_name/lv_name] [/dev/mapper/vdo_volume]```

显示将要进行的操作而**不做任何更改**

```lvm_import_vdo --dry-run [/dev/mapper/vdo_volume]```

就地转换且**不使用临时快照**（安全性较低）

```lvm_import_vdo --no-snapshot [/dev/mapper/vdo_volume]```

**详细输出**并自动对所有提示回答 "yes"

```lvm_import_vdo -v -y [/dev/mapper/vdo_volume]```

导入期间使用 **VDO 管理器配置文件**

```lvm_import_vdo --vdo-config [path/to/vdo.conf] [/dev/mapper/vdo_volume]```

# SYNOPSIS

**lvm_import_vdo** [_options_] _device_

# PARAMETERS

**-n, --name _vg/lv_**
> 指定目标卷组和逻辑卷名称

**--dry-run**
> 预览导入操作而不做更改

**--no-snapshot**
> 转换期间跳过创建临时快照（更快但风险更高）

**-v, --verbose**
> 启用详细输出

**-y, --yes**
> 自动对所有提示回答 yes

**--vdo-config _file_**
> 导入期间使用 VDO 管理器配置文件

# DESCRIPTION

**lvm_import_vdo** 将用独立 VDO 管理器创建的 VDO（Virtual Data Optimizer）卷转换为 LVM 管理的 VDO 逻辑卷。这样可以在保留 VDO 去重和压缩特性的同时，与 LVM 的卷管理能力集成。

转换过程是**不可逆的**，会迁移 VDO 元数据格式。默认情况下，转换过程中会创建临时快照以保证安全。

VDO 为块存储提供内联去重和压缩，可减少虚拟机和容器等具有冗余数据的工作负载的存储需求。

# CAVEATS

此操作**不可逆**；原始 VDO 卷格式无法恢复。**--no-snapshot** 选项会跳过安全机制，只应在快照创建失败时使用。导入前请备份重要数据。需要 root 权限。

# INSTALL

```apk: sudo apk add lvm2-extra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [lvcreate](/man/lvcreate)(8)
