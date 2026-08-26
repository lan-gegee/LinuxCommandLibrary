# TAGLINE

合并分支并立即删除它

# TLDR

**将某个分支 graft（嫁接）**到当前分支

```git graft [feature-branch]```

**将某个分支 graft** 到指定的**目标**分支

```git graft [feature-branch] [dest-branch]```

# SYNOPSIS

**git graft** _src-branch_ [_dest-branch_]

# PARAMETERS

_src-branch_
> 要合并然后删除的分支

_dest-branch_
> 合并的目标分支（默认为当前分支）

# DESCRIPTION

**git graft** 合并一个分支后立即删除它，把 git merge 加 git branch -d 组合为单一操作。它适用于将已完成的功能分支并入主历史的同时清理分支杂项。

它是 **git-extras** 套件的组成部分，为那些应当成为历史一部分、无需保留分支引用的分支简化了常见的"合并并删除"工作流。

# CAVEATS

需要安装 **git-extras** 软件包。源分支会在合并后被删除。只应用于已完成且不再需要保留分支引用的工作。合并必须是干净的快进或普通合并提交；出现冲突会导致失败。

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

[git-merge](/man/git-merge)(1), [git-branch](/man/git-branch)(1), [git-extras](/man/git-extras)(1)
