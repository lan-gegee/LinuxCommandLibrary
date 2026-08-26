# TAGLINE

管理初始 RAM 文件系统镜像

# TLDR

为特定内核版本**创建**新的 initramfs

```sudo update-initramfs -c -k [kernel_version]```

为所有已安装内核版本**创建** initramfs

```sudo update-initramfs -c -k all```

**更新**现有的 initramfs

```sudo update-initramfs -u```

**删除**现有的 initramfs

```sudo update-initramfs -d -k [kernel_version]```

# SYNOPSIS

**update-initramfs** [_options_]

# PARAMETERS

**-c**
> 创建新的 initramfs

**-u**
> 更新现有的 initramfs

**-d**
> 删除现有的 initramfs

**-k** _version_
> 指定内核版本（默认：最新版本）。使用 "all" 表示全部版本。

**-t**
> 使用较新的 initramfs 接管自定义的 initramfs。

**-v**
> 详细输出模式

**-b** _directory_
> 设置替代的 boot 目录

**-h, --help**
> 打印帮助信息并退出。

**--version**
> 打印底层 initrd 生成工具的版本。

# DESCRIPTION

**update-initramfs** 管理 Linux 启动过程中使用的初始 RAM 文件系统（initramfs）镜像。initramfs 包含挂载根文件系统所需的必要驱动程序和脚本。

该工具通常在安装新内核模块、修改启动配置之后，或者在 initramfs 损坏时使用。在基于 Debian 的系统上，它依托 **initramfs-tools** 工作。

# CAVEATS

需要 root 权限。将 "all" 与删除选项搭配使用时务必小心。initramfs 损坏或缺失可能导致系统无法启动。这是 Debian/Ubuntu 特有的工具；其他发行版使用 **mkinitcpio** 或 **dracut**。

# SEE ALSO

[mkinitramfs](/man/mkinitramfs)(8), [initramfs-tools](/man/initramfs-tools)(7), [dracut](/man/dracut)(8), [mkinitcpio](/man/mkinitcpio)(8)
