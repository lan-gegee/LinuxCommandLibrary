# TAGLINE

Linux 逻辑卷管理器工具

# TLDR

启动**交互式** shell

```sudo lvm```

初始化**物理卷**

```sudo lvm pvcreate /dev/sda1```

显示**物理卷**

```sudo lvm pvdisplay```

创建**卷组**

```sudo lvm vgcreate vg1 /dev/sda1```

显示**卷组**

```sudo lvm vgdisplay```

创建**逻辑卷**

```sudo lvm lvcreate -L 10G vg1```

显示**逻辑卷**

```sudo lvm lvdisplay```

# SYNOPSIS

**lvm** [_command_ [_OPTIONS_]]

# DESCRIPTION

**lvm** 是 Linux 逻辑卷管理器，通过物理卷（PV）、卷组（VG）和逻辑卷（LV）提供灵活的磁盘管理。它支持动态调整大小、快照、镜像和条带化。

# PARAMETERS

**pvcreate**
> 初始化物理卷

**pvdisplay**
> 显示物理卷信息

**vgcreate**
> 创建卷组

**vgdisplay**
> 显示卷组信息

**lvcreate**
> 创建逻辑卷

**lvdisplay**
> 显示逻辑卷信息

**lvextend**
> 扩展逻辑卷

**lvreduce**
> 缩减逻辑卷

**pvs**
> 报告物理卷信息

**vgs**
> 报告卷组信息

**lvs**
> 报告逻辑卷信息

**pvremove**
> 移除物理卷

**vgremove**
> 移除卷组

**help** _command_
> 显示特定命令的帮助

**-d, --debug**
> 启用详细调试输出（最多重复 6 次以增强）

**-v, --verbose**
> 设置详细级别（重复 1 到 3 次以增强）

**-t, --test**
> 以测试模式运行（不更新元数据）

**-y, --yes**
> 对所有确认提示回答 yes

# CAVEATS

LVM 要求先初始化物理卷才能使用。缩减卷时必须小心操作以避免数据丢失。某些操作要求先卸载逻辑卷。

# HISTORY

**LVM2** 是 Linux 逻辑卷管理器的第二个大版本，提供企业级的存储管理能力。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvcreate](/man/lvcreate)(8), [lvextend](/man/lvextend)(8), [vgcreate](/man/vgcreate)(8), [pvcreate](/man/pvcreate)(8), [pvs](/man/pvs)(8), [vgs](/man/vgs)(8), [lvs](/man/lvs)(8)
