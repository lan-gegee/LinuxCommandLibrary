# TAGLINE

检测 VMware 虚拟机环境

# TLDR

检查是否运行在 **VMware** 中

```vmware-checkvm```

获取**硬件**版本

```vmware-checkvm -h```

# SYNOPSIS

**vmware-checkvm** [_OPTIONS_]

# PARAMETERS

**-h**
> 返回 VMware 硬件版本

# DESCRIPTION

**vmware-checkvm** 检查当前主机是否运行在 VMware 虚拟机内部。退出状态表明系统是否为虚拟机（是则返回 0，否则返回非零值）。

在 VMware 内运行时，它会返回 VMware 软件版本信息。

# CAVEATS

仅适用于 VMware。只能检测 VMware 虚拟化。属于 open-vm-tools 软件包。

# INSTALL

```apt: sudo apt install open-vm-tools```

```dnf: sudo dnf install open-vm-tools```

```pacman: sudo pacman -S open-vm-tools```

```apk: sudo apk add open-vm-tools```

```zypper: sudo zypper install open-vm-tools```

```nix: nix profile install nixpkgs#open-vm-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-what](/man/virt-what)(1), [systemd-detect-virt](/man/systemd-detect-virt)(1)
