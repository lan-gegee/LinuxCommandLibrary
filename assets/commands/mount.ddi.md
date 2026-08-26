# TAGLINE

可发现磁盘镜像（Discoverable Disk Image）的挂载助手

# TLDR

**挂载**一个可发现磁盘镜像

```mount.ddi [path/to/image.raw] [/mnt/image]```

通过**标准 mount 命令**挂载

```mount -t ddi [path/to/image.raw] [/mnt/image]```

以**只读方式**挂载

```mount -t ddi -o ro [path/to/image.raw] [/mnt/image]```

# SYNOPSIS

**mount.ddi** _image-file_ _mount-directory_ [**-o** _options_]

# PARAMETERS

**ro**
> 以只读方式挂载

**rw**
> 以读写方式挂载

**discard**
> 启用块丢弃（discard）

**nodiscard**
> 禁用块丢弃（discard）

**defaults**
> 使用标准挂载行为

# DESCRIPTION

**mount.ddi** 是可发现磁盘镜像（DDI）的挂载助手。它实现了 mount(8) 的外部助手接口，使 DDI 镜像能够使用标准 mount 语法进行挂载。

当 systemd-dissect 被符号链接为 /sbin/mount.ddi 后，系统可以通过 mount 命令配合 -t ddi 文件系统类型直接挂载 DDI 镜像。这使得通过 /etc/fstab 条目在启动时自动挂载成为可能。

DDI 镜像遵循可发现分区规范（Discoverable Partitions Specification），无需手动配置即可自动识别和挂载分区。

# FSTAB EXAMPLE

```
/path/to/image.raw /images/myimage/ ddi defaults 0 0
```

# CAVEATS

需要安装 systemd-dissect 并将其符号链接到 /sbin/mount.ddi。递归卸载镜像内嵌套的文件系统请使用 umount -R。镜像必须符合可发现分区规范。

# HISTORY

**mount.ddi** 是 **systemd** 的一部分，提供了 DDI 磁盘镜像与标准 Unix 挂载基础设施之间的集成。它的开发目的是简化操作系统镜像和可移植服务镜像的挂载。

# INSTALL

```apt: sudo apt install systemd-container```

```dnf: sudo dnf install systemd-container```

```zypper: sudo zypper install systemd-container```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-dissect](/man/systemd-dissect)(1), [mount](/man/mount)(8), [umount](/man/umount)(8)
