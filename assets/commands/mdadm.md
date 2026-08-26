# TAGLINE

管理 Linux 软件 RAID 阵列

# TLDR

**创建** RAID 阵列

```sudo mdadm --create /dev/md/MyRAID --level raid1 --raid-devices 2 /dev/sda1 /dev/sdb1```

**停止**阵列

```sudo mdadm --stop /dev/md0```

将磁盘标记为**故障**

```sudo mdadm --fail /dev/md0 /dev/sda1```

**移除**磁盘

```sudo mdadm --remove /dev/md0 /dev/sda1```

**添加**磁盘

```sudo mdadm --assemble /dev/md0 /dev/sdc1```

显示**详情**

```sudo mdadm --detail /dev/md0```

**清除** RAID 元数据

```sudo mdadm --zero-superblock /dev/sda1```

# SYNOPSIS

**mdadm** [_mode_] [_OPTIONS_] _device_

# DESCRIPTION

**mdadm** 管理 Linux 软件 RAID 阵列（md 设备）。它可以创建、组装、监控、扩展和管理各种 RAID 级别的阵列，包括 RAID 0、1、5、6 和 10。

# PARAMETERS

**--create** _device_
> 创建新阵列

**--assemble** _device_
> 组装先前创建的阵列

**--stop** _device_
> 停止活动阵列

**--detail** _device_
> 显示阵列的详细信息

**--examine** _device_
> 检查组件设备上的 RAID 超级块

**--fail** _device_ _component_
> 将组件标记为故障

**--remove** _device_ _component_
> 从阵列中移除组件

**--add** _device_ _component_
> 向阵列添加组件

**--level** _level_
> RAID 级别（0、1、5、6、10、linear）

**--raid-devices** _n_
> 阵列中的活动设备数量

**--zero-superblock** _device_
> 从设备上擦除 RAID 超级块

# CAVEATS

创建阵列会销毁组件设备上的现有数据。RAID 不是备份方案。RAID 5/6 分别需要至少 3/4 个设备。务必持续监控阵列中的故障硬盘。

# HISTORY

**mdadm** 是现代的 Linux 软件 RAID 管理工具，取代了旧的 raidtools。

# INSTALL

```apt: sudo apt install mdadm```

```dnf: sudo dnf install mdadm```

```pacman: sudo pacman -S mdadm```

```apk: sudo apk add mdadm```

```zypper: sudo zypper install mdadm```

```nix: nix profile install nixpkgs#mdadm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsblk](/man/lsblk)(8), [blkid](/man/blkid)(8)
