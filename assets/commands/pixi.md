# TAGLINE

快速的跨平台 conda 软件包管理器

# TLDR

**初始化新项目**

```pixi init [project_name]```

**添加依赖**

```pixi add [numpy]```

**添加开发依赖**

```pixi add --dev [pytest]```

**运行任务**

```pixi run [test]```

**安装依赖**

```pixi install```

**激活 Shell**

```pixi shell```

**创建全局工具安装**

```pixi global install [ruff]```

**显示项目信息**

```pixi info```

**搜索软件包**

```pixi search [numpy]```

# SYNOPSIS

**pixi** _command_ [_options_] [_arguments_]

# PARAMETERS

**init** [_name_]
> 初始化新项目并创建 pixi.toml。

**add** _packages_
> 向项目添加依赖。

**remove** _packages_
> 移除依赖。

**install**
> 安装所有依赖。

**run** _task_
> 运行某个项目任务。

**shell**
> 激活环境 Shell。

**task** _subcommand_
> 管理项目任务。

**project** _subcommand_
> 管理项目配置。

**global** _subcommand_
> 管理全局工具安装。

**update**
> 更新依赖。

**list**
> 列出项目依赖。

**tree**
> 显示依赖树。

**info**
> 显示项目信息。

**search** _query_
> 在已配置的频道中搜索软件包。

**clean**
> 移除环境和缓存。

**--dev**, **-d**
> 操作开发依赖。

**--platform** _PLATFORM_
> 目标平台。

**--feature** _FEATURE_
> 目标特性（feature）。

**--manifest-path** _PATH_
> pixi.toml 的路径。

**--frozen**
> 使用现有锁文件且不更新。

**--locked**
> 要求锁文件必须是最新的。

# DESCRIPTION

**pixi** 是构建在 conda 生态之上的快速跨平台软件包管理器。它将 Python 和原生依赖统一管理，通过单一锁文件提供可复现的环境。

项目使用 pixi.toml 进行配置，类似于 Cargo.toml。来自 conda-forge、PyPI 和自定义频道的依赖可以混合使用。锁文件（pixi.lock）固定确切版本以保证可复现性。

多平台支持会为每个平台生成单独的锁文件，使同一个项目无需人工干预即可在 Linux、macOS 和 Windows 上工作。

在 pixi.toml 中定义的任务提供了类似 npm 的脚本能力。test、build、lint 等命令只需配置一次，之后用 pixi run 运行。任务依赖可以将命令串联起来。

全局安装（pixi global install）的工作方式类似 pipx，为 CLI 工具创建隔离的环境，使开发工具与项目依赖相互独立。

# CONFIGURATION

**pixi.toml**
> 项目配置文件，定义依赖、任务和频道。

**pixi.lock**
> 锁文件，按平台固定版本以实现可复现环境。

**~/.pixi/config.toml**
> 全局配置，包含默认频道、身份验证和缓存设置。

**PIXI_HOME**
> 覆盖默认的 Pixi 主目录。

# CAVEATS

较新的工具，生态仍在成长中。某些 conda 软件包可能无法完美运行。混合使用 PyPI 与 conda 依赖需谨慎。大型环境的求解耗时较长。平台特定的软件包需要正确的 feature 标志。

# HISTORY

**pixi** 由 **prefix.dev**（mamba 的开发者）创建并于 **2023 年**发布。它用 Rust 编写，旨在将 conda、pip 和 cargo 的优点融合到统一的工具中。它利用 rattler-build 的快速依赖求解器并与 conda 生态集成，同时加入了现代项目管理特性。

# INSTALL

```pacman: sudo pacman -S pixi```

```brew: brew install pixi```

```nix: nix profile install nixpkgs#pixi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [mamba](/man/mamba)(1), [poetry](/man/poetry)(1), [cargo](/man/cargo)(1), [pip](/man/pip)(1)
