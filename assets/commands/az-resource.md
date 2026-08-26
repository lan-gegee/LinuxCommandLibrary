# TAGLINE

以通用方式管理所有类型的 Azure 资源

# TLDR

**列出订阅中的所有资源**

```az resource list```

**列出资源组中的资源**

```az resource list --resource-group [rg_name]```

**按 ID 显示资源**

```az resource show --ids [/subscriptions/.../resourceGroups/.../providers/.../name]```

**按名称和类型显示资源**

```az resource show --resource-group [rg_name] --resource-type [Microsoft.Web/sites] --name [resource_name]```

**删除资源**

```az resource delete --ids [resource_id]```

**将资源移动到另一个资源组**

```az resource move --destination-group [dest_rg] --ids [resource_id1] [resource_id2]```

**为资源添加标记**

```az resource tag --tags [env=prod] [team=backend] --ids [resource_id]```

**更新资源属性**

```az resource update --ids [resource_id] --set properties.someProperty=value```

# SYNOPSIS

**az resource** _subcommand_ [_options_]

# DESCRIPTION

**az resource** 是 Azure CLI 的一个子命令，用于以通用方式管理所有资源类型的 Azure 资源。它为适用于任何资源的操作提供统一接口，与具体服务无关。

Azure 中的资源是可识别的实体，例如虚拟机、存储账户或数据库。每个资源都有唯一的资源 ID，遵循 /subscriptions/{sub}/resourceGroups/{rg}/providers/{provider}/{type}/{name} 这一模式。

该命令适合编写跨资源操作的脚本、进行批量管理，以及处理可能尚无专用 CLI 命令组的资源类型。

# PARAMETERS

**list**
> 列出资源，可附带筛选条件。

**show**
> 显示资源详细信息。

**create**
> 根据属性创建资源。

**delete**
> 删除资源。

**update**
> 通过 PUT 请求更新资源。

**patch**
> 通过 PATCH 请求更新资源。

**move**
> 在资源组或订阅之间移动资源。

**tag**
> 为资源添加标记。

**invoke-action**
> 对资源调用某个操作。

**wait**
> 等待资源满足某个条件（预配、删除等）。

**--ids** _ids_
> 一个或多个资源 ID。

**--resource-group** _rg_
> 资源组名称。

**--resource-type** _type_
> 资源类型（例如 Microsoft.Compute/virtualMachines）。

**--name** _name_
> 资源名称。

**--namespace** _namespace_
> 提供程序命名空间。

**--api-version** _version_
> 该资源类型的 API 版本。

**--set** _property=value_
> 更新资源上的某个属性（例如 properties.someProperty=value）。

**--add** _list property=value_
> 向对象列表添加对象（例如 --add tags.newKey=value）。

**--remove** _property/index_
> 移除某个属性或列表中的元素。

**--tags** _tags_
> 以空格分隔的标记（key=value）。

**--query-string** _query_
> 使用 OData 查询筛选资源。

# CAVEATS

某些资源无法在资源组或订阅之间移动。删除资源可能会留下孤立的依赖资源。API 版本的兼容性因资源类型而异。通用命令可能缺少专用命令组所具备的服务特定验证。资源移动可能耗时较长，且存在服务特定的限制。

# HISTORY

通用资源命令自 **2017** 年 **Azure CLI 2.0** 发布起就是 Azure CLI 的一部分。它们可为任何资源类型提供 ARM（Azure Resource Manager）API 访问。随着 Azure 的成长，各服务的专用命令组不断增多，但通用资源命令在自动化、批量操作以及抢先使用尚无专用命令的新资源类型方面仍然很有价值。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-group](/man/az-group)(1), [az-deployment](/man/az-deployment)(1), [az-provider](/man/az-provider)(1), [az-tag](/man/az-tag)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/resource)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
