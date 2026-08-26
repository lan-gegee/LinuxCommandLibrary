# TAGLINE

恢复工作树文件或取消暂存改动

# TLDR

**恢复工作树文件**

```git restore [file]```

**从指定提交恢复**

```git restore --source=[commit] [file]```

**取消暂存文件**

```git restore --staged [file]```

**恢复所有文件**

```git restore .```

**同时恢复暂存区和工作树**

```git restore --staged --worktree [file]```

**交互式恢复**

```git restore -p [file]```

**恢复合并冲突中己方一侧的版本**

```git restore --ours [file]```

**恢复合并冲突中对方一侧的版本**

```git restore --theirs [file]```

# SYNOPSIS

**git** **restore** [_options_] [_files_...]

# PARAMETERS

**--source** _tree_
> 从指定 tree 恢复。

**-s** _tree_
> --source 的缩写。

**--staged**
> 恢复索引（取消暂存）。

**--worktree**
> 恢复工作树。

**-S**
> --staged 的缩写。

**-W**
> --worktree 的缩写。

**-p**, **--patch**
> 交互模式。

**--ours** / **--theirs**
> 在合并冲突期间，恢复当前分支或被合入分支的版本。

**-m**, **--merge**
> 在文件中重建冲突的合并状态。

# DESCRIPTION

**git restore** 用于恢复工作树文件，或将改动从索引中取消暂存。它于 Git 2.23 引入，为 `git checkout` 中与文件恢复相关的功能提供了更清晰的替代方案。

用 `--staged` 取消暂存文件，用 `--worktree`（默认）丢弃工作树中的改动，或者两者一起使用，将文件完全恢复到之前的状态。

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

[git-checkout](/man/git-checkout)(1), [git-reset](/man/git-reset)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-restore)```

<!-- verified: 2026-07-17 -->
