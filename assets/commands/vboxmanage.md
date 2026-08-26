# TAGLINE

VirtualBox 命令行管理界面

# TLDR

**列出虚拟机**

```vboxmanage list vms```

**启动虚拟机**

```vboxmanage startvm [vmname]```

**无界面启动**

```vboxmanage startvm [vmname] --type headless```

**停止虚拟机**

```vboxmanage controlvm [vmname] poweroff```

**创建虚拟机**

```vboxmanage createvm --name [vmname] --register```

**创建快照**

```vboxmanage snapshot [vmname] take [snapname]```

# SYNOPSIS

**vboxmanage** _command_ [_options_]

# PARAMETERS

**list**
> 列出对象。

**startvm**
> 启动虚拟机。

**controlvm**
> 控制运行中的虚拟机。

**createvm**
> 创建虚拟机。

**modifyvm**
> 修改设置。

**snapshot**
> 快照操作。

**showvminfo**
> 显示虚拟机配置详情。

**clonevm**
> 克隆现有虚拟机。

**storagectl**
> 管理存储控制器。

**storageattach**
> 将存储介质挂接到虚拟机。

**sharedfolder**
> 管理主机与客户机之间的共享文件夹。

**guestcontrol**
> 在客户机操作系统中执行命令。

**--type** _TYPE_
> 启动类型（gui、headless、separate）。

**-q**, **--nologo**
> 抑制 logo 输出，便于脚本处理。

**--machinereadable**
> 机器可解析的输出格式。

# DESCRIPTION

**vboxmanage** 是 Oracle VirtualBox 的命令行界面，提供对虚拟机创建、配置和运行的完全控制。它暴露了图形界面中的全部功能，还有许多只能通过命令行使用的功能。

该工具使用不同的子命令执行不同操作：**createvm** 和 **modifyvm** 用于初始设置，**startvm** 和 **controlvm** 用于运行时管理，**snapshot** 用于保存状态，**list** 用于查询已注册的对象。大多数通过 **modifyvm** 进行的配置更改要求虚拟机处于关机状态。可以通过名称或 UUID 标识虚拟机。

# CAVEATS

必须安装 VirtualBox。大多数 **modifyvm** 更改要求虚拟机处于关机状态。共享文件夹和客户机控制等高级功能需要安装 Guest Additions。

# SEE ALSO

[qemu](/man/qemu)(1), [virsh](/man/virsh)(1)
