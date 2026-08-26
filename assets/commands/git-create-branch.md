# TAGLINE

创建新分支并可选择切换过去

# TLDR

**创建并切换到分支**

```git create-branch [branch_name]```

**从指定起点创建并切换到分支**

```git create-branch [name] [start_point]```

**创建并推送到远程**

```git create-branch -r [name]```

# SYNOPSIS

**git** **create-branch** [_options_] _name_ [_commit_]

# PARAMETERS

**-r**, **--remote**
> 同时建立远程跟踪分支。会在本地创建分支、推送到 origin 并设置跟踪。

# DESCRIPTION

**git create-branch** 是 git-extras 提供的便捷命令，用于简化创建分支的工作流。它会创建新分支并切换过去。加上 **-r** 标志时，还会把分支推送到 origin 并设置远程跟踪，将多个手动步骤合并为一条命令。

不带 -r 标志时，该命令创建本地分支并切换过去，等价于 **git checkout -b**。可以可选地指定起始点（提交哈希或分支名）；否则分支从 HEAD 开始。

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

[git-branch](/man/git-branch)(1), [git-checkout](/man/git-checkout)(1), [git-switch](/man/git-switch)(1), [git-delete-branch](/man/git-delete-branch)(1), [git-extras](/man/git-extras)(1)
