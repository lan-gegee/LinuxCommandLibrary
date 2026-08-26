# TAGLINE

将分支压缩为单个提交

# TLDR

**将分支压缩进当前分支**（改动保留在暂存区但不提交）

```git squash [branch]```

**带提交信息压缩**（提交结果）

```git squash [branch] "[message]"```

**压缩当前分支上最近的 N 个提交**

```git squash HEAD~[5] "[message]"```

**用拼接的提交信息进行压缩**

```git squash --squash-msg [branch]```

# SYNOPSIS

**git** **squash** [**--squash-msg**] _source-branch|commit-ref_ [_message_]

# PARAMETERS

**--squash-msg**
> 提交压缩结果时使用所有被压缩提交拼接而成的信息。不能与提交信息参数同时使用。

# DESCRIPTION

**git squash** 将来自指定分支或提交范围的所有提交合并到当前分支，成为一个压缩后的提交。它属于 git-extras，适合在功能分支合入主分支前清理其历史。当给定的是当前分支上的某个提交引用时，会压缩从该引用到 HEAD 的范围。如果没有提供提交信息且未使用 **--squash-msg**，则改动只暂存不提交。

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

[git-merge](/man/git-merge)(1), [git-rebase](/man/git-rebase)(1), [git-extras](/man/git-extras)(1)
