# TAGLINE

检查和修复 LVM 物理卷元数据

# TLDR

打印磁盘上的 LVM **头部和结构**

```sudo pvck /dev/sdX1 --dump headers```

打印当前的 **VG 元数据**文本

```sudo pvck /dev/sdX1 --dump metadata```

列出元数据区域中发现的所有**元数据版本**

```sudo pvck /dev/sdX1 --dump metadata_all```

当头部可能损坏时**搜索**元数据

```sudo pvck /dev/sdX1 --dump metadata_search -f path/to/metadata.txt```

打印时选择**第二个元数据区域**

```sudo pvck /dev/sdX1 --dump metadata --settings "mda_num=2"```

使用元数据文件**修复**头部和元数据

```sudo pvck /dev/sdX1 --repair -f path/to/metadata_file```

仅修复 **PV 头部和标签**

```sudo pvck /dev/sdX1 --repairtype pv_header```

# SYNOPSIS

**pvck** [_options_] _PhysicalVolume_

# PARAMETERS

**--dump** _type_
> 转储指定类型：headers、metadata、metadata_all、metadata_search。

**--repair**
> 修复物理卷上的 LVM 元数据。

**--repairtype** _type_
> 指定修复类型：pv_header、metadata、label_header。

**-f**, **--file** _file_
> 元数据操作的输入/输出文件。

**--settings** _settings_
> 附加设置（例如 mda_num=2）。

**--labelsector** _sector_
> 读取 PV 标签的扇区号（0-3，默认：1）。

**-d**, **--debug**
> 启用调试输出。

**-v**, **--verbose**
> 启用详细输出。

**-y**, **--yes**
> 自动对所有提示回答 yes。

**-t**, **--test**
> 以测试模式运行，不做任何更改。

# DESCRIPTION

**pvck** 检查并修复物理卷上的 LVM 元数据。它可以转储磁盘上的头部和结构（label_header、pv_header、mda_header）、检查元数据区域、在损坏的卷中搜索元数据，以及使用备份元数据文件执行修复。

**--dump** 选项读取并显示元数据而不修改任何内容。**--repair** 选项使用提供的备份文件写入修正后的头部和元数据。一个 PV 最多可以有两个元数据区域（前部和后部），可通过 `--settings "mda_num=2"` 选择。

当物理卷元数据损坏时，该工具对于 LVM 灾难恢复至关重要。

# CAVEATS

修复操作可能具有破坏性。尝试修复前务必备份元数据。在生产系统上使用时须格外谨慎。

# HISTORY

属于 **LVM2**（逻辑卷管理器 2），Linux 的标准卷管理系统。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pvcreate](/man/pvcreate)(8), [pvdisplay](/man/pvdisplay)(8), [vgcfgrestore](/man/vgcfgrestore)(8), [lvm](/man/lvm)(8)
