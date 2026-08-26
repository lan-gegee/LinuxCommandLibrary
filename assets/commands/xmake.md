# TAGLINE

跨平台的基于 Lua 的构建系统

# TLDR

**创建新项目**

```xmake create [project_name]```

**构建项目**

```xmake```

**以指定模式构建**

```xmake -m [release]```

**运行目标**

```xmake run [target]```

**安装软件包**

```xmake require [package]```

**清理构建产物**

```xmake clean```

**配置项目**

```xmake config -p [linux] -a [x86_64]```

**生成 IDE 项目文件**

```xmake project -k [cmake]```

# SYNOPSIS

**xmake** [_build_] [_run_] [_clean_] [_require_] [_config_] [_options_] [_target_]

# PARAMETERS

**build**
> 构建项目（默认）。

**run** [_TARGET_]
> 运行目标。

**clean**
> 清理构建文件。

**config**
> 配置项目。

**require** _PKG_
> 安装软件包。

**create** _NAME_
> 创建项目。

**project** **-k** _KIND_
> 生成项目文件。

**-m** _MODE_
> 构建模式（debug、release）。

**-p** _PLATFORM_
> 目标平台。

**-a** _ARCH_
> 目标架构。

**-v**
> 详细输出。

**-j** _N_
> 并行任务数。

# DESCRIPTION

**xmake** 是一个跨平台构建系统。它使用 Lua 进行配置，在保持简单的同时提供了灵活性。

xmake.lua 中的构建配置定义目标、依赖项和编译器选项。其语法比 CMake 更易读。

软件包管理是集成的。只需声明依赖项，即可自动下载并构建。

跨平台支持覆盖 Windows、Linux、macOS 等。交叉编译和工具链管理均为内置功能。

项目生成可以为 CMake、Make、Ninja、Visual Studio 和 Xcode 创建项目文件，便于与其他工具集成。

远程编译可将构建分发到多台机器。缓存共享可加快团队的整体构建速度。

# CAVEATS

普及程度不及 CMake。软件包仓库比 vcpkg/conan 小。Lua 配置对某些人来说有学习曲线。

# HISTORY

**xmake** 由 **ruki** 于 **2015** 年前后在中国创建。它凭借集成的软件包管理和更简洁的语法，成为 CMake 的现代替代品。

# INSTALL

```apt: sudo apt install xmake```

```dnf: sudo dnf install xmake```

```pacman: sudo pacman -S xmake```

```apk: sudo apk add xmake```

```brew: brew install xmake```

```nix: nix profile install nixpkgs#xmake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmake](/man/cmake)(1), [make](/man/make)(1), [meson](/man/meson)(1), [ninja](/man/ninja)(1)
