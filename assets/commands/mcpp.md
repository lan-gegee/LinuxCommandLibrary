# TAGLINE

C++23 模块优先的构建工具与软件包管理器

# TLDR

**创建**新的模块化 C++ 项目

```mcpp new [project_name]```

**构建**当前目录中的项目

```mcpp build```

**构建并运行**默认目标

```mcpp run```

**运行测试**（自动发现 tests/ 下的测试）

```mcpp test```

从软件包索引**添加依赖**

```mcpp add [package]```

**安装捆绑的工具链**（如 GCC 16）

```mcpp toolchain install gcc 16```

**打包**发布 tarball（默认 vendored 模式）

```mcpp pack```

**诊断**本地环境

```mcpp self doctor```

# SYNOPSIS

**mcpp** [_global-options_] _command_ [_args_]

# DESCRIPTION

**mcpp** 是一个面向 C++23 模块优先开发的现代 C++ 构建工具。它创建、构建、测试和打包使用 `import std`、模块接口单元和模块分区的项目，具备自动模块依赖分析和文件级增量构建。

项目由 **mcpp.toml** 清单描述。按照约定，`src/main.cpp` 成为二进制目标，`tests/` 下的测试由 **mcpp test** 自动发现。首次构建会将感知宿主的默认工具链（依平台为 GCC 或 LLVM）下载到 **~/.mcpp/** 下的隔离沙箱中，因此不要求系统编译器。

依赖管理针对软件包索引解析 SemVer 约束（默认：mcpp-index / mcpplibs），写入锁文件，并可从索引、Git 或本地路径拉取模块。多包工作区共享同一个锁文件和目标目录。**mcpp pack** 生成可分发的产物（system、vendored、self-contained，或 Linux 上完全静态的 musl 构建）。

该工具尚处于早期阶段且是自举的（用纯 C++23 模块编写）。每个子命令的完整选项列表可通过 **mcpp** _command_ **--help** 查看。

# PARAMETERS

**new** _name_
> 脚手架生成模块化项目（可选 **--template** 使用库提供的模板）。

**build**
> 编译项目（增量构建；Ninja 后端）。

**run** [**--** _args_]
> 构建并运行默认目标。

**test** [_pattern_]
> 发现、构建并运行测试；按名称模式过滤。

**clean**
> 删除目标目录下的构建产物。

**add** / **remove** / **update**
> 管理 mcpp.toml 中声明的依赖。

**search**
> 搜索已配置的软件包索引。

**pack**
> 打包发布包（**--mode** system | vendored | self-contained | static）。

**publish**
> 将软件包发布到已配置的索引。

**toolchain** _install_|_list_|_default_ ...
> 安装、列出或选择沙箱化的编译器工具链。

**cache** / **index**
> 管理 BMI/构建缓存和软件包索引。

**self** _doctor_|_version_|_env_|_config_|_explain_ ...
> 环境检查与自我维护命令。

**why** [_toolchain_|_runtime_|_deps_]
> 解释已确定的构建决策。

**explain** _CODE_
> 打印错误代码的详细说明。

**--offline**
> 仅使用已有的本地状态（不下载、不刷新索引）。也可用 **MCPP_OFFLINE=1**。

**--version**
> 打印 mcpp 版本。

# CAVEATS

名称冲突：许多 Linux/Homebrew 发行版自带无关的 **mcpp** C 预处理器。此构建工具的软件包名称通常是 **mcpp-m** / **mcpp-bin**（AUR）或 Homebrew tap 配方 **mcpp-m**，而安装后的命令仍为 **mcpp**。如果 **which mcpp** 指向预处理器，请优先采用项目 README 中的安装方式。

早期阶段软件：接口和行为可能随版本更迭而变化。首次构建可能耗时较长，因为工具链要下载到 **~/.mcpp/**。

# CONFIGURATION

项目清单：**mcpp.toml**（软件包元数据、依赖、工具链、工作区）。

锁文件：**mcpp.lock**。

用户数据和沙箱化工具链：**~/.mcpp/**（注册表、缓存、安装布局）。

# HISTORY

mcpp 是 mcpp-community 下的社区项目，专注于原生 C++23 模块和自举。它构建于 xlings 工具链/软件包基础之上，并受 Cargo、xmake 和 Ninja 等工具启发。

# INSTALL

```aur: yay -S mcpp-bin```

```brew: brew install mcpp-community/mcpp/mcpp-m```

<!-- packages: 2026-08-08 -->

# SEE ALSO

[xmake](/man/xmake)(1), [cargo](/man/cargo)(1), [ninja](/man/ninja)(1), [cmake](/man/cmake)(1), [meson](/man/meson)(1)

# RESOURCES

```[Source code](https://github.com/mcpp-community/mcpp)```

```[Documentation](https://github.com/mcpp-community/mcpp/tree/main/docs)```

<!-- verified: 2026-08-08 -->
