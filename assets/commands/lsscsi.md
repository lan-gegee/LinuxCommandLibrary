# TAGLINE

列出 SCSI 设备及其属性

# TLDR

**列出所有 SCSI 设备**

```lsscsi```

**显示磁盘容量**

```lsscsi -s```

**显示详细属性**

```lsscsi -L```

**显示传输层信息**（SAS、SATA、USB 等）

```lsscsi -t```

**列出 SCSI 主机**

```lsscsi -H```

**显示通用设备名**（sg*）

```lsscsi -g```

# SYNOPSIS

**lsscsi** [_OPTIONS_]

# DESCRIPTION

**lsscsi** 列出 SCSI 设备（包括通过 libata 接入的 SATA 磁盘）及其属性。它提供设备类型、厂商、型号和设备节点路径等信息。

# PARAMETERS

**-L, --list**
> 以 key=value 格式列出属性

**-s, --size**
> 以人类可读的格式显示磁盘容量

**-g, --generic**
> 显示通用 SCSI 设备名（sg*）

**-H, --hosts**
> 列出 SCSI 主机而非设备

**-l, --long**
> 输出附加信息

**-c, --classic**
> 经典输出格式（类似 lsscsi 0.21）

**-d, --device**
> 显示设备的主次设备号

**-t, --transport**
> 显示传输层信息

# CAVEATS

显示的是 Linux SCSI 子系统下的设备，包括 SATA、SAS、USB 大容量存储等。某些虚拟或模拟设备可能不会出现。

# HISTORY

**lsscsi** 以人类可读的方式呈现 sysfs 中内核的 SCSI 设备信息。

# INSTALL

```apt: sudo apt install lsscsi```

```dnf: sudo dnf install lsscsi```

```pacman: sudo pacman -S lsscsi```

```apk: sudo apk add lsscsi```

```zypper: sudo zypper install lsscsi```

```nix: nix profile install nixpkgs#lsscsi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lsblk](/man/lsblk)(8), [lspci](/man/lspci)(8), [lsusb](/man/lsusb)(8)
