# TAGLINE

D 语言软件包管理器与构建工具

# TLDR

**构建项目**

```dub build```

**运行项目**

```dub run```

**初始化新项目**

```dub init [name]```

**添加依赖**

```dub add [package]```

**更新依赖**

```dub upgrade```

**运行测试**

```dub test```

**构建文档**

```dub build --build=docs```

**仅获取依赖**

```dub fetch [package]```

# SYNOPSIS

**dub** _command_ [_options_]

# SUBCOMMANDS

**build**
> 构建项目。

**run**
> 构建并运行。

**test**
> 运行单元测试。

**init**
> 初始化新项目。

**add**
> 添加依赖。

**remove**
> 移除依赖。

**upgrade**
> 升级依赖。

**fetch**
> 获取软件包。

**clean**
> 清理构建产物。

**describe**
> 显示项目描述。

**search**
> 搜索软件包注册表。

**list**
> 列出已安装的软件包。

# COMMON OPTIONS

**--build=**_TYPE_
> 构建类型：debug、release、release-debug、unittest、profile、docs。

**--compiler=**_NAME_
> 使用指定的编译器（dmd、ldc2、gdc）。

**--arch=**_ARCH_
> 强制使用指定的目标架构（如 x86_64）。

**--config=**_NAME_
> 使用 dub.json 中指定的构建配置。

**-v**, **--verbose**
> 输出详细日志。

# CONFIGURATION

**dub.json** 或 **dub.sdl**
> 项目配置文件，定义依赖、构建设置和元数据。

**~/.dub/settings.json**
> 用户级 DUB 设置，包括自定义注册表 URL 和默认路径。

# DESCRIPTION

**dub** 是 D 编程语言官方的软件包管理器和构建工具。它负责依赖管理、项目编译、测试和分发，为 D 开发者提供完整的项目生命周期管理方案。

该工具使用 JSON 或 SDL（Simple Declarative Language）格式的配置文件（dub.json 或 dub.sdl）描述项目结构、依赖、构建配置和元数据。依赖会自动从 DUB 注册表（code.dlang.org）获取并缓存到本地。

dub 支持多种构建配置（debug、release、unittest），允许开发者为不同场景定义不同的编译器标志和依赖。它可以为 IDE 生成项目文件，并自动与 D 编译器（dmd、ldc、gdc）集成。

整个软件包生态围绕语义化版本控制运转，dub 负责解析依赖树并选择兼容的版本。项目可以为依赖指定确切版本、版本范围或分支引用。upgrade 命令会在遵守版本约束的前提下更新依赖。

# INSTALL

```apt: sudo apt install dub```

```dnf: sudo dnf install dub```

```pacman: sudo pacman -S dub```

```apk: sudo apk add dub```

```zypper: sudo zypper install dub```

```brew: brew install dub```

```nix: nix profile install nixpkgs#dub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmd](/man/dmd)(1), [ldc](/man/ldc)(1)
