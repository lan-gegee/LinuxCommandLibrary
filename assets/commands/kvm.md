# TAGLINE

Linux 内核虚拟化模块

# TLDR

**检查 KVM 支持**

```lscpu | grep Virtualization```

**加载 KVM 模块**

```sudo modprobe kvm-intel```  # 或 kvm-amd

**使用 QEMU/KVM 运行虚拟机**

```qemu-system-x86_64 -enable-kvm -m [2048] -hda [disk.qcow2]```

**检查 KVM 是否已启用**

```ls /dev/kvm```

**列出运行中的虚拟机（libvirt）**

```virsh list --all```

# DESCRIPTION

**KVM**（基于内核的虚拟机）是 Linux 内核的一个虚拟化模块。它让 Linux 变成虚拟机监控器（hypervisor），从而能够以接近原生的性能运行多个虚拟机。

KVM 需要硬件虚拟化支持（Intel VT-x 或 AMD-V）。它通常搭配 QEMU 做设备模拟，也可以选择搭配 libvirt 进行管理。

# ARCHITECTURE

```
Applications → Guest OS → KVM → Host Kernel → Hardware

Components:
- kvm.ko: Core virtualization
- kvm-intel.ko or kvm-amd.ko: CPU-specific
- QEMU: Device emulation
- libvirt: Management API
```

# VERIFY SUPPORT

```bash
# Check CPU support
grep -E 'vmx|svm' /proc/cpuinfo

# Check KVM module
lsmod | grep kvm

# Check device
ls -la /dev/kvm
```

# CAVEATS

需要在 BIOS 中启用 VT-x/AMD-V。嵌套虚拟化需要额外配置。性能随工作负载而异。

# HISTORY

KVM 由 **Qumranet** 创建，于 **2007 年**合入 Linux 内核 **2.6.20**。Red Hat 在 2008 年收购了 Qumranet。此后 KVM 成为标准的 Linux 虚拟机监控器，在许多部署场景中取代了 Xen。

# INSTALL

```apt: sudo apt install qemu-system-x86```

```dnf: sudo dnf install qemu-system-x86```

```pacman: sudo pacman -S qemu-system-x86```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu](/man/qemu)(1), [virsh](/man/virsh)(1), [virt-manager](/man/virt-manager)(1)
