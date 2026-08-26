# TAGLINE

基于 C# 的跨平台构建自动化工具

# TLDR

**运行默认构建脚本**

```dotnet cake```

**运行指定构建脚本**

```dotnet cake [build.cake]```

**运行指定目标**

```dotnet cake --target=[Clean]```

**以详细输出运行**

```dotnet cake --verbosity=[diagnostic]```

**显示可用任务**

```dotnet cake --showdescription```

**试运行而不实际执行**

```dotnet cake --dryrun```

**带自定义参数运行**

```dotnet cake --configuration=[Release]```

# SYNOPSIS

**dotnet cake** [_script_] [_options_]

# DESCRIPTION

**Cake**（C# Make）是一个使用 C# DSL 的跨平台构建自动化系统。它可以编译代码、复制文件、运行测试、压缩文件以及构建 NuGet 软件包。脚本用 C# 编写，通过 Roslyn 执行。

# PARAMETERS

**--target**=_name_
> 要运行的目标任务

**--verbosity**=_level_
> 输出详细程度（quiet、minimal、normal、verbose、diagnostic）

**--dryrun**
> 只显示任务而不执行

**--showdescription**
> 显示任务描述

**--showtree**
> 显示任务依赖树

**--configuration**=_config_
> 构建配置（Debug、Release）

**--exclusive**
> 只执行目标任务，不含依赖任务

**--version**
> 显示版本

**--help**
> 显示帮助

# INSTALLATION

```
dotnet new tool-manifest
dotnet tool install Cake.Tool
```

# CAVEATS

需要已安装 .NET SDK。按惯例会执行当前目录下的 build.cake。通过插件（addin）支持 MSBuild、.NET CLI、NuGet 等众多工具。

# INSTALL

```brew: brew install cake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [msbuild](/man/msbuild)(1), [make](/man/make)(1)
