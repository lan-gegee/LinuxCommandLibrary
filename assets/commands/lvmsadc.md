# TAGLINE

曾是用于收集 I/O 数据的 LVM 系统活动数据收集器

# TLDR

启动**旧版 LVM1** 统计收集器（在现代 LVM2 上已废弃）

```lvmsadc```

在当前系统上，改用 **dmstats** 报告 I/O 统计信息

```dmstats report [/dev/mapper/device]```

# SYNOPSIS

**lvmsadc**

# DESCRIPTION

**lvmsadc** 曾是 LVM 的系统活动数据收集器，用于收集逻辑卷的 I/O 统计信息。它收集原始性能数据，供配套工具 **lvmsar** 分析。

此命令**不受 LVM2 支持**。现代 LVM2 安装应改用 **dmstats**，它提供更全面的设备映射器统计信息，包括直方图数据和基于区域的测量。

# CAVEATS

**已弃用**：此命令只能在旧版 LVM1 系统上工作。对于 LVM2，请使用 **dmstats** 收集并报告设备映射器设备的 I/O 统计信息。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvmsar](/man/lvmsar)(8), [iostat](/man/iostat)(1), [lvm](/man/lvm)(8)
