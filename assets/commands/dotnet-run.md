# TAGLINE

构建并执行 .NET 项目

# TLDR

**运行当前项目**

```dotnet run```

**带参数运行**

```dotnet run -- [arg1] [arg2]```

**运行指定项目**

```dotnet run --project [path/to/project.csproj]```

**以 Release** 配置运行

```dotnet run -c Release```

**跳过构建直接运行**

```dotnet run --no-build```

**按指定框架运行**

```dotnet run -f [net8.0]```

# SYNOPSIS

**dotnet run** [_options_] [**--** _args_]

# PARAMETERS

**--project** _PATH_
> 要运行的项目。

**-c**, **--configuration** _CONFIG_
> 构建配置。

**-f**, **--framework** _FRAMEWORK_
> 目标框架。

**--no-build**
> 运行前不构建。

**--no-restore**
> 跳过包还原。

**--launch-profile** _NAME_
> 使用 launchSettings.json 中的启动配置文件。

**--no-launch-profile**
> 不使用任何启动配置文件。

**--arch** _ARCH_
> 目标体系结构（如 x86、x64、arm64）。

**--** _ARGS_
> 传递给应用程序的参数。

**--help**
> 显示帮助信息。

# CONFIGURATION

**Properties/launchSettings.json**
> 通过环境变量和应用程序参数配置启动配置文件。

# DESCRIPTION

**dotnet run** 一键完成 .NET 项目的构建和执行。它是开发期间运行应用程序的标准方式，不会创建部署工件。

双横线（--）用于分隔 dotnet 选项与传给应用程序的参数。launchSettings.json 中的启动配置文件可为开发场景配置环境变量和参数。

对于 web 应用程序，新版 dotnet run 会启动开发服务器并支持热重载。

# CAVEATS

执行时间中包含构建时间。追求更快的迭代请用 --no-build。启动配置文件只在项目目录内生效。不适合生产环境使用。

# HISTORY

dotnet run 是 **.NET CLI** 的一部分，提供精简的开发迭代方式。它把构建和执行合二为一，相比先编译后运行的分离工作流改善了开发者体验。

# INSTALL

```dnf: sudo dnf install dotnet-host```

```pacman: sudo pacman -S dotnet-host```

```apk: sudo apk add dotnet-host```

```brew: brew install dotnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [dotnet-build](/man/dotnet-build)(1), [dotnet-test](/man/dotnet-test)(1)
