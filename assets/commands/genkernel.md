# TAGLINE

Gentoo 的自动化内核编译与安装工具

# TLDR

自动**编译并安装**通用内核

```sudo genkernel all```

仅构建并安装 **bzImage**、**initramfs**、**kernel** 或 **ramdisk**

```sudo genkernel [bzImage|initramfs|kernel|ramdisk]```

编译前对内核**配置**进行修改

```sudo genkernel --menuconfig all```

生成具有**自定义名称**的内核

```sudo genkernel --kernname=[custom_name] all```

使用默认目录**之外**的内核源码

```sudo genkernel --kerneldir=[path/to/directory] all```

# SYNOPSIS

**genkernel** [_options_] _action_

# PARAMETERS

**all**
> 构建内核、模块和 initramfs。

**bzImage**
> 仅构建压缩内核镜像。

**initramfs**
> 仅构建初始 ramdisk。

**kernel**
> 仅构建内核和模块。

**ramdisk**
> 仅构建 ramdisk。

**--menuconfig**
> 编译前运行 menuconfig。

**--nconfig**
> 编译前运行 nconfig（基于 ncurses）。

**--kernname** _NAME_
> 用 _NAME_ 标记内核和 initramfs。

**--kerneldir** _DIR_
> 使用 _DIR_ 中的内核源码而非 /usr/src/linux。

**--makeopts** _OPTS_
> 向 make 传递选项（例如 -j4）。

**--no-clean**
> 跳过编译前的 `make clean`。

**--no-mrproper**
> 跳过编译前的 `make mrproper`，保留现有内核配置。

**--lvm**
> 为 initramfs 添加 LVM 支持。

**--luks**
> 为 initramfs 添加 LUKS 加密支持。

# CONFIGURATION

**/etc/genkernel.conf**
> 主配置文件，控制默认构建选项、路径和特性。

# DESCRIPTION

**genkernel** 是一个 Gentoo Linux 工具，用于自动化内核的编译与安装过程。它构建具有广泛硬件支持的通用内核，类似于二进制发行版中的内核。

该工具负责配置、编译和安装内核，并生成启动所需的 initramfs（初始 ramdisk）。它可以自动检测硬件并启用相应的内核模块。

genkernel 从 **/etc/genkernel.conf** 读取配置，并通过命令行选项支持各种文件系统、加密和引导特性。

# CAVEATS

通用内核比自定义配置的内核更大，启动可能更慢。编译需要大量时间和磁盘空间。/usr/src/linux 符号链接必须指向正确的内核源码。

# HISTORY

genkernel 为 Gentoo Linux 开发，提供手动内核配置之外的替代方案。虽然 Gentoo 传统上强调定制编译，但 genkernel 让用户无需深入的内核配置知识也能快速生成可用的内核。

# SEE ALSO

[make](/man/make)(1), [emerge](/man/emerge)(1), [eselect](/man/eselect)(1), [dracut](/man/dracut)(8), [mkinitcpio](/man/mkinitcpio)(8)
