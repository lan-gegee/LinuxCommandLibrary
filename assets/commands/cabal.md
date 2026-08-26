# TAGLINE

Haskell 软件包管理器与构建系统

# TLDR

**构建**项目

```cabal build```

**运行**可执行文件

```cabal run```

**安装**软件包

```cabal install [package]```

**创建**新项目

```cabal init```

**测试**项目

```cabal test```

**更新**软件包列表

```cabal update```

# SYNOPSIS

**cabal** _command_ [_options_]

# DESCRIPTION

**cabal**（Common Architecture for Building Applications and Libraries）是 Haskell 的软件包管理器和构建系统。它负责依赖解析、构建、测试和分发 Haskell 软件包。Cabal 默认使用 Nix 风格的本地构建，将每个项目的依赖隔离开以避免冲突。

# PARAMETERS

**build**
> 构建项目

**run** [_target_]
> 构建并运行可执行文件

**install** _package_
> 安装软件包

**update**
> 更新软件包索引

**test**
> 运行测试套件

**repl**
> 启动已加载项目的 GHCi

**clean**
> 删除构建产物

**sdist**
> 创建源代码发行包

**init**
> 交互式创建新的 Cabal 软件包

**bench**
> 运行基准测试

**haddock**
> 构建 Haddock 文档

**upload**
> 将软件包上传到 Hackage

**freeze**
> 将依赖冻结到精确版本

**outdated**
> 检查过时的依赖

# PROJECT FILE

myproject.cabal 示例：
```
cabal-version: 2.4
name: myproject
version: 0.1.0.0

executable myproject
  main-is: Main.hs
  build-depends: base >=4.14 && <5
  hs-source-dirs: src
  default-language: Haskell2010
```

# WORKFLOW

```bash
# Create new project
cabal init

# Update package list
cabal update

# Build project
cabal build

# Run executable
cabal run myproject

# Install dependencies
cabal install --only-dependencies

# Run tests
cabal test

# Start REPL
cabal repl
```

# FEATURES

- 依赖解析
- 沙盒化构建
- 多个构建目标
- 测试框架集成
- 基准测试支持
- 文档生成
- 向 Hackage 发布软件包

# CAVEATS

依赖解析可能较慢。“Cabal hell”（依赖冲突）在历史上一直是问题（Nix 风格的构建已有所改善）。下载体积较大。编译耗时可能较长。需注意 GHC 版本兼容性。

# HISTORY

**Cabal** 从 **2003** 年前后开始为 Haskell 开发，Cabal 2.0（2017 年）带来重大改进，引入了 Nix 风格的本地构建。

# CONFIGURATION

**~/.cabal/config**
> 全局配置，包括软件仓库、安装目录和构建设置

# INSTALL

```apt: sudo apt install cabal-install```

```dnf: sudo dnf install cabal-install```

```pacman: sudo pacman -S cabal-install```

```apk: sudo apk add cabal```

```zypper: sudo zypper install cabal-install```

```brew: brew install cabal-install```

```nix: nix profile install nixpkgs#cabal-install```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stack](/man/stack)(1), [ghc](/man/ghc)(1), [ghci](/man/ghci)(1)
