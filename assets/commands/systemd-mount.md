# TAGLINE

创建临时挂载单元

# TLDR

**自动挂载**设备到 /run/media/system/LABEL

```systemd-mount [path/to/device]```

**挂载**设备到指定位置

```systemd-mount [path/to/device] [path/to/mount_point]```

**列出**所有已知的含可挂载文件系统的块设备

```systemd-mount --list```

**创建**自动挂载点

```systemd-mount --automount yes [path/to/device]```

**卸载**一个或多个设备

```systemd-mount -u [path/to/mount_point]```

以指定的文件系统类型**挂载**

```systemd-mount -t [filesystem_type] [path/to/device] [path/to/mount_point]```

附加选项进行**挂载**

```systemd-mount -o [mount_options] [path/to/device] [path/to/mount_point]```

# SYNOPSIS

**systemd-mount** [_options_] _what_ [_where_]

# PARAMETERS

**--list**
> 列出已知的存在可挂载文件系统的块设备

**--automount _bool_**
> 创建自动挂载点

**-u, --umount**
> 卸载指定的挂载点或设备

**-t, --type _fstype_**
> 指定文件系统类型

**-o, --options _opts_**
> 挂载选项

**--owner _user_**
> 设置挂载点的所有者

**-A, --automount**
> 创建 automount 单元

**--discover**
> 使用自动设备发现

# DESCRIPTION

**systemd-mount** 利用 systemd 的挂载处理机制创建和销毁临时的挂载点或自动挂载点。它创建的临时挂载单元会在卸载时被自动清理。

该工具与 systemd 的设备和挂载管理相集成，支持自动挂载（按需挂载）等特性，并通过 systemd 单元正确跟踪挂载状态。

# CAVEATS

所创建的挂载点是临时的，重启后不会保留。若需持久挂载，请使用 fstab 或创建正式的 systemd 挂载单元。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [udisksctl](/man/udisksctl)(1)
