# TAGLINE

按标签或 UUID 定位文件系统

# TLDR

**按文件系统标签查找设备**

```findfs LABEL=[label]```

**按文件系统 UUID 查找设备**

```findfs UUID=[uuid]```

**按 GPT 分区标签查找设备**

```findfs PARTLABEL=[partition_label]```

**按 GPT 分区 UUID 查找设备**

```findfs PARTUUID=[partition_uuid]```

# SYNOPSIS

**findfs** _tag_=_value_

# DESCRIPTION

**findfs** 通过标签或 UUID 查找文件系统，并打印对应的设备路径。它会遍历所有块设备，寻找文件系统元数据匹配的那一个。

启动脚本和挂载操作常用它来可靠地定位文件系统。

# PARAMETERS

**LABEL=**_label_
> 按文件系统标签搜索

**UUID=**_uuid_
> 按文件系统 UUID 搜索

**PARTLABEL=**_label_
> 按 GPT/MAC 分区标签搜索

**PARTUUID=**_uuid_
> 按 GPT 分区 UUID 搜索

# CAVEATS

属于 util-linux。PARTUUID 仅存在于 GPT 分区表上。要想匹配可靠，标签与 UUID 必须唯一。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[blkid](/man/blkid)(8), [lsblk](/man/lsblk)(8), [fstab](/man/fstab)(5)
