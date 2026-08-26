# TAGLINE

使用 ARM 模板和 Bicep 部署 Azure 资源

# TLDR

从模板**创建资源组部署**

```az deployment group create --resource-group [rg_name] --template-file [template.json]```

使用参数文件**部署**

```az deployment group create --resource-group [rg_name] --template-file [template.json] --parameters [parameters.json]```

**部署 Bicep 文件**

```az deployment group create --resource-group [rg_name] --template-file [main.bicep]```

**验证部署**而不实际执行

```az deployment group validate --resource-group [rg_name] --template-file [template.json]```

部署前用 what-if **预览变更**

```az deployment group what-if --resource-group [rg_name] --template-file [template.json]```

**显示部署详情**

```az deployment group show --resource-group [rg_name] --name [deployment_name]```

**列出资源组中的部署**

```az deployment group list --resource-group [rg_name]```

**删除某个部署**

```az deployment group delete --resource-group [rg_name] --name [deployment_name]```

在订阅范围**部署**

```az deployment sub create --location [eastus] --template-file [template.json]```

# SYNOPSIS

**az deployment** _scope_ _subcommand_ [_options_]

# DESCRIPTION

**az deployment** 是 Azure CLI 的一个子命令，用于管理 Azure Resource Manager（ARM）部署。它通过 ARM 模板（JSON）或 Bicep 文件以基础设施即代码的方式创建和更新 Azure 资源。

部署可以面向不同的作用域：资源组、订阅、管理组或租户。模板定义要创建的资源、其属性和依赖关系。参数允许在不修改模板的情况下进行自定义。

部署模式包括增量（添加/更新资源）和完全（删除不在模板中的资源）。what-if 操作可在部署前预览变更。

# PARAMETERS

**group create**
> 在资源组范围部署。

**group validate**
> 验证模板而不部署。

**group show**
> 显示部署详情。

**group list**
> 列出资源组中的部署。

**group delete**
> 移除部署历史条目。

**group what-if**
> 预览部署变更。

**sub create**
> 在订阅范围部署。

**mg create**
> 在管理组范围部署。

**tenant create**
> 在租户范围部署。

**--resource-group** _rg_
> 目标资源组。

**--template-file** _file_
> ARM 模板或 Bicep 文件路径。

**--template-uri** _uri_
> 模板文件的 URL。

**--parameters** _params_
> 参数值（文件路径或内联）。

**--name** _name_
> 部署名称。

**--mode** _mode_
> Incremental 或 Complete。

**--location** _region_
> 订阅范围的部署必填。

**--confirm-with-what-if**, **-c**
> 部署前显示 what-if 结果并提示确认。

**--no-wait**
> 不等待长时间运行的部署完成。

# CAVEATS

Complete 模式会删除不在模板中的资源；请谨慎使用。每个资源组的部署历史最多 800 条（最旧的会被自动删除）。模板文件大小上限为 4 MB。更大的基础设施需要用嵌套模板的链接部署或模板规格。Bicep 文件会在部署前编译为 ARM JSON。

# HISTORY

**Azure Resource Manager** 模板于 **2014** 年推出，作为 Azure 的基础设施即代码解决方案。部署命令随多个 CLI 版本不断演进。**What-if** 预览功能于 **2020** 年加入。可编译为 ARM 模板的领域特定语言 **Bicep** 于 **2021** 年 **5 月**达到 1.0 版本，现已成为推荐的编写方式。用于版本化、可共享模板的 Template Specs 于 **2020** 年引入。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-group](/man/az-group)(1), [az-bicep](/man/az-bicep)(1), [az-resource](/man/az-resource)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/deployment)```

<!-- verified: 2026-06-18 -->
