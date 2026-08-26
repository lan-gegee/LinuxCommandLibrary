# TAGLINE

以详细格式列出分支并附带时间信息

# TLDR

**详细列出分支**

```git brv```

# SYNOPSIS

**git** **brv**

# PARAMETERS

不接受任何选项；运行 **git brv** 总是会列出所有本地分支，最近有提交的分支排在最前。

# DESCRIPTION

**git brv** 是一个 git-extras 命令，提供带有丰富上下文信息的增强版分支列表。它以格式良好的表格显示分支及其最近提交日期、缩写的提交哈希、相对时间（如 "2 days ago"）和提交信息。

其输出比标准的 git branch -v 更具信息量，通过颜色标记和更合理的间距让分支信息一目了然。这有助于开发者快速识别过时分支、近期活动以及并行开发工作的当前状态。

在分支较多的仓库中，该命令尤为有用——快速掌握各分支状态对维护和工作流管理很有价值。

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

[git-branch](/man/git-branch)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-brv)```

<!-- verified: 2026-07-17 -->
