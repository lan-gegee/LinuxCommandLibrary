# TAGLINE

选择 SteamOS 更新发布通道

# TLDR

查看**当前**分支

```steamos-select-branch -c```

**列出**可用分支

```steamos-select-branch -l```

切换到 **beta** 分支

```steamos-select-branch beta```

切换到 **stable** 版本

```steamos-select-branch stable```

切换到**最新开发版**

```steamos-select-branch main```

# SYNOPSIS

**steamos-select-branch** [_OPTIONS_] [_BRANCH_]

# PARAMETERS

**-c**
> 查看当前分支

**-l**
> 列出所有可用分支

# BRANCHES

**stable**
> 稳定版通道（默认，推荐）

**beta**
> 带有较新功能的 Beta 测试通道

**main**
> 最新开发版通道

# DESCRIPTION

**steamos-select-branch** 选择 SteamOS 的系统发布分支，控制系统使用的更新通道。stable 分支接收经过充分测试的更新，beta 提供预览版本，main 则提供最新的开发构建。

切换分支后，请运行 `steamos-update` 更新到所选分支的最新版本。

# CAVEATS

beta 和 main 分支可能包含 bug 且不够稳定。切换到较旧的分支可能需要恢复出厂设置。非稳定分支的更新可能更频繁。

# HISTORY

**steamos-select-branch** 是 **Valve** 开发的 **SteamOS** 工具的一部分。分支系统让用户可以在稳定版发布前选择体验较新的功能。

# SEE ALSO

[steamos-update](/man/steamos-update)(1)
