# TAGLINE

图形化虚拟机管理器

# TLDR

启动 **GUI**

```virt-manager```

**连接**到 hypervisor

```virt-manager --connect [hypervisor_uri]```

在**前台**运行

```virt-manager --no-fork```

**调试**模式

```virt-manager --debug```

打开**新建虚拟机**向导

```virt-manager --show-domain-creator```

显示虚拟机**详情**

```virt-manager --show-domain-editor [name|id|uuid]```

显示虚拟机**性能**

```virt-manager --show-domain-performance [name|id|uuid]```

显示**连接**详情

```virt-manager --show-host-summary```

# SYNOPSIS

**virt-manager** [_OPTIONS_]

# PARAMETERS

**--connect** _URI_
> 连接到指定的 hypervisor

**--no-fork**
> 不转入后台运行

**--debug**
> 打印调试输出

**--show-domain-creator**
> 打开新建虚拟机向导

**--show-domain-editor** _VM_
> 显示虚拟机详情窗口

**--show-domain-performance** _VM_
> 显示虚拟机性能窗口

**--show-host-summary**
> 显示连接详情

**--show-domain-console** _VM_
> 打开域的控制台窗口

**--spice-disable-auto-usbredir**
> 禁用通过 SPICE 的自动 USB 重定向

**--version**
> 显示程序版本并退出

# DESCRIPTION

**virt-manager** 是一个桌面用户界面，用于管理 KVM 和 Xen 虚拟机以及 LXC 容器。它提供图形界面来创建、配置和监控虚拟机。

该工具连接到 libvirt，可同时管理本地和远程 hypervisor。

# CAVEATS

需要 libvirt 和一个 hypervisor（KVM、Xen 等）。远程管理需要正确的 libvirt 配置。建议具备硬件虚拟化支持。

# INSTALL

```dnf: sudo dnf install virt-manager```

```pacman: sudo pacman -S virt-manager```

```apk: sudo apk add virt-manager```

```zypper: sudo zypper install virt-manager```

```brew: brew install virt-manager```

```nix: nix profile install nixpkgs#virt-manager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virsh](/man/virsh)(1), [virt-install](/man/virt-install)(1), [virt-clone](/man/virt-clone)(1), [virt-viewer](/man/virt-viewer)(1), [qemu](/man/qemu)(1), [kvm](/man/kvm)(1)
