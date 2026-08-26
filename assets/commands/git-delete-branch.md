# TAGLINE

同时删除本地和远程分支

# TLDR

**删除本地和远程分支**

```git delete-branch [branch]```

# SYNOPSIS

**git** **delete-branch** _branch_

# PARAMETERS

_branch_
> 要在本地和远程删除的分支名。

# DESCRIPTION

**git delete-branch** 用一条命令同时删除本地和远程的分支。它属于 **git-extras** 合集，将通常需要分开执行的 **git branch -D** 和 **git push origin --delete** 两步操作合并，简化了分支清理工作。

该命令在拉取请求工作流中特别有用——功能分支合并后即告过时。可以传入多个分支，它们会被依次删除。

# CAVEATS

需要安装 **git-extras**。远程删除需要对远程的推送权限。本地删除使用 **-D**（强制），未合并的工作可能丢失。

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

[git-branch](/man/git-branch)(1), [git-extras](/man/git-extras)(1), [git-push](/man/git-push)(1)
