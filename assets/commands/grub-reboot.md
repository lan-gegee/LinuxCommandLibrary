# TAGLINE

仅为下一次重启设置默认启动条目

# TLDR

仅为下一次启动设置**默认启动条目**

```sudo grub-reboot [entry_number]```

为下次启动设置**替代启动目录**的默认条目

```sudo grub-reboot --boot-directory=/[path/to/boot_directory] [entry_number]```

为**子菜单条目**设置默认项（用 > 分隔子菜单和条目标题）

```sudo grub-reboot "[submenu_title]>[entry_title]"```

# SYNOPSIS

**grub-reboot** [_options_] _entry_

# PARAMETERS

_entry_
> 菜单条目编号（从 0 开始）、完整条目名称或标识符。

**--boot-directory**=_DIR_
> 在 DIR/grub 下查找 GRUB 镜像，而不是默认的 /boot/grub。

**-h**, **--help**
> 打印帮助信息并退出。

**-V**, **--version**
> 打印版本信息并退出。

**-v**, **--verbose**
> 打印详细消息。

# DESCRIPTION

**grub-reboot** 仅为下一次启动设置默认启动条目。启动一次之后，GRUB 会恢复为 **grub-set-default** 或配置文件中设定的永久默认条目。

条目可以指定为编号（第一个条目为 0）、grub.cfg 中的完整条目名称或菜单条目标识符。对于子菜单内的条目，使用大于号（>）分隔子菜单标题和条目标题，中间不能有空格（例如 "Advanced options>Ubuntu, with Linux 5.15"）。可用 **grep menuentry /boot/grub/grub.cfg** 查看可用条目。

这对于一次性启动到恢复模式、备用内核或其他操作系统非常有用，且不会永久更改启动顺序。

# CONFIGURATION

**/etc/default/grub**
> 必须包含 GRUB_DEFAULT=saved，grub-reboot 才能生效。

# CAVEATS

需要在 /etc/default/grub 中设置 **GRUB_DEFAULT=saved** 并随后运行一次 **grub-mkconfig** 才能生效。该设置存储在 grubenv 中，此文件必须可写。只影响紧接着的下一次启动。当 GRUB 无法写入环境块时（例如在 MDRAID 或 LVM 上），所选条目可能在重启后仍保持为默认项。

# HISTORY

grub-reboot 是 GRUB 2 的一部分，提供了 GRUB Legacy 中就存在的"仅启动一次"功能。它支持安全地测试替代启动配置并自动回退。

# INSTALL

```apt: sudo apt install grub2-common```

```dnf: sudo dnf install grub2-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

```zypper: sudo zypper install grub2-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-set-default](/man/grub-set-default)(8), [grub-mkconfig](/man/grub-mkconfig)(8), [grub-editenv](/man/grub-editenv)(1)
