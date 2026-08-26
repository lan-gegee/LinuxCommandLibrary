# TAGLINE

Linux 系统的 GRand Unified Bootloader（GRUB）

# TLDR

**将 GRUB 安装到磁盘**

```sudo grub-install /dev/sda```

**更新 GRUB 配置**（Debian/Ubuntu）

```sudo update-grub```

**直接生成配置文件**

```sudo grub-mkconfig -o /boot/grub/grub.cfg```

**设置默认启动条目**

```sudo grub-set-default 0```

**检查 GRUB 版本**

```grub-install --version```

# SYNOPSIS

**grub-install** [_options_] _device_

**grub-mkconfig** [**-o** _file_]

# PARAMETERS

**--root-directory** _DIR_
> 安装到备用根目录。

**--boot-directory** _DIR_
> 启动目录位置。

**--target** _TARGET_
> 目标平台。

**--recheck**
> 重新探测设备。

**--removable**
> 为可移动介质安装。

**--help**
> 显示帮助信息。

# DESCRIPTION

**GRUB**（GRand Unified Bootloader）是 Linux 系统的标准引导加载程序。它负责加载内核和 initrd，并显示启动菜单供选择系统。

GRUB 2 支持多种文件系统、LVM、RAID 和加密分区。它提供用于系统恢复的救援模式，以及面向高级配置的脚本功能。

与 GRUB Legacy 不同，GRUB 2 没有单一的统一 **grub** 命令；其功能分散在 **grub-install**、**grub-mkconfig**、**grub-set-default**、**grub-editenv** 等独立工具中。交互式 GRUB 命令行可在启动菜单本身中进入（按 **c**），而不是在运行中的 Linux Shell 里。

# CONFIGURATION

**/etc/default/grub**
> 主 GRUB 配置文件，控制默认启动条目、超时时间、内核参数和显示设置。

**/etc/grub.d/**
> 存放生成 grub.cfg 文件所需脚本的目录。可以在此添加自定义条目。

**/boot/grub/grub.cfg**
> 生成的配置文件。不要直接编辑；应使用 grub-mkconfig 重新生成。

# CAVEATS

配置错误可能导致无法启动。请保留可用的救援介质。GRUB 2 与旧版 GRUB 有所不同。

# HISTORY

GRUB 作为 **GNU 工程**的一部分创建。GRUB 2 于 **2002 年**发布，是一次功能增强的完全重写。

# INSTALL

```pacman: sudo pacman -S grub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grub-mkconfig](/man/grub-mkconfig)(8), [update-grub](/man/update-grub)(8), [grub-install](/man/grub-install)(8)

# RESOURCES

```[Homepage](https://www.gnu.org/software/grub/)```

```[Source code](https://git.savannah.gnu.org/cgit/grub.git)```

```[Documentation](https://www.gnu.org/software/grub/manual/grub/grub.html)```

<!-- verified: 2026-07-17 -->
