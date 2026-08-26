# TAGLINE

统计仓库中的提交数

# TLDR

**统计提交总数**

```git count```

**按作者统计提交**

```git count --all```

# SYNOPSIS

**git count** [_options_]

# PARAMETERS

**--all**
> 按作者分别统计提交。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git count** 显示仓库中的提交总数。加上 --all 标志时，会按作者细分显示提交数。

该命令可快速概览仓库活跃度和贡献者参与情况，比手动解析 **git shortlog** 输出更简单。

使用 **--all** 标志时会生成按提交数排名的贡献者列表，非常适合项目统计和活跃度报告。

# CAVEATS

属于 git-extras 软件包。只统计当前分支上的提交。包含合并提交。

# HISTORY

git count 是 **git-extras** 的一部分，提供简单的提交计数功能，与 git shortlog 相辅相成。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-count-objects](/man/git-count-objects)(1), [git-shortlog](/man/git-shortlog)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

<!-- verified: 2026-07-17 -->
