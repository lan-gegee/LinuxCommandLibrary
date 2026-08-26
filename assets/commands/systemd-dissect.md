# TAGLINE

检查和挂载磁盘镜像

# TLDR

**显示**镜像的一般信息

```systemd-dissect [path/to/image.raw]```

**挂载**一个 OS 镜像

```systemd-dissect -m [path/to/image.raw] [/mnt/image]```

**卸载**一个 OS 镜像

```systemd-dissect -u [/mnt/image]```

**列出**镜像中的文件

```systemd-dissect -l [path/to/image.raw]```

将 OS 镜像**接入**回环设备

```systemd-dissect --attach [path/to/image.raw]```

将 OS 镜像从回环设备**分离**

```systemd-dissect --detach [path/to/device]```

# SYNOPSIS

**systemd-dissect** [_options_] [_image_]

# PARAMETERS

**-m, --mount**
> 将镜像挂载到目录

**-u, --umount**
> 卸载已挂载的镜像

**-l, --list**
> 列出镜像中的文件

**--attach**
> 将镜像接入回环设备

**--detach**
> 将镜像从回环设备分离

**-x, --copy-from**
> 从镜像复制文件

**-a, --copy-to**
> 向镜像复制文件

**--root-hash _hash_**
> 指定 dm-verity 根哈希

# DESCRIPTION

**systemd-dissect** 用于检查和操作可发现磁盘镜像（DDI）及其他 OS 磁盘镜像。它可以挂载、列出和操作镜像内容，无需手动设置回环设备。

该工具支持多种镜像格式，包括带 GPT 分区表的原始磁盘镜像，并遵循可发现分区规范自动识别分区类型。

# CAVEATS

需要内核对镜像中的文件系统类型提供相应支持。dm-verity 镜像需要提供根哈希。属于 systemd 工具套件的一部分。

# INSTALL

```apt: sudo apt install systemd-container```

```dnf: sudo dnf install systemd-container```

```zypper: sudo zypper install systemd-container```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-nspawn](/man/systemd-nspawn)(1), [losetup](/man/losetup)(8), [mount](/man/mount)(8)
