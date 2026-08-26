# TAGLINE

.NET 项目编译构建工具

# TLDR

**构建当前项目**

```dotnet build```

**以 Release** 配置构建

```dotnet build -c Release```

**构建指定项目**

```dotnet build [path/to/project.csproj]```

**不还原直接构建**

```dotnet build --no-restore```

**面向指定框架**构建

```dotnet build -f [net8.0]```

**输出到指定目录**构建

```dotnet build -o [./output]```

# SYNOPSIS

**dotnet build** [_project_] [_options_]

# PARAMETERS

_PROJECT_
> 要构建的项目或解决方案文件。

**-c**, **--configuration** _CONFIG_
> 构建配置（Debug、Release）。

**-f**, **--framework** _FRAMEWORK_
> 目标框架。

**-o**, **--output** _DIR_
> 输出目录。

**--no-restore**
> 构建时不还原依赖项。

**--no-dependencies**
> 忽略项目到项目的引用。

**-v**, **--verbosity** _LEVEL_
> 详细程度：quiet、minimal、normal、detailed。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dotnet build** 编译 .NET 项目及其依赖项，生成程序集和其他输出文件。它在底层调用 MSBuild 并应用 .NET 特有的配置。

除非指定 --no-restore，否则该命令会在构建前自动还原 NuGet 包。它支持构建解决方案文件中的多个项目，并能处理项目引用。

输出包括编译后的程序集（.dll）、调试符号以及项目中配置的所有内容文件。

# CAVEATS

增量构建可能遗漏某些更改；如有需要可在重新构建前使用 **dotnet clean**。多目标框架要求在项目文件中列出框架。默认配置是 Debug，除非指定 **-c Release**。

# HISTORY

dotnet build 是随 .NET Core 推出的 **.NET CLI** 的一部分。它提供了跨平台的构建体验，取代了各平台专属的构建工具。

# INSTALL

```dnf: sudo dnf install dotnet-host```

```pacman: sudo pacman -S dotnet-host```

```apk: sudo apk add dotnet-host```

```brew: brew install dotnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [dotnet-publish](/man/dotnet-publish)(1)
