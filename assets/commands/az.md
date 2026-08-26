# TAGLINE

Microsoft Azure 的统一命令行界面

# TLDR

**登录**Azure

```az login```

**列出**资源组

```az group list```

**创建**资源组

```az group create --name [MyResourceGroup] --location [eastus]```

**列出**虚拟机

```az vm list```

**获取**账户信息

```az account show```

使用**指定的订阅**

```az account set --subscription [subscription-id]```

# SYNOPSIS

**az** [_group_] [_subgroup_] [_command_] [_options_]

# DESCRIPTION

**az** 是 Microsoft Azure 的统一命令行界面。它通过一致的跨平台接口提供对各类 Azure 服务的访问，包括虚拟机、存储、数据库、Kubernetes 以及数百种其他云资源。

借助该 CLI，无需使用 Web 门户即可实现 Azure 资源的自动化、脚本化和集中管理。

# PARAMETERS

**--output**, **-o** _format_
> 输出格式（json、jsonc、table、tsv、yaml、none）

**--query**
> 用于筛选输出的 JMESPath 查询

**--subscription** _id_
> 订阅名称或 ID

**--resource-group**, **-g** _name_
> 资源组名称

**--location**, **-l** _region_
> Azure 区域

**--verbose**
> 提高日志详细程度

**--debug**
> 启用调试日志

**--only-show-errors**
> 仅显示错误

# COMMON SERVICES

- **vm** - 虚拟机
- **storage** - 存储账户
- **aks** - Azure Kubernetes Service
- **webapp** - Web 应用
- **sql** - SQL 数据库
- **cosmosdb** - Cosmos DB
- **keyvault** - Key Vault
- **network** - 网络资源
- **group** - 资源组
- **account** - 账户管理

# CONFIGURATION

**~/.azure/config**
> INI 格式的配置文件，保存默认值和设置。包含 [core]、[defaults] 和 [cloud] 等节。可通过 `az config set` 管理。

```bash
# Set default output format
az config set core.output=table

# Set default location
az config set defaults.location=eastus
```

# CAVEATS

需要有效的 Azure 订阅，并且事先执行过 `az login`。某些操作具有破坏性且无法撤销。API 限流可能影响大规模批量脚本。新的 Azure 服务可能需要数周甚至数月才能获得功能对等的 CLI 支持。为了脚本可靠性，建议使用 **--query** 配合 JMESPath，而不是通过 shell 工具管道处理输出。

# HISTORY

**Azure CLI 2.0** 由微软于 **2017** 年发布，是对最初 Azure CLI 的完全重写，采用 Python 构建，注重易用性和跨平台支持。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[az-login](/man/az-login)(1), [az-account](/man/az-account)(1), [terraform](/man/terraform)(1)
