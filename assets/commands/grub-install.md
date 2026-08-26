# TAGLINE

将 GRUB 引导加载程序安装到设备

# TLDR

在 **BIOS 系统**上安装 GRUB

```sudo grub-install [/dev/device]```

以**指定架构**在 BIOS 系统上安装 GRUB

```sudo grub-install --target i386-pc [/dev/device]```

在 **UEFI 系统**上安装 GRUB

```sudo grub-install --efi-directory [/path/to/efi]```

在 UEFI 上以**指定架构和引导加载程序 ID** 安装 GRUB

```sudo grub-install --target x86_64-efi --efi-directory [/path/to/efi] --bootloader-id GRUB```

安装 GRUB 并**预加载指定模块**

```sudo grub-install --target x86_64-efi --efi-directory [/path/to/efi] --modules "part_gpt part_msdos"```

显示**帮助**

```grub-install --help```

# SYNOPSIS

**grub-install** [_options_] _device_

# PARAMETERS

**--target** _PLATFORM_
> 安装目标：i386-pc（BIOS）、x86_64-efi、i386-efi、arm-efi

**--efi-directory** _DIR_
> EFI 系统分区挂载点

**--bootloader-id** _ID_
> 在 EFI 菜单中显示的引导管理器标识符

**--boot-directory** _DIR_
> 存放启动文件的目录（默认：/boot）

**--modules** _MODULES_
> 预加载指定的 GRUB 模块

**--recheck**
> 删除设备映射并重新生成

**--removable**
> 安装到可移动介质路径

**--force**
> 即使检测到问题也强制安装

# DESCRIPTION

**grub-install** 将 GRUB 引导加载程序安装到磁盘设备或 EFI 系统分区。BIOS/legacy 与 UEFI 系统的安装方式有所不同。

对于 **BIOS 系统**，GRUB 被安装到主引导记录（MBR）或 GPT 磁盘上的 BIOS Boot 分区。对于 **UEFI 系统**，GRUB 被安装到 EFI 系统分区（ESP），并且 **--bootloader-id** 选项设置在 UEFI 启动菜单中显示的名称。

安装完成后，运行 **grub-mkconfig** 生成配置文件。

# CAVEATS

需要 root 权限。错误的安装可能导致系统无法启动——请提前准备好恢复介质。UEFI 安装要求 ESP 已挂载。安全启动（Secure Boot）可能需要经过签名的 GRUB 二进制文件。

# HISTORY

大约在 **2009 年**，GRUB 2 的 grub-install 取代了较旧的 GRUB Legacy 安装方式。它支持 GPT 分区表、UEFI 和模块化设计等现代特性。

# INSTALL

```apt: sudo apt install grub2-common```

```dnf: sudo dnf install grub2-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

```zypper: sudo zypper install grub2-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-mkconfig](/man/grub-mkconfig)(8), [grub-set-default](/man/grub-set-default)(8), [efibootmgr](/man/efibootmgr)(8)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
