# TAGLINE

列出 VirtualBox 对象和信息

# TLDR

**列出所有虚拟机**

```vboxmanage list vms```

**列出运行中的虚拟机**

```vboxmanage list runningvms```

**列出主机信息**

```vboxmanage list hostinfo```

**列出操作系统类型**

```vboxmanage list ostypes```

**列出扩展包**

```vboxmanage list extpacks```

# SYNOPSIS

**vboxmanage** **list** _what_ [_options_]

# PARAMETERS

**vms**
> 所有已注册的虚拟机。

**runningvms**
> 运行中的虚拟机。

**ostypes**
> 支持的操作系统类型。

**hostinfo**
> 主机系统信息。

**hdds**
> 硬盘镜像。

**dvds**
> DVD 镜像。

**extpacks**
> 扩展包。

**groups**
> 虚拟机组。

**--long**
> 详细输出。

# DESCRIPTION

**vboxmanage list** 显示 VirtualBox 对象的信息，可列出虚拟机、磁盘镜像、网络和系统信息。用于查找虚拟机名称和 UUID 的重要命令。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-showvminfo](/man/vboxmanage-showvminfo)(1)
