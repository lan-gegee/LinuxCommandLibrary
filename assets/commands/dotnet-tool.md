# TAGLINE

.NET CLI 工具包管理器

# TLDR

**安装全局工具**

```dotnet tool install -g [tool-name]```

**列出全局工具**

```dotnet tool list -g```

**更新全局工具**

```dotnet tool update -g [tool-name]```

**卸载全局工具**

```dotnet tool uninstall -g [tool-name]```

**安装本地工具**

```dotnet tool install [tool-name]```

**还原本地工具**

```dotnet tool restore```

# SYNOPSIS

**dotnet tool** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作类型：install、list、update、uninstall、restore。

**install** _PACKAGE_
> 安装工具包。

**list**
> 列出已安装的工具。

**update** _PACKAGE_
> 将工具更新到最新版本。

**uninstall** _PACKAGE_
> 移除工具。

**restore**
> 从清单还原本地工具。

**-g**, **--global**
> 全局安装（用户范围）。

**--tool-path** _PATH_
> 自定义安装目录。

**--help**
> 显示帮助信息。

# CONFIGURATION

**dotnet-tools.json**
> 清单文件，声明项目所需的本地工具依赖及其版本。

# DESCRIPTION

**dotnet tool** 管理 .NET CLI 工具，这类工具是包含控制台应用程序的 NuGet 包。工具可以全局安装（用户范围）或本地安装（针对项目）。

全局工具可从任意目录调用，安装在用户专属的位置。本地工具在清单文件（dotnet-tools.json）中声明，按项目安装。

常用工具包括 dotnet-ef（Entity Framework）、dotnet-format（代码格式化），以及各种分析器和生成器。

# CAVEATS

全局工具可能出现版本冲突。本地工具需要还原清单。工具版本应与项目要求匹配。全局工具需要配置 PATH。

# HISTORY

dotnet tool 于 **.NET Core 2.1**（**2018 年**）推出，旨在通过 NuGet 分发的 CLI 工具提供扩展能力，推动生态在内置命令之外继续成长。

# INSTALL

```dnf: sudo dnf install dotnet-host```

```pacman: sudo pacman -S dotnet-host```

```apk: sudo apk add dotnet-host```

```brew: brew install dotnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [dotnet-ef](/man/dotnet-ef)(1)
