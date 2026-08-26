# TAGLINE

从挂载点卸载文件系统

# TLDR

按设备路径**卸载**文件系统

```sudo umount [path/to/device]```

按挂载点**卸载**文件系统

```sudo umount [path/to/mounted_directory]```

卸载失败时**重新以只读方式挂载**

```sudo umount -r [path/to/mounted_directory]```

**递归地**卸载每个目录

```sudo umount -R [path/to/mounted_directory]```

**延迟卸载**（立即脱离，不再繁忙时清理）

```sudo umount -l [path/to/mounted_directory]```

对无法访问的 NFS 文件系统**强制卸载**

```sudo umount -f [path/to/mounted_directory]```

**卸载**所有已挂载的文件系统（proc 除外）

```sudo umount -a```

# SYNOPSIS

**umount** [_options_] _target_...

# PARAMETERS

**-a**, **--all**
> 卸载 /etc/mtab 中描述的所有文件系统（proc 除外）。

**-A**, **--all-targets**
> 卸载当前命名空间中指定文件系统的所有挂载点。

**-r**, **--read-only**
> 如果卸载失败，尝试重新以只读方式挂载。

**-R**, **--recursive**
> 递归卸载每个指定的目录。

**-l**, **--lazy**
> 延迟卸载：立即从文件层次结构中脱离，等不再繁忙时再清理引用。

**-f**, **--force**
> 强制卸载（用于无法访问的 NFS 挂载）。

**-d**, **--detach-loop**
> 如果被卸载的设备是回环设备，则释放该回环设备。

**-n**, **--no-mtab**
> 不写入 /etc/mtab。

**-t**, **--types** _type_
> 仅卸载指定类型的文件系统。

**-O**, **--test-opts** _opts_
> 仅卸载在 /etc/fstab 中带有指定选项的文件系统。

**-v**, **--verbose**
> 详细输出模式。

# DESCRIPTION

**umount** 将文件系统从其挂载点脱离，使其不再可访问。可以通过源设备或挂载点目录来指定文件系统。

文件系统处于"繁忙"状态时无法卸载——即其上的文件仍处于打开状态，或进程的工作目录位于其中。使用 **lsof** 或 **fuser** 查找正在使用该文件系统的进程。

# CAVEATS

需要 root 权限，除非 fstab 中指定了 **user** 选项。繁忙的文件系统无法正常卸载。延迟卸载（**-l**）可能使文件系统处于不一致状态。强制卸载（**-f**）仅对 NFS 有效。属于 util-linux 软件包的一部分。

# HISTORY

**umount** 自最早的 Unix 版本起就是标准命令，在 Linux 上是 **util-linux** 软件包的一部分。延迟卸载选项（**-l**）在 Linux 2.4.11 中加入。

# INSTALL

```apt: sudo apt install mount```

```apk: sudo apk add umount```

```nix: nix profile install nixpkgs#mount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [fuser](/man/fuser)(1), [lsof](/man/lsof)(8), [findmnt](/man/findmnt)(8)
