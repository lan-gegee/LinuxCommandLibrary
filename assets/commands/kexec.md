# TAGLINE

允许系统跳过 BIOS 直接引导进入新内核

# TLDR

**加载**新内核

```kexec -l [path/to/kernel] --initrd=[path/to/initrd] --command-line=[arguments]```

使用**当前启动参数**加载内核

```kexec -l [path/to/kernel] --initrd=[path/to/initrd] --reuse-cmdline```

**执行**已加载的内核

```kexec -e```

**卸载**当前 kexec 目标内核

```kexec -u```

# SYNOPSIS

**kexec** [_options_]

# PARAMETERS

**-l**, **--load** _KERNEL_
> 将新内核加载进内存

**-e**, **--exec**
> 执行当前已加载的内核

**-u**, **--unload**
> 卸载已加载的内核

**--initrd** _FILE_
> 指定 initramfs/initrd 镜像

**--command-line** _ARGS_
> 内核命令行参数

**--reuse-cmdline**
> 使用当前内核的命令行

**-p**, **--load-panic**
> 加载用于崩溃转储（kdump）的内核

# DESCRIPTION

**kexec** 允许系统不经过 BIOS/UEFI 和引导加载程序而直接引导进入新内核。这可以实现更快的重启，并且对于 kdump（内核崩溃转储）至关重要。

其流程是先用 -l 将内核加载进内存，再用 -e 执行它。这绕过了硬件初始化过程，从而显著缩短重启时间。

# CAVEATS

需要内核启用 CONFIG_KEXEC。由于缺少初始化，某些硬件在 kexec 之后可能无法正常工作。并非所有驱动都能正确处理 kexec 切换。

# HISTORY

kexec 的开发目的是实现快速重启和内核崩溃转储。它在 Linux 内核 **2.6.13** 版本（**2005 年**）中被合并，如今已成为 kdump 功能的重要组成部分。

# INSTALL

```apt: sudo apt install kexec-tools```

```dnf: sudo dnf install kexec-tools```

```pacman: sudo pacman -S kexec-tools```

```apk: sudo apk add kexec-tools```

```zypper: sudo zypper install kexec-tools```

```nix: nix profile install nixpkgs#kexec-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [reboot](/man/reboot)(8)
