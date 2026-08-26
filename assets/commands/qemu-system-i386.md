# TAGLINE

用 QEMU 模拟 32 位 x86 系统

# TLDR

**从 ISO 镜像启动**

```qemu-system-i386 -cdrom [image.iso] -boot d```

**以指定内存从磁盘启动**

```qemu-system-i386 -m [512M] -hda [disk.img]```

**启用 KVM 启动**

```qemu-system-i386 -enable-kvm -hda [disk.img]```

# SYNOPSIS

**qemu-system-i386** [_options_] [_disk_image_]

# PARAMETERS

**-m** _size_
> 内存大小。

**-hda** _file_
> 硬盘镜像。

**-cdrom** _file_
> CD-ROM 镜像。

**-enable-kvm**
> 启用 KVM 加速。

**-boot** _order_
> 启动顺序。

# DESCRIPTION

**qemu-system-i386** 用于模拟 32 位 x86 系统。适合运行旧式 32 位操作系统。选项与 qemu-system-x86_64 相同，但针对 i386 架构。

# INSTALL

```apt: sudo apt install qemu-system-x86```

```dnf: sudo dnf install qemu-system-x86```

```pacman: sudo pacman -S qemu-system-x86```

```apk: sudo apk add qemu-system-i386```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu-system-x86_64](/man/qemu-system-x86_64)(1), [qemu-img](/man/qemu-img)(1)
