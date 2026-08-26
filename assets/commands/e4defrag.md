# TAGLINE

ext4 文件系统碎片整理工具

# TLDR

对整个已挂载的文件系统进行**碎片整理**

```sudo e4defrag [/dev/sdXN]```

**整理单个文件**

```sudo e4defrag [path/to/file]```

**整理目录**及其下所有内容

```sudo e4defrag [path/to/directory]```

检查**碎片程度**而不做整理

```sudo e4defrag -c [path/to/file_or_device]```

打印**详细**的逐文件信息

```sudo e4defrag -v [/dev/sdXN]```

# SYNOPSIS

**e4defrag** [**-c**] [**-v**] _target_...

# DESCRIPTION

**e4defrag** 对 ext4 文件系统进行碎片整理。它可以作用于整个文件系统、目录或单个文件。

与离线碎片整理工具不同，e4defrag 可以在文件系统已挂载并正在使用的情况下运行。

# PARAMETERS

**-c**
> 检查当前碎片状态并打印碎片评分，而不进行整理。对你拥有的文件无需 root 权限。

**-v**
> 详细输出，打印每个文件的结果

_target_
> 要整理的设备、目录或文件。设备必须处于挂载状态。

# CAVEATS

仅限 ext4：实际工作由内核的 EXT4_IOC_MOVE_EXT ioctl 完成，因此 ext2/ext3 文件系统会被拒绝。目标文件系统必须处于挂载状态，因为 e4defrag 是在线操作的。碎片整理需要连续的空闲空间，因此对几乎占满的文件系统基本无效。碎片评分低于 30 的文件已被认为状态良好，不会被动。

# INSTALL

```apt: sudo apt install e2fsprogs```

```dnf: sudo dnf install e2fsprogs```

```pacman: sudo pacman -S e2fsprogs```

```apk: sudo apk add e2fsprogs-extra```

```zypper: sudo zypper install e2fsprogs```

```brew: brew install e2fsprogs```

```nix: nix profile install nixpkgs#e2fsprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[e2freefrag](/man/e2freefrag)(8), [e2fsck](/man/e2fsck)(8), [filefrag](/man/filefrag)(8)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/fs/ext2/e2fsprogs.git)```

```[Homepage](https://e2fsprogs.sourceforge.net/)```

<!-- verified: 2026-07-14 -->
