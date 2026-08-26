# TAGLINE

编辑 libvirt 域 XML 配置

# TLDR

**列出可用的磁盘子选项**

```virt-xml --disk=?```

**编辑虚拟机元数据**

```virt-xml [domain] --edit --metadata description="[new_description]"```

**切换启动菜单**

```virt-xml [domain] --edit --boot bootmenu=[on]```

**为虚拟机添加磁盘**

```virt-xml [domain] --add-device --disk [path=/var/lib/libvirt/images/disk.qcow2]```

**向运行中的虚拟机挂载 USB 设备**

```virt-xml [domain] --update --add-device --hostdev [bus].[device]```

# SYNOPSIS

**virt-xml** [_OPTIONS_] _DOMAIN_

# PARAMETERS

**--edit**
> 编辑现有配置

**--add-device**
> 添加新设备

**--update**
> 将更改应用到运行中的虚拟机

**--disk**
> 磁盘配置选项

**--network**
> 网络配置选项

**--boot**
> 启动配置选项

**--metadata**
> 元数据选项（description、title 等）

**--hostdev**
> 主机设备直通

# DESCRIPTION

**virt-xml** 使用显式的命令行选项编辑 libvirt 域 XML 文件。它提供了一种无需手动编辑 XML 即可修改虚拟机配置的方式。

对于现有虚拟机，可以按名称、UUID 或 ID 指定域。在任何选项后添加 =? 可列出可用的子选项。

# CAVEATS

对运行中虚拟机的更改可能需要重启才能生效。并非所有选项都能在运行中的虚拟机上修改。需要适当的 libvirt 权限。

# INSTALL

```dnf: sudo dnf install virt-manager```

```pacman: sudo pacman -S virt-manager```

```apk: sudo apk add virt-manager```

```zypper: sudo zypper install virt-manager```

```brew: brew install virt-manager```

```nix: nix profile install nixpkgs#virt-manager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virsh](/man/virsh)(1), [virt-manager](/man/virt-manager)(1), [virt-xml-validate](/man/virt-xml-validate)(1)
