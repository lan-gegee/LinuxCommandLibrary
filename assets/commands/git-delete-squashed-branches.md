# TAGLINE

删除已通过 squash 合并的分支

# TLDR

**删除已 squash 合并的分支**

```git delete-squashed-branches```

# SYNOPSIS

**git** **delete-squashed-branches**

# DESCRIPTION

**git delete-squashed-branches** 删除那些已被 squash 合并进当前分支的本地分支。它是 **git-extras** 的组成部分，能够检测出提交被合并为单个 squash 提交的分支，而 Git 标准的 **--merged** 选项无法识别这类分支。

Squash 合并会创建一个包含分支上全部改动的新提交，这使得原分支上的提交在技术上仍处于未合并状态。由于 **git branch --merged** 不会将这些分支标记为可删除，分支会不断累积。该命令使用树比较启发式算法来检测某个分支的改动是否已存在于目标分支中，即使两者的提交历史不同。

对于以 squash 合并为默认合并策略的 GitHub 和 GitLab 工作流尤其有用。

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

[git-delete-merged-branches](/man/git-delete-merged-branches)(1), [git-extras](/man/git-extras)(1)
