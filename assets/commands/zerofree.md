# TAGLINE

将 ext2/3/4 文件系统的空闲块清零

# TLDR

将**未挂载**文件系统的空闲块清零

```sudo zerofree /dev/[sda1]```

清理时显示**进度**

```sudo zerofree -v /dev/[sda1]```

**试运行**：只统计非零空闲块的数量而不写入

```sudo zerofree -n /dev/[sda1]```

先将**根**文件系统重新挂载为只读，再清理

```sudo mount -o remount,ro / && sudo zerofree /dev/[sda1]```

# SYNOPSIS

**zerofree** [_OPTIONS_] _device_

# PARAMETERS

**-n**
> 试运行：报告有多少空闲块非零，但不写入任何内容。

**-v**
> 详细输出：清理时以百分比打印进度。

**-f** _fillval_
> 用字节值 fillval（0-255）而非零来填充空闲块。

# DESCRIPTION

**zerofree** 扫描 ext2、ext3 或 ext4 文件系统，并将每个尚未为零的未分配块覆盖为零（或指定的填充字节）。已分配文件中的数据不会被改动。

清零空闲空间主要用于磁盘镜像或压缩之前。一旦空闲块被清零，虚拟机镜像或稀疏文件的体积会显著缩小，随后主机或支持稀疏的工具即可回收这些未使用的空间。

目标文件系统必须处于未挂载或只读挂载状态，因为 zerofree 直接读写块设备，在内核同时修改它时无法安全运行。

# CAVEATS

文件系统不得以读写方式挂载。请从 live/救援环境运行 zerofree，或者先将设备重新挂载为只读（根文件系统通常需要单用户或恢复模式）。仅支持 ext2/3/4。清零不是安全擦除；它只是让空闲空间便于压缩。要销毁已写入的数据，请使用 **shred** 或 **blkdiscard**。

# HISTORY

**zerofree** 由 Ron Yorston 编写，用于帮助缩小 User-Mode Linux 和虚拟机磁盘镜像。它在大多数发行版中以 **zerofree** 软件包形式提供。

# INSTALL

```apt: sudo apt install zerofree```

```dnf: sudo dnf install zerofree```

```apk: sudo apk add zerofree```

```zypper: sudo zypper install zerofree```

```nix: nix profile install nixpkgs#zerofree```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[e2fsck](/man/e2fsck)(8), [fstrim](/man/fstrim)(8), [blkdiscard](/man/blkdiscard)(8), [shred](/man/shred)(1)
