# TAGLINE

创建 FAT 文件系统（指向 mkfs.fat 的符号链接）

# TLDR

此命令是 **mkfs.fat** 的别名

在设备 X 的分区 Y 内创建 **FAT 文件系统**

```sudo mkfs.vfat [/dev/sdXY]```

创建带**卷名**的 FAT 文件系统

```sudo mkfs.vfat -n [volume_name] [/dev/sdXY]```

指定 **FAT 类型**（12、16 或 32 位）

```sudo mkfs.vfat -F [12|16|32] [/dev/sdXY]```

创建带**自定义簇大小**的 FAT32 文件系统

```sudo mkfs.vfat -F 32 -s [8] [/dev/sdXY]```

设置每簇的**扇区数量**

```sudo mkfs.vfat -F 32 -S [512] [/dev/sdXY]```

# SYNOPSIS

**mkfs.vfat** [_options_] _device_ [_block-count_]

# DESCRIPTION

**mkfs.vfat** 是指向 **mkfs.fat** 的符号链接。它创建 FAT（File Allocation Table，文件分配表）文件系统，常用于 U 盘、SD 卡和 EFI 系统分区。

"vfat" 这个名称指的是 Virtual FAT 扩展，它在 FAT 文件系统上启用了长文件名支持（最长 255 个字符），同时保持与原始 8.3 文件名格式的兼容性。

# INSTALL

```apt: sudo apt install dosfstools```

```dnf: sudo dnf install dosfstools```

```pacman: sudo pacman -S dosfstools```

```apk: sudo apk add dosfstools```

```zypper: sudo zypper install dosfstools```

```brew: brew install dosfstools```

```nix: nix profile install nixpkgs#dosfstools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs.fat](/man/mkfs.fat)(8), [mkfs](/man/mkfs)(8), [fsck](/man/fsck)(8), [fatlabel](/man/fatlabel)(8), [mount](/man/mount)(8)
