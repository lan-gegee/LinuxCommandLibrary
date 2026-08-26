# TAGLINE

Haskell 工具链的通用安装器

# TLDR

**安装指定版本的 GHC**

```ghcup install ghc [9.4.7]```

**安装最新版 GHC**

```ghcup install ghc```

**设置默认 GHC**

```ghcup set ghc [9.4.7]```

**安装 Cabal**

```ghcup install cabal```

**安装 HLS**

```ghcup install hls```

**列出可用及已安装的工具**

```ghcup list```

**移除某个 GHC 版本**

```ghcup rm ghc [9.4.7]```

**交互式 TUI**

```ghcup tui```

**升级 ghcup 本身**

```ghcup upgrade```

# SYNOPSIS

**ghcup** _command_ [_options_]

# SUBCOMMANDS

**install**
> 安装工具。

**set**
> 设置默认版本。

**list**
> 列出版本。

**rm**
> 移除版本。

**upgrade**
> 升级 ghcup。

**tui**
> 交互式界面。

**whereis**
> 显示工具位置。

**run**
> 使用指定的工具链版本运行命令。

**gc**
> 清理（回收）旧版本。

# PARAMETERS

**ghc**
> Glasgow Haskell Compiler。

**cabal**
> Cabal 构建工具。

**hls**
> Haskell Language Server。

**stack**
> Stack 构建工具。

# DESCRIPTION

**ghcup** 是 Haskell 工具链的通用安装器和版本管理器。它提供一种集中方式，用于安装、管理并在多个版本的 GHC、Cabal、Stack 和 HLS（Haskell Language Server）之间切换。

该工具负责为所有 Haskell 开发工具完成下载、安装以及 PATH 条目的配置。它支持安装特定版本、设置全局默认版本，并支持多版本并存。交互式 TUI 模式则提供了可视化的安装管理界面。

# CONFIGURATION

**~/.ghcup/config.yaml**
> ghcup 的配置文件，包含下载镜像和缓存偏好等设置。

**~/.ghcup/bin/**
> 所有受管理工具链二进制文件的安装目录。

# INSTALL

```brew: brew install ghcup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ghc](/man/ghc)(1), [cabal](/man/cabal)(1), [stack](/man/stack)(1)
