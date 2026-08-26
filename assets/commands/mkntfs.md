# TAGLINE

创建 NTFS 文件系统

# TLDR

**创建 NTFS 文件系统**

```mkntfs [/dev/sdb1]```

**快速格式化**

```mkntfs -f [/dev/sdb1]```

**设置卷标**

```mkntfs -L "[Label]" [/dev/sdb1]```

**详细输出**

```mkntfs -v [/dev/sdb1]```

**强制创建**

```mkntfs -F [/dev/sdb1]```

**设置簇大小**

```mkntfs -c [4096] [/dev/sdb1]```

# SYNOPSIS

**mkntfs** [_options_] _device_

# PARAMETERS

_DEVICE_
> 要格式化的块设备。

**-f**
> 快速格式化。

**-L** _LABEL_
> 卷标。

**-v**
> 详细输出。

**-F**
> 强制创建。

**-c** _SIZE_
> 簇大小。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mkntfs** 创建 NTFS 文件系统。NTFS 是 Windows 的原生文件系统。

该工具是 ntfs-3g/ntfsprogs 的一部分。可创建兼容的 NTFS 卷。

# CAVEATS

会销毁现有数据。属于 ntfs-3g。与 Windows 兼容。

# HISTORY

mkntfs 属于 **ntfs-3g** 项目，在 Linux 上提供 NTFS 文件系统的创建能力。

# INSTALL

```apt: sudo apt install ntfs-3g```

```dnf: sudo dnf install ntfs-3g```

```pacman: sudo pacman -S ntfs-3g```

```apk: sudo apk add ntfs-3g-progs```

```zypper: sudo zypper install ntfs-3g```

```brew: brew install ntfs-3g```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs.ntfs](/man/mkfs.ntfs)(8), [ntfs-3g](/man/ntfs-3g)(8), [ntfsfix](/man/ntfsfix)(8)
