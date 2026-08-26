# TAGLINE

管理 Azure 中的自定义虚拟机镜像

# TLDR

从虚拟机**创建托管镜像**

```az image create --name [MyImage] --resource-group [MyResourceGroup] --source [MyVM]```

从托管磁盘**创建镜像**

```az image create --name [MyImage] --resource-group [MyResourceGroup] --os-disk [disk-id] --os-type [Linux]```

**列出资源组中的所有镜像**

```az image list --resource-group [MyResourceGroup]```

**显示**某个镜像的**详情**

```az image show --name [MyImage] --resource-group [MyResourceGroup]```

**更新镜像标签**

```az image update --name [MyImage] --resource-group [MyResourceGroup] --tags [env=prod]```

**删除镜像**

```az image delete --name [MyImage] --resource-group [MyResourceGroup]```

# SYNOPSIS

**az** **image** _subcommand_ [_options_]

# SUBCOMMANDS

**copy**
> 将托管镜像复制到其他区域（需要扩展）。

**create**
> 从托管磁盘或快照创建自定义虚拟机镜像。

**delete**
> 删除镜像。

**list**
> 列出资源组或订阅中的镜像。

**show**
> 获取镜像的信息。

**update**
> 更新自定义 VM 镜像。

**wait**
> 让 CLI 进入等待状态，直到满足条件。

# PARAMETERS

**--name** **-n**
> 镜像的名称。

**--resource-group** **-g**
> 资源组的名称。

**--source**
> 用于创建镜像的源虚拟机、托管磁盘或快照。

**--os-disk**
> 作为 OS 磁盘的源托管磁盘。

**--os-type**
> 操作系统类型：Linux 或 Windows。

**--location** **-l**
> 镜像的位置。

**--hyper-v-generation**
> 虚拟机的虚拟机监控程序代次：V1 或 V2。

**--tags**
> 空格分隔的标签：key[=value]。

**--data-disk-sources**
> 用作数据磁盘的托管磁盘或快照。

# DESCRIPTION

**az image** 管理 Azure 中的自定义虚拟机镜像。自定义镜像可以从已通用化的虚拟机、托管磁盘或快照创建。之后可以用这些镜像创建带有自定义配置的新虚拟机。

自定义镜像不同于市场镜像（通过 **az vm image** 管理），因为它们包含你特定的软件和配置。

# CAVEATS

需要安装 Azure CLI 并已通过 **az login** 完成身份验证。创建镜像前，源虚拟机必须已通用化（Windows 上运行 sysprep，Linux 上运行 waagent -deprovision）。镜像只能在同一区域创建虚拟机。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-disk](/man/az-disk)(1), [az-vm](/man/az-vm)(1)
