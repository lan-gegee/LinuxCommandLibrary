# TAGLINE

显示 Homebrew 软件包的详细信息

# TLDR

**显示**某个 formula 的**信息**

```brew info [formula]```

**显示**某个 cask 的**信息**

```brew info --cask [cask]```

以 JSON 格式**输出** formula 信息

```brew info --json=v2 [formula]```

显示所有已安装 formula 的信息

```brew info --installed```

显示详细的使用统计数据

```brew info --analytics [formula]```

显示已安装 formula 的大小

```brew info --sizes [formula]```

在 GitHub 上打开 formula 源码页面

```brew info --github [formula]```

# SYNOPSIS

**brew info** [_options_] [_formula|cask_]

# DESCRIPTION

**brew info** 显示某个 formula 或 cask 的信息，包括名称、版本、描述、主页、依赖、安装状态和可用选项。

对于已禁用（disabled）和已弃用（deprecated）的 formula，它还会给出状态说明。

# PARAMETERS

**--json** _version_
> 输出 JSON 表示。默认版本为 v1（仅 formula），使用 v2 可同时包含 formula 和 cask。

**--installed**
> 以人类可读的方式列出已安装的 formula 和 cask。

**--formula**
> 将所有参数视为 formula。

**--cask**
> 将所有参数视为 cask。

**--analytics**
> 显示全局使用统计而非 formula 或 cask 信息。

**--days** _count_
> 显示指定周期的统计数据，可选 30、90 或 365 天。

**--github**
> 在浏览器中打开该 formula 或 cask 的 GitHub 源码页面。

**--sizes**
> 显示已安装 formula 和 cask 占用的空间大小。

**--variations**
> 在每个 formula 的 JSON 输出中包含 variations 哈希。

# CAVEATS

JSON 输出格式可能随 Homebrew 版本而变化。使用统计数据需要访问 GitHub 网络。某些信息并非对所有 formula 可用。

# SEE ALSO

[brew](/man/brew)(1), [brew-search](/man/brew-search)(1), [brew-list](/man/brew-list)(1), [brew-install](/man/brew-install)(1)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-19 -->
