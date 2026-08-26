# TAGLINE

查找尚未合并入上游的提交

# TLDR

**显示未拣选的提交**

```git cherry [upstream] [branch]```

**显示提交信息**

```git cherry -v [upstream]```

**比较分支**

```git cherry [main] [feature]```

# SYNOPSIS

**git cherry** [_options_] [_upstream_] [_head_]

# PARAMETERS

_UPSTREAM_
> 要与之比较的分支。

_HEAD_
> 要检查的分支（默认：当前分支）。

_LIMIT_
> 只报告可从 LIMIT 到达的提交，进一步限定输出范围。

**-v**
> 显示提交主题。

**--abbrev** _N_
> 缩短提交哈希。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git cherry** 查找尚未应用到上游的提交。它比较两个分支间的提交，基于补丁内容而非提交哈希来识别你的分支中哪些提交在上游缺失。

输出中用 **+** 表示上游没有的提交，用 **-** 表示上游已存在的等价提交。这有助于确定哪些更改还需要合并或拣选。

该命令特别适合在合并前审查分支状态，确保所有预期的更改都已集成，并识别可能在变基过程中丢失的提交。

# CAVEATS

比较的是补丁内容而非提交 ID。被变基过的提交会显示为缺失。对线性历史效果最佳。

# HISTORY

git cherry 是 **Git** 的核心命令之一，用于按补丁等价性比较分支，其名称源自它所辅助规划的 cherry-pick 操作。

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

[git-cherry-pick](/man/git-cherry-pick)(1), [git-log](/man/git-log)(1), [git-rebase](/man/git-rebase)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-cherry)```

<!-- verified: 2026-07-17 -->
