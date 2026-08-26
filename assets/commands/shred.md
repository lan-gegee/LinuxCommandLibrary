# TAGLINE

安全覆写并删除文件

# TLDR

**安全删除文件**

```shred [file]```

**粉碎并移除文件**

```shred -u [file]```

**按指定次数粉碎**

```shred -n [5] [file]```

**粉碎后补零覆盖**（掩盖粉碎痕迹）

```shred -z [file]```

**详细输出地粉碎**（显示进度）

```shred -v [file]```

**粉碎多个文件**

```shred -u [file1] [file2] [file3]```

**粉碎磁盘分区**（危险）

```sudo shred -v /dev/[sdX]```

# SYNOPSIS

**shred** [_options_] _file_...

# PARAMETERS

**-u**, **--remove**
> 覆写后截断并删除文件

**-n** _N_, **--iterations**=_N_
> 覆写 N 次（默认：3）

**-z**, **--zero**
> 最后追加一次全零覆写，掩盖粉碎痕迹

**-v**, **--verbose**
> 显示进度

**-f**, **--force**
> 必要时修改权限以允许写入

**-s** _N_, **--size**=_N_
> 只粉碎前 N 字节（接受 K、M、G 后缀）

**--random-source**=_FILE_
> 从 FILE 获取随机字节

**-x**, **--exact**
> 不把文件大小向上取整到完整块

# DESCRIPTION

**shred** 通过多次覆写文件使其难以恢复，随后可选地将其删除。它会向文件数据写入多遍随机模式，尝试从物理层面销毁信息。

默认情况下，shred 执行 3 遍随机覆写。加上 **-z** 会进行最后一遍全零覆写，使粉碎不那么显眼（文件看起来只是被清零，而不是被刻意销毁）。

shred 可用于普通文件或整个设备（磁盘分区）。对设备使用时会覆写设备上的全部数据。

**-u** 选项在粉碎后删除文件，删除前还会先重命名文件以掩盖原始文件名。

# CAVEATS

**日志式文件系统**：在 ext3、ext4、ReiserFS 等文件系统上，shred 可能无效，因为文件系统可能先在其他位置写入数据，而只有当前位置会被粉碎。

**写时复制文件系统**：在 Btrfs、ZFS 等文件系统上，shred 无效，因为旧数据仍保留在之前的快照中。

**SSD 和闪存**：磨损均衡机制使数据不会被就地覆写。请改用厂商提供的安全擦除命令或整盘加密。

**RAID**：条带化和镜像机制增加了安全删除的难度。数据可能残留在各个单独的磁盘上。

**要获得最大安全性**，应从一开始就启用整盘加密；这样无论文件系统或存储类型如何，销毁密钥即可让所有数据无法恢复。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rm](/man/rm)(1), [wipe](/man/wipe)(1), [srm](/man/srm)(1), [dd](/man/dd)(1)
