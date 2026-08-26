# TAGLINE

列出尚未合并进当前分支的分支

# TLDR

**显示所有未合并的分支**

```git show-unmerged-branches```

**显示未合并的分支（等价的原生 git 命令）**

```git branch --no-merged```

# SYNOPSIS

**git** **show-unmerged-branches**

# DESCRIPTION

**git show-unmerged-branches** 列出所有尚未合并进当前 HEAD 的本地分支。它是 **git-extras** 工具集的一员，适合用于识别进行中的分支和未完成的功能开发。

内部实现是运行 `git branch --no-merged`，同时过滤掉当前分支和默认分支。

# CAVEATS

需要安装 **git-extras**。只检查本地分支，不包括远程跟踪分支。作者为 Paul Schreiber。

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

[git-branch](/man/git-branch)(1), [git-show-merged-branches](/man/git-show-merged-branches)(1), [git-extras](/man/git-extras)(1), [git-log](/man/git-log)(1)
