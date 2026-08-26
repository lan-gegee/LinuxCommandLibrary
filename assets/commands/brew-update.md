# TAGLINE

拉取最新的 Homebrew 与软件包定义

# TLDR

**更新 Homebrew 和软件包定义**

```brew update```

带详细输出进行更新

```brew update --verbose```

仅在需要时更新（用于脚本）

```brew update --auto-update```

从最新提交**强制**更新

```brew update --force```

将 Homebrew 和各 tap 重置为上游状态

```brew update-reset```

# SYNOPSIS

**brew update** [_options_]

# DESCRIPTION

**brew update** 使用 git 从 GitHub 拉取最新版本的 Homebrew 和全部 formula，并执行必要的迁移。

该命令不会升级已安装的软件包——请使用 **brew upgrade**。

别名：**brew up**。

# PARAMETERS

**--verbose, -v**
> 显示详细的更新信息。

**--debug, -d**
> 显示调试信息。

**--force**
> 总是执行较慢的完整更新。

**--auto-update**
> 仅在需要时运行（否则快速空操作）。

**--merge**
> 使用 git merge 而不是 git rebase。

# AUTO-UPDATE

默认情况下，Homebrew 会在 **brew install** 之前自动更新。可通过以下变量配置：

**HOMEBREW_AUTO_UPDATE_SECS**
> 自动更新的间隔秒数。

**HOMEBREW_NO_AUTO_UPDATE=1**
> 完全禁用自动更新。

# WORKFLOW

```
brew update      # Fetch latest definitions
brew outdated    # See what can be upgraded
brew upgrade     # Install newer versions
brew cleanup     # Remove old versions
```

# CAVEATS

只更新定义，不更新已安装的软件。对于已安装的软件包，更新后需运行 **brew upgrade**。自动更新可能拖慢安装命令；如有需要可用环境变量禁用。

# SEE ALSO

[brew](/man/brew)(1), [brew-upgrade](/man/brew-upgrade)(1), [brew-outdated](/man/brew-outdated)(1)
