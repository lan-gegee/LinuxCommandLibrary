# TAGLINE

快速检测假冒闪存

# TLDR

**探测闪存盘是否为假冒内存**（具有破坏性）

```sudo f3probe --destructive [/dev/sdX]```

**探测并附带计时信息**

```sudo f3probe --destructive --time-ops [/dev/sdX]```

**探测时占用最少的内存**（较慢但更省 RAM）

```sudo f3probe --destructive --min-memory [/dev/sdX]```

**使用指定的重置方法探测**

```sudo f3probe --destructive --reset-type=[2] [/dev/sdX]```

**强制指定块大小**

```sudo f3probe --destructive --block-order=[9] [/dev/sdX]```

# SYNOPSIS

**f3probe** [_OPTIONS_] _DEVICE_

# PARAMETERS

**-b**, **--block-order**=_ORDER_
> 强制驱动器的块大小为 2^ORDER 字节。

**-l**, **--min-memory**
> 以速度换取更低的内存占用。

**-n**, **--destructive**
> 探测后不还原块内容（更快但数据会丢失）。

**-s**, **--reset-type**=_TYPE_
> 探测期间使用的重置方法。

**-t**, **--time-ops**
> 对读取、写入和重置操作计时，用于诊断输出。

**-?**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 输出程序版本。

# DESCRIPTION

**f3probe** 是 F3（Fight Flash Fraud）套件的一部分，用于检测虚报存储容量的假冒闪存设备，如 U 盘和 SD 卡。许多假货标称大容量（如 256GB），但实际只包含其中一小部分的存储芯片，一旦写入超过真实容量就会导致数据丢失。

该工具从报告容量的末端开始反向写入唯一的顺序模式。当读取因闪存单元不存在而失败时，它便能确定实际可用容量。f3probe 直接在未挂载的块设备上运行，需要 root 权限。

如果检测到假货，f3probe 会报告其造假类型和真实内存大小。输出结果可以配合 **f3fix** 使用，创建一个与设备实际大小相符的分区。

# CAVEATS

**f3probe 会销毁被测设备上的所有数据。** 切勿在已挂载的文件系统、HDD 或包含重要数据的驱动器上使用。测试前务必卸载设备。大容量驱动器的测试可能耗时较长。可以使用 **lsblk** 命令找到设备路径。

# HISTORY

F3（Fight Flash Fraud）由 Michel Machado 创建，旨在应对网上销售的假冒闪存设备这一普遍问题。这些假货通过修改固件来虚报容量，当用户尝试存储超过实际容量的数据时便会损坏数据。在把重要数据托付给闪存之前，先用它进行验证已成为必要步骤。

# INSTALL

```apt: sudo apt install f3```

```dnf: sudo dnf install f3```

```apk: sudo apk add f3-extra```

```zypper: sudo zypper install f3```

```brew: brew install f3```

```nix: nix profile install nixpkgs#f3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[f3write](/man/f3write)(1), [f3read](/man/f3read)(1), [f3fix](/man/f3fix)(1), [lsblk](/man/lsblk)(8), [badblocks](/man/badblocks)(8)

# RESOURCES

```[Source code](https://github.com/AltraMayor/f3)```

<!-- verified: 2026-07-15 -->
