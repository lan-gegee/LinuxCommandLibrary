# TAGLINE

从 NTFS 卷读取文件并输出到 stdout

# TLDR

**从 NTFS 提取文件**

```ntfscat /dev/[sda1] [path/to/file] > [output]```

**按 inode 号提取**

```ntfscat /dev/[sda1] -i [12345] > [output]```

**提取命名数据流**

```ntfscat /dev/[sda1] [file]:stream > [output]```

**强制提取**

```ntfscat -f /dev/[sda1] [file] > [output]```

# SYNOPSIS

**ntfscat** [_options_] _device_ _file_

# PARAMETERS

**-i**, **--inode** _num_
> 使用 inode 号。

**-a**, **--attribute** _type_
> 属性类型。

**-n**, **--attr-name** _name_
> 属性名称。

**-f**, **--force**
> 强制操作。

**-q**, **--quiet**
> 安静模式。

# DESCRIPTION

**ntfscat** 从 NTFS 卷中读取文件并将其内容输出到标准输出。文件可以通过其在卷内的路径引用，也可以通过 MFT inode 号引用；命名备用数据流可使用 `filename:stream` 语法访问。

适用于不挂载卷的情况下从 NTFS 分区进行取证和数据恢复。

# CAVEATS

需要 ntfs-3g 软件包。设备应处于卸载状态或以只读方式挂载。Windows 路径使用反斜杠。

# HISTORY

ntfscat 属于 **ntfs-3g**（开源 NTFS 驱动及实用工具集），提供对 NTFS 文件系统的读取访问。

# INSTALL

```apt: sudo apt install ntfs-3g```

```dnf: sudo dnf install ntfs-3g```

```pacman: sudo pacman -S ntfs-3g```

```apk: sudo apk add ntfs-3g-progs```

```zypper: sudo zypper install ntfs-3g```

```brew: brew install ntfs-3g```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ntfsls](/man/ntfsls)(8), [ntfs-3g](/man/ntfs-3g)(8), [ntfsresize](/man/ntfsresize)(8)
