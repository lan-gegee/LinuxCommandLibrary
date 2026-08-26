# TAGLINE

以普通用户身份挂载可移动设备

# TLDR

**挂载**设备到 /media/

```pmount [/dev/sdb1]```

使用指定**文件系统**和标签挂载

```pmount -t [ext4] [/dev/sdb1] [mylabel]```

以只读方式挂载 **CD-ROM**

```pmount -t iso9660 -r [/dev/cdrom]```

以读写方式挂载 **NTFS**

```pmount -t ntfs -w [/dev/sdX]```

显示已**挂载**的可移动设备

```pmount```

# SYNOPSIS

**pmount** [**-t** _type_] [**-r**|**-w**] _device_ [_label_]

# PARAMETERS

**-t, --type _fstype_**
> 文件系统类型

**-r, --read-only**
> 以只读方式挂载

**-w, --read-write**
> 强制以读写方式挂载

**-s, --sync**
> 以 sync 选项挂载（不使用写缓存）

**-A, --noatime**
> 以 noatime 选项挂载

**-u, --umask _mask_**
> 为挂载设置 umask

**-e, --exec**
> 允许执行二进制文件（默认：noexec）

**-c, --charset _charset_**
> 设置 I/O 字符集（在 UTF-8 区域环境下默认为 utf8）

**-d, --debug**
> 启用详细的调试信息

**label**
> /media/ 下的挂载点名称

# DESCRIPTION

**pmount** 允许普通用户在无需 root 权限的情况下挂载可移动设备。它会将设备挂载到 /media/ 下，并以设备名或指定标签作为挂载点。默认挂载标志为：async,atime,nodev,noexec,noauto,nosuid,user,rw。

该工具强制执行安全限制：只能挂载 /media 中的设备，且禁用 suid 等危险选项。它专为缺少自动挂载功能的桌面环境而设计。

# CAVEATS

仅适用于可移动设备。挂载点会在 /media/ 下自动创建。卸载请使用 pumount。需要安装 pmount 软件包并具备相应权限。

# HISTORY

**pmount** 的诞生早于 udisks 和现代桌面自动挂载器，旨在提供安全的用户级挂载能力。对于精简系统或不希望使用自动挂载的场景，它依然有用。

# INSTALL

```apt: sudo apt install pmount```

```dnf: sudo dnf install pmount```

```nix: nix profile install nixpkgs#pmount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pumount](/man/pumount)(1), [mount](/man/mount)(8), [udisksctl](/man/udisksctl)(1)
