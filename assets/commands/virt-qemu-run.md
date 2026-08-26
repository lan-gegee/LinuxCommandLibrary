# TAGLINE

无需 libvirtd 运行 QEMU 虚拟机

# TLDR

**运行**QEMU 虚拟机

```virt-qemu-run [path/to/guest.xml]```

使用**状态**目录运行

```virt-qemu-run -r [path/to/directory] [path/to/guest.xml]```

以**详细**输出运行

```virt-qemu-run -v [path/to/guest.xml]```

显示**帮助**

```virt-qemu-run -h```

# SYNOPSIS

**virt-qemu-run** [_OPTIONS_] _GUEST.XML_

# PARAMETERS

**-r** _DIR_, **--root** _DIR_
> 将虚拟机状态文件存储在指定目录中。关机后必须手动移除。若省略，则会创建一个临时目录并在虚拟机退出时自动清理。

**-s** _SECRET-XML-FILE_,_SECRET-VALUE-FILE_, **--secret** _SECRET-XML-FILE_,_SECRET-VALUE-FILE_
> 向 secret 驱动加载一个密钥。XML 文件定义该密钥（UUID 必须与域 XML 中引用的一致）；值文件包含密钥数据。可重复指定。

**-v**, **--verbose**
> 显示详细的启动信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**virt-qemu-run** 是一个实验性工具，用于独立于 **libvirtd** 守护进程运行 QEMU 虚拟机。它提供了一种使用 libvirt 域 XML 定义运行虚拟机的方式，而无需完整的 libvirt 基础设施。客户机在前台运行，客户机关闭时命令退出。

这适用于测试、嵌入式场景，或在没有守护进程开销的情况下运行隔离的虚拟机。成功关闭时退出状态为 0，失败时为非零。

# CAVEATS

实验性工具；行为可能随版本变化。客户机 XML 必须是有效的 libvirt 格式。某些依赖 libvirtd 的功能（如完整的设备管理 API）可能无法工作。不建议用于生产环境。

# INSTALL

```apt: sudo apt install libvirt-daemon-driver-qemu```

```dnf: sudo dnf install libvirt-daemon-driver-qemu```

```apk: sudo apk add libvirt-client```

```zypper: sudo zypper install libvirt-daemon-driver-qemu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-manager](/man/virt-manager)(1), [virsh](/man/virsh)(1), [qemu](/man/qemu)(1)
