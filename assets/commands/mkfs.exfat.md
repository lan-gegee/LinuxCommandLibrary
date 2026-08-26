# TAGLINE

在设备上创建 exFAT 文件系统

# TLDR

创建 **exFAT** 文件系统

```sudo mkfs.exfat /dev/sdXY```

创建带**卷标**的文件系统

```sudo mkfs.exfat -L [name] /dev/sdXY```

以指定的**簇大小**创建

```sudo mkfs.exfat -c [32K] /dev/sdXY```

执行**完整格式化**（将整个设备清零）

```sudo mkfs.exfat -f /dev/sdXY```

以**安静模式**创建（只输出错误）

```sudo mkfs.exfat -q /dev/sdXY```

# SYNOPSIS

**mkfs.exfat** [_options_] _device_

# DESCRIPTION

**mkfs.exfat** 在设备上创建 exFAT 文件系统。exFAT 为闪存盘设计，支持大文件（大于 4GB），同时兼容 Windows、macOS 和 Linux。它属于 **exfatprogs** 软件包。

# PARAMETERS

**-L, --volume-label=LABEL**
> 设置卷标

**-U, --volume-guid=GUID**
> 设置卷 GUID

**-c, --cluster-size=SIZE**
> 以字节为单位设置簇大小（必须是 2 的幂）；支持 k/K 表示 kibibyte、m/M 表示 mebibyte

**-s, --sector-size=SIZE**
> 以字节为单位设置扇区大小（512、1024、2048 或 4096）

**-b, --boundary-align=SIZE**
> FAT 与簇堆起始位置的对齐边界

**-f, --full-format**
> 执行完整格式化，将整个磁盘设备清零

**-K, --no-discard**
> 不尝试丢弃（discard）块

**-C, --verify-written**
> 写入后通过回读校验文件系统元数据

**--pack-bitmap**
> 重新定位分配位图，使其结束于 FAT 之后的对齐边界处

**-q, --quiet**
> 只输出错误信息

**-v, --verbose**
> 输出详细的调试信息

**-h, --help**
> 显示帮助并退出

**-V, --version**
> 显示版本并退出

# CAVEATS

设备上的所有数据都将丢失。exFAT 适合需要存放大于 4GB 文件的 U 盘和 SD 卡。

# INSTALL

```apt: sudo apt install exfatprogs```

```dnf: sudo dnf install exfatprogs```

```pacman: sudo pacman -S exfatprogs```

```apk: sudo apk add exfatprogs```

```zypper: sudo zypper install exfatprogs```

```nix: nix profile install nixpkgs#exfatprogs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mkfs](/man/mkfs)(8), [fsck.exfat](/man/fsck.exfat)(8), [mkfs.vfat](/man/mkfs.vfat)(8), [exfatlabel](/man/exfatlabel)(8)
