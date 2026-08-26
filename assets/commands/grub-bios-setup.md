# TAGLINE

将 GRUB 引导代码写入 BIOS 系统的 MBR

# TLDR

设置某个设备以**通过 GRUB 启动**

```grub-bios-setup /dev/sdX```

即使**检测到问题**也继续安装

```grub-bios-setup -f /dev/sdX```

在**特定目录**中安装 GRUB

```grub-bios-setup -d /boot/grub /dev/sdX```

同时使驱动器可作为**软盘启动**

```grub-bios-setup -a /dev/sdX```

# SYNOPSIS

**grub-bios-setup** [_options_] _device_

# PARAMETERS

**-b**, **--boot-image** _FILE_
> 使用 _FILE_ 作为引导映像，而不是 boot.img

**-c**, **--core-image** _FILE_
> 使用 _FILE_ 作为核心映像，而不是 core.img

**-d**, **--directory** _DIR_
> 使用 _DIR_ 中的 GRUB 文件，而非默认位置

**-m**, **--device-map** _FILE_
> 使用来自 _FILE_ 的设备映射

**-f**, **--force**
> 即使检测到问题也安装

**-a**, **--allow-floppy**
> 使驱动器同时可作为软盘启动（在某些 BIOS 上可能失效）

**-s**, **--skip-fs-probe**
> 跳过文件系统探测

**--no-rs-codes**
> 不添加 Reed-Solomon 纠错码（仅限 x86 BIOS 目标）

**-v**, **--verbose**
> 启用详细输出

# DESCRIPTION

**grub-bios-setup** 是一个底层工具，用于将 GRUB 引导代码写入磁盘的主引导记录（MBR）或 BIOS 引导分区，供 BIOS/传统引导系统使用。

大多数情况下应改用 **grub-install**，它会自动完成复制 GRUB 文件和运行 grub-bios-setup 两个步骤。本工具通常用于高级场景，例如把 GRUB 安装到与 GRUB 文件所在位置不同的设备上。

# CAVEATS

仅适用于 BIOS 系统；UEFI 系统使用不同的方法。使用不当可能导致系统无法启动。要求 GRUB 文件已经就位（常规安装请使用 grub-install）。

# HISTORY

grub-bios-setup 属于 GRUB 2，提供了原先由单一 grub-install 命令处理的底层 MBR 安装功能。这种拆分为复杂的安装场景带来了更大的灵活性。

# INSTALL

```apt: sudo apt install grub-pc```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-install](/man/grub-install)(8), [grub-mkconfig](/man/grub-mkconfig)(8)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
