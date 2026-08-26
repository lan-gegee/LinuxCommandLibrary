# TAGLINE

修改 LVM 卷组属性

# TLDR

**激活**所有卷组

```sudo vgchange -a y```

**停用**特定卷组

```sudo vgchange -a n [volume_group]```

**刷新**卷组中所有活动逻辑卷的元数据

```sudo vgchange --refresh [volume_group]```

**设置**卷组允许的最大逻辑卷数量

```sudo vgchange -l [128] [volume_group]```

**使**卷组不可调整大小

```sudo vgchange -x n [volume_group]```

# SYNOPSIS

**vgchange** [_options_] [_volume_group_...]

# PARAMETERS

**-a, --activate y|n|ay**
> 激活或停用逻辑卷（y=yes，n=no，ay=自动激活）

**-x, --resizeable y|n**
> 启用或禁用添加/移除物理卷

**-l, --logicalvolume _Number_**
> 设置卷组允许的最大逻辑卷数量

**-p, --maxphysicalvolumes _Number_**
> 设置卷组中物理卷的最大数量

**-s, --physicalextentsize _Size_**
> 更改物理卷上的物理区块（extent）大小

**--refresh**
> 为所有活动逻辑卷重新加载元数据

**--monitor y|n**
> 启动或停止 dmeventd 对逻辑卷的监控

**--poll y|n**
> 控制逻辑卷的后台转换过程

**--sysinit**
> 表示该命令是在系统初始化早期被调用的

**-u, --uuid**
> 为卷组生成新的随机 UUID

**--addtag _tag_**
> 向卷组添加标签

**--deltag _tag_**
> 从卷组删除标签

**-f, --force**
> 覆盖各种检查、确认和保护机制

**--alloc contiguous|cling|normal|anywhere|inherit**
> 设置物理区块分配策略

# DESCRIPTION

**vgchange** 修改 LVM 卷组的属性。最常见的用途是激活或停用卷组内的逻辑卷，这是挂载这些卷之前的必要步骤。

激活卷组后，其中的逻辑卷即可供系统使用。在移除物理卷或安全关机之前，必须先停用卷组。

# CAVEATS

需要 root 权限。如果卷组中的文件系统已挂载或处于活动状态，停用会失败。缺少物理卷时进行激活需要 **--activationmode partial** 或 **-P** 选项。使用 **vgscan** 发现卷组。属于 LVM2 软件包。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [vgcreate](/man/vgcreate)(8), [vgdisplay](/man/vgdisplay)(8), [vgscan](/man/vgscan)(8), [vgremove](/man/vgremove)(8), [lvchange](/man/lvchange)(8), [pvchange](/man/pvchange)(8)
