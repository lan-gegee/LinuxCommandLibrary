# TAGLINE

conda 软件包管理器的微型静态链接重新实现

# TLDR

**创建环境**

```micromamba create -n [myenv] python=[3.11]```

**激活环境**

```micromamba activate [myenv]```

**安装软件包**

```micromamba install -n [myenv] [numpy] [pandas]```

**从 conda-forge 安装**

```micromamba install -c conda-forge [package]```

**列出环境**

```micromamba env list```

**列出环境中的软件包**

```micromamba list -n [myenv]```

**删除环境**

```micromamba env remove -n [myenv]```

**更新所有软件包**

```micromamba update --all```

# SYNOPSIS

**micromamba** _command_ [_-n env_] [_-c channel_] [_options_] [_packages_]

# PARAMETERS

**create**
> 创建新环境。

**activate** _ENV_
> 激活环境。

**deactivate**
> 停用当前环境。

**install** _PACKAGES_
> 安装软件包。

**remove** _PACKAGES_
> 删除软件包。

**update** _PACKAGES_
> 更新软件包。

**list**
> 列出已安装的软件包。

**env list**
> 列出环境。

**env remove**
> 删除环境。

**search** _PACKAGE_
> 搜索软件包。

**clean**
> 清理软件包缓存。

**-n** _NAME_, **--name** _NAME_
> 环境名称。

**-c** _CHANNEL_, **--channel** _CHANNEL_
> 软件包频道。

**-f** _FILE_, **--file** _FILE_
> 环境文件。

**-y**, **--yes**
> 不询问确认。

**--no-deps**
> 不安装依赖。

**-q**, **--quiet**
> 安静输出。

# DESCRIPTION

**micromamba** 是 conda 软件包管理器的微型静态链接重新实现。它提供与 mamba/conda 相同的功能，但是单个、快速、独立的二进制文件。

与 conda/mamba 不同，micromamba 无需基础环境或 Python 安装。它是纯 C++ 实现，可以从零开始引导构建整个 conda 环境。

软件包解析使用与 mamba 相同的 libsolv 库，提供快速的依赖求解。conda-forge 等频道提供对数千个软件包的访问。

环境管理与 conda 一致：创建隔离的环境、安装软件包并在它们之间切换。环境文件（YAML）支持可复现的环境创建。

该工具特别适用于希望占用空间最小的 CI/CD 流水线和容器。无需初始化或基础安装——下载即可运行。

Shell 集成支持 bash、zsh、fish 和 PowerShell。activate 命令会相应地修改 PATH 和环境变量。

# CAVEATS

部分 conda 功能未实现。没有图形界面。一些较旧的软件包可能存在兼容性问题。必须初始化 Shell 钩子。默认频道与 conda 不同（使用 conda-forge）。

# HISTORY

**micromamba** 由 QuantStack 的 **mamba 团队**开发，于 **2020 年**前后发布。它专为 conda 的体积和启动时间成为问题的场景而设计。该项目与 mamba 共享求解器，为受限环境带来类似 conda 的能力。

# INSTALL

```brew: brew install micromamba```

```nix: nix profile install nixpkgs#micromamba```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [mamba](/man/mamba)(1), [pip](/man/pip)(1), [pixi](/man/pixi)(1)
