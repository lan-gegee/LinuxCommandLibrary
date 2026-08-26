# TAGLINE

显示作者的贡献摘要

# TLDR

**显示作者贡献**

```git contrib [author-name]```

**按邮箱查看贡献**

```git contrib "[email@example.com]"```

# SYNOPSIS

**git contrib** _author_

# PARAMETERS

_AUTHOR_
> 要搜索的作者姓名或邮箱。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git contrib** 显示特定作者的提交摘要。它展示提交数量和提交详情，让你快速了解某人对仓库的贡献情况。

该命令使用子串匹配按作者姓名或邮箱模式搜索提交。它适用于审查贡献者的工作、生成贡献报告，或者核实提交署名。

它比 **git log --author** 的视图更聚焦，专为快速评估个人对项目的贡献而设计。

# CAVEATS

属于 git-extras 软件包。作者匹配基于子串。只显示当前分支可达的提交。

# HISTORY

git contrib 是 **git-extras** 的一部分，由 **TJ Holowaychuk** 创建，用于快速生成贡献者摘要。

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

[git-authors](/man/git-authors)(1), [git-shortlog](/man/git-shortlog)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

<!-- verified: 2026-07-17 -->
