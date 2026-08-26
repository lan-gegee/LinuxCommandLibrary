# TAGLINE

创建 GRUB 设备映射文件

# TLDR

**生成设备映射**

```sudo grub-mkdevicemap```

**指定输出文件**

```sudo grub-mkdevicemap -m /boot/grub/device.map```

**详细输出**

```sudo grub-mkdevicemap -v```

# SYNOPSIS

**grub-mkdevicemap** [_options_]

# PARAMETERS

**-m**, **--device-map** _FILE_
> 输出的设备映射文件（默认：/boot/grub/device.map）。

**-n**, **--no-floppy**
> 跳过软盘检测。

**-s**, **--probe-second-floppy**
> 同时探测第二个软盘驱动器。

**-v**, **--verbose**
> 详细模式。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**grub-mkdevicemap** 为 GRUB 创建设备映射文件，将 BIOS 驱动器编号映射到 Linux 设备名。该映射帮助 GRUB 理解磁盘顺序。

映射会自动生成，但在磁盘顺序需要显式控制的特殊配置下也可以手动定制。

# CAVEATS

如今大多已无必要，因为 GRUB 会动态生成设备映射，并在 grub.cfg 中通过 UUID 或标签识别磁盘。但在需要覆盖自动检测结果时仍然有用，例如用分区或逻辑卷充当虚拟机的磁盘时。

# HISTORY

grub-mkdevicemap 作为 **GNU GRUB** 的一部分开发，用于 BIOS 与 Linux 之间的设备映射。

# INSTALL

```apt: sudo apt install grub-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-install](/man/grub-install)(8), [grub-mkconfig](/man/grub-mkconfig)(8), [grub](/man/grub)(8)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
