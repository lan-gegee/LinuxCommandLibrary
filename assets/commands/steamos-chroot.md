# TAGLINE

访问备用的 SteamOS 分区

# TLDR

切换到**另一个** A/B 分区

```steamos-chroot -p other```

切换到**其他磁盘**上的分区

```steamos-chroot -d [/dev/sdX] -p [A|B]```

显示**帮助**

```steamos-chroot -h```

# SYNOPSIS

**steamos-chroot** [_OPTIONS_]

# PARAMETERS

**-p**, **--partset** _A|B|other_
> 选择分区集（A、B 或另一个非活动的分区）

**-d**, **--disk** _DEVICE_
> 指定目标磁盘设备

**-h**, **--help**
> 显示帮助

# DESCRIPTION

**steamos-chroot** 在 SteamOS 环境中切换根目录，从而能够访问备用的 A/B 分区或其他驱动器上的分区。SteamOS 采用 A/B 分区方案来实现可靠的更新，允许一个分区更新时另一个分区保持可启动状态。

该工具可用于恢复操作、系统修复或访问非活动分区上的文件。

# CAVEATS

需要 root 权限。在 chroot 中所做的更改会影响目标分区。在进行中的更新期间切换 A/B 分区时请务必小心。

# HISTORY

**steamos-chroot** 是 **Valve** 为 Steam Deck 开发的 **SteamOS** 工具的一部分。基于 Arch Linux 的 SteamOS 3.0 于 **2022 年**随 Steam Deck 掌上游戏设备一同发布。

# SEE ALSO

[steamos-readonly](/man/steamos-readonly)(1), [chroot](/man/chroot)(1)
