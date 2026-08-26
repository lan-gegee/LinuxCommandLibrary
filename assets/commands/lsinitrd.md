# TAGLINE

显示 initramfs 镜像的内容

# TLDR

显示**当前内核** initramfs 的内容

```lsinitrd```

显示**指定内核**的内容

```lsinitrd --kver [kernel_version]```

显示**指定镜像**的内容

```lsinitrd [path/to/initramfs.img]```

列出**包含的模块**

```lsinitrd --mod```

将 initramfs **解包**到当前目录

```lsinitrd --unpack```

# SYNOPSIS

**lsinitrd** [_options_] [_image_]

# DESCRIPTION

**lsinitrd** 显示 initramfs（初始 RAM 文件系统）镜像的内容。它列出镜像中包含的文件、模块和驱动程序，这对排查启动问题至关重要。

# PARAMETERS

**-k, --kver VERSION**
> 显示指定内核版本的 initramfs

**-m, --mod**
> 列出包含的内核模块

**--unpack**
> 将 initramfs 内容解压到当前目录

**-f, --file FILE**
> 显示镜像中特定文件的内容

**-l, --list**
> 列出 initramfs 中的文件

# CAVEATS

属于 dracut 工具集。initramfs 的位置因发行版而异（/boot 或 /boot/efi）。部分操作可能需要 root 权限。

# INSTALL

```apt: sudo apt install dracut-core```

```apk: sudo apk add dracut-core```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dracut](/man/dracut)(8), [mkinitcpio](/man/mkinitcpio)(8), [update-initramfs](/man/update-initramfs)(8)
