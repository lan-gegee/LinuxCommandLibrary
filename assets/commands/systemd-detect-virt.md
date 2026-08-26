# TAGLINE

检测虚拟化环境

# TLDR

**列出**可检测的虚拟化技术

```systemd-detect-virt --list```

**检测**虚拟化并打印结果

```systemd-detect-virt```

**静默**检查而不打印任何内容

```systemd-detect-virt -q```

**只**检测容器虚拟化

```systemd-detect-virt -c```

**只**检测硬件虚拟化

```systemd-detect-virt -v```

**检测**是否处于 chroot 环境

```systemd-detect-virt -r```

# SYNOPSIS

**systemd-detect-virt** [_options_]

# PARAMETERS

**--list**
> 列出所有可检测的虚拟化技术

**-q, --quiet**
> 抑制输出，仅返回退出码

**-c, --container**
> 只检测容器虚拟化

**-v, --vm**
> 只检测硬件虚拟机

**-r, --chroot**
> 检测 chroot 环境

**--private-users**
> 检测用户命名空间

# DESCRIPTION

**systemd-detect-virt** 检测系统是否运行在虚拟化环境中，并打印检测到的虚拟化技术。检测到虚拟化时返回退出码 0，否则返回非零值。

可检测的技术包括：KVM、QEMU、VMware、VirtualBox、Xen、Hyper-V、Docker、LXC、systemd-nspawn 等等。**--list** 选项会显示所有支持的技术。

# CAVEATS

检测依赖多种启发式方法，可能无法识别所有虚拟化类型。某些嵌套虚拟化场景可能只报告最内层。属于 systemd 工具套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-nspawn](/man/systemd-nspawn)(1), [machinectl](/man/machinectl)(1)
