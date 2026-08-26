# TAGLINE

Microsoft 构建引擎

# TLDR

**构建解决方案**

```msbuild [solution.sln]```

**以特定配置构建**

```msbuild [project.csproj] /p:Configuration=[Release]```

**构建特定目标**

```msbuild /t:[Clean]```

**还原并构建**

```msbuild /t:Restore;Build```

**设置详细程度**

```msbuild /v:[detailed]```

**并行构建**

```msbuild /m:[4]```

**构建到输出目录**

```msbuild /p:OutputPath=[bin/output]```

# SYNOPSIS

**msbuild** [_options_] [_project_file_]

# PARAMETERS

_PROJECT_FILE_
> 解决方案或项目文件。

**/t:** _TARGET_
> 要构建的目标。

**/p:** _PROPERTY=VALUE_
> 设置属性值。

**/v:** _LEVEL_
> 详细程度级别。

**/m** [_N_]
> 最大并行构建数。

**/restore**
> 在构建前先运行还原。

**/?**
> 显示帮助信息。

# DESCRIPTION

**msbuild** 是 Microsoft 构建引擎（Build Engine）。它用于构建 .NET 应用程序和解决方案。

该工具处理项目文件，支持并行构建和自定义目标。

# CAVEATS

需要 .NET SDK。以 Windows 为中心但可跨平台。项目文件基于 XML。

# HISTORY

MSBuild 由 **Microsoft** 创建，作为 .NET 的构建平台，最早随 Visual Studio 2005 发布。

# INSTALL

```nix: nix profile install nixpkgs#msbuild```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [make](/man/make)(1)
