# TAGLINE

已弃用的 LVM1 系统活动报告器，用于逻辑卷 I/O 统计

# TLDR

运行**旧版 LVM1** 统计报告器（在现代 LVM2 上已废弃）

```lvmsar```

报告设备映射器的 **I/O 统计信息**

```dmstats report [/dev/mapper/device]```

**列出**已配置的统计区域

```dmstats list [/dev/mapper/device]```

# SYNOPSIS

**lvmsar**

# DESCRIPTION

**lvmsar** 曾是 LVM 的系统活动报告器，用于显示逻辑卷的 I/O 统计信息。它处理由 **lvmsadc** 收集的数据，并呈现性能指标供分析。

此命令**不受 LVM2 支持**。现代系统应改用 **dmstats**，它提供全面的设备映射器统计信息，包括读/写操作、吞吐量和延迟直方图。

# CAVEATS

**已弃用**：此命令只能在旧版 LVM1 系统上工作。对于 LVM2，请使用 **dmstats report** 查看设备映射器设备上的 I/O 统计信息。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvmsadc](/man/lvmsadc)(8), [sar](/man/sar)(1), [lvm](/man/lvm)(8)
