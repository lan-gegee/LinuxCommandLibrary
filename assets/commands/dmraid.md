# TAGLINE

固件 RAID 元数据的发现与激活

# TLDR

**列出所有 RAID 集**

```dmraid -s```

**激活所有 RAID** 集

```dmraid -ay```

**激活指定的 RAID** 集

```dmraid -ay [raidset_name]```

**停用所有 RAID** 集

```dmraid -an```

**显示详细 RAID** 信息

```dmraid -s -s```

**列出块设备**

```dmraid -b```

**清除失效的 RAID** 元数据

```dmraid -E [/dev/sda]```

# SYNOPSIS

**dmraid** [_options_] [_device_...]

# PARAMETERS

**-s**
> 显示 RAID 集（重复使用可查看详情）。

**-ay**
> 激活 RAID 集。

**-an**
> 停用 RAID 集。

**-b**
> 列出块设备。

**-r**
> 列出 RAID 设备。

**-E** _DEVICE_
> 擦除 RAID 元数据。

**-n**
> 试运行（只显示而不执行）。

**-v**
> 详细输出。

# DESCRIPTION

**dmraid** 借助 Linux device-mapper 发现并激活软件 RAID 集。它支持多种硬件 RAID 元数据格式，包括 Intel、NVIDIA、VIA 及其他主板 RAID 控制器的格式。

该工具从磁盘读取 RAID 元数据，并创建 device-mapper 映射，使 RAID 阵列呈现为单个块设备。这让 Linux 能够使用消费级主板上常见的"伪 RAID"（fake RAID）或"固件 RAID"。

dmraid 的运行不依赖 RAID 控制器的 BIOS，即使没有控制器专用驱动也能使用阵列。

# CAVEATS

仅支持特定的元数据格式。某些 RAID 级别的支持有限。激活降级阵列可能有数据风险。不能替代硬件 RAID 控制器或 mdadm 软件 RAID。

# HISTORY

dmraid 由 **Red Hat** 的 **Heinz Mauelshagen** 开发，用于在 Linux 中支持硬件 RAID 元数据格式，解决与使用专有元数据格式的消费级主板 RAID 实现兼容的需求。目前该项目已基本停止维护；大多数发行版已将 Intel IMSM 和 DDF"伪 RAID"支持转移到 **mdadm**——它能读取相同的元数据，是新部署的推荐工具。

# INSTALL

```pacman: sudo pacman -S dmraid```

```apk: sudo apk add dmraid```

```zypper: sudo zypper install dmraid```

```nix: nix profile install nixpkgs#dmraid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mdadm](/man/mdadm)(8), [dmsetup](/man/dmsetup)(8), [lvm](/man/lvm)(8)
