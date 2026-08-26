# TAGLINE

管理 Azure 资源上的标记

# TLDR

**设置资源的完整标记集**（类似 init，会替换现有标记）

```az tag create --resource-id [resource-id] --tags [env=prod team=dev]```

**列出资源、资源组或订阅上的标记**

```az tag list --resource-id [resource-id]```

**将标记合并进现有集合**（添加或更新）

```az tag update --resource-id [resource-id] --operation Merge --tags [newkey=newvalue]```

**替换资源上的全部标记**

```az tag update --resource-id [resource-id] --operation Replace --tags [key=value]```

**从资源中选择性删除标记**

```az tag update --resource-id [resource-id] --operation Delete --tags [keytoremove=value]```

**在订阅级别创建预定义标记名称**

```az tag create --name [tagname]```

**为标记名称添加预定义值**

```az tag add-value --name [tagname] --value [tagvalue]```

**从订阅中删除预定义标记名称**

```az tag delete --name [tagname]```

# SYNOPSIS

**az** **tag** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 创建（设置）资源、资源组或订阅上的整套标记。会替换任何现有标记。只提供 --name 时，则在订阅上创建预定义标记名称。

**delete**
> 删除资源上的整套标记，或从订阅中删除预定义标记名称。

**list**
> 列出资源、资源组或订阅上的整套标记。

**update**
> 使用 Merge、Replace 或 Delete 选择性更新资源上的标记。

**add-value**
> 为预定义标记名称创建预定义标记值。

**remove-value**
> 删除预定义标记名称下的预定义标记值。

# PARAMETERS

**--resource-id**
> 要打标记的实体的资源标识符。可对资源、资源组或订阅打标记。

**--tags**
> 以空格分隔的 key=value 标记对。

**--operation**
> 更新操作：Merge、Replace 或 Delete。

**--name** **-n**
> 订阅级操作所用的预定义标记名称。

**--value**
> 标记值，与 add-value 和 remove-value 配合使用。

**--yes** **-y**
> 不提示确认（用于 delete）。

# DESCRIPTION

**az tag** 管理 Azure 资源标记，即用于组织和归类资源的元数据键值对。标记有助于成本管理、自动化和治理。

可以通过 **--resource-id** 在订阅、资源组或单个资源级别应用标记。资源不会继承其父资源组的标记。此外，**--name** 和 **--value** 用于在订阅级别管理预定义的标记名称和值（一套可复用的分类体系），而不将其附加到具体资源上。

# CAVEATS

需要安装并完成 Azure CLI 身份验证。每个资源最多 50 个标记。标记名称不区分大小写，但标记值区分大小写。某些资源类型不支持标记。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-resource](/man/az-resource)(1), [az-lock](/man/az-lock)(1), [az-provider](/man/az-provider)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/tag)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
