# TAGLINE

查看和管理 Azure 最佳实践建议

# TLDR

**列出所有 Azure Advisor 建议**

```az advisor recommendation list```

针对特定类别**列出建议**

```az advisor recommendation list --category [Cost|Security|HighAvailability|Performance|OperationalExcellence]```

**显示订阅的 Advisor 配置**

```az advisor configuration show```

**列出整个订阅的配置**

```az advisor configuration list```

**禁用一条建议**

```az advisor recommendation disable --name [recommendation-name] --resource-group [rg-name]```

**启用之前被禁用的**建议

```az advisor recommendation enable --name [recommendation-name] --resource-group [rg-name]```

# SYNOPSIS

**az** **advisor** _subcommand_ [_options_]

# SUBCOMMANDS

**configuration list**
> 列出整个订阅的 Azure Advisor 配置。

**configuration show**
> 显示给定订阅或资源组的 Azure Advisor 配置。

**configuration update**
> 更新 Azure Advisor 配置。

**recommendation list**
> 列出 Azure Advisor 建议。

**recommendation disable**
> 忽略 Azure Advisor 建议。

**recommendation enable**
> 启用 Azure Advisor 建议。

# DESCRIPTION

**az advisor** 管理 Azure Advisor——一个个性化的云顾问，帮助你遵循最佳实践来优化 Azure 部署。Azure Advisor 会分析资源配置和使用遥测数据，然后推荐能提升成本效益、性能、可靠性和安全性的解决方案。

建议分为以下类别：Cost、Security、HighAvailability（可靠性）、Performance 和 OperationalExcellence。

# CAVEATS

需要安装 Azure CLI 并已通过 **az login** 完成身份验证。查看和管理 Advisor 建议需要相应的 Azure RBAC 权限。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-config](/man/az-config)(1), [az-feedback](/man/az-feedback)(1)
