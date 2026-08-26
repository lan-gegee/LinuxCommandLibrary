# TAGLINE

跨平台构建系统生成器

# TLDR

**在构建目录中生成构建文件**

```cmake -B [build]```

**构建项目**

```cmake --build [build]```

**以指定的构建类型构建**

```cmake -B [build] -DCMAKE_BUILD_TYPE=[Release]```

**使用 Ninja 生成器构建**

```cmake -B [build] -G Ninja```

**并行构建**

```cmake --build [build] -j [8]```

**安装项目**

```cmake --install [build]```

# SYNOPSIS

**cmake** [_options_] _source-dir_

# DESCRIPTION

**cmake** 是一个跨平台构建系统生成器。它读取与平台无关的 CMakeLists.txt 项目描述，并为用户选择的构建工具生成原生构建文件，包括 Unix Makefiles、Ninja、Visual Studio 解决方案和 Xcode 项目。

典型工作流程包括：先执行配置步骤，在源码外的构建目录中生成构建文件；随后执行构建步骤，调用原生构建工具。CMake 通过其 find-module 系统处理依赖检测、编译器特性检查和库发现。

CMake 是 C 和 C++ 项目的主流构建系统，同时也支持 Fortran、CUDA 等语言。它还包含用于测试自动化的 CTest 和用于创建可分发软件包的 CPack。

# PARAMETERS

**-B** _dir_
> 构建目录

**-S** _dir_
> 源码目录（默认：当前目录）

**-G** _generator_
> 构建系统生成器（Unix Makefiles、Ninja、Xcode）

**-D** _var_**=**_value_
> 设置 CMake 变量

**--build** _dir_
> 构建项目

**--install** _dir_
> 安装项目

**--preset** _name_
> 使用配置预设

**-j** _N_
> 并行构建任务数（传递给底层构建工具）。

**--target** _target_
> 构建指定目标而非默认目标。

**--verbose**
> 启用详细的构建输出。

**--clean-first**
> 构建前先清理。

**-DCMAKE_INSTALL_PREFIX=**_path_
> 设置安装前缀目录。

**-DCMAKE_CXX_COMPILER=**_compiler_
> 指定 C++ 编译器。

**-DCMAKE_BUILD_TYPE=**_type_
> 构建类型：Debug、Release、RelWithDebInfo 或 MinSizeRel。

# CAVEATS

高级功能的语法复杂。学习曲线陡峭。生成的文件可能很大。缓存问题需要清理才能解决。版本差异会导致兼容性问题。有人认为它对简单项目来说过于复杂。

# HISTORY

**CMake** 由 Bill Hoffman 和 Ken Martin 于 **2000 年**在 Kitware 创建，旨在解决跨平台构建的复杂性，到 **2010 年**已被广泛采用。

# INSTALL

```apt: sudo apt install cmake```

```dnf: sudo dnf install cmake```

```pacman: sudo pacman -S cmake```

```apk: sudo apk add cmake```

```zypper: sudo zypper install cmake```

```brew: brew install cmake```

```nix: nix profile install nixpkgs#cmake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [ninja](/man/ninja)(1), [meson](/man/meson)(1)
