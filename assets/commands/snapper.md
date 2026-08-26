# TAGLINE

面向 Btrfs 的文件系统快照管理工具

# TLDR

列出快照**配置**

```snapper list-configs```

**创建**配置

```snapper -c [config] create-config [path/to/directory]```

创建带描述的**快照**

```snapper -c [config] create -d "[description]"```

为某个配置**列出**快照

```snapper -c [config] list```

**删除**快照

```snapper -c [config] delete [snapshot_number]```

删除一个**范围**内的快照

```snapper -c [config] delete [snapshot1]-[snapshot2]```

显示快照之间的**差异**

```snapper -c [config] status [snapshot1]..[snapshot2]```

**回滚**到某个快照

```snapper -c [config] rollback [snapshot_number]```

# SYNOPSIS

**snapper** [**-c** _config_] _command_ [_OPTIONS_]

# PARAMETERS

**-c, --config** _name_
> 使用指定的配置

**list-configs**
> 列出所有配置

**create-config** _path_
> 为子卷创建新配置

**delete-config**
> 删除一个配置

**create**
> 创建新快照

**delete** _number_
> 删除快照

**list**
> 列出快照

**status** _num1..num2_
> 显示快照之间的变化

**diff** _num1..num2_
> 显示文件差异

**undochange** _num1..num2_ _files_
> 撤销快照之间的更改

**rollback** [_number_]
> 将系统回滚到某个快照

**cleanup** _algorithm_
> 运行清理算法（number、timeline、empty-pre-post）

**setup-quota**
> 设置配额（仅限 btrfs）

**-d, --description** _text_
> 快照描述

**-t, --type** _type_
> 快照类型（single、pre、post）

**-u, --userdata** _key=value_
> 设置快照元数据

**-s, --sync**
> 删除后同步文件系统

# DESCRIPTION

**snapper** 是一个文件系统快照管理工具，主要配合 Btrfs 使用。它可以创建、比较和管理快照，实现系统回滚和文件恢复。Snapper 支持带可配置保留策略的自动快照时间线。

每个配置管理特定子卷或逻辑卷的快照。快照可以手动创建，也可以在系统更改前后自动创建。清理算法会根据时间或数量限制自动删除旧快照。

# CONFIGURATION

**/etc/snapper/configs/**
> 每个子卷一份的配置文件，定义快照类型、清理算法以及保留策略（timeline 和 number 限制）。

**/etc/sysconfig/snapper**
> snapper 全局设置，包括活动配置列表（SNAPPER_CONFIGS）。

# CAVEATS

只有在 Btrfs 且系统配置正确的情况下才支持回滚。快照会占用磁盘空间；请用 **btrfs filesystem df** 监控用量。非 root 用户需要通过 ALLOW_USERS 授予配置权限。/.snapshots 目录必须具有正确的权限。

# HISTORY

**snapper** 由 **openSUSE/SUSE** 的 **Arvin Schnell** 创建，大约于 **2011 年**首次发布。它的设计初衷是利用 Btrfs 的快照能力进行系统恢复，后来成为 openSUSE 和 SUSE Linux Enterprise 的关键组件。对精简配置 LVM 的支持是后来加入的。

# INSTALL

```apt: sudo apt install snapper```

```dnf: sudo dnf install snapper```

```pacman: sudo pacman -S snapper```

```zypper: sudo zypper install snapper```

```nix: nix profile install nixpkgs#snapper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-subvolume](/man/btrfs-subvolume)(8), [timeshift](/man/timeshift)(1), [lvcreate](/man/lvcreate)(8)
