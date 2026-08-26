# TAGLINE

显示虚拟机图形控制台

# TLDR

**连接到虚拟机**

```virt-viewer [vmname]```

**通过 URI 连接**

```virt-viewer -c [qemu:///system] [vmname]```

**连接到远程**

```virt-viewer -c [qemu+ssh://host/system] [vmname]```

**全屏显示**

```virt-viewer --full-screen [vmname]```

**等待虚拟机**

```virt-viewer --wait [vmname]```

# SYNOPSIS

**virt-viewer** [_-c uri_] [_--full-screen_] [_options_] _vmname_

# PARAMETERS

**-c** _URI_
> 连接 URI。

**--full-screen**
> 全屏模式。

**--wait**
> 等待虚拟机。

**--reconnect**
> 自动重连。

**--hotkeys** _KEYS_
> 自定义快捷键。

# DESCRIPTION

**virt-viewer** 是一个轻量级的图形控制台客户端，用于查看由 libvirt 管理的虚拟机的显示内容。它连接到运行中的虚拟机，并在本地窗口中渲染其图形输出，在只需要控制台访问时提供了比完整的 virt-manager 应用更简单的选择。

该工具同时支持 SPICE 和 VNC 显示协议，会从虚拟机配置中自动检测合适的连接方式。远程连接通过 SSH 隧道实现，让用户无需直接暴露显示端口即可安全访问远程 hypervisor 上的虚拟机控制台。

其他功能包括用于独占显示的全屏模式、将本地硬件传给客户机的 USB 设备重定向、共享剪贴板支持以及自动调整屏幕分辨率。查看器还可以在虚拟机启动后再进行连接，非常适合脚本化或自动化工作流。

# CAVEATS

需要 libvirt。虚拟机必须处于运行状态。需要 X11/Wayland。

# HISTORY

**virt-viewer** 是 **virt-manager** 项目的一部分，提供一个用于查看虚拟机图形控制台的极简工具。

# INSTALL

```apt: sudo apt install virt-viewer```

```dnf: sudo dnf install virt-viewer```

```pacman: sudo pacman -S virt-viewer```

```apk: sudo apk add virt-viewer```

```zypper: sudo zypper install virt-viewer```

```nix: nix profile install nixpkgs#virt-viewer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virsh](/man/virsh)(1), [virt-manager](/man/virt-manager)(1), [remote-viewer](/man/remote-viewer)(1)
