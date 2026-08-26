# TAGLINE

转换或修改逻辑卷的类型、冗余度或状态

# TLDR

转换为 **RAID1**

```sudo lvconvert --type raid1 -m 1 /dev/vg_name/lv_name```

**移除镜像**（转换为 linear）

```sudo lvconvert -m 0 /dev/vg_name/lv_name```

将快照**合并**回源卷

```sudo lvconvert --merge /dev/vg_name/snapshot_lv```

**修复**降级的 RAID

```sudo lvconvert --repair /dev/vg_name/lv_name```

转换为**精简池（thin pool）**

```sudo lvconvert --type thin-pool --poolmetadata /dev/vg_name/meta_lv /dev/vg_name/pool_lv```

# SYNOPSIS

**lvconvert** [_options_] _vg_/_lv_

# DESCRIPTION

**lvconvert** 转换或修改逻辑卷的类型、冗余度或状态。它可以添加/移除镜像、在 linear 与 RAID 之间转换、合并快照，以及转换为精简池。

# PARAMETERS

**--type TYPE**
> 转换为指定类型（raid1、linear、thin-pool、cache-pool）

**-m, --mirrors N**
> 镜像数量（0 表示移除镜像）

**--merge**
> 将快照合并回源卷

**--repair**
> 修复降级的 RAID 卷

**--poolmetadata LV**
> 为精简池指定元数据 LV

**--stripes N**
> 转换时的条带数量

# CAVEATS

需要 root 权限。数据迁移可能需要时间。快照合并在下次激活时生效。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvcreate](/man/lvcreate)(8), [lvchange](/man/lvchange)(8), [lvextend](/man/lvextend)(8), [lvm](/man/lvm)(8)
