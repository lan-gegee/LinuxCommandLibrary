# TAGLINE

配置 VirtualBox 虚拟机设置

# TLDR

**设置内存**

```vboxmanage modifyvm [vmname] --memory [2048]```

**设置 CPU 数量**

```vboxmanage modifyvm [vmname] --cpus [2]```

**启用嵌套虚拟化**

```vboxmanage modifyvm [vmname] --nested-hw-virt on```

**配置网络**

```vboxmanage modifyvm [vmname] --nic1 nat```

**设置启动顺序**

```vboxmanage modifyvm [vmname] --boot1 dvd --boot2 disk```

# SYNOPSIS

**vboxmanage** **modifyvm** _vmname_ [_options_]

# PARAMETERS

**--name** _name_
> 重命名虚拟机。

**--memory** _mb_
> 内存大小（MB）。

**--cpus** _n_
> CPU 数量。

**--nic1** _type_
> 网卡类型。

**--boot1** _device_
> 第一启动设备。

**--nested-hw-virt** _on|off_
> 嵌套虚拟化。

**--vram** _mb_
> 显存大小。

**--accelerate3d** _on|off_
> 3D 加速。

**--clipboard** _mode_
> 剪贴板模式。

# DESCRIPTION

**vboxmanage modifyvm** 配置虚拟机设置，可修改 CPU、内存、网络、存储和显示设置。大多数更改要求虚拟机处于关机状态。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-createvm](/man/vboxmanage-createvm)(1)
