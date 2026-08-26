# TAGLINE

列出有可用更新的 Homebrew 软件包

# TLDR

**列出过时的软件包**

```brew outdated```

**仅列出过时的 formula**

```brew outdated --formula```

**仅列出过时的 cask**

```brew outdated --cask```

**显示详细的版本信息**

```brew outdated --verbose```

以 JSON 格式**输出**

```brew outdated --json```

**包含**会自动更新的 cask

```brew outdated --greedy```

**安静模式**（只显示名称）

```brew outdated --quiet```

# SYNOPSIS

**brew outdated** [_options_]

# DESCRIPTION

**brew outdated** 列出有更新版本可用的已安装 formula 和 cask。默认情况下，在交互式 shell 中会显示版本信息。

该命令使用本地缓存的软件包信息。请先运行 **brew update** 以确保结果准确。

# PARAMETERS

**--formula**
> 仅列出过时的 formula。

**--cask**
> 仅列出过时的 cask。

**--verbose, -v**
> 显示详细的版本信息。

**--quiet, -q**
> 仅列出名称（优先级高于 --verbose）。

**--json**
> 以 JSON 格式输出（v2 同时包含 formula 和 cask）。

**-g, --greedy**
> 同时包含版本为 :latest 或 auto_updates 为 true 的过时 cask。

**--greedy-latest**
> 同时包含版本为 :latest 的过时 cask。

**--greedy-auto-updates**
> 同时包含 auto_updates 为 true 的过时 cask。

**--fetch-HEAD**
> 拉取上游仓库，检测过时的 HEAD 安装。

# OUTPUT FORMAT

默认：package_name (installed_version) != available_version

安静模式：仅 package_name

JSON：完整元数据，包括版本和时间戳

# CAVEATS

不执行网络请求；依赖 brew update 的本地缓存。除非指定 --greedy，否则会排除带 auto_updates 的 cask。部分 cask 使用无法比较的 :latest 版本。

# SEE ALSO

[brew](/man/brew)(1), [brew-update](/man/brew-update)(1), [brew-upgrade](/man/brew-upgrade)(1), [brew-list](/man/brew-list)(1)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-19 -->
