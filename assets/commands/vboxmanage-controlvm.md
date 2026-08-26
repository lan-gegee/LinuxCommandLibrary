# TAGLINE

控制运行中的 VirtualBox 虚拟机

# TLDR

**暂停虚拟机**

```vboxmanage controlvm [vmname] pause```

**恢复虚拟机**

```vboxmanage controlvm [vmname] resume```

**重置虚拟机**

```vboxmanage controlvm [vmname] reset```

**强制关闭虚拟机电源**

```vboxmanage controlvm [vmname] poweroff```

**保存状态**

```vboxmanage controlvm [vmname] savestate```

**发送 ACPI 关机信号**（温和关机）

```vboxmanage controlvm [vmname] acpipowerbutton```

**截取屏幕截图**

```vboxmanage controlvm [vmname] screenshotpng [file.png]```

**设置共享剪贴板模式**

```vboxmanage controlvm [vmname] clipboard mode bidirectional```

**连接/断开网络电缆**

```vboxmanage controlvm [vmname] setlinkstate1 [on|off]```

# SYNOPSIS

**vboxmanage** **controlvm** _vmname_ _command_ [_options_]

# PARAMETERS

**pause**
> 挂起虚拟机的执行。

**resume**
> 恢复已暂停的虚拟机。

**reset**
> 硬重置虚拟机。

**poweroff**
> 强制断电。

**savestate**
> 保存状态并停止虚拟机。

**acpipowerbutton**
> 发送 ACPI 关机信号。

**screenshotpng** _file_
> 捕获屏幕画面。

**setvideomodehint** _w_ _h_ _bpp_
> 设置视频模式。

**clipboard mode** _disabled|hosttoguest|guesttohost|bidirectional_
> 设置共享剪贴板模式。

**setlinkstate**_N_ _on|off_
> 连接或断开虚拟网线 N。

**nic**_N_ _null|nat|bridged|intnet|hostonly_
> 更改网卡 N 的类型。

**nicpromisc**_N_ _deny|allow-vms|allow-all_
> 设置网卡 N 的混杂模式。

**draganddrop** _disabled|hosttoguest|guesttohost|bidirectional_
> 设置拖放模式。

# DESCRIPTION

**vboxmanage controlvm** 用于控制正在运行的虚拟机。可以管理虚拟机状态、发送输入、在运行的虚拟机上修改设置。它是虚拟机运行时控制的核心命令。

# CAVEATS

**poweroff** 和 **reset** 命令相当于直接拔掉电源线——如需温和关机请使用 **acpipowerbutton**。大多数命令要求虚拟机处于运行状态。与网络相关的更改（nic、setlinkstate）会立即对运行中的虚拟机生效。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-startvm](/man/vboxmanage-startvm)(1), [vboxmanage-modifyvm](/man/vboxmanage-modifyvm)(1), [vboxmanage-showvminfo](/man/vboxmanage-showvminfo)(1)
