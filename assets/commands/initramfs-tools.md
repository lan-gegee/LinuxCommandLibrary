# TAGLINE

管理基于 Debian 的系统上的初始 RAM 文件系统

# TLDR

**更新当前内核的 initramfs**

```sudo update-initramfs -u```

**创建新的 initramfs**

```sudo update-initramfs -c -k [$(uname -r)]```

**更新所有 initramfs 镜像**

```sudo update-initramfs -u -k all```

**删除内核的 initramfs**

```sudo update-initramfs -d -k [5.10.0-1]```

**显示详细输出**

```sudo update-initramfs -u -v```

# SYNOPSIS

**update-initramfs** [_options_]

# PARAMETERS

**-c**
> 创建新的 initramfs。

**-u**
> 更新已有的 initramfs。

**-d**
> 删除 initramfs。

**-k** _version_
> 内核版本（或 "all"）。

**-v**
> 详细输出。

**-b** _directory_
> 设置 boot 目录。

# CONFIGURATION

```
/etc/initramfs-tools/initramfs.conf    Main config
/etc/initramfs-tools/modules           Modules to include
/etc/initramfs-tools/hooks/            Hook scripts
/etc/initramfs-tools/scripts/          Boot scripts
```

# DESCRIPTION

**initramfs-tools** 管理基于 Debian 的系统上的初始 RAM 文件系统（initramfs）。initramfs 包含挂载真正的根文件系统之前加载的最小文件系统。

其中包括早期启动所需的驱动、脚本和工具，如文件系统驱动、LVM、RAID 或加密设置。

# CAVEATS

仅限 Debian/Ubuntu。配置不当可能导致无法启动。务必保留一份可用的备份。自定义模块需要手动配置。

# HISTORY

initramfs-tools 在 Debian 上取代了较旧的 initrd 机制。它由 Debian 项目开发，提供了一个模块化、可脚本化的框架来构建初始文件系统。

# SEE ALSO

[mkinitramfs](/man/mkinitramfs)(8), [dracut](/man/dracut)(8)
