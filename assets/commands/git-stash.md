# TAGLINE

临时保存未提交的改动以备后用

# TLDR

**贮藏改动**

```git stash```

**带信息贮藏**

```git stash push -m "[message]"```

**列出贮藏**

```git stash list```

**应用最新的贮藏**

```git stash apply```

**弹出最新的贮藏**

```git stash pop```

**应用指定的贮藏**

```git stash apply stash@{[n]}```

**查看贮藏内容**

```git stash show -p```

**删除一个贮藏**

```git stash drop stash@{[n]}```

**清空所有贮藏**

```git stash clear```

# SYNOPSIS

**git** **stash** _command_ [_options_]

# SUBCOMMANDS

**push**
> 贮藏改动。

**list**
> 列出贮藏。

**show**
> 查看贮藏内容。

**apply**
> 应用但不移除。

**pop**
> 应用并移除。

**drop**
> 删除某个贮藏。

**clear**
> 删除所有贮藏。

**branch**
> 从贮藏创建分支。

# PARAMETERS

**-m**, **--message** _msg_
> 贮藏说明信息。

**-u**, **--include-untracked**
> 包含未跟踪的文件。

**-a**, **--all**
> 包含被忽略的文件。

**-p**, **--patch**
> 交互式贮藏。

# DESCRIPTION

**git stash** 将未提交的改动暂时搁置，让你可以先去做别的事情。它会同时保存已暂存和未暂存的修改，然后把工作目录还原到与 HEAD 一致的状态。

用 `pop` 可以恢复并移除贮藏，或用 `apply` 在恢复的同时保留它。贮藏以栈的形式存放，最近一次位于 `stash@{0}`。

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

[git-checkout](/man/git-checkout)(1), [git-reset](/man/git-reset)(1), [git-restore](/man/git-restore)(1), [git-commit](/man/git-commit)(1), [git-switch](/man/git-switch)(1)
