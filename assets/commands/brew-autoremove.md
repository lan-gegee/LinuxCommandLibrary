# TAGLINE

移除 Homebrew 的孤立依赖

# TLDR

**移除**不再使用的依赖

```brew autoremove```

**预览**将被移除的内容

```brew autoremove --dry-run```

# SYNOPSIS

**brew autoremove** [_options_]

# DESCRIPTION

**brew autoremove** 会卸载那些仅作为依赖安装、且不再被任何已安装 formula 需要的 formula。它可以清理卸载软件包后遗留的孤立依赖。

# PARAMETERS

**--dry-run, -n**
> 仅列出将被移除的内容，而不实际移除。

# HOW IT WORKS

当你安装 **git** 这类软件包时，其依赖（gettext、pcre2）会被自动安装。卸载 **git** 后，这些依赖仍然保留。运行 **brew autoremove** 即可清除这些孤立的依赖。

# EXAMPLE WORKFLOW

```
brew uninstall git          # Remove package
brew autoremove             # Clean up dependencies
brew cleanup                # Remove cached downloads
```

# PREVENTING REMOVAL

要防止某个 formula 被 autoremove 移除，可将其显式重装一次，使其状态变为"按需安装"：

```brew install formula```

这会把该 formula 的状态从依赖改为显式安装。

# RELATED COMMANDS

**brew leaves**
> 显示顶层软件包（非依赖）。

**brew deps --installed**
> 显示依赖树。

**brew cleanup**
> 清理缓存的下载和旧版本。

# CAVEATS

只移除作为依赖安装的 formula，不移除显式安装的 formula。可在卸载软件包后定期安全运行。不会移除 cask。

# SEE ALSO

[brew](/man/brew)(1), [brew-uninstall](/man/brew-uninstall)(1), [brew-cleanup](/man/brew-cleanup)(1), [brew-leaves](/man/brew-leaves)(1)
