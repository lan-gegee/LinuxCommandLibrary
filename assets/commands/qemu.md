# TAGLINE

开源的机器模拟器和虚拟化器

# TLDR

**运行虚拟机**

```qemu-system-x86_64 -hda [disk.img]```

**指定内存运行**

```qemu-system-x86_64 -m [2048] -hda [disk.img]```

**从 ISO 启动**

```qemu-system-x86_64 -cdrom [installer.iso] -boot d```

**启用 KVM 加速**

```qemu-system-x86_64 -enable-kvm -hda [disk.img]```

**配置端口转发的网络**

```qemu-system-x86_64 -hda [disk.img] -netdev user,id=net0,hostfwd=tcp::2222-:22 -device e1000,netdev=net0```

# SYNOPSIS

**qemu-system-***_arch_ [_options_]

# PARAMETERS

**-hda** _FILE_
> 主硬盘。

**-m** _SIZE_
> 以 MB 计的内存大小。

**-cdrom** _FILE_
> CD-ROM 镜像。

**-enable-kvm**
> KVM 加速。

**-boot** _ORDER_
> 启动顺序。

**-smp** _CPUS_
> CPU 数量。

# DESCRIPTION

**QEMU**（Quick EMUlator）是一个开源的机器模拟器和虚拟化器，可以在任意宿主机上运行任意受支持架构的操作系统。它提供完整的系统模拟，涵盖 CPU、内存、存储和外设设备，支持 x86、ARM、RISC-V、MIPS、PowerPC 等架构。

在 Linux 上与 KVM（Kernel-based Virtual Machine）结合时，QEMU 借助硬件虚拟化扩展达到接近原生的性能。没有 KVM 时，它使用动态二进制翻译进行纯软件模拟，速度较慢但可跨平台工作。QEMU 磁盘镜像支持多种格式（qcow2、raw、vmdk），并提供快照、精简配置和后备文件等特性。

# CAVEATS

性能因模式而异。追求最佳性能请使用 KVM。

# HISTORY

QEMU 由 **Fabrice Bellard** 为处理器模拟而创建。

# INSTALL

```dnf: sudo dnf install qemu```

```zypper: sudo zypper install qemu```

```brew: brew install qemu```

```nix: nix profile install nixpkgs#qemu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu-img](/man/qemu-img)(1), [kvm](/man/kvm)(1), [virsh](/man/virsh)(1)
