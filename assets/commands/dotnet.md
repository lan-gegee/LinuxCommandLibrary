# TAGLINE

跨平台 .NET 开发 CLI

# TLDR

**创建新项目**

```dotnet new [console] -n [MyApp]```

**构建项目**

```dotnet build```

**运行项目**

```dotnet run```

**运行测试**

```dotnet test```

**添加 NuGet 包**

```dotnet add package [PackageName]```

**还原依赖项**

```dotnet restore```

**发布以供部署**

```dotnet publish -c Release```

**列出已安装的 SDK**

```dotnet --list-sdks```

# SYNOPSIS

**dotnet** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作类型：new、build、run、test、publish、add、restore 等。

**new** _TEMPLATE_
> 从模板创建项目。

**build**
> 构建项目。

**run**
> 构建并运行项目。

**test**
> 运行单元测试。

**publish**
> 发布以供部署。

**add package** _NAME_
> 添加 NuGet 包引用。

**restore**
> 还原 NuGet 包。

**-c** _CONFIG_
> 构建配置（Debug、Release）。

**--help**
> 显示帮助信息。

# CONFIGURATION

**global.json**
> 在解决方案级别指定 SDK 版本和项目设置。

**nuget.config**
> 配置 NuGet 包源和凭据。

# DESCRIPTION

**dotnet** 是 .NET 的命令行界面，用于创建、构建、运行和发布 .NET 应用程序。它支持 C#、F# 和 Visual Basic，覆盖控制台应用、Web API、类库等多种形态。

该 CLI 覆盖从项目创建到部署的完整开发工作流。它管理 NuGet 包、运行测试并生成部署工件。各种模板为不同类型的应用提供了起点。

dotnet 可在 Windows、macOS 和 Linux 上跨平台运行，让 .NET 开发无处不在。

# CAVEATS

需要已安装 .NET SDK。多个 SDK 版本可以共存。大型项目的构建可能较慢。某些功能需要特定的 SDK 版本。

# HISTORY

dotnet CLI 随 **.NET Core** 于 **2016 年**推出，是微软跨平台的 .NET 实现。它把碎片化的 .NET 工具链统一到一个 CLI 之下，成为 .NET 开发的标准方式。

# INSTALL

```dnf: sudo dnf install dotnet-host```

```pacman: sudo pacman -S dotnet-host```

```apk: sudo apk add dotnet-host```

```brew: brew install dotnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msbuild](/man/msbuild)(1)
