# TAGLINE

显示 VirtualBox 虚拟机配置详情

# TLDR

**显示虚拟机信息**

```vboxmanage showvminfo [vmname]```

**以机器可读格式显示**

```vboxmanage showvminfo [vmname] --machinereadable```

**显示特定详情**

```vboxmanage showvminfo [vmname] --details```

# SYNOPSIS

**vboxmanage** **showvminfo** _vmname_ [_options_]

# PARAMETERS

**--machinereadable**
> 输出可解析的格式。

**--details**
> 显示详细信息。

**--log** _n_
> 显示第 n 个日志文件。

# DESCRIPTION

**vboxmanage showvminfo** 显示虚拟机的详细配置，包括硬件设置、状态、快照和共享文件夹。脚本处理时请使用 --machinereadable。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-list](/man/vboxmanage-list)(1)
