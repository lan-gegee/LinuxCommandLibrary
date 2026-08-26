# TAGLINE

基于已挂载文件系统生成 /etc/fstab

# TLDR

在 Arch 安装过程中使用卷 UUID 生成 **/etc/fstab**

```genfstab -U /mnt >> /mnt/etc/fstab```

基于卷**标签**显示 fstab 兼容输出

```genfstab -L [path/to/mount_point]```

基于卷 **UUID** 显示 fstab 兼容输出

```genfstab -U [path/to/mount_point]```

基于**指定标识符**显示 fstab 兼容输出

```genfstab -t [LABEL|UUID|PARTLABEL|PARTUUID]```

将卷**追加**到 /etc/fstab 以实现自动挂载

```genfstab -U [path/to/mount_point] | sudo tee -a /etc/fstab```

# SYNOPSIS

**genfstab** [_options_] _root_

# PARAMETERS

**-U**
> 使用 UUID 作为源标识符

**-L**
> 使用文件系统标签作为源标识符

**-t** _TAG_
> 使用指定的标签：LABEL、UUID、PARTLABEL 或 PARTUUID

**-f** _FILTER_
> 将输出限制为匹配给定前缀过滤器的挂载点。

**-p**
> 排除伪文件系统挂载点（默认行为）。

**-P**
> 包含伪文件系统挂载点。

**-h**
> 显示用法和选项。

# DESCRIPTION

**genfstab** 通过检测给定根目录下已挂载的文件系统来生成适用于 /etc/fstab 文件的输出。它主要用于 Arch Linux 安装过程中为新系统创建 fstab 文件。

该工具从 /proc/self/mountinfo 读取挂载信息，并输出规范的 fstab 条目，包括适当的源标识符（UUID、LABEL 等）、相对于指定根目录调整后的挂载点、文件系统类型和挂载选项。

推荐使用 UUID（**-U**），因为它们在硬件变更后保持稳定，而不像 /dev/sda1 这类设备名可能会变化。

# CAVEATS

必须以适当权限运行才能读取挂载信息。目标文件系统必须在运行 genfstab 之前挂载好。写入 /etc/fstab 前请检查输出内容，错误的条目可能导致系统无法启动。

# HISTORY

genfstab 是 **arch-install-scripts** 软件包的一部分，为 Arch Linux 安装而开发。它简化了 fstab 的创建——传统上这一步需要手动完成或使用可靠性较差的方法。该工具已被其他基于 Arch 的发行版采用。

# INSTALL

```apk: sudo apk add alpine-conf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [fstab](/man/fstab)(5), [blkid](/man/blkid)(8), [lsblk](/man/lsblk)(8)
