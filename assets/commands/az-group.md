# TAGLINE

管理 Azure 资源组

# TLDR

**创建资源组**

```az group create -l [westus] -n [MyResourceGroup]```

**列出所有资源组**

```az group list -o table```

**显示**某个资源组的**详情**

```az group show -n [MyResourceGroup]```

**检查资源组是否存在**

```az group exists -n [MyResourceGroup]```

**删除资源组**及其所有资源

```az group delete -n [MyResourceGroup] --yes```

**更新**资源组上的**标签**

```az group update -n [MyResourceGroup] --tags [Dept=IT] [Env=Test]```

将资源组**导出为模板**

```az group export -n [MyResourceGroup]```

在特定位置**列出资源组**

```az group list --query "[?location=='westus']"```

# SYNOPSIS

**az group** _subcommand_ [_options_]

# DESCRIPTION

**az group** 管理 Azure 资源组——Azure 资源的逻辑容器。Azure 中的所有资源都必须属于某个资源组，资源组提供组织、管理相关资源以及对其应用策略的方式。

资源组定义了资源的生命周期范围；删除组会删除其中所有资源。资源组还提供基于角色的访问控制（RBAC）和策略分配的作用域。

# SUBCOMMANDS

**Management**
> create, delete, update, show, list, exists

**Templates**
> export

**Locks**
> lock create, lock delete, lock list, lock show, lock update

**Waiting**
> wait

# PARAMETERS

**-n, --name** _value_
> 资源组的名称

**-l, --location** _value_
> 资源组的位置（例如 westus、eastus）

**--tags** _value_
> 空格分隔的标签，格式为 key[=value]。使用 "" 清除现有标签

**--set** _value_
> 更新时按路径设置属性，例如 --set tags.Dept=IT

**-y, --yes**
> 不提示确认（删除时）

**--no-wait**
> 不等待长时间运行的删除操作完成

**-f, --force-deletion-types** _value_
> 要强制删除的资源类型（例如 Microsoft.Compute/virtualMachines）

**--export-format** _value_
> 导出模板的格式：json（默认）、bicep 或 arm

# CAVEATS

资源组名称在订阅内必须唯一，且只能包含字母数字字符、句点、下划线、连字符和圆括号。删除资源组不可逆，会移除其中所有资源。组的位置仅是元数据；资源可以位于不同区域。

# HISTORY

自 **2014** 年推出以来，资源组一直是 Azure Resource Manager（ARM）的基础，取代了经典部署模型。它们为 Azure 基于角色的访问控制和策略管理提供了组织基础。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-resource](/man/az-resource)(1), [az-deployment](/man/az-deployment)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/group)```

<!-- verified: 2026-06-18 -->
