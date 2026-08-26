# TAGLINE

管理 Azure 资源提供程序

# TLDR

**列出所有资源提供程序**

```az provider list```

仅**列出已注册的提供程序**

```az provider list --query "[?registrationState=='Registered']"```

**显示**特定提供程序的**详情**

```az provider show --namespace [Microsoft.Compute]```

**注册资源提供程序**并等待完成

```az provider register --namespace [Microsoft.ContainerService] --wait```

**取消注册资源提供程序**

```az provider unregister --namespace [Microsoft.ContainerService]```

**显示**特定提供程序的**操作**

```az provider operation show --namespace [Microsoft.Compute]```

# SYNOPSIS

**az** **provider** _subcommand_ [_options_]

# SUBCOMMANDS

**list**
> 列出订阅的资源提供程序。

**show**
> 获取某个资源提供程序的详情。

**register**
> 注册资源提供程序。

**unregister**
> 取消注册资源提供程序。

**operation list**
> 获取所有提供程序的操作。

**operation show**
> 获取单个提供程序的操作。

**permission list**
> 列出某个提供程序的权限。

# PARAMETERS

**--namespace** **-n**
> 资源提供程序命名空间（例如 Microsoft.Compute）。

**--wait**
> 等待注册完成。默认：false。

**--management-group-id** **-m**
> 用于注册提供程序的管理组 ID。

**--consent-to-permissions** **-c**
> 指示是否同意授权（register 使用）。默认：false。

**--accept-terms**
> 注册 RPaaS（Resource Provider as a Service）提供程序时接受条款。

**--expand**
> 要包含在 list/show 结果中的属性，例如 resourceTypes/aliases。

# DESCRIPTION

**az provider** 管理 Azure 资源提供程序。资源提供程序是提供 Azure 资源（虚拟机、存储账户、数据库等）的服务。在使用某种资源类型之前，必须在你的订阅中注册相应的提供程序。

常见提供程序包括 Microsoft.Compute（虚拟机）、Microsoft.Storage（存储账户）、Microsoft.Network（网络）和 Microsoft.ContainerService（AKS）。

# CAVEATS

需要安装 Azure CLI 并已完成身份验证。某些提供程序会在创建资源时自动注册。取消注册提供程序不会删除现有资源，但会阻止创建新资源。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-resource](/man/az-resource)(1), [az-lock](/man/az-lock)(1), [az-tag](/man/az-tag)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/provider)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
