# TAGLINE

列出已合并进当前分支的分支

# TLDR

**显示已合并的分支**

```git show-merged-branches```

# SYNOPSIS

**git** **show-merged-branches**

# DESCRIPTION

**git show-merged-branches** 列出已完全合并进 HEAD 的本地分支。它属于 git-extras，会运行 `git branch --merged` 并过滤掉当前分支和仓库的默认分支（如 `main`/`master`），只留下真正可以删除的候选分支。

# CAVEATS

属于 git-extras 软件包；仅检查本地分支。反向视图请见 `git-show-unmerged-branches`。

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

[git-branch](/man/git-branch)(1), [git-delete-merged-branches](/man/git-delete-merged-branches)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-show-merged-branches)```

<!-- verified: 2026-07-17 -->
