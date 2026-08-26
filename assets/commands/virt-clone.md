# TAGLINE

克隆 libvirt 虚拟机

# TLDR

**克隆**虚拟机，自动生成名称、存储和 MAC 地址

```virt-clone --original [vm_name] --auto-clone```

**克隆**虚拟机并指定新名称和存储路径

```virt-clone --original [vm_name] --name [new_vm_name] --file [path/to/new_disk.qcow2]```

**克隆**虚拟机并使用随机 MAC 地址

```virt-clone --original [vm_name] --name [new_vm_name] --auto-clone --mac RANDOM```

**克隆并替换**同名现有虚拟机

```virt-clone --original [vm_name] --name [new_vm_name] --auto-clone --replace```

**克隆但不复制存储**（引用现有磁盘）

```virt-clone --original [vm_name] --name [new_vm_name] --preserve-data```

**打印生成的克隆 XML**而不执行克隆

```virt-clone --original [vm_name] --auto-clone --print-xml```

# SYNOPSIS

**virt-clone** [_options_]

# PARAMETERS

**-o**, **--original** _name_
> 要克隆的原始虚拟机名称（必须处于关闭状态）。

**--original-xml** _file_
> 用作原始客户机的 libvirt guest XML 文件。

**-n**, **--name** _name_
> 新克隆虚拟机的名称。

**--auto-clone**
> 自动生成新的名称、存储和 MAC 地址。

**-f**, **--file** _path_
> 新磁盘镜像的路径。多磁盘客户机可重复使用。

**-m**, **--mac** _address_
> 新虚拟机的 MAC 地址（或 RANDOM）。

**-u**, **--uuid** _uuid_
> 新客户机的 UUID（默认：随机生成）。

**--preserve-data**
> 不复制存储；保留磁盘镜像并直接引用。

**--reflink**
> 若文件系统支持，使用写时复制的 reflink。

**--nonsparse**
> 完全分配新存储，而不是创建稀疏文件。

**--force-copy** _target_
> 强制克隆指定的磁盘目标（例如 'hdc'、'sda'）。

**--replace**
> 关闭并移除与目标名称相同的现有客户机。

**--print-xml**
> 打印生成的克隆 XML 并退出，不执行克隆。

**-c**, **--connect** _uri_
> 连接到指定的 hypervisor URI。

**-d**, **--debug**
> 打印调试信息。

# DESCRIPTION

**virt-clone** 创建现有 libvirt 虚拟机的副本。它会克隆虚拟机配置，可以复制或新建磁盘镜像，并为克隆生成唯一标识符。

该工具会生成新的 UUID、MAC 地址和存储路径，避免与原始虚拟机冲突。它常用于创建测试环境或部署多个相似的虚拟机。标记为 readonly 或 shareable 的磁盘默认会被跳过，除非使用 **--force-copy**。

# CAVEATS

需要 libvirt 及适当的虚拟化后端（KVM、QEMU 等）。原始虚拟机必须处于关闭状态才能保证克隆一致。克隆大型磁盘镜像可能耗时较长，且需要足够的存储空间。如果文件系统对稀疏文件支持不佳，可使用 **--nonsparse** 进行完全分配。

# INSTALL

```dnf: sudo dnf install virt-install```

```pacman: sudo pacman -S virt-install```

```apk: sudo apk add virt-install```

```zypper: sudo zypper install virt-install```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virt-install](/man/virt-install)(1), [virsh](/man/virsh)(1), [virt-manager](/man/virt-manager)(1)
