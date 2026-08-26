# TAGLINE

命令行固件更新客户端

# TLDR

显示 fwupd 检测到的所有**设备**

```fwupdmgr get-devices```

从 LVFS 下载最新**固件元数据**

```fwupdmgr refresh```

列出系统设备**可用的更新**

```fwupdmgr get-updates```

**安装**固件更新

```fwupdmgr update```

显示固件**更新历史**

```fwupdmgr get-history```

# SYNOPSIS

**fwupdmgr** [_command_]

# PARAMETERS

**get-devices**
> 显示 fwupd 检测到的所有设备

**refresh**
> 从 Linux Vendor Firmware Service（LVFS）下载最新固件元数据

**get-updates**
> 列出检测到的设备的可用固件更新

**update**
> 下载并安装固件更新

**get-history**
> 显示固件更新历史

**downgrade**
> 将固件降级到旧版本

**get-releases**
> 显示设备的可用固件发行版本

**reinstall**
> 重新安装当前固件

**--version**
> 显示 fwupdmgr 版本

# DESCRIPTION

**fwupdmgr** 是 fwupd（Linux 固件更新守护进程）的命令行客户端。它可以更新 UEFI/BIOS、SSD、Thunderbolt 控制器以及其他受支持硬件的设备固件。

该工具连接 Linux Vendor Firmware Service（LVFS）下载经签名的固件更新。厂商将固件提交至 LVFS，再分发给 Linux 用户。根据设备类型的不同，更新要么立即应用，要么安排在下一次重启时应用。

UEFI 更新要求 EFI System Partition 已正确挂载且可写。

# CAVEATS

固件更新若被中断可能导致硬件变砖。更新期间请确保供电稳定。某些更新需要重启才能生效。更新 UEFI 固件前，可能需要以写权限重新挂载 /boot 或 EFI 分区。

# HISTORY

fwupdmgr 属于 fwupd，由 Richard Hughes 于 **2015 年**创建。该项目旨在为 Linux 带来可靠的固件更新，并通过 Linux Vendor Firmware Service 与硬件厂商合作。Dell、联想、HP 和罗技等主要厂商现在都通过 LVFS 分发固件。

# INSTALL

```apt: sudo apt install fwupd```

```dnf: sudo dnf install fwupd```

```pacman: sudo pacman -S fwupd```

```apk: sudo apk add fwupd```

```zypper: sudo zypper install fwupd```

```brew: brew install fwupd```

```nix: nix profile install nixpkgs#fwupd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fwupdtool](/man/fwupdtool)(1), [efibootmgr](/man/efibootmgr)(8)

# RESOURCES

```[Source code](https://github.com/fwupd/fwupd)```

```[Homepage](https://fwupd.org/)```

<!-- verified: 2026-07-15 -->
