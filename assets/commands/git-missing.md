# TAGLINE

显示分支之间缺失的提交

# TLDR

**显示当前分支有而另一分支缺失的提交，以及反向情况**

```git missing [branch]```

**比较两个特定分支**

```git missing [branch1] [branch2]```

# SYNOPSIS

**git** **missing** [_branch1_] [_branch2_]

# DESCRIPTION

**git missing** 显示存在于一个分支但不存在于另一分支的提交。这个 git-extras 命令执行对称比较，揭示每个分支各自独有的更改。

若只指定一个分支，则会与当前分支比较。若未指定任何分支，则将当前分支与默认分支（通常是 master 或 main）比较。

该命令在合并之前特别有用，因为它清楚地显示双方各会引入哪些提交。它本质上执行的是 `git log --left-right --oneline branch1...branch2`，提供分支分叉的双向视图。

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

[git-log](/man/git-log)(1), [git-extras](/man/git-extras)(1), [git-cherry](/man/git-cherry)(1), [git-branch](/man/git-branch)(1)
