# TAGLINE

管理 Azure DevOps 组织和项目

# TLDR

**配置默认组织**和项目

```az devops configure --defaults organization=[https://dev.azure.com/contoso] project=[ContosoWebApp]```

**列出组织中的团队项目**

```az devops project list```

**显示**某个项目的**详情**

```az devops project show --project [MyProject]```

**创建新项目**

```az devops project create --name [MyProject] --org [https://dev.azure.com/contoso]```

**删除项目**

```az devops project delete --id [project-id] --yes```

在 Web 浏览器中**打开项目**

```az devops project show --project [MyProject] --open```

使用个人访问令牌**登录 Azure DevOps**

```az devops login --organization [https://dev.azure.com/contoso]```

**登出 Azure DevOps**

```az devops logout```

直接**调用 DevOps REST API** 终结点

```az devops invoke --area core --resource projects --api-version 6.0```

# SYNOPSIS

**az** **devops** _subcommand_ [_options_]

# SUBCOMMANDS

**configure**
> 配置 Azure DevOps CLI 或查看配置。

**project list**
> 列出团队项目。

**project show**
> 显示项目详情。

**project create**
> 创建团队项目。

**project delete**
> 删除团队项目。

**admin**
> 管理管理操作。

**extension**
> 管理扩展。

**security**
> 管理与安全相关的操作。

**service-endpoint**
> 管理服务终结点/连接。

**team**
> 管理团队。

**user**
> 管理用户。

**wiki**
> 管理 Wiki。

**login**
> 为特定组织设置凭证。

**logout**
> 清除特定组织的凭证。

**invoke**
> 对任意 DevOps REST API 发起请求。

# DESCRIPTION

**az devops** 管理 Azure DevOps 组织级别的操作。它提供 CLI 方式来管理 Azure DevOps Services 中的项目、团队、用户、安全和扩展。

相关命令组包括用于 CI/CD 管道的 **az pipelines**、管理工作项的 **az boards**、管理 Git 仓库的 **az repos**，以及管理包源的 **az artifacts**。

# CAVEATS

需要先用 **az extension add --name azure-devops** 安装 Azure DevOps CLI 扩展。仅适用于 Azure DevOps Services（云），不适用于 Azure DevOps Server（本地部署）。需要 Azure CLI v2.0.69 或更高版本。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-pipelines](/man/az-pipelines)(1), [az-repos](/man/az-repos)(1)
