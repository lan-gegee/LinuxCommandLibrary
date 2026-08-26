# TAGLINE

将设备上的文件系统挂载到目录树

# TLDR

显示所有**已挂载的文件系统**

```mount```

将设备**挂载**到目录

```mount [path/to/device] [path/to/target_directory]```

为**指定用户**挂载设备

```mount -o uid=[user_id],gid=[group_id] [device] [directory]```

以只读方式挂载 **CD-ROM**

```mount -t iso9660 -o ro /dev/cdrom /cdrom```

挂载 **/etc/fstab** 中定义的所有文件系统

```mount -a```

将目录**绑定挂载**到另一个位置

```mount --bind [old_directory] [new_directory]```

必要时创建目录并**挂载**

```mount -m [device] [directory]```

# SYNOPSIS

**mount** [_-t type_] [_-o options_] [_device_] [_directory_]

# DESCRIPTION

**mount** 将设备上的文件系统挂载到目录树。不带参数时，它会显示当前已挂载的文件系统。大多数情况下文件系统类型可以自动检测。

# PARAMETERS

**-t, --types type**
> 指定文件系统类型（ext4、ntfs、iso9660、vfat 等）

**-o, --options options**
> 挂载选项（ro、rw、noexec、nosuid、uid、gid 等）

**-a, --all**
> 挂载 /etc/fstab 中的所有文件系统

**-B, --bind**
> 绑定挂载（将目录挂载到另一个位置）

**-m, --mkdir**
> 若挂载点目录不存在则创建它

**-r, --read-only**
> 以只读方式挂载（等价于 -o ro）

**-w, --rw**
> 以读写方式挂载（默认）

**-v, --verbose**
> 详细模式

**-n**
> 挂载时不写入 /etc/mtab

**-L label**
> 按卷标挂载分区

**-U uuid**
> 按 UUID 挂载分区

# COMMON OPTIONS

**ro**: 只读
**rw**: 读写
**noexec**: 不允许执行程序
**nosuid**: 忽略 setuid 位
**noatime**: 不更新访问时间
**uid/gid**: 设置属主用户/组

# CAVEATS

大多数挂载操作需要 root 权限。若要在重启后保持挂载，请使用 /etc/fstab。

# HISTORY

属于 **util-linux** 软件包。mount 命令自 Unix 早期版本起就已存在，可追溯到 **1971 年**。

# INSTALL

```apt: sudo apt install mount```

```apk: sudo apk add mount```

```nix: nix profile install nixpkgs#mount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[umount](/man/umount)(8), [fstab](/man/fstab)(5), [findmnt](/man/findmnt)(8), [lsblk](/man/lsblk)(8)
