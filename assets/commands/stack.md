# TAGLINE

Haskell 构建工具与项目管理器

# TLDR

**创建新项目**

```stack new [project_name]```

**构建项目**

```stack build```

**运行项目可执行文件**

```stack run```

**运行测试**

```stack test```

**加载项目启动 REPL**

```stack ghci```

**全局安装软件包**

```stack install [package_name]```

**以脚本方式执行 Haskell 文件**

```stack script [script.hs]```

**更新软件包索引**

```stack update```

**显示项目路径**

```stack path```

# SYNOPSIS

**stack** _command_ [_--snapshot version_] [_options_] [_arguments_]

# PARAMETERS

**new** _NAME_ [_TEMPLATE_]
> 创建新项目。

**init**
> 在现有项目中初始化 stack。

**build**
> 构建项目。

**run**
> 构建并运行可执行文件。

**test**
> 构建并运行测试。

**bench**
> 构建并运行基准测试。

**ghci**
> 加载项目并启动 REPL。

**install** _PACKAGES_
> 构建并将可执行文件复制到 bin 目录。

**exec** _COMMAND_
> 在构建环境中运行命令。

**script** _FILE_
> 运行 Haskell 脚本。

**setup**
> 为项目下载并安装 GHC。

**path**
> 显示 stack 使用的路径。

**ls**
> 列出信息（快照、依赖等）。

**clean**
> 清理构建产物。

**purge**
> 删除 stack 的工作目录（clean --full）。

**upgrade**
> 升级 stack 本身。

**--snapshot** _SNAPSHOT_, **--resolver** _RESOLVER_
> Stackage 快照（例如 lts-22.0、nightly-2025-01-01）。

**--system-ghc**
> 使用系统 GHC 而不是 stack 管理的 GHC。

**--no-install-ghc**
> 不自动安装 GHC。

**--fast**
> 禁用优化以加快构建速度。

**--test**
> 启用测试构建。

**--bench**
> 启用基准测试构建。

**--file-watch**
> 文件变更时重新构建。

**--ghc-options** _OPTS_
> 额外的 GHC 选项。

**--jobs** _N_, **-j** _N_
> 并发任务数。

**--stack-yaml** _FILE_
> 覆盖项目的 stack.yaml 文件。

# DESCRIPTION

**stack** 是 Haskell 的构建工具和项目管理器。它通过 Stackage 快照固定 GHC 版本和软件包集合，从而提供可重现的构建。

Stackage 快照（LTS 或 Nightly）定义了经过筛选、可一起构建的软件包集合。这通过确保版本兼容来避免"依赖地狱"。stack.yaml 中的 resolver 指定使用哪个快照。

Stack 自动管理 GHC 的安装。不同项目可以使用不同的 GHC 版本而不会产生系统级冲突。正确的版本会在首次使用时下载并构建。

项目结构包括 stack.yaml（配置）、package.yaml（软件包定义）和源代码目录。模板为库、可执行文件或特定框架提供了起点。

REPL（ghci）会加载项目代码以便进行交互式开发。文件监视（--file-watch）会在变更时重新构建，实现快速迭代。

与 Cabal 软件包的集成通过 package.yaml 或 .cabal 文件完成。Stack 可以通过 extra-deps 使用不在 Stackage 中的 Hackage 软件包。

# CAVEATS

初次构建需要下载 GHC 和大量依赖。工作流与 cabal 不同——团队应统一标准。Stackage 对新发布的软件包可能滞后于 Hackage。磁盘空间占用可能相当可观。某些高级 Cabal 特性需要变通处理。

# HISTORY

**stack** 由 **FP Complete** 于 **2015 年**创建，旨在解决 Haskell 的依赖管理难题。它建立在 Stackage（稳定软件包集合）的工作之上。该工具凭借可重现性保证和简化的工作流得到了广泛采用。目前仍在社区参与下持续开发。

# INSTALL

```apt: sudo apt install haskell-stack```

```dnf: sudo dnf install stack```

```pacman: sudo pacman -S stack```

```apk: sudo apk add stack```

```brew: brew install haskell-stack```

```nix: nix profile install nixpkgs#stack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ghc](/man/ghc)(1), [ghci](/man/ghci)(1), [cabal](/man/cabal)(1), [runghc](/man/runghc)(1)
