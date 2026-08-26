# TAGLINE

克隆 VirtualBox 虚拟机

# TLDR

**克隆虚拟机**

```vboxmanage clonevm [vmname] --name [newname]```

**以完整克隆方式复制**

```vboxmanage clonevm [vmname] --mode all --name [newname]```

**克隆并注册**

```vboxmanage clonevm [vmname] --name [newname] --register```

# SYNOPSIS

**vboxmanage** **clonevm** _vmname_ [_options_]

# PARAMETERS

**--name** _name_
> 克隆出的虚拟机名称。

**--mode** _mode_
> 克隆模式（machine、machinechildren、all）。

**--register**
> 将克隆注册到 VirtualBox。

**--basefolder** _path_
> 克隆到指定文件夹。

**--snapshot** _name_
> 从快照克隆。

# DESCRIPTION

**vboxmanage clonevm** 创建现有虚拟机的副本。支持完整克隆（相互独立）和链接克隆（共享基础磁盘）。适合从模板创建测试环境。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-createvm](/man/vboxmanage-createvm)(1)
