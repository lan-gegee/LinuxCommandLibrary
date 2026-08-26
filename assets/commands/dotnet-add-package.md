# TAGLINE

向项目添加或更新 NuGet 包引用

# TLDR

**添加 NuGet 包**

```dotnet add package [package_name]```

**添加指定版本**

```dotnet add package [package_name] --version [1.0.0]```

**向指定项目添加包**

```dotnet add [project.csproj] package [package_name]```

**添加预发布版本**

```dotnet add package [package_name] --prerelease```

**从指定源添加**

```dotnet add package [package_name] --source [https://api.nuget.org/v3/index.json]```

**添加面向特定框架的包**

```dotnet add package [package_name] --framework [net8.0]```

# SYNOPSIS

**dotnet** **add** [_project_] **package** _package_name_ [_options_]

# PARAMETERS

**-v**, **--version** _version_
> 要安装的特定版本。

**--prerelease**
> 允许安装预发布包。

**-f**, **--framework** _framework_
> 仅当面向特定框架时才添加包引用。

**-s**, **--source** _source_
> 还原期间使用的 NuGet 包源 URI。

**-n**, **--no-restore**
> 添加引用但不执行还原预览和兼容性检查。

**--package-directory** _dir_
> 包还原到的目录。

**--interactive**
> 允许命令停下等待用户输入或操作。

# DESCRIPTION

**dotnet add package** 向项目文件添加 NuGet 包引用并执行兼容性检查。它会修改 .csproj 或 .fsproj 文件以加入 PackageReference 元素，使依赖关系可以在版本控制中被跟踪。

如果该包已被引用，则将引用更新为最新的兼容版本。除非指定 **--no-restore**，否则该命令在添加引用后会隐式运行 **dotnet restore**。使用中央包管理（CPM）的项目将在 Directory.Packages.props 文件中更新 PackageVersion 元素。

# INSTALL

```dnf: sudo dnf install dotnet-host```

```pacman: sudo pacman -S dotnet-host```

```apk: sudo apk add dotnet-host```

```brew: brew install dotnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet-restore](/man/dotnet-restore)(1), [dotnet-build](/man/dotnet-build)(1), [dotnet](/man/dotnet)(1)
