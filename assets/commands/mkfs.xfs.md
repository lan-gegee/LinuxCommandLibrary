# TAGLINE

在分区或设备上创建 XFS 文件系统

# TLDR

在分区上创建 **XFS 文件系统**

```sudo mkfs.xfs /dev/sdXY```

创建带**卷标**的文件系统

```sudo mkfs.xfs -L mylabel /dev/sdXY```

**强制**创建（覆盖已有内容）

```sudo mkfs.xfs -f /dev/sdXY```

设置**块大小**

```sudo mkfs.xfs -b size=4096 /dev/sdXY```

以指定的 **inode 大小**创建

```sudo mkfs.xfs -i size=512 /dev/sdXY```

# SYNOPSIS

**mkfs.xfs** [_options_] _device_

# DESCRIPTION

**mkfs.xfs** 在分区或设备上创建 XFS 文件系统。XFS 是一款高性能日志文件系统，专为可扩展性和并行 I/O 操作而设计。

# PARAMETERS

**-L LABEL**
> 设置文件系统卷标（最长 12 个字符）

**-f**
> 强制覆盖已有的文件系统

**-b size=N**
> 以字节为单位设置块大小（512-65536，通常默认为 4096）

**-i size=N**
> 以字节为单位设置 inode 大小

**-d options**
> 数据区选项（agcount、file、name、size 等）

**-l options**
> 日志区选项（internal、size、version 等）

**-n options**
> 命名选项（size、version 等）

**-r options**
> 实时区选项

**-q**
> 安静模式；抑制输出

**-N**
> 试运行；只打印参数而不创建文件系统

# CAVEATS

创建文件系统会销毁设备上的所有现有数据。设备不应处于挂载状态。XFS 无法缩小，只能扩大。

# HISTORY

**mkfs.xfs** 属于 **xfsprogs**（XFS 文件系统工具集）。XFS 最初由硅图（Silicon Graphics）为其 IRIX 系统开发，2001 年被移植到 Linux。

# INSTALL

```apt: sudo apt install xfsprogs```

```dnf: sudo dnf install xfsprogs```

```pacman: sudo pacman -S xfsprogs```

```apk: sudo apk add xfsprogs```

```zypper: sudo zypper install xfsprogs```

```nix: nix profile install nixpkgs#xfsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xfs](/man/xfs)(5), [xfs_admin](/man/xfs_admin)(8), [xfs_repair](/man/xfs_repair)(8), [mkfs](/man/mkfs)(8)
