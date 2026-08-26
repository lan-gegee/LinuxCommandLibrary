# TAGLINE

管理 LVM devices 文件，控制哪些块设备可供 LVM 使用

# TLDR

**列出** devices 文件中记录的设备

```sudo lvmdevices```

向 devices 文件**添加设备**

```sudo lvmdevices --adddev [/dev/sdXN]```

从 devices 文件**移除设备**

```sudo lvmdevices --deldev [/dev/sdXN]```

按 PVID **添加物理卷**

```sudo lvmdevices --addpvid [PVID]```

按 PVID **移除物理卷**

```sudo lvmdevices --delpvid [PVID]```

设备名称变更后**更新** devices 文件

```sudo lvmdevices --update```

**检查** devices 文件是否有问题

```sudo lvmdevices --check```

显示**版本号**

```lvmdevices --version```

# SYNOPSIS

**lvmdevices** [_options_]

# PARAMETERS

**--adddev _device_**
> 按路径向 LVM devices 文件添加设备

**--deldev _device_**
> 按路径从 devices 文件移除设备

**--addpvid _PVID_**
> 按 PVID 添加物理卷

**--delpvid _PVID_**
> 按 PVID 移除物理卷

**--update**
> 更新 devices 文件以反映变化的设备名称

**--check**
> 校验 devices 文件并报告问题

**--version**
> 显示版本信息

# DESCRIPTION

**lvmdevices** 管理 LVM 的 devices 文件，该文件控制哪些块设备可以被 LVM 用作物理卷。它位于 **/etc/lvm/devices/system.devices**，将 LVM 的扫描范围限制为仅列出的设备，从而提升性能并防止意外使用不相关的磁盘。

当添加或移除设备，或设备名称发生变化（例如硬件更换后），lvmdevices 可以相应地更新 devices 文件。**--check** 选项会验证所列设备是否存在且可访问。

devices 文件使用稳定的设备标识符（WWID、序列号）而非可能变化的 /dev/sdX 路径，确保跨重启行为一致。

# CAVEATS

需要 root 权限。如果启用了 devices 文件但某设备未被列出，即使该设备包含有效的 PV 元数据，LVM 也会忽略它。硬件变更后请使用 **--update** 以确保设备路径是最新的。

# INSTALL

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [lvmconfig](/man/lvmconfig)(8), [pvcreate](/man/pvcreate)(8), [pvs](/man/pvs)(8), [vgchange](/man/vgchange)(8)
