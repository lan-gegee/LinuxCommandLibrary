# TAGLINE

显示分支及其提交的关系指示

# TLDR

**显示分支关系**

```git show-branch```

**显示指定分支**

```git show-branch [branch1] [branch2]```

**显示所有分支**

```git show-branch --all```

**显示更多上下文**

```git show-branch --more=[10]```

**带颜色显示**

```git show-branch --color```

# SYNOPSIS

**git** **show-branch** [_options_] [_refs_...]

# PARAMETERS

**-a**, **--all**
> 显示所有引用。

**-r**, **--remotes**
> 显示远程分支。

**--more** _n_
> 显示更多提交。

**--list**
> 列表模式。

**--topo-order**
> 拓扑顺序。

**--date-order**
> 日期顺序。

**--color**
> 彩色输出。

# DESCRIPTION

**git show-branch** 显示各分支及其提交，并用直观的标记指示哪些提交属于哪些分支。它以紧凑的方式呈现分支的分叉情况和共享历史。

当你想了解分支之间的相互关系时它很有用，尤其是多个分支共享共同祖先的时候。

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

[git-branch](/man/git-branch)(1), [git-log](/man/git-log)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-show-branch)```

<!-- verified: 2026-07-17 -->
