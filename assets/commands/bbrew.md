# TAGLINE

用于搜索 Homebrew 和 Linuxbrew formula 与 cask 的命令行工具

# TLDR

**搜索** formula

```bbrew search [query]```

**隐藏描述**进行搜索

```bbrew search --no-desc [query]```

**只搜索 formula**（排除 cask）

```bbrew search --no-casks [query]```

**只搜索 cask**（排除 formula）

```bbrew search --no-formulae [query]```

**显示帮助**

```bbrew --help```

# SYNOPSIS

**bbrew** **search** [_options_] [_query_]

# PARAMETERS

**search** _query_
> 搜索与查询匹配的 formula 和 cask。

**-h**, **--help**
> 显示帮助信息。

**-d**, **--desc** / **--no-desc**
> 在结果中显示或隐藏 formula 描述（默认显示）。

**-c**, **--casks** / **--no-casks**
> 包含或排除 cask 结果（macOS 上默认包含）。

**-f**, **--formulae** / **--no-formulae**
> 包含或排除 formula 结果（默认包含）。

# DESCRIPTION

**bbrew** 是一个命令行工具，为搜索 Homebrew 和 Linuxbrew 软件仓库提供了更快的方式。它不调用本地 Homebrew 安装，而是直接查询 formulae.brew.sh API，同时获取 core formula 和 cask 的元数据。结果在客户端过滤，以大小写不敏感的方式匹配软件包名称、别名和描述。

bbrew 基于 Node.js 和 oclif CLI 框架构建，同时支持 macOS（Homebrew）和 Linux（Linuxbrew）。在 macOS 上，默认启用 cask 搜索。该工具通过 keyv 进行基于文件的缓存，避免冗余的 API 调用，从而加快重复查询的速度。

# CAVEATS

该工具不管理也不安装软件包，只是查询 Homebrew API 的纯搜索接口。需要安装 Node.js。项目目前处于 0.0.1 版本，文档很少。

# INSTALL

```brew: brew install bbrew```

```nix: nix profile install nixpkgs#bbrew```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[brew](/man/brew)(1), [npm](/man/npm)(1)
