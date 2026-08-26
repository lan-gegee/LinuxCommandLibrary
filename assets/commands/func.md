# TAGLINE

Azure Functions 开发 CLI

# TLDR

**创建新函数**

```func new```

**启动本地服务器**

```func start```

**部署到 Azure**

```func azure functionapp publish [appname]```

从模板**创建函数**

```func new --template "[HTTP trigger]" --name [MyFunction]```

**列出模板**

```func templates list```

# SYNOPSIS

**func** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：new、start、deploy、init 等。

**new**
> 创建新函数。

**start**
> 启动本地 Functions 主机。

**init**
> 初始化函数项目。

**azure functionapp publish** _NAME_
> 部署到 Azure。

**templates list**
> 显示可用模板。

**--help**
> 显示帮助信息。

# CONFIGURATION

**local.settings.json**
> 本地开发设置，包括运行时、连接和应用设置。

**host.json**
> 函数应用中所有函数的全局配置。

# DESCRIPTION

**func** 是 Azure Functions Core Tools 的 CLI，用于在本地开发无服务器函数。它可以创建、运行和部署多种语言的 Azure Functions。

该工具提供支持调试的本地开发环境，模拟 Azure 环境。它负责项目脚手架、依赖管理和部署工作流。

func 支持 JavaScript、Python、C#、Java 等语言的 Azure Functions 开发。

# CAVEATS

部署需要 Azure 账户。本地模拟器存在局限。语言支持因版本而异。

# HISTORY

func 是 Microsoft **Azure Functions Core Tools** 的一部分，为 Azure 平台提供无服务器函数的本地开发能力。

# INSTALL

```nix: nix profile install nixpkgs#func```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[az](/man/az)(1), [dotnet](/man/dotnet)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-functions-core-tools)```

<!-- verified: 2026-07-15 -->
