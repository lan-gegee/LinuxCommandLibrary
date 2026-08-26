# TAGLINE

exFAT 文件系统检查与修复工具

# TLDR

**检查** exFAT 文件系统错误

```fsck.exfat [/dev/sdXN]```

**自动修复**并对所有问题回答 yes

```fsck.exfat -y [/dev/sdXN]```

以提示方式**交互式修复**

```fsck.exfat -r [/dev/sdXN]```

**自动修复**并在 /LOST+FOUND 中为孤立簇创建文件

```fsck.exfat -p -s [/dev/sdXN]```

**只检查不修复**（只读模式）

```fsck.exfat -n [/dev/sdXN]```

检查时**显示详细输出**

```fsck.exfat -v [/dev/sdXN]```

# SYNOPSIS

**fsck.exfat** [_-rynpavVh_] [_-s_] _device_

# PARAMETERS

**-r**, **--repair**
> 交互式修复文件系统，每次修复前都会提示确认。

**-y**, **--repair-yes**
> 自动修复文件系统，对所有问题回答 yes。

**-n**, **--repair-no**
> 只检查文件系统而不做任何修复（只读模式）。

**-p**, **--repair-auto**
> 自动修复文件系统且不提示（等同于 **-a**）。

**-a**
> 自动修复（**-p** 的别名）。

**-s**
> 在 /LOST+FOUND 目录中为孤立簇创建文件。

**-v**, **--verbose**
> 检查过程中输出调试信息。

**-V**, **--version**
> 显示版本信息并退出。

**-h**, **--help**
> 显示帮助信息并退出。

# DESCRIPTION

**fsck.exfat** 用于在 Linux 上检查和修复 exFAT 文件系统。它是 **exfatprogs** 软件包的一部分，exfatprogs 是自 Linux 内核 5.7 起合并的 exFAT 文件系统的官方用户空间工具集。

该工具可以检测并修复多种文件系统损坏，包括无效的引导扇区参数、错误的簇位图条目、无效的簇链、簇链中的循环以及多个文件共享相同簇的情况。当主引导扇区损坏而备份引导扇区有效时，它还能还原主引导扇区。

运行 fsck.exfat 前，请先卸载文件系统。使用 **lsblk -f** 确认正确的设备名。

# CAVEATS

运行 fsck.exfat 前必须卸载文件系统。对已挂载的文件系统运行可能造成数据损坏。部分早期版本（尤其是 1.1.3）存在可能导致修复失败的 bug；请确保使用 1.2.0 或更高版本以保证可靠运行。

# HISTORY

Samsung 将其 exFAT 驱动贡献给 Linux 内核后，**exfatprogs** 软件包于 **2019** 年创建，成为 Linux 官方的 exFAT 用户空间工具集。该驱动于 **2020** 年合并进 Linux **5.7**，取代了旧的基于 FUSE 的 exfat-utils 实现。Microsoft 于 **2019** 年公开 exFAT 规范的决定促成了这一原生内核支持。

# INSTALL

```apt: sudo apt install exfatprogs```

```dnf: sudo dnf install exfatprogs```

```pacman: sudo pacman -S exfatprogs```

```apk: sudo apk add exfatprogs```

```zypper: sudo zypper install exfatprogs```

```nix: nix profile install nixpkgs#exfatprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fsck](/man/fsck)(8), [mkfs.exfat](/man/mkfs.exfat)(8), [lsblk](/man/lsblk)(8), [mount](/man/mount)(8)

# RESOURCES

```[Source code](https://github.com/exfatprogs/exfatprogs)```

<!-- verified: 2026-07-15 -->
