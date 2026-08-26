# TAGLINE

管理 Azure API Management 服务

# TLDR

**创建新的 API Management** 服务实例

```az apim create --name [MyApim] --resource-group [MyResourceGroup] --publisher-email [email@domain.com] --publisher-name [MyCompany] --location [eastus]```

**列出资源组中的所有 API Management** 服务

```az apim list --resource-group [MyResourceGroup]```

**显示**某个 API Management 服务的**详情**

```az apim show --name [MyApim] --resource-group [MyResourceGroup]```

从 OpenAPI 规范**导入 API**

```az apim api import --service-name [MyApim] --resource-group [MyResourceGroup] --path [myapi] --specification-format OpenAPI --specification-url [https://example.com/swagger.json]```

**列出服务中的所有 API**

```az apim api list --service-name [MyApim] --resource-group [MyResourceGroup]```

为服务**创建备份**

```az apim backup --name [MyApim] --resource-group [MyResourceGroup] --backup-name [myBackup] --storage-account-name [mystorageaccount] --storage-account-container [backups]```

**删除某个 API Management** 服务

```az apim delete --name [MyApim] --resource-group [MyResourceGroup] --yes```

# SYNOPSIS

**az** **apim** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 创建新的 API Management 服务实例。

**show**
> 获取某个 API Management 服务的详情。

**list**
> 列出 API Management 服务实例。

**update**
> 更新 API Management 服务实例。

**delete**
> 删除 API Management 服务实例。

**backup**
> 为 API Management 服务创建备份。

**restore**
> 从备份恢复 API Management 服务。

**api create**
> 创建新 API。

**api import**
> 从规范导入 API。

**api list**
> 列出服务中的 API。

**api operation**
> 管理 API 操作。

**product**
> 管理 API 产品。

**nv**
> 管理用于配置的命名值。

**apply-network-updates**
> 更新 API Management 服务的虚拟网络设置。

# DESCRIPTION

**az apim** 管理 Azure API Management 服务，它为现有后端服务提供创建一致且现代化 API 网关的方式。它负责 API 的创建、版本管理、文档、安全策略、速率限制以及开发人员门户管理。

API Management 支持多个 SKU 层级：Basic、Consumption、Developer、Isolated、Premium 和 Standard，各自提供不同的能力和规模选项。

# CAVEATS

需要安装 Azure CLI 并已通过 **az login** 完成身份验证。非 Consumption 层级的 API Management 服务创建可能需要 30-40 分钟。长时间运行的操作请使用 **--no-wait**。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-advisor](/man/az-advisor)(1), [az-config](/man/az-config)(1)
