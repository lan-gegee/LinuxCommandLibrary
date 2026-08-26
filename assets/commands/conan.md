# TAGLINE

适用于所有平台的 C/C++ 软件包管理器

# TLDR

**根据 conanfile 安装依赖**

```conan install [.]```

**使用指定 profile 安装**

```conan install [.] --profile=[release]```

**根据配方创建软件包**

```conan create [.]```

**搜索软件包**

```conan search "[boost/*]"```

**列出已安装的软件包**

```conan list "*"```

**添加远程仓库**

```conan remote add [name] [url]```

**上传软件包到远程仓库**

```conan upload [package/version] -r [remote]```

**显示软件包信息**

```conan inspect [package/version]```

# SYNOPSIS

**conan** _command_ [_options_] [_arguments_]

# DESCRIPTION

**conan** 是一款专为 C 和 C++ 项目设计的现代去中心化软件包管理器，旨在解决这两种语言历史上碎片化的依赖管理局面。与假定单一构建系统的语言专用包管理器不同，Conan 能与 CMake、MSBuild、Meson、Autotools 以及自定义构建系统集成，真正实现跨 Windows、Linux、macOS 和嵌入式系统的跨平台支持。

该工具基于二进制软件包模型：软件包可以针对特定配置（编译器、操作系统、架构、构建类型）预编译并缓存复用，相比纯源码方式能显著加快构建速度。Conan 的 profile 定义这些构建配置，包管理器会执行复杂的依赖解析，在整个依赖图上考虑二进制兼容性。

Conan 采用类似 Git 的去中心化仓库模型：团队可以托管私有的 Conan 服务器（Artifactory、ConanCenter），同时仍可访问公共的 ConanCenter 仓库。软件包配方（conanfile.py）用 Python 编写，为复杂构建场景提供了完全的可编程性。Conan 2.x 是一次重大演进，改进了版本管理、更好地集成了 CMake，并提供了更简洁的 CLI，但相对 1.x 系列引入了破坏性变更。

# COMMANDS

**install**
> 根据 conanfile 安装依赖

**create**
> 根据配方构建并创建软件包

**build**
> 在本地构建软件包

**search**
> 搜索软件包

**list**
> 列出缓存中的软件包

**remote**
> 管理远程仓库

**upload**
> 将软件包上传到远程仓库

**download**
> 下载软件包

**export**
> 将配方导出到缓存

**profile**
> 管理构建 profile

**config**
> 管理 Conan 配置

**new**
> 创建新的软件包模板

# PARAMETERS

**-pr**, **--profile** _name_
> 要使用的构建 profile

**-r**, **--remote** _name_
> 远程仓库

**-of**, **--output-folder** _path_
> 输出文件夹

**-b**, **--build** _policy_
> 构建策略（missing、never、always）

**-s** _setting=value_
> 覆盖 setting

**-o** _option=value_
> 覆盖 option

# CONFIGURATION

**conanfile.txt**
> 用于声明依赖的简单文本格式。

**conanfile.py**
> 基于 Python 的软件包配方，可完全控制。

**~/.conan2/profiles/**
> 定义编译器、操作系统、架构设置的构建 profile。

**~/.conan2/global.conf**
> Conan 行为的全局配置。

# CAVEATS

当前主流为 Conan 2.x；Conan 1.x 已属遗留版本。二进制兼容性可配置。可与 CMake、MSBuild、Meson 及自定义构建系统集成。

# INSTALL

```dnf: sudo dnf install conan```

```zypper: sudo zypper install conan```

```brew: brew install conan```

```nix: nix profile install nixpkgs#conan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmake](/man/cmake)(1), [vcpkg](/man/vcpkg)(1)

# RESOURCES

```[Source code](https://github.com/conan-io/conan)```

```[Homepage](https://conan.io)```

```[Documentation](https://docs.conan.io)```

<!-- verified: 2026-06-22 -->
