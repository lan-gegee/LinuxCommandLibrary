# TAGLINE

管理 bcachefs 文件系统中的设备

# TLDR

移除设备前先**迁出**其数据

```bcachefs device evacuate [path/to/device]```

从文件系统中**永久移除**设备

```bcachefs device remove [path/to/device]```

**添加并格式化**带标签的新设备

```sudo bcachefs device add --label [group].[name] [path/to/mountpoint] [path/to/device]```

# SYNOPSIS

**bcachefs device** _command_ [_options_] _device_

# DESCRIPTION

**bcachefs device** 管理运行中的 bcachefs 文件系统内的设备。它支持添加新设备以扩展存储、在移除前迁出数据以及永久删除设备。

设备标签将存储划分为组（如 ssd 或 hdd）和单独的设备名，从而实现分层存储配置。

# SUBCOMMANDS

**add**
> 向现有文件系统添加设备

**remove**
> 从文件系统中移除设备

**online**
> 将设备重新加入运行中的文件系统

**offline**
> 将设备下线但不移除

**evacuate**
> 将指定设备上的所有数据迁移出去

**set-state** _new-state_ _device_
> 将设备状态设为 rw、ro、failed 或 spare

**resize**
> 调整设备上文件系统的大小

# PARAMETERS

**-l, --label** _label_
> 为设备分配磁盘标签以便归类（如 ssd.cache、hdd.bulk）

**--fs_size** _size_
> 设备上要使用的文件系统大小（add）

**--bucket** _size_
> 设置 bucket 大小（add）

**--discard**
> 在设备上启用 discard（add）

**-f, --force**
> 即使数据冗余度会降低也强制执行操作，或强制使用看起来已格式化的设备

**-F, --force-metadata**
> 即使部分元数据无法迁移也强制移除（remove）

**--force-if-data-lost**
> 即使会丢失数据也强制更改状态（set-state）

**-o, --offline**
> 对离线设备执行操作（set-state）

# CAVEATS

移除设备可能耗时较长，取决于数据量。迁出数据前请确保剩余设备上有足够的空闲空间。设备操作要求文件系统处于挂载状态。

# INSTALL

```dnf: sudo dnf install bcachefs-tools```

```pacman: sudo pacman -S bcachefs-tools```

```apk: sudo apk add bcachefs-tools```

```nix: nix profile install nixpkgs#bcachefs-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bcachefs](/man/bcachefs)(8), [mkfs](/man/mkfs)(8), [fsck](/man/fsck)(8), [mount](/man/mount)(8)

# RESOURCES

```[Homepage](https://bcachefs.org)```

```[Source code](https://evilpiepirate.org/git/bcachefs-tools.git)```

<!-- verified: 2026-06-19 -->
