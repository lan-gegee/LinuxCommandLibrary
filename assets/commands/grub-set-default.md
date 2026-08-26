# TAGLINE

设置永久的 GRUB 默认启动条目

# TLDR

永久设置**默认启动条目**

```sudo grub-set-default [entry_number]```

为**替代启动目录**设置默认条目

```sudo grub-set-default --boot-directory /[path/to/boot_directory] [entry_number]```

# SYNOPSIS

**grub-set-default** [_options_] _entry_

# PARAMETERS

_entry_
> 菜单条目编号（从 0 开始）、名称或标识符

**--boot-directory** _DIR_
> 使用替代启动目录而不是 /boot

# DESCRIPTION

**grub-set-default** 为 GRUB 设置永久的默认启动条目。与 **grub-reboot** 不同，该设置会在之后所有启动中持续生效，直到被更改。

条目可以指定为编号（第一个条目为 0）、grub.cfg 中的完整条目名称或菜单条目标识符。子菜单条目使用类似 "1>2" 的记法，表示第二个子菜单中的第三项。

# CONFIGURATION

**/etc/default/grub**
> 必须包含 GRUB_DEFAULT=saved，grub-set-default 才能生效。

# CAVEATS

需要在 /etc/default/grub 中设置 GRUB_DEFAULT=saved，并使用 grub-mkconfig 重新生成配置。否则 grubenv 中的设置将被忽略。添加或移除内核时，条目编号可能发生变化。

# HISTORY

grub-set-default 是 GRUB 2 保存默认条目功能的一部分。它提供了一种无需编辑配置文件即可更改默认启动项的方式，将选择存储在 grubenv 文件中。

# INSTALL

```apt: sudo apt install grub2-common```

```dnf: sudo dnf install grub2-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

```zypper: sudo zypper install grub2-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-reboot](/man/grub-reboot)(8), [grub-mkconfig](/man/grub-mkconfig)(8), [grub-editenv](/man/grub-editenv)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
