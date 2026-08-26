# TAGLINE

闪存盘容量测试工具

# TLDR

用测试文件**填满已挂载的闪存盘**

```f3write [/media/flash_drive]```

从指定文件编号**开始写**测试文件

```f3write --start-at=[10] [/media/flash_drive]```

写到指定文件编号为止

```f3write --end-at=[50] [/media/flash_drive]```

**写入裸设备**（未挂载）

```sudo f3write -g [/dev/sdX]```

即使设备看起来繁忙也**强制写入**

```f3write --force [/media/flash_drive]```

针对低内存系统优化

```f3write --low-memory [/media/flash_drive]```

# SYNOPSIS

**f3write** [**--start-at**=_NUM_] [**--end-at**=_NUM_] _PATH_

# PARAMETERS

**--start-at**=_NUM_
> 文件名的起始编号（默认：1）。

**--end-at**=_NUM_
> 文件名的结束编号（默认：无限）。

**-a**, **--append**
> 将新文件追加到目标设备上已有文件的后面。

**-b** _BYTES_, **--block-size**=_BYTES_
> 设置 I/O 块大小（字节）（默认：1M）。

**-f**, **--force**
> 即使设备看起来繁忙或已含数据也强制写入。

**-g**, **--full-device**
> 写入整个裸设备（设备必须未挂载）。

**-L**, **--low-memory**
> 为内存有限的系统优化运行方式。

**-s** _OFFSET_, **--start-offset**=_OFFSET_
> 相对设备起始处的偏移量（字节）。

**-S** _OFFSET_, **--end-offset**=_OFFSET_
> 写入应停止的位置偏移量（字节）。

# DESCRIPTION

**f3write** 是 F3（Fight Flash Fraud）套件的一部分，通过用已知数据模式填满闪存设备来测试其真实容量。它向目标文件系统写入名为 N.h2w 的 1GB 文件（N 为数字），直到驱动器写满为止。

典型工作流程是先用 f3write 写入测试数据，再用 **f3read** 进行校验。如果驱动器是虚报容量的假货，f3read 将检测到超出实际物理容量部分的数据损坏。

f3write 可以在已挂载的文件系统上运行（写入目录），也可以使用 **-g** 选项直接写入未挂载的裸设备。

# CAVEATS

**被测磁盘上的所有数据都会被覆盖。** 测试前务必备份重要数据。使用裸设备模式（-g）时，请确保指定正确的设备，以免破坏其他驱动器上的数据。视驱动器容量和速度不同，测试可能耗时较长。

# HISTORY

f3write 由 Michel Machado 作为 F3（Fight Flash Fraud）套件的一部分创建。该工具针对的是普遍存在的假冒闪存问题：这类产品修改固件以虚报容量。当用户尝试存储超过实际容量的数据时，驱动器会通过覆盖已有内容或直接丢弃写入的方式悄悄破坏数据。

# INSTALL

```apt: sudo apt install f3```

```dnf: sudo dnf install f3```

```apk: sudo apk add f3```

```zypper: sudo zypper install f3```

```brew: brew install f3```

```nix: nix profile install nixpkgs#f3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[f3read](/man/f3read)(1), [f3probe](/man/f3probe)(1), [f3fix](/man/f3fix)(1), [dd](/man/dd)(1)

# RESOURCES

```[Source code](https://github.com/AltraMayor/f3)```

<!-- verified: 2026-07-15 -->
