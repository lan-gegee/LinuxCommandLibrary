# TAGLINE

用 QEMU 模拟 64 位 RISC-V 系统

# TLDR

**在通用 virt 机器上启动 RISC-V 内核**

```qemu-system-riscv64 -machine virt -kernel [kernel] -append "root=/dev/vda"```

**使用显式的固件（OpenSBI）和内核启动**

```qemu-system-riscv64 -machine virt -bios [opensbi.bin] -kernel [kernel]```

**以 2 GB 内存、4 个 SMP 核心和 raw 磁盘镜像运行**

```qemu-system-riscv64 -machine virt -m [2G] -smp [4] -drive file=[disk.img],format=raw```

**无头模式运行，串口控制台重定向到 stdio**

```qemu-system-riscv64 -machine virt -nographic -kernel [kernel]```

**挂接用户态网络并转发 SSH 端口**

```qemu-system-riscv64 -machine virt -netdev user,id=net0,hostfwd=tcp::[2222]-:22 -device virtio-net-device,netdev=net0```

**列出支持的机器类型**

```qemu-system-riscv64 -machine help```

# SYNOPSIS

**qemu-system-riscv64** [_options_] [_disk_image_]

# PARAMETERS

**-machine** _type_
> 要模拟的机器类型（如 **virt**、**sifive_u**、**sifive_e**、**spike**）。

**-cpu** _model_
> CPU 型号（如 **rv64**、**sifive-u54**）。默认为 **rv64**。

**-smp** _n_
> 虚拟 CPU 数量。

**-m** _size_
> 内存大小（如 **512M**、**2G**）。

**-kernel** _file_
> 可启动的内核镜像（ELF、uImage 或 raw）。

**-bios** _file_
> 在内核之前加载的固件镜像（默认：OpenSBI）。

**-initrd** _file_
> 初始内存盘镜像。

**-append** _args_
> 内核命令行参数。

**-drive** _options_
> 定义块设备（如 **file=disk.img,format=raw,if=virtio**）。

**-netdev** _options_
> 定义网络后端（如 user、tap）。

**-device** _options_
> 添加设备（如 **virtio-net-device**、**virtio-blk-device**）。

**-nographic**
> 禁用图形输出；将串口/控制台重定向到 stdio。

**-serial** _dev_
> 重定向串口（如 **stdio**、**mon:stdio**、**file:log**）。

**-display** _type_
> 显示后端（**none**、**gtk**、**sdl**、**vnc**）。

**-S**
> 启动时冻结 CPU（配合 **-s** 用于 gdb）。

**-s**
> **-gdb tcp::1234** 的简写。

# DESCRIPTION

**qemu-system-riscv64** 是面向 64 位 RISC-V 客户机的 QEMU 系统模拟器。它可以在多种模拟的开发板上运行裸机代码、引导加载程序或完整的 Linux 发行版。默认的 **virt** 机器是一块为虚拟化设计的半虚拟化开发板，配备 VirtIO 设备、CLINT/PLIC 中断控制器以及可选的 OpenSBI 固件。

其他开发板则模拟真实硬件，例如 **sifive_u**（SiFive HiFive Unleashed）、**sifive_e** 和 **spike** 模拟器。该模拟器支持标准 RV64GC ISA 以及大量可选扩展（H、V、Zicbom、Zba、Zbb 等），可通过 **-cpu** 选项启用。

# CAVEATS

RISC-V 上的 KVM 加速需要具备 H 扩展的主机 CPU；否则只能使用 TCG 软件模拟，速度明显慢于原生执行。某些客户机操作系统要求特定的 **-bios** 固件；OpenSBI 与 Linux 版本混搭可能导致启动失败。使用 **-nographic** 时，按 **Ctrl-A X** 可退出模拟器。

# INSTALL

```apt: sudo apt install qemu-system-riscv```

```dnf: sudo dnf install qemu-system-riscv```

```pacman: sudo pacman -S qemu-system-riscv```

```apk: sudo apk add qemu-system-riscv64```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qemu-system-x86_64](/man/qemu-system-x86_64)(1), [qemu-img](/man/qemu-img)(1)
