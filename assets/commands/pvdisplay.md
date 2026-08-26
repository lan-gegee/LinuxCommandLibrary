# TAGLINE

显示 LVM 物理卷的详细信息

# TLDR

**显示所有物理卷**

```sudo pvdisplay```

**显示某一个指定的 PV**

```sudo pvdisplay [/dev/sda2]```

**包含物理区块到逻辑卷的映射**

```sudo pvdisplay --maps [/dev/sda2]```

**简短 / 列式输出**

```sudo pvdisplay -s```

**只显示给定卷组中的 PV**

```sudo pvdisplay --select "vg_name=[vg0]"```

**以易读单位显示大小**（而非默认的两位小数 MiB）

```sudo pvdisplay --units h```

**JSON 格式的输出**

```sudo pvdisplay --reportformat json```

# SYNOPSIS

**pvdisplay** [_options_] [_PhysicalVolume_...]

**pvdisplay** **-c** | **--columns** [_options_] [_PhysicalVolume_...]

# PARAMETERS

_PhysicalVolume_
> 设备路径（例如 `/dev/sda2`、`/dev/nvme0n1p3`）。不提供时列出所有 PV。

**-v**, **--verbose**
> 打印更多细节（可重复使用：`-vv`、`-vvv` 显示更多）。

**-m**, **--maps**
> 显示该 PV 上的物理区块与使用它的每个 LV 的逻辑区块之间的映射。

**-s**, **--short**
> 简短输出——仅显示名称和大小。

**-c**, **--colon**
> 每个 PV 输出为一行冒号分隔的单行（便于脚本处理）。

**-C**, **--columns**
> 等价于 `pvs(8)` 风格的列式输出。

**--units** _u_
> 以单位 _u_ 报告大小：`b`、`k`/`K`、`m`/`M`、`g`/`G`、`t`/`T`、`h`（人类可读）。小写 = SI（1000 的幂）；大写 = IEC（1024 的幂）。

**--select** _SELECTION_
> 仅显示匹配选择表达式的 PV（例如 `vg_name=vg0`、`pv_size>10g`）。

**--reportformat** _FMT_
> `basic`、`json` 或 `json_std`。

**--foreign**
> 显示属于其他主机的 PV（共享存储）。

**--ignorelockingfailure**
> 即使文件/锁定失败也继续（只读操作）。

**--nolocking**
> 禁用锁定（用于调试 / 只读救援）。

**--help**
> 显示帮助。

# DESCRIPTION

**pvdisplay** 打印每个 PV 的信息：设备名、所属卷组、PV 大小、物理区块（PE）大小、总区块数 / 空闲区块数 / 已分配区块数、分配策略、UUID 和状态。配合 `--maps` 还会列出每个 PE 属于哪些 LV 的哪些逻辑区块范围——在使用 `pvmove` 规划数据迁移或检查设备故障时很有用。

对于脚本化输出，建议使用 `pvs`（简短/列式，可调整列列表）或 `pvdisplay -c`。

# CAVEATS

需要 root 权限（或 `cap_sys_admin`）才能读取 PV 元数据。设备必须已用 `pvcreate` 初始化，否则不会出现。在使用 `lvmlockd`/`sanlock` 共享存储的系统上，需添加 `--foreign` 才能看到属于其他主机的 PV。拥有大量快照的超大 VG 可能产生很长的 `--maps` 输出——请分页查看。

# HISTORY

**pvdisplay** 是 **LVM2**（内核级逻辑卷管理器的用户空间工具集）的一部分。LVM2 由 **Red Hat** 维护并以 GPL 许可证发布。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pvs](/man/pvs)(8), [pvcreate](/man/pvcreate)(8), [pvmove](/man/pvmove)(8), [vgdisplay](/man/vgdisplay)(8), [lvdisplay](/man/lvdisplay)(8), [lvm](/man/lvm)(8)
