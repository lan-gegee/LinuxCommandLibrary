# TAGLINE

.NET 项目测试运行器

# TLDR

**运行测试**

```dotnet test```

**运行指定项目中的测试**

```dotnet test [tests/Tests.csproj]```

**按过滤器运行**

```dotnet test --filter "[FullyQualifiedName~UnitTests]"```

**运行特定测试**

```dotnet test --filter "Name=[TestMethodName]"```

**指定详细程度运行**

```dotnet test --verbosity [detailed]```

**跳过构建运行**

```dotnet test --no-build```

**生成覆盖率报告**

```dotnet test --collect:"XPlat Code Coverage"```

# SYNOPSIS

**dotnet** **test** [_project_] [_options_]

# PARAMETERS

**--filter** _expression_
> 按表达式过滤测试。

**--no-build**
> 测试前不构建。

**--no-restore**
> 测试前不还原。

**-c**, **--configuration** _CONFIG_
> 构建配置（如 Debug、Release）。

**-v**, **--verbosity** _level_
> 详细程度（quiet、minimal、normal、detailed、diagnostic）。

**--logger** _logger_
> 测试日志记录器。

**--collect** _data_
> 启用数据收集器。

**--blame**
> 以 blame 模式运行测试。

**-r**, **--results-directory** _dir_
> 结果目录。

# DESCRIPTION

**dotnet test** 使用配置好的测试框架适配器执行 .NET 项目中的单元测试。通过相应的 NuGet 包，它支持 MSTest、NUnit 和 xUnit 等主流测试框架。

该命令通过框架特有的特性发现测试方法并逐一执行，报告结果包括通过/失败状态、执行时间和详细的失败信息。它通过各种日志记录器和输出格式与代码覆盖率工具及 CI/CD 流水线集成。

# INSTALL

```dnf: sudo dnf install dotnet-host```

```pacman: sudo pacman -S dotnet-host```

```apk: sudo apk add dotnet-host```

```brew: brew install dotnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [dotnet-build](/man/dotnet-build)(1), [dotnet-run](/man/dotnet-run)(1)
