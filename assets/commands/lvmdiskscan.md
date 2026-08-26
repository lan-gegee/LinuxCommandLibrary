# TAGLINE

扫描系统中所有可见的 SCSI、IDE 和其他磁盘并列出设备

# TLDR

**扫描所有**可用作物理卷的设备

```lvmdiskscan```

只显示**物理卷**（PV）

```lvmdiskscan -l```

提高**详细程度**（重复使用可获得更多细节）

```lvmdiskscan -v```

# SYNOPSIS

**lvmdiskscan** [_options_]

# PARAMETERS

**-l, --lvmpartition**
> 只显示作为 LVM 物理卷的分区

**-v, --verbose**
> 提高详细级别；可重复使用以获得更多细节

# DESCRIPTION

**lvmdiskscan** 扫描系统中所有可见的 SCSI、IDE 及其他磁盘，列出可被 LVM 用作物理卷的设备。它会报告每个设备的大小，以及它是否已经是 LVM 物理卷。

输出显示分区和整块磁盘，并指出哪些包含 LVM 元数据。这有助于在创建新物理卷之前识别可用存储。

# CAVEATS

此命令已**弃用**；列出物理卷请用 **pvs**，设备枚举请用 **lsblk** 等标准工具。在设备众多的系统上扫描可能较慢。获取完整设备信息需要 root 权限。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pvs](/man/pvs)(8), [pvscan](/man/pvscan)(8), [lsblk](/man/lsblk)(8), [lvm](/man/lvm)(8)
