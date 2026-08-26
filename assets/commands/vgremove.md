# TAGLINE

移除 LVM 卷组

# TLDR

**移除**卷组（需确认）

```sudo vgremove [volume_group]```

**强制移除**卷组（无需确认）

```sudo vgremove -f [volume_group]```

带调试日志**移除**

```sudo vgremove -d -d [volume_group]```

按选择条件**移除**卷组

```sudo vgremove --select '[vg_name=~old_*]'```

# SYNOPSIS

**vgremove** [_options_] _volume_group_...

# PARAMETERS

**-f, --force**
> 强制移除，无需确认

**-d, --debug**
> 启用调试输出（可重复使用以增加细节，最多 6 次）

**-S, --select** _string_
> 根据指定条件选择要处理的对象

**-t, --test**
> 测试模式，不做实际更改

**-v, --verbose**
> 详细输出

**-y, --yes**
> 对所有提示回答 yes

# DESCRIPTION

**vgremove** 移除一个或多个 LVM 卷组。在移除卷组之前，必须先用 **lvremove** 删除其中所有的逻辑卷。

该命令更新 LVM 元数据，将卷组标记为已移除。底层的物理卷仍然保留，但不再与任何卷组关联。

# CAVEATS

需要 root 权限。必须先删除所有逻辑卷。无法移除包含已挂载文件系统的活动卷组。卷组上的数据在移除后将无法访问。属于 LVM2 软件包。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [vgcreate](/man/vgcreate)(8), [lvremove](/man/lvremove)(8), [pvremove](/man/pvremove)(8)
