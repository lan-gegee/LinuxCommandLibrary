# TAGLINE

挂载或卸载 SteamOS 文件系统分区，主要用于访问

# TLDR

将设备上所有必要的分区**挂载**到目标目录

```sudo mount.steamos [/dev/sdX] [/mnt]```

挂载时使用选项**排除特定分区**（如 /home、overlay）

```sudo mount.steamos -o nohome,nooverlay [/dev/sdX] [/mnt]```

**卸载**目标目录下挂载的所有分区

```sudo mount.steamos -u [/mnt]```

显示**帮助**

```mount.steamos -h```

# SYNOPSIS

**mount.steamos** [_options_] _device_ _mountpoint_

# PARAMETERS

**-o, --options _opts_**
> 挂载选项（nohome、nooverlay 等）

**-u, --unmount**
> 卸载指定目录下的所有分区

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**mount.steamos** 用于挂载或卸载 SteamOS 文件系统分区，主要用途是在从其他操作系统或恢复介质启动时访问 Steam Deck 的存储。

SteamOS 使用复杂的分区布局，通过多个 overlay 来实现系统更新和用户数据分离。此工具负责处理这些特定的挂载需求，包括 A/B 根分区、overlay 文件系统和 home 目录。

该命令简化了原本需要对每个分区执行多条带特定选项的 mount 命令的操作。

# CAVEATS

需要 root 权限。专为 SteamOS 分区布局（Steam Deck）设计。设备应为完整磁盘设备（如 /dev/sda），而非单个分区。从其他系统挂载其分区时，请确保 SteamOS 未在运行。

# SEE ALSO

[mount](/man/mount)(8), [steamos-dump-info](/man/steamos-dump-info)(1), [umount](/man/umount)(8)
