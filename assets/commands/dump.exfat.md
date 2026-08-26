# TAGLINE

exFAT 文件系统信息显示工具

# TLDR

打印 **exFAT 文件系统**的磁盘结构信息

```dump.exfat [/dev/sdXY]```

显示指定路径的**目录项**信息

```dump.exfat -d [/path/to/file] [/dev/sdXY]```

从给定路径开始**递归扫描**目录项

```dump.exfat -s [/] -r [/dev/sdXY]```

在目录项之外同时显示**簇链**

```dump.exfat -d [/path/to/file] -c [/dev/sdXY]```

打印**版本**信息

```dump.exfat -V```

# SYNOPSIS

**dump.exfat** [**-d** _file-path_] [**-s** _dir-path_] [**-r**] [**-c**] _device_

# DESCRIPTION

**dump.exfat** 显示 exFAT（Extended File Allocation Table）文件系统的详细磁盘结构信息。它读取并展示文件系统元数据，包括引导扇区参数、FAT（文件分配表）区域布局、簇大小、卷序列号以及其他底层细节。

该工具主要用于取证分析、排查文件系统问题以及理解 exFAT 结构。它能揭示卷标、文件系统版本、每扇区字节数、每簇扇区数、FAT 偏移与长度、簇堆偏移和根目录位置等信息。

exFAT 因支持大文件并且在 Windows、macOS 和 Linux 上兼容性广泛，常用于闪存介质（SD 卡、U 盘）和外部硬盘。dump.exfat 有助于诊断损坏、核对文件系统参数，并分析数据在存储设备上的组织方式。

该工具以只读方式运行，不会修改文件系统。为获得准确的结果，最好先卸载文件系统，不过对已挂载的文件系统进行只读访问也是可行的。

# PARAMETERS

**-V**
> 打印版本并退出。

**-d**, **--dentry-set=**_path_
> 打印设备上给定路径的目录项信息。

**-s**, **--scan-dir=**_dir-path_
> 从给定路径扫描并打印目录项信息。

**-r**, **--recursive**
> 递归扫描目录项。只能与 **-s** 配合使用。

**-c**, **--cluster-chain**
> 在目录项之外同时打印簇链信息。只能与 **-d** 或 **-s** 配合使用。

_device_
> 包含 exFAT 文件系统的设备。

# CAVEATS

属于 exfatprogs 软件包。只读操作。除非从根目录开始递归扫描，否则未发现双重分配的簇并不能保证它们没有被双重分配。

# INSTALL

```apt: sudo apt install exfatprogs```

```dnf: sudo dnf install exfatprogs```

```pacman: sudo pacman -S exfatprogs```

```apk: sudo apk add exfatprogs```

```zypper: sudo zypper install exfatprogs```

```nix: nix profile install nixpkgs#exfatprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fsck.exfat](/man/fsck.exfat)(8), [mkfs.exfat](/man/mkfs.exfat)(8), [tune.exfat](/man/tune.exfat)(8), [exfatlabel](/man/exfatlabel)(8)
