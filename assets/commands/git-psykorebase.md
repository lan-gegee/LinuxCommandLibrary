# TAGLINE

用单个合并提交将一个分支变基到另一个之上

# TLDR

**使用合并提交将当前分支变基到另一分支之上**

```git psykorebase [primary_branch]```

**将特定分支变基到另一分支**

```git psykorebase [primary_branch] [secondary_branch]```

**即使可以 fast-forward 也强制生成合并提交**

```git psykorebase [primary_branch] --no-ff```

**解决冲突后继续**

```git psykorebase --continue```

# SYNOPSIS

**git** **psykorebase** _primary-branch_ [_secondary-branch_] [_--no-ff_]

**git** **psykorebase** **--continue**

# PARAMETERS

_PRIMARY-BRANCH_
> 要变基到的分支。

_SECONDARY-BRANCH_
> 被变基的分支；默认为当前分支。

**--no-ff**
> 强制生成合并提交而不是 fast-forward。

**-c**, **--continue**
> 手动解决冲突后继续执行。

# DESCRIPTION

**git psykorebase** 通过检出主分支、从其创建分支，然后用一个生成的合并提交合入次级分支来完成变基，而不像 `git rebase` 那样逐个重放每个提交。这个 git-extras 命令避免了每个提交都要重新解决一次相同冲突的问题，代价是把整个变基折叠成一个合并点。

如果合并发生冲突，它会停留在临时 `<secondary>-rebased-on-top-of-<primary>` 分支上，并提示你解决冲突并提交，然后运行 `git psykorebase --continue` 完成分支重命名的收尾工作。

# CAVEATS

属于 git-extras。由于它用一次合并代替逐个重放提交，次级分支相对主分支的单个提交级别的历史不会像交互式 rebase 那样得到保留。

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

[git-rebase](/man/git-rebase)(1), [git-merge](/man/git-merge)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-psykorebase)```

<!-- verified: 2026-07-17 -->
