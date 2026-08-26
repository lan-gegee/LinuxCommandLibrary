# TAGLINE

管理 GRUB 环境块变量

# TLDR

设置**默认启动项**

```grub-editenv /boot/grub/grubenv set default=Ubuntu```

显示所有 GRUB **环境变量**

```grub-editenv /boot/grub/grubenv list```

将 saved_entry 变量**重置**为默认值

```grub-editenv /boot/grub/grubenv unset saved_entry```

# SYNOPSIS

**grub-editenv** _file_ _command_

# PARAMETERS

**list**
> 列出环境文件中的所有变量

**set** _NAME=VALUE_
> 将变量设置为某个值

**unset** _NAME_
> 移除变量

**create**
> 创建一个新的空环境文件

**-v**, **--verbose**
> 打印详细消息

# DESCRIPTION

**grub-editenv** 管理 GRUB 的环境块（grubenv），其中保存着跨启动持久化的变量。环境文件通常位于 /boot/grub/grubenv 或 /boot/grub2/grubenv。

常见变量包括 **saved_entry**（当 GRUB_DEFAULT=saved 时使用的启动项）、**next_entry**（仅下一次启动生效的条目，由 grub-reboot 使用）以及 **recordfail**（启动失败时设置）。

该工具支持以脚本方式管理启动配置，而无需重新生成 grub.cfg。

# CONFIGURATION

**/boot/grub/grubenv**
> 存储持久化启动变量的 GRUB 环境块文件。

**/etc/default/grub**
> 必须包含 GRUB_DEFAULT=saved，grub-editenv 的设置才能生效。

# CAVEATS

grubenv 文件大小固定（1024 字节）。变量和值必须能放进这个空间。某些引导加载程序配置可能不使用 grubenv。更改要求 /etc/default/grub 中设置了 GRUB_DEFAULT=saved。

# HISTORY

grub-editenv 是 GRUB 2 已保存默认项机制的一部分，允许启动偏好在无需修改主配置文件的情况下持久保存。这使得"仅启动一次"以及记住上次成功启动等特性成为可能。

# INSTALL

```apt: sudo apt install grub-common```

```pacman: sudo pacman -S grub```

```apk: sudo apk add grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-set-default](/man/grub-set-default)(8), [grub-reboot](/man/grub-reboot)(8), [grub-mkconfig](/man/grub-mkconfig)(8)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
