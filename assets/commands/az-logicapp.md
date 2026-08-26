# TAGLINE

管理 Azure Logic Apps

# TLDR

在 App Service 计划上**创建 Logic App**

```az logicapp create --name [MyLogicApp] --resource-group [MyResourceGroup] --storage-account [MyStorageAccount] --plan [MyPlan]```

**列出资源组中的所有 Logic Apps**

```az logicapp list --resource-group [MyResourceGroup]```

**显示**某个 Logic App 的**详情**

```az logicapp show --name [MyLogicApp] --resource-group [MyResourceGroup]```

**启动 Logic App**

```az logicapp start --name [MyLogicApp] --resource-group [MyResourceGroup]```

**停止 Logic App**

```az logicapp stop --name [MyLogicApp] --resource-group [MyResourceGroup]```

**删除 Logic App**

```az logicapp delete --name [MyLogicApp] --resource-group [MyResourceGroup] --yes```

# SYNOPSIS

**az** **logicapp** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 创建 Logic App。

**delete**
> 删除 Logic App。

**list**
> 列出 Logic Apps。

**show**
> 获取 Logic App 的详情。

**start**
> 启动 Logic App。

**stop**
> 停止 Logic App。

**restart**
> 重启 Logic App。

**deployment**
> 管理 Logic App 部署。

**config**
> 配置 Logic App 设置。

# COMMON PARAMETERS

**--name**, **-n** _NAME_
> Logic App 的名称。

**--resource-group**, **-g** _RG_
> 包含该 Logic App 的资源组。

**--storage-account** _ACCOUNT_
> Logic App 使用的存储账户（名称或资源 ID）（Standard 层级，创建时必填）。

**--plan** _PLAN_
> 承载 Logic App 的 App Service 计划名称或资源 ID。

**--functions-version** _VERSION_
> Functions 运行时版本（例如 4）。

**--runtime-version** _VERSION_
> 运行时版本（例如 ~14、~16、~18）。

**--https-only** {false,true}
> 将所有流量重定向到 HTTPS。

**--tags** _TAGS_
> 空格分隔的 `key=value` 标签。

**--yes**
> 跳过确认提示（由 `delete` 使用）。

# DESCRIPTION

**az logicapp** 管理 Azure Logic Apps（Standard），这是一种集成应用、数据、服务和系统的无服务器工作流。Logic Apps 为企业集成场景提供可视化设计器和预构建的连接器。

此命令组管理 Standard 层级的 Logic Apps。对于 Consumption 层级的 Logic Apps，请使用 Azure 门户或 ARM 模板。

# CAVEATS

需要安装 Azure CLI 并已完成身份验证。Standard 层级 Logic Apps 需要存储账户。某些功能需要特定的 Azure 区域。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-functionapp](/man/az-functionapp)(1)
