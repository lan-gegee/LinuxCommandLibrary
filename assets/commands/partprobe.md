# TAGLINE

将分区表的变更告知操作系统内核

# TLDR

**通知**内核分区表的变更

```sudo partprobe```

显示变更**摘要**

```sudo partprobe -s```

**试运行**并显示摘要

```sudo partprobe -d -s```

**探测指定的设备**

```sudo partprobe /dev/[sda]```

# SYNOPSIS

**partprobe** [_OPTIONS_] [_device_...]

# DESCRIPTION

**partprobe** 将分区表的变更告知操作系统内核。在使用 fdisk、parted 或类似工具修改分区之后，partprobe 可以更新内核中的分区表，而无需重启。

# PARAMETERS

**-d, --dry-run**
> 并不真正通知内核，只打印将要执行的操作

**-s, --summary**
> 显示各设备及其分区的摘要

**-h, --help**
> 显示帮助信息

**-v, --version**
> 显示版本

# CAVEATS

无法更新正在使用或已挂载的分区。如果设备上有任何分区处于忙碌状态，内核可能会拒绝更新分区表。这种情况下可能需要重启。

# HISTORY

**partprobe** 属于 **parted** 软件包，负责让分区表与内核保持同步。

# INSTALL

```apt: sudo apt install parted```

```dnf: sudo dnf install parted```

```pacman: sudo pacman -S parted```

```apk: sudo apk add parted```

```zypper: sudo zypper install parted```

```nix: nix profile install nixpkgs#parted```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[parted](/man/parted)(8), [fdisk](/man/fdisk)(8), [lsblk](/man/lsblk)(8)
