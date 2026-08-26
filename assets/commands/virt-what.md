# TAGLINE

检测虚拟化技术

# TLDR

**检测**虚拟化技术（需要 root）

```sudo virt-what```

将输出**记录**到文件

```sudo virt-what > [path/to/file]```

显示**版本**

```virt-what --version```

# SYNOPSIS

**virt-what** [_OPTIONS_]

# PARAMETERS

**--version**
> 显示版本信息

# DESCRIPTION

**virt-what** 是一个 shell 脚本，用于检测你是否运行在虚拟机中。它会输出一行或多行内容来标识虚拟化技术。如果没有输出，说明系统运行在裸机上。

该工具可以检测多种 hypervisor，包括 KVM、QEMU、Xen（HVM 和 PV）、VMware、VirtualBox、Hyper-V、Docker、LXC、OpenVZ、Podman 等。嵌套虚拟化时可能输出多行（例如在 Hyper-V 中运行 KVM 时同时输出 "kvm" 和 "hyperv"）。

# OUTPUT VALUES

常见的输出值包括：**kvm**、**qemu**、**xen**、**xen-hvm**、**xen-pv**、**vmware**、**virtualbox**、**hyperv**、**docker**、**lxc**、**openvz**、**podman**、**parallels**、**bhyve**、**uml**（User-Mode Linux）。

# CAVEATS

需要 root 权限才能可靠检测。某些检测方法会读取只有 root 才能访问的 DMI 数据或内核模块。嵌套虚拟化可能产生多行输出。也支持容器检测（Docker、LXC、Podman）。

# HISTORY

**virt-what** 由 Red Hat 的 **Richard W.M. Jones** 开发，作为 virt-what 软件包的一部分分发，常用于供应脚本中以检测运行环境。

# INSTALL

```apt: sudo apt install virt-what```

```dnf: sudo dnf install virt-what```

```pacman: sudo pacman -S virt-what```

```apk: sudo apk add virt-what```

```zypper: sudo zypper install virt-what```

```nix: nix profile install nixpkgs#virt-what```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-detect-virt](/man/systemd-detect-virt)(1), [lscpu](/man/lscpu)(1)
