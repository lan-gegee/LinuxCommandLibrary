# TAGLINE

调整 exFAT 文件系统参数

# TLDR

打印卷**标签**

```tune.exfat -l [/dev/sdXY]```

设置卷**标签**

```tune.exfat -L [new_label] [/dev/sdXY]```

打印卷 **GUID**

```tune.exfat -u [/dev/sdXY]```

设置卷 **GUID**

```tune.exfat -U [new_guid] [/dev/sdXY]```

打印卷**序列号**

```tune.exfat -i [/dev/sdXY]```

设置卷**序列号**

```tune.exfat -I [new_serial] [/dev/sdXY]```

# SYNOPSIS

**tune.exfat** [_OPTIONS_] _DEVICE_

# PARAMETERS

**-l, --print-label**
> 打印卷标签

**-L, --set-label** _LABEL_
> 设置卷标签

**-u, --print-guid**
> 打印卷 GUID

**-U, --set-guid** _GUID_
> 设置卷 GUID

**-i, --print-serial**
> 打印卷序列号

**-I, --set-serial** _SERIAL_
> 设置卷序列号

# DESCRIPTION

**tune.exfat** 调整 exFAT 文件系统上的可调参数。它可以在不重新格式化文件系统的情况下修改卷标签、GUID 和序列号。

修改参数前必须先卸载设备。该工具适合在不丢失数据的情况下更改卷的标识信息。

# CAVEATS

修改时必须先卸载文件系统。需要 root 权限。不正确的 GUID 或序列号更改可能影响系统对卷的识别。

# INSTALL

```apt: sudo apt install exfatprogs```

```dnf: sudo dnf install exfatprogs```

```pacman: sudo pacman -S exfatprogs```

```apk: sudo apk add exfatprogs```

```zypper: sudo zypper install exfatprogs```

```nix: nix profile install nixpkgs#exfatprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs.exfat](/man/mkfs.exfat)(8), [fsck.exfat](/man/fsck.exfat)(8), [dump.exfat](/man/dump.exfat)(8)
