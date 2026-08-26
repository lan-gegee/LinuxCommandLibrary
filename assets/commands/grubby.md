# TAGLINE

Red Hat 系统的命令行引导加载程序配置工具

# TLDR

向所有内核菜单条目添加内核启动**参数**

```sudo grubby --update-kernel=ALL --args 'quiet console=ttyS0'```

从默认内核条目中**移除**现有参数

```sudo grubby --update-kernel=DEFAULT --remove-args quiet```

**列出**所有内核菜单条目

```sudo grubby --info=ALL```

# SYNOPSIS

**grubby** [_options_]

# PARAMETERS

**--info=**_KERNEL_
> 显示指定内核（或 ALL）的启动信息

**--update-kernel=**_KERNEL_
> 更新指定的内核（ALL、DEFAULT 或路径）

**--args=**_ARGS_
> 添加内核参数

**--remove-args=**_ARGS_
> 移除内核参数

**--set-default=**_KERNEL_
> 设置默认启动内核

**--default-kernel**
> 显示默认内核的路径

**--default-index**
> 显示默认内核的索引

**--add-kernel=**_PATH_
> 添加新的内核条目（需要 **--title**）

**--remove-kernel=**_PATH_
> 移除一个内核条目

**--title=**_TITLE_
> 为新内核条目设置标题

**--initrd=**_PATH_
> 为新内核条目设置 initrd

**--copy-default**
> 从当前默认条目复制参数和根设备

**--make-default**
> 将新添加的条目设为默认项

**--grub2**
> 使用 grub2 风格的配置（x86_64/BLS 系统上的默认值）

# DESCRIPTION

**grubby** 是一款命令行工具，用于更新和修改基于 Red Hat 的系统上的引导加载程序配置。它支持 GRUB、GRUB2 和 zipl（用于 s390 系统），为启动配置修改提供统一接口。

该工具可以修改内核命令行参数、管理启动条目并设置默认内核，而无需直接编辑配置文件。在使用带 BLS（Boot Loader Specification）的 GRUB2 的现代 Fedora/RHEL 系统上，grubby 会修改 /boot/loader/entries/ 中各个内核条目文件。

# CAVEATS

在 GRUB Legacy、GRUB2 和 BLS 配置之间行为有所差异。某些选项可能不适用于所有引导加载程序配置。更改在下次启动时生效。更改后务必验证配置。

# HISTORY

grubby 由 Red Hat 开发，用于简化跨不同配置的引导加载程序管理。它成为基于 Red Hat 的发行版上自动化系统管理和内核更新的重要工具。最初的 **rhboot/grubby** 项目于 2022 年退役；随着 BLS 的采用，其功能如今作为兼容的 shell 脚本延续，由 Fedora 的 dist-git 维护。

# INSTALL

```dnf: sudo dnf install grubby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-mkconfig](/man/grub-mkconfig)(8), [grub-set-default](/man/grub-set-default)(8), [kernel-install](/man/kernel-install)(8)

# RESOURCES

```[Source code](https://github.com/rhboot/grubby)```

<!-- verified: 2026-07-17 -->
