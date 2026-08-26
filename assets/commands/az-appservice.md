# TAGLINE

管理 Azure App Service 计划和环境

# TLDR

**列出所有 App Service 计划**

```az appservice plan list```

**显示某个 App Service 计划**的详情

```az appservice plan show --name [plan_name] --resource-group [rg_name]```

**创建 App Service 计划**

```az appservice plan create --name [plan_name] --resource-group [rg_name] --sku [B1] --is-linux```

**缩放 App Service 计划**层级

```az appservice plan update --name [plan_name] --resource-group [rg_name] --sku [S1]```

**删除 App Service 计划**

```az appservice plan delete --name [plan_name] --resource-group [rg_name]```

**列出 App Service 可用的位置**

```az appservice list-locations --sku [S1]```

**显示 ASE（App Service Environment）**详情

```az appservice ase show --name [ase_name] --resource-group [rg_name]```

# SYNOPSIS

**az appservice** _subcommand_ [_options_]

# DESCRIPTION

**az appservice** 是 Azure CLI 的一个子命令，用于管理 Azure App Service 计划和环境。App Service 计划定义了托管 Web 应用、API 应用、移动后端和函数应用所需的计算资源和定价层级。

计划决定了区域、VM 实例数量、实例大小和定价层级（Free、Shared、Basic、Standard、PremiumV2、PremiumV3、Isolated）。多个应用可以共享同一个计划，共用分配的计算资源。

App Service 环境（ASE）提供完全隔离的专用环境，可大规模运行 App Service 应用，并直接集成 VNet 和专用终结点。

# PARAMETERS

**plan list**
> 列出所有 App Service 计划。

**plan show**
> 获取某个计划的详情。

**plan create**
> 创建新的 App Service 计划。

**plan update**
> 修改计划设置或缩放层级。

**plan delete**
> 移除某个 App Service 计划。

**list-locations**
> 列出支持 App Service 的区域。

**ase list**
> 列出 App Service 环境。

**ase show**
> 获取 ASE 详情。

**ase create**
> 创建 App Service 环境。

**--name** _name_
> 计划或 ASE 的名称。

**--resource-group** _rg_
> 包含该资源的资源组。

**--sku** _sku_
> 定价层级：F1（Free）、D1（Shared）、B1/B2/B3（Basic）、S1/S2/S3（Standard）、P1V2/P2V2/P3V2（Premium V2）、P0V3/P1V3/P2V3/P3V3（Premium V3）、I1V2/I2V2/I3V2（Isolated V2）等。

**--is-linux**
> 创建 Linux 计划。Linux 与 Windows 应用不能共用同一个计划。

**--number-of-workers** _count_
> 要分配的实例（工作进程）数量。

**--zone-redundant**
> 启用区域冗余以实现高可用（仅限 Premium 和 Isolated SKU）。

**--location** _region_
> Azure 区域。

# CAVEATS

如果计划中仍包含应用，则无法删除。Free 和 Shared 层级无法横向扩展。Linux 与 Windows 应用不能共用同一个计划。不同层级的 App Service 计划功能可用性不同（自定义域名、SSL、部署槽位）。缩放操作可能需要几分钟。

# HISTORY

**Azure App Service** 由 **Azure Web Sites** 演变而来，后者于 **2012** 年 **6** 月作为 Microsoft 首个 PaaS Web 托管服务推出。**2015** 年 **3 月**，它统一了 Web Apps、Mobile Apps、Logic Apps 和 API Apps，更名为 **Azure App Service**。**Linux 版 App Service** 于 **2017** 年推出。**App Service Environment v3** 于 **2021** 年发布，性能更佳且网络配置更简化。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-webapp](/man/az-webapp)(1), [az-functionapp](/man/az-functionapp)(1), [az-group](/man/az-group)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/appservice)```

<!-- verified: 2026-06-18 -->
