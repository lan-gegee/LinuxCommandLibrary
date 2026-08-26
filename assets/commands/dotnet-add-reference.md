# TAGLINE

项目到项目引用的添加工具

# TLDR

**添加项目引用**

```dotnet add reference [../Other/Other.csproj]```

**添加多个引用**

```dotnet add reference [../Lib1/Lib1.csproj] [../Lib2/Lib2.csproj]```

**向指定项目添加引用**

```dotnet add [src/App/App.csproj] reference [../Lib/Lib.csproj]```

# SYNOPSIS

**dotnet** **add** [_project_] **reference** _project_path_... [_options_]

# PARAMETERS

**-f**, **--framework** _framework_
> 仅为特定的目标框架添加引用。

**--interactive**
> 允许命令提示输入。

# DESCRIPTION

**dotnet add reference** 向项目文件添加项目到项目（P2P）引用，在解决方案中的项目之间建立构建期依赖。被引用的项目会在引用它的项目之前自动构建，以确保正确的构建顺序。

P2P 引用在解决方案内实现代码共享，同时保持清晰的依赖边界。该命令修改 `.csproj`（或 `.fsproj`、`.vbproj`）文件，添加带有指向被引用项目的相对路径的 `<ProjectReference>` 元素。

# CAVEATS

不允许循环引用，否则会产生错误。被引用的项目必须存在。可用 `dotnet list reference` 验证已有的引用。

# INSTALL

```dnf: sudo dnf install dotnet-host```

```pacman: sudo pacman -S dotnet-host```

```apk: sudo apk add dotnet-host```

```brew: brew install dotnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dotnet](/man/dotnet)(1), [dotnet-build](/man/dotnet-build)(1), [dotnet-add-package](/man/dotnet-add-package)(1)
