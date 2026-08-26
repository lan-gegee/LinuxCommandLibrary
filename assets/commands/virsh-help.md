# TAGLINE

显示 virsh 命令帮助

# TLDR

**按类别列出所有可用命令**

```virsh help```

**显示特定命令的详细帮助**

```virsh help [start]```

**列出所有域管理命令**

```virsh help domain```

**列出所有网络命令**

```virsh help network```

**列出所有存储池命令**

```virsh help pool```

# SYNOPSIS

**virsh** **help** [_command_|_group_]

# PARAMETERS

_command_
> 显示特定 virsh 命令的详细帮助。

**domain**
> 域（虚拟机）管理命令。

**interface**
> 主机接口命令。

**network**
> 虚拟网络命令。

**nodedev**
> 主机设备命令。

**pool**
> 存储池命令。

**volume**
> 存储卷命令。

**snapshot**
> 域快照命令。

**monitor**
> 连接与事件监控命令。

# DESCRIPTION

**virsh help** 显示 virsh 命令及命令组的帮助。不带参数调用时，它按类别列出所有命令，并为每个组给出一个关键字。给定命令名时，它显示该命令的详细用法、选项和描述。给定组关键字时，它只列出该组中的命令。

# INSTALL

```apt: sudo apt install libvirt-clients```

```dnf: sudo dnf install libvirt-client```

```apk: sudo apk add libvirt-client```

```zypper: sudo zypper install libvirt-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virsh](/man/virsh)(1)

