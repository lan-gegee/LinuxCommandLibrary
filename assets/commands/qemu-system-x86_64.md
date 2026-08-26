# TAGLINE

用 QEMU 模拟 x86_64 系统

# TLDR

**从 ISO 镜像启动**

```qemu-system-x86_64 -cdrom [image.iso] -boot d```

**从磁盘镜像启动**

```qemu-system-x86_64 -hda [disk.qcow2]```

**指定内存和 CPU 启动**

```qemu-system-x86_64 -m [2G] -smp [2] -hda [disk.qcow2]```

**启用 KVM 加速启动**

```qemu-system-x86_64 -enable-kvm -m [4G] -hda [disk.qcow2]```

**带网络启动**

```qemu-system-x86_64 -hda [disk.qcow2] -nic user,hostfwd=tcp::2222-:22```

# SYNOPSIS

**qemu-system-x86_64** [_options_] [_disk_image_]

# PARAMETERS

**-m** _size_
> 内存大小（如 2G、4096M）。

**-smp** _cpus_
> CPU 数量。

**-hda** _file_
> 主硬盘镜像。

**-cdrom** _file_
> CD-ROM 镜像。

**-boot** _order_
> 启动顺序（c=硬盘，d=光驱）。

**-enable-kvm**
> 启用 KVM 加速。

**-nic** _options_
> 网络配置。

**-nographic**
> 禁用图形输出。

**-vnc** _display_
> 启用 VNC 服务器。

**-cpu** _model_
> 要模拟的 CPU 型号。

**-drive** _options_
> 定义驱动器（file、format、if、media）。

**-serial** _device_
> 重定向串口。

# DESCRIPTION

**qemu-system-x86_64** 是 x86_64 架构的全系统模拟器。它可以运行包括 Linux、Windows 和 BSD 在内的完整操作系统。在 Linux 上配合 **KVM** 硬件加速，可以达到接近原生的性能。

QEMU 模拟 CPU、内存、存储、网络和显示设备。它支持多种磁盘镜像格式（qcow2、raw、vmdk）、各种网络配置，以及图形和串口控制台输出。它是 libvirt、virt-manager 和 Proxmox 等更高层虚拟化工具的后端。

# CAVEATS

KVM 需要硬件虚拟化支持（Intel VT-x/AMD-V）以及 kvm 内核模块。没有 KVM 时，模拟速度会明显变慢。分配过多的内存和 CPU 可能影响宿主系统。

# HISTORY

**QEMU** 由 **Fabrice Bellard** 创建，于 **2003 年**首次发布。KVM 硬件加速于 **2007 年**合并进 Linux 内核，使 QEMU 成为 Linux 虚拟化的标准用户空间组件。

# INSTALL

```apt: sudo apt install qemu-system-x86```

```dnf: sudo dnf install qemu-system-x86```

```pacman: sudo pacman -S qemu-system-x86```

```apk: sudo apk add qemu-system-x86_64```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu-img](/man/qemu-img)(1), [qemu-system-i386](/man/qemu-system-i386)(1)
