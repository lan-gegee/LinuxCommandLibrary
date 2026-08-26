# TAGLINE

清理过期下载和旧的软件包版本

# TLDR

**移除过期的下载和旧版本**

```brew cleanup```

**预览**将被移除的内容

```brew cleanup --dry-run```

**清理**指定的 formula

```brew cleanup [formula]```

**移除超过指定天数的缓存文件**

```brew cleanup --prune=[30]```

**移除所有缓存的下载文件**

```brew cleanup --prune=all```

**深度清理缓存**（含最新版本的下载）

```brew cleanup -s```

**删除整个缓存目录**

```rm -rf "$(brew --cache)"```

# SYNOPSIS

**brew cleanup** [_options_] [_formula|cask_]

# DESCRIPTION

**brew cleanup** 移除失效的锁文件、formula 和 cask 的过期下载，以及已安装 formula 的旧版本。它会清理 Cellar 和下载缓存，释放磁盘空间。

默认情况下，超过 120 天的下载文件会被移除。该阈值可通过 HOMEBREW_CLEANUP_MAX_AGE_DAYS 更改。

除非设置了 HOMEBREW_NO_INSTALL_CLEANUP，否则 Homebrew 会在升级后以及每 30 天自动执行一次清理。

# PARAMETERS

**--dry-run, -n**
> 显示将被移除的内容，但不实际移除。

**--prune** _days_
> 移除超过指定天数的所有缓存文件。使用 --prune=all 移除全部内容。

**-s, --scrub**
> 深度清理缓存，包括最新版本的下载文件。

**--prune-prefix**
> 只修剪 prefix 中的符号链接和目录，不移除其他文件。

**--formula**
> 将所有参数视为 formula。

**--cask**
> 将所有参数视为 cask。

# CACHE LOCATION

默认缓存位置：**~/Library/Caches/Homebrew**（macOS）。

查看缓存路径：**brew --cache**。

# RELATED COMMANDS

**brew autoremove**
> 移除不再使用的依赖。

**brew upgrade**
> 升级后应执行 cleanup。

# CAVEATS

旧版本会在 **brew upgrade** 过程中自动移除。-s 标志连当前版本的下载文件也会清除，之后可能需要重新下载。不带参数运行时会清理所有已安装软件包。

# SEE ALSO

[brew](/man/brew)(1), [brew-upgrade](/man/brew-upgrade)(1), [brew-autoremove](/man/brew-autoremove)(1)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-19 -->
