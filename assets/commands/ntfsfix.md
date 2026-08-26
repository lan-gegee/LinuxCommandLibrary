# TAGLINE

修复阻碍文件系统挂载的常见 NTFS 问题

# TLDR

修复块设备上的 **NTFS 文件系统**

```sudo ntfsfix [/dev/sdXN]```

# SYNOPSIS

**ntfsfix** [_options_] _device_

# PARAMETERS

**-b, --clear-bad-sectors**
> 清除坏扇区列表

**-d, --clear-dirty**
> 清除卷上的脏标记

**-n, --no-action**
> 执行试运行；不实际写入更改

# DESCRIPTION

**ntfsfix** 修复阻碍文件系统挂载的常见 NTFS 问题。它会重置 NTFS 日志、清除脏标记，并修复一些结构性问题，但不执行完整的文件系统检查。

当 Windows 未正常关机导致 NTFS 分区被标记为需要检查（脏）时，这个工具非常有用。它让 Linux 无需先启动进入 Windows 就能以读写模式挂载该分区。

要进行全面的 NTFS 修复，应使用 Windows 内置的 **chkdsk**，因为 ntfsfix 只处理阻碍挂载的基础问题。

# CAVEATS

**不是完整的修复工具**；全面修复请使用 Windows chkdsk。分区必须处于卸载状态。不能修复所有 NTFS 损坏——严重问题仍需 Windows 处理。属于 ntfs-3g 软件包。

# INSTALL

```apt: sudo apt install ntfs-3g```

```dnf: sudo dnf install ntfs-3g```

```pacman: sudo pacman -S ntfs-3g```

```apk: sudo apk add ntfs-3g-progs```

```zypper: sudo zypper install ntfs-3g```

```brew: brew install ntfs-3g```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntfs-3g](/man/ntfs-3g)(8), [mount](/man/mount)(8), [fsck](/man/fsck)(8)
