# TAGLINE

为 Linux 创建初始内存盘镜像

# TLDR

**为当前内核生成 initramfs**

```sudo mkinitramfs -o [/boot/initrd.img]```

**为特定内核版本生成 initramfs**

```sudo mkinitramfs -o [/boot/initrd.img-5.10.0] [5.10.0-generic]```

**生成时输出详细信息**

```sudo mkinitramfs -v -o [/boot/initrd.img]```

**保留临时工作目录以便检查**

```sudo mkinitramfs -k -o [/boot/initrd.img]```

**使用指定的配置目录**

```sudo mkinitramfs -d [/etc/initramfs-tools] -o [/boot/initrd.img]```

# SYNOPSIS

**mkinitramfs** [_options_] **-o** _outfile_ [_version_]

# PARAMETERS

**-o** _FILE_
> 输出文件（必需）。即生成的 initramfs 镜像路径。

**-d** _CONFDIR_
> 使用备用的配置目录（默认：/etc/initramfs-tools）。

**-k**
> 保留生成过程中使用的临时目录以便调试。

**-v**
> 详细输出，显示正在添加的文件。

**-c** _COMPRESS_
> 覆盖压缩方法（gzip、lz4、lzma、lzop、xz、zstd）。

_VERSION_
> 要为其生成 initramfs 的内核版本。默认为当前正在运行的内核。

# DESCRIPTION

**mkinitramfs** 为 Linux 创建初始内存盘镜像（initramfs）。initramfs 包含启动期间挂载根文件系统所需的关键驱动和脚本，包括存储驱动、文件系统模块和早期用户空间工具。

此工具为 Debian/Ubuntu 专用，通常通过 **update-initramfs** 间接调用。其他发行版使用不同的工具（Arch 用 mkinitcpio，Fedora/RHEL 用 dracut）。

# CONFIGURATION

```
/etc/initramfs-tools/
├── initramfs.conf    # Main configuration (MODULES, COMPRESS, etc.)
├── modules           # Additional kernel modules to include
├── hooks/            # Scripts to customize initramfs contents
└── scripts/          # Boot scripts for the initramfs environment
```

# CAVEATS

Debian/Ubuntu 专用（Arch 用 mkinitcpio，Fedora/RHEL 用 dracut）。内核版本必须与 /lib/modules/ 中已安装的内核模块匹配。需要 root 权限。建议用 **update-initramfs** 而不是直接调用 mkinitramfs，因为它会处理备份和引导加载程序集成。

# HISTORY

mkinitramfs 属于为 Debian 系系统开发的 **initramfs-tools**，用更灵活的基于 cpio 的 initramfs 方案取代了较旧的 initrd 系统。

# SEE ALSO

[update-initramfs](/man/update-initramfs)(8), [mkinitcpio](/man/mkinitcpio)(8), [dracut](/man/dracut)(8)
