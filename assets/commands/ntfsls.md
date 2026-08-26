# TAGLINE

列出 NTFS 分区上的文件

# TLDR

**列出目录内容**

```ntfsls [/dev/sda1]```

**列出指定目录**

```ntfsls [/dev/sda1] -p [/Users]```

**显示所有文件（包括隐藏文件）**

```ntfsls -a [/dev/sda1]```

**长列表格式**

```ntfsls -l [/dev/sda1]```

# SYNOPSIS

**ntfsls** [_options_] _device_ [_path_]

# PARAMETERS

_DEVICE_
> NTFS 分区设备。

**-p** _PATH_
> 要列出的目录路径。

**-a**, **--all**
> 显示隐藏文件。

**-l**, **--long**
> 长列表格式。

**-F**, **--classify**
> 附加文件类型指示符。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ntfsls** 无需挂载文件系统即可列出 NTFS 分区上目录的内容。它直接从块设备读取 NTFS 结构，为检查 NTFS 卷提供类似 ls 的界面。

# CAVEATS

属于 ntfs-3g。只读操作。设备必须为 NTFS 格式。

# HISTORY

ntfsls 作为 **ntfs-3g** 工具的一部分被创建，用于检查 NTFS 文件系统。

# INSTALL

```apt: sudo apt install ntfs-3g```

```dnf: sudo dnf install ntfs-3g```

```pacman: sudo pacman -S ntfs-3g```

```apk: sudo apk add ntfs-3g-progs```

```zypper: sudo zypper install ntfs-3g```

```brew: brew install ntfs-3g```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntfs-3g](/man/ntfs-3g)(1), [ls](/man/ls)(1), [ntfscat](/man/ntfscat)(1)
