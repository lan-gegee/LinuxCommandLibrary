# TAGLINE

管理 Azure App Service Web 应用

# TLDR

**创建**Web 应用

```az webapp create --resource-group [MyRG] --plan [MyPlan] --name [MyApp]```

**列出**Web 应用

```az webapp list```

**部署**制品（zip、war、jar、静态文件）

```az webapp deploy --name [MyApp] --resource-group [MyRG] --src-path [app.zip]```

**启用**本地 git 部署

```az webapp deployment source config-local-git --name [MyApp] --resource-group [MyRG]```

**在浏览器中打开**Web 应用

```az webapp browse --name [MyApp] --resource-group [MyRG]```

**列出**可用的运行时堆栈

```az webapp list-runtimes --os-type [linux]```

**查看**日志

```az webapp log tail --name [MyApp] --resource-group [MyRG]```

**重启**Web 应用

```az webapp restart --name [MyApp] --resource-group [MyRG]```

# SYNOPSIS

**az webapp** _command_ [_options_]

# DESCRIPTION

**az webapp** 管理 Azure App Service Web 应用。它提供用于创建、部署、配置和监控 Web 应用的命令，支持多种平台，包括 .NET、Node.js、Python、PHP 和 Java。

该命令组让你无需使用门户即可完成 Web 应用的全生命周期管理。

# PARAMETERS

**create**
> 创建 Web 应用

**list**
> 列出 Web 应用

**delete**
> 删除 Web 应用

**restart**
> 重启 Web 应用

**stop**
> 停止 Web 应用

**start**
> 启动 Web 应用

**show**
> 显示 Web 应用详情

**browse**
> 在浏览器中打开 Web 应用

**deploy**
> 向应用部署制品（zip、war、jar、静态文件）

**ssh**
> 打开到 Linux Web 应用的交互式 SSH 会话

**list-runtimes**
> 列出受支持的运行时堆栈

**up**
> 从当前本地目录创建并部署（已弃用；建议改用 create + deploy）

**--resource-group**, **-g** _name_
> 资源组名称

**--name**, **-n** _name_
> Web 应用名称（全局唯一）

**--plan**, **-p** _name_
> App Service 计划名称或资源 ID

**--runtime**, **-r** _stack_
> 运行时堆栈（例如 "NODE:20LTS"、"PYTHON:3.12"、"JAVA:21-java21"）。运行 `az webapp list-runtimes` 查看当前可用值。

**--deployment-container-image-name**, **-i** _image_
> 要部署的容器镜像（例如 myregistry.azurecr.io/image:tag）

# COMMON OPERATIONS

```bash
# Create Python web app
az webapp create -g MyRG -p MyPlan -n MyApp --runtime "PYTHON:3.12"

# Deploy from a zip artifact
az webapp deploy -g MyRG -n MyApp --src-path app.zip --type zip

# Set environment variables
az webapp config appsettings set -g MyRG -n MyApp --settings KEY=VALUE

# Enable logging
az webapp log config -g MyRG -n MyApp --application-logging filesystem --level information

# Stream logs
az webapp log tail -g MyRG -n MyApp
```

# CAVEATS

Web 应用名称必须全局唯一（会用于 azurewebsites.net URL）。新应用默认禁用基本（SCM/发布配置文件）身份验证；如果你的部署工具需要，可以用 `--basic-auth Enabled` 或 `az webapp auth` 启用。部署槽位需要标准（Standard）层或更高。某些运行时并非在所有区域都可用。费用因 App Service 计划层级而异。`az webapp up` 已弃用；建议先用 `az webapp create` 再用 `az webapp deploy`。

# HISTORY

**az webapp** 自 **2017** 年的 Azure CLI 2.0 版本起就是其组成部分，取代了旧版 Azure CLI 中管理 App Service Web 应用的功能。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [azure-cli](/man/azure-cli)(1), [az-functionapp](/man/az-functionapp)(1), [az-appservice](/man/az-appservice)(1)

# RESOURCES

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/webapp)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

```[Source code](https://github.com/Azure/azure-cli)```

<!-- verified: 2026-06-19 -->
