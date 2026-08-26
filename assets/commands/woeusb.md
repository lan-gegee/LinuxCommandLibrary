# TAGLINE

创建可启动的 Windows USB 安装盘

# TLDR

创建可启动 USB（**格式化**设备）

```woeusb -d [path/to/windows.iso] [/dev/sdX]```

创建可启动**分区**（不格式化）

```woeusb -p [path/to/windows.iso] [/dev/sdXN]```

# SYNOPSIS

**woeusb** [_OPTIONS_] _SOURCE_ _TARGET_

# PARAMETERS

**-d**, **--device**
> 格式化整个设备并使其可启动（会清除所有数据）

**-p**, **--partition**
> 使用现有分区，不擦除其他分区

**--target-filesystem** _FS_, **--tgt-fs** _FS_
> 目标分区文件系统：FAT 或 NTFS（仅限 device 模式）

**-l** _LABEL_, **--label** _LABEL_
> 所建分区的文件系统标签（仅限 device 模式）

**--workaround-bios-boot-flag**
> 为需要它的 BIOS 切换分区引导标志

**-v**, **--verbose**
> 启用详细输出

**--no-color**
> 禁用彩色输出

**-h**, **--help**
> 显示帮助信息

**-V**, **--version**
> 打印版本信息

# DESCRIPTION

**woeusb** 是 Linux 上的 Windows 介质创建工具。它可以从 ISO 镜像创建可启动的 Windows U 盘安装介质。

--device 模式会格式化整个 U 盘。--partition 模式则保留其他分区上的现有数据。

# CAVEATS

device 模式会擦除 U 盘上的所有数据。需要足够容量的 U 盘。UEFI 启动可能需要 FAT32 文件系统。某些 Windows ISO 可能无法正常工作。

# INSTALL

```nix: nix profile install nixpkgs#woeusb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [ventoy](/man/ventoy)(8)
