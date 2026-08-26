# TAGLINE

管理 LVM 物理卷上的 SCSI 持久预留

# TLDR

以**本地密钥**在 VG 中的所有 PV 上启动 PR（默认独占访问）

```lvmpersist start --ourkey [0x1234abcd] --vg [vg_name]```

为**共享 VG** 启动 PR（允许多台主机）

```lvmpersist start --ourkey [0x1234abcd] --access sh --vg [vg_name]```

**停止** VG 上的 PR 并注销本地密钥

```lvmpersist stop --ourkey [0x1234abcd] --vg [vg_name]```

启动 PR 时通过抢占另一主机来**接管**本地 VG

```lvmpersist start --ourkey [0xmy_key] --removekey [0xother_key] --vg [vg_name]```

从共享 VG 中**移除另一主机的密钥**

```lvmpersist remove --ourkey [0xmy_key] --removekey [0xother_key] --vg [vg_name]```

显示 VG 的**已注册密钥**和预留

```lvmpersist read --vg [vg_name]```

对**指定设备**而非 VG 进行操作

```lvmpersist start --ourkey [0x1234abcd] --device [/dev/sdX] --device [/dev/mapper/mpathY]```

# SYNOPSIS

**lvmpersist** _command_ [_options_]

# PARAMETERS

**start**
> 注册密钥并创建持久预留

**stop**
> 释放预留并注销密钥

**remove**
> 从设备上移除另一主机的密钥

**read**
> 显示已注册的密钥和当前预留

**--ourkey _key_**
> 本地主机的预留密钥（十六进制）

**--removekey _key_**
> 要抢占或移除的另一主机的密钥

**--vg _vg_name_**
> 对指定卷组中的所有物理卷进行操作

**--device _device_**
> 对特定设备进行操作（可重复使用）

**--access _type_**
> 预留类型：ex（独占）或 sh（共享）

# DESCRIPTION

**lvmpersist** 管理用作 LVM 物理卷的块设备上的 SCSI 持久预留（PR）。持久预留防止多台主机同时访问共享存储，保护集群或故障转移配置中的数据免遭损坏。

该工具可以建立独占预留（一台主机拥有访问权）或共享预留（多台主机协调访问）。密钥用于标识每台主机，当主机故障或需要强制移除时，可以抢占其预留。

常见用例包括基于 SAN 的集群、高可用故障转移对，以及需要隔离（fencing）的共享存储环境。

# CAVEATS

要求 SCSI 设备支持持久预留（SCSI-3 PR）。并非所有存储阵列都以相同方式实现 PR；请在你自己的环境中测试。不当使用可能导致共享存储环境中的数据丢失。需要 root 权限。

# INSTALL

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [vgchange](/man/vgchange)(8), [pvcreate](/man/pvcreate)(8), [pvs](/man/pvs)(8)
