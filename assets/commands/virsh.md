# TAGLINE

Libvirt 虚拟化管理 CLI

# TLDR

**列出运行中的虚拟机**

```virsh list```

**列出所有虚拟机**

```virsh list --all```

**启动虚拟机**

```virsh start [vm-name]```

**关闭虚拟机**

```virsh shutdown [vm-name]```

**强制停止虚拟机**

```virsh destroy [vm-name]```

**连接到控制台**

```virsh console [vm-name]```

**显示虚拟机信息**

```virsh dominfo [vm-name]```

**从 XML 定义虚拟机**

```virsh define [vm.xml]```

# SYNOPSIS

**virsh** [_-c uri_] _command_ [_args_]

# PARAMETERS

**list**
> 列出域。

**start** _NAME_
> 启动域。

**shutdown** _NAME_
> 优雅关机。

**destroy** _NAME_
> 强制停止。

**console** _NAME_
> 串行控制台。

**dominfo** _NAME_
> 域信息。

**define** _XML_
> 定义域。

**undefine** _NAME_
> 移除域。

**-c** _URI_
> 连接 URI。

# DESCRIPTION

**virsh** 是通过 libvirt 虚拟化 API 管理虚拟机的命令行界面。它提供对 KVM、QEMU、Xen 及其他 hypervisor 的统一控制，处理域生命周期操作、存储池、虚拟网络和快照。

域（虚拟机）可以启动、停止、暂停和迁移。**console** 命令提供到运行中虚拟机的串行访问（使用 Ctrl+] 退出）。域配置以 XML 定义，可以创建、修改和导出。该工具还管理存储池、卷和虚拟网络，实现对整个虚拟化基础设施的控制。

# CAVEATS

需要 libvirt 守护进程。管理系统级虚拟机需要 root。XML 语法较复杂。

# HISTORY

**virsh** 是 **libvirt**（虚拟化 API）的命令行界面，为多种 hypervisor 提供统一管理。

# INSTALL

```apt: sudo apt install libvirt-clients```

```dnf: sudo dnf install libvirt-client```

```apk: sudo apk add libvirt-client```

```zypper: sudo zypper install libvirt-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-manager](/man/virt-manager)(1), [qemu](/man/qemu)(1), [kvm](/man/kvm)(1)
