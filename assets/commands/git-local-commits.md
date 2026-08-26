# TAGLINE

列出尚未推送的本地提交

# TLDR

**显示未推送的本地提交**

```git local-commits```

**以图形方式显示本地提交**

```git local-commits --graph```

# SYNOPSIS

**git** **local-commits** [_git-log-options_]

# PARAMETERS

_GIT-LOG-OPTIONS_
> **git log** 接受的任意选项；原样传递。

# DESCRIPTION

**git local-commits** 是一条 git-extras 命令，用于列出当前分支上尚未推送到其上游跟踪分支的提交。它运行 `git log @{upstream}..@`，因此要求 HEAD 正在跟踪一个远程分支。任何额外的参数都会直接转发给 `git log`，因此 `--graph` 或 `--stat` 等选项可以按预期工作。

这提供了一种在实际推送之前快速查看将要推送哪些改动的方式。

# CAVEATS

要求当前分支已设置上游；否则 Git 会报错说没有配置上游。

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

[git-log](/man/git-log)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md)```

<!-- verified: 2026-07-17 -->
