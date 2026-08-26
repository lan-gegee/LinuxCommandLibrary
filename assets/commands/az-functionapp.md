# TAGLINE

管理 Azure Functions 无服务器应用

# TLDR

**列出所有函数应用**

```az functionapp list```

**创建函数应用**（消耗计划）

```az functionapp create --resource-group [rg_name] --consumption-plan-location [eastus] --runtime [node] --functions-version [4] --name [app_name] --storage-account [storage_name]```

在 Flex Consumption 计划上**创建函数应用**

```az functionapp create --resource-group [rg_name] --flexconsumption-location [northeurope] --runtime [java] --name [app_name] --storage-account [storage_name]```

在 App Service 计划上**创建函数应用**

```az functionapp create --resource-group [rg_name] --plan [plan_name] --runtime [python] --runtime-version [3.11] --functions-version [4] --name [app_name] --storage-account [storage_name]```

**显示函数应用详情**

```az functionapp show --name [app_name] --resource-group [rg_name]```

从 zip 文件**部署代码**

```az functionapp deployment source config-zip --name [app_name] --resource-group [rg_name] --src [function.zip]```

**重启函数应用**

```az functionapp restart --name [app_name] --resource-group [rg_name]```

**查看应用程序设置**

```az functionapp config appsettings list --name [app_name] --resource-group [rg_name]```

**设置某个应用程序设置**

```az functionapp config appsettings set --name [app_name] --resource-group [rg_name] --settings "[KEY=value]"```

**列出应用中的函数**

```az functionapp function list --name [app_name] --resource-group [rg_name]```

# SYNOPSIS

**az functionapp** _subcommand_ [_options_]

# DESCRIPTION

**az functionapp** 是 Azure CLI 的一个子命令，用于管理 Azure Functions 应用。Azure Functions 是一种无服务器计算服务，无需管理基础设施即可运行事件触发的代码。

函数应用承载一个或多个共享配置、部署和缩放的函数。它们可以运行在消耗计划（按执行付费、自动缩放）、高级计划（预热的实例、VNet 集成）或专用 App Service 计划上。

支持的运行时包括 .NET、Node.js、Python、Java、PowerShell 和自定义处理程序。函数可由 HTTP 请求、计时器、队列、Blob、Event Grid 及其他 Azure 服务触发。

# PARAMETERS

**list**
> 列出所有函数应用。

**create**
> 创建新的函数应用。

**delete**
> 移除某个函数应用。

**show**
> 获取函数应用详情。

**restart**
> 重启函数应用。

**start**
> 启动已停止的函数应用。

**stop**
> 停止运行中的函数应用。

**deployment source config-zip**
> 从 zip 文件部署。

**config appsettings list**
> 列出应用程序设置。

**config appsettings set**
> 设置应用程序设置。

**function list**
> 列出应用中的函数。

**--name** _name_
> 函数应用名称（全局唯一）。

**--resource-group** _rg_
> 资源组名称。

**--consumption-plan-location** _location_
> 消耗计划的区域。

**--plan** _plan_
> App Service 计划名称。

**--runtime** _runtime_
> Functions 运行时栈（例如 node、python、dotnet、dotnet-isolated、java、powershell、custom）。运行 `az functionapp list-runtimes` 查看支持的值。

**--runtime-version** _version_
> 运行时栈版本。运行 `az functionapp list-runtimes` 检查兼容性。

**--functions-version** _version_
> Azure Functions 运行时主版本（当前为 4）。

**--os-type** _{Linux, Windows}_
> 应用使用的操作系统。

**--flexconsumption-location** _location_
> Flex Consumption 计划应用的区域。

**--storage-account** _storage_, **-s**
> 用于存储函数状态的存储账户名称（或资源 ID）。必填。

# CAVEATS

函数应用名称必须全局唯一。消耗计划存在冷启动延迟。触发器和状态需要存储账户。VNet 集成等功能需要 Premium 或 App Service 计划。Linux 消耗计划可用区域有限。Functions 版本 4 要求与运行时特定版本兼容。

# HISTORY

**Azure Functions** 于 **2016** 年 **3 月**作为 Microsoft 的无服务器计算平台推出，灵感来自 AWS Lambda。面向有状态工作流的 **Durable Functions** 于 **2017** 年加入。面向企业场景的 **Premium 计划**于 **2019** 年推出。支持 .NET 6 的 **Functions 4.0** 于 **2021** 年 **11 月**发布。该服务已扩展到支持容器、通过 KEDA 的 Kubernetes，以及面向混合部署的 Azure Arc。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-appservice](/man/az-appservice)(1), [az-storage](/man/az-storage)(1), [func](/man/func)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/functionapp)```

<!-- verified: 2026-06-18 -->
