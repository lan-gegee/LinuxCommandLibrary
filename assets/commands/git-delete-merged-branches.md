# TAGLINE

移除所有已合并入当前分支的分支

# TLDR

移除已经**合并入当前分支**的本地分支

```git delete-merged-branches```

# SYNOPSIS

**git** **delete-merged-branches**

# DESCRIPTION

**git delete-merged-branches** 删除所有已合并入当前分支的分支，自动完成合并后的清理。作为 git-extras 工具集的一部分，它会识别哪些分支的更改已完全并入当前分支，并批量移除。

该命令利用 Git 的 merge-base 计算来判断哪些分支可以安全删除，确保只移除没有独有提交的分支。它常在发布周期结束后或仓库例行维护时运行，以防止分支泛滥。

# INSTALL

```brew: brew install git-delete-merged-branches```

```nix: nix profile install nixpkgs#git-delete-merged-branches```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-branch](/man/git-branch)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

<!-- verified: 2026-07-17 -->
