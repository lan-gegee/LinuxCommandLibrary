# TAGLINE

管理 Azure 托管磁盘

# TLDR

**创建指定大小的托管磁盘**

```az disk create --name [MyDisk] --resource-group [MyResourceGroup] --size-gb [128]```

**从快照创建磁盘**

```az disk create --name [MyDisk] --resource-group [MyResourceGroup] --source [snapshot_id]```

**创建 Premium SSD 磁盘**

```az disk create --name [MyDisk] --resource-group [MyResourceGroup] --size-gb [128] --sku Premium_LRS```

**列出资源组中的所有托管磁盘**

```az disk list --resource-group [MyResourceGroup]```

**显示某个托管磁盘的详情**

```az disk show --name [MyDisk] --resource-group [MyResourceGroup]```

**更新磁盘大小**

```az disk update --name [MyDisk] --resource-group [MyResourceGroup] --size-gb [256]```

**授予托管磁盘的读取权限以供导出**

```az disk grant-access --name [MyDisk] --resource-group [MyResourceGroup] --duration-in-seconds [3600] --access-level Read```

**撤销对托管磁盘的访问**

```az disk revoke-access --name [MyDisk] --resource-group [MyResourceGroup]```

**删除托管磁盘**

```az disk delete --name [MyDisk] --resource-group [MyResourceGroup] --yes```

# SYNOPSIS

**az** **disk** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 创建托管磁盘。

**delete**
> 删除托管磁盘。

**list**
> 列出托管磁盘。

**show**
> 获取托管磁盘的信息。

**update**
> 更新托管磁盘。

**grant-access**
> 授予磁盘读取或读写访问权限。

**revoke-access**
> 撤销对磁盘的访问。

**wait**
> 等待磁盘达到特定状态。

# PARAMETERS

**--name** **-n**
> 托管磁盘的名称。

**--resource-group** **-g**
> 资源组的名称。

**--size-gb** **-z**
> 托管磁盘的大小，以 GB 为单位。

**--source**
> 用于创建磁盘的源磁盘、快照或 URI。

**--sku**
> 存储类型：Standard_LRS、Premium_LRS、StandardSSD_LRS、UltraSSD_LRS、PremiumV2_LRS、Premium_ZRS、StandardSSD_ZRS。

**--location** **-l**
> 磁盘的位置。

**--zone**
> 创建磁盘所在的可用性区域。

**--encryption-type**
> 加密类型：EncryptionAtRestWithPlatformKey（默认）、EncryptionAtRestWithCustomerKey。

**--access-level**
> grant-access 的访问级别：Read 或 Write。

**--duration-in-seconds**
> SAS 访问 URI 的有效期，以秒为单位。

# DESCRIPTION

**az disk** 管理 Azure 托管磁盘。托管磁盘是由 Azure 管理的块级存储卷，与 Azure 虚拟机配合使用。它们自动处理存储账户管理，从而简化了磁盘管理。

支持的存储类型包括标准 HDD（Standard_LRS）、标准 SSD（StandardSSD_LRS）、高级 SSD（Premium_LRS）、高级 SSD v2（PremiumV2_LRS）和超级磁盘（UltraSSD_LRS）。区域冗余选项（Premium_ZRS、StandardSSD_ZRS）提供跨区域复制。

# CAVEATS

需要安装 Azure CLI 并已通过 **az login** 完成身份验证。磁盘只能挂载到同一区域的虚拟机。扩容磁盘需要先解除虚拟机的分配或卸下磁盘；磁盘无法缩小。除非配置了客户管理的密钥，否则磁盘加密默认使用平台管理的密钥。

# HISTORY

**az disk** 是 **Azure CLI**（`az`）的一部分，由 **Microsoft** 开发，用于从命令行管理 Azure 资源。Azure 引入托管磁盘是为了免去单独管理存储账户的需要，从而简化磁盘管理。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-vm](/man/az-vm)(1), [az-image](/man/az-image)(1)
