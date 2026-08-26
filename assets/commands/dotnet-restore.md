# TAGLINE

还原 .NET 项目的 NuGet 包依赖

# TLDR

**还原**当前目录中项目的依赖

```dotnet restore```

**还原指定的项目**

```dotnet restore [project.csproj]```

**从指定的 NuGet 源还原**

```dotnet restore --source [https://api.nuget.org/v3/index.json]```

**不使用 HTTP 缓存还原**

```dotnet restore --no-cache```

**面向特定运行时还原**（RID）

```dotnet restore --runtime [linux-x64]```

**以锁定模式还原**（任何包版本漂移都会失败）

```dotnet restore --locked-mode```

**以详细日志还原**

```dotnet restore --verbosity detailed```

# SYNOPSIS

**dotnet** **restore** [_project_|_solution_] [_options_]

# PARAMETERS

**-s**, **--source** _SOURCE_
> 还原期间使用的 NuGet 包源（覆盖 nuget.config）。

**--packages** _DIR_
> 安装还原包的目录（默认：~/.nuget/packages）。

**--no-cache**
> 不缓存 HTTP 请求，总是从源重新获取。

**--no-dependencies**
> 只还原根项目，忽略项目到项目的引用。

**--force**
> 即使存在缓存的锁文件也强制重新解析所有依赖。

**--locked-mode**
> 不允许更新 **packages.lock.json** —— 若会导致变化则失败。

**--use-lock-file**
> 生成或更新 **packages.lock.json**。

**--runtime** _RID_
> 面向特定的运行时标识符（如 **linux-x64**、**win-x86**）。

**--configfile** _FILE_
> 使用指定的 NuGet 配置文件替代默认链。

**--disable-parallel**
> 禁用并行下载。

**-v**, **--verbosity** _LEVEL_
> 详细程度：q[uiet]、m[inimal]、n[ormal]、d[etailed]、diag[nostic]。

**-?**, **-h**, **--help**
> 显示帮助。

# DESCRIPTION

**dotnet restore** 下载并安装项目、解决方案或 **dotnet-tools.json** 中声明的所有 NuGet 包依赖。它读取 .csproj/.fsproj/.vbproj 文件中的 **PackageReference** 条目，查询配置好的 NuGet 源，并把还原后的资产写入 **obj/project.assets.json**。

**dotnet build** 和 **dotnet run** 等其他命令默认都会触发隐式还原，因此显式调用主要用于 CI 流水线（希望缓存还原步骤）、排查包解析问题时，或在下游命令使用 **--no-restore** 的场景。

# CAVEATS

还原遵循标准的 NuGet 配置链：机器级、用户级和目录级 **NuGet.config** 文件。**--source** 是替换（而非追加）已配置的源。在没有现成 **packages.lock.json** 的情况下设置 **--locked-mode** 会立即失败。

# INSTALL

```dnf: sudo dnf install dotnet-host```

```pacman: sudo pacman -S dotnet-host```

```apk: sudo apk add dotnet-host```

```brew: brew install dotnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet-build](/man/dotnet-build)(1), [dotnet-add-package](/man/dotnet-add-package)(1), [dotnet](/man/dotnet)(1)
