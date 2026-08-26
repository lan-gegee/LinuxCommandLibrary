# TAGLINE

C/C++ 跨平台软件包管理器

# TLDR

**搜索软件包**

```vcpkg search [package_name]```

**安装软件包**

```vcpkg install [package_name]```

**为特定 triplet**（平台）**安装软件包**

```vcpkg install [package_name]:[triplet]```

**列出已安装的软件包**

```vcpkg list```

**移除软件包**

```vcpkg remove [package_name]```

**更新 vcpkg** 和软件包目录

```vcpkg update```

**与系统级 MSBuild/CMake 集成**

```vcpkg integrate install```

**显示软件包信息**

```vcpkg search [package_name] --x-full-desc```

# SYNOPSIS

**vcpkg** _command_ [_options_] [_package_...]

# PARAMETERS

**search** [_pattern_]
> 搜索匹配模式的软件包。

**install** _package_[_:triplet_]
> 安装软件包，可选指定目标 triplet。

**remove** _package_
> 移除已安装的软件包。

**list**
> 列出所有已安装的软件包。

**update**
> 更新 vcpkg 本身并刷新软件包目录。

**upgrade**
> 重新构建所有过期的软件包。

**integrate install**
> 启用与构建系统的系统级集成。

**integrate remove**
> 移除系统级集成。

**export** _package_ **--zip**|**--nuget**
> 将已安装的软件包导出为可移植格式。

**help** [_topic_]
> 显示特定命令或主题的帮助信息。

**--triplet** _triplet_
> 指定目标平台（例如 x64-linux、x86-windows、arm64-osx）。

**--disable-metrics**
> 禁用遥测数据收集。

# DESCRIPTION

**vcpkg** 是 Microsoft 推出的跨平台 C/C++ 软件包管理器，用于获取和管理库依赖。它提供数千个开源库，可在 Windows、macOS 和 Linux 上构建并集成到项目中。

与系统软件包管理器不同，vcpkg 允许同一库的多个版本共存，并通过 triplet 支持交叉编译。它与 CMake 和 MSBuild 无缝集成，自动配置头文件路径和链接库。

软件包使用 vcpkg 仓库中维护的精选构建脚本（portfile）从源码构建。这确保了跨平台构建的一致性，并允许自定义构建选项。该工具可以在经典模式下集中安装，也可以在清单模式下按项目管理依赖。

配置通过环境变量（VCPKG_ROOT、VCPKG_DEFAULT_TRIPLET）或命令行选项完成。

# CAVEATS

从源码构建软件包可能耗时较长，大型库尤其明显。某些软件包需要先安装系统依赖。二进制缓存可以加速重复构建，但需要额外配置。默认 triplet 因平台而异。

# HISTORY

**vcpkg** 由 **Microsoft** 开发，于 **2016 年 9 月**首次发布，旨在帮助 C++ 开发者管理 Windows 上的依赖。它最初专注于 Visual Studio 集成，后来扩展为支持 Linux 和 macOS 的跨平台工具。该项目以 MIT 许可证开源，托管在 GitHub 上并有活跃的社区贡献。

# INSTALL

```dnf: sudo dnf install vcpkg```

```pacman: sudo pacman -S vcpkg```

```brew: brew install vcpkg```

```nix: nix profile install nixpkgs#vcpkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmake](/man/cmake)(1), [conan](/man/conan)(1), [apt](/man/apt)(8), [brew](/man/brew)(1)
