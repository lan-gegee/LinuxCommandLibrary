# TAGLINE

从整个历史中移除文件

# TLDR

**从整个历史中移除文件**

```git obliterate [filename]```

**移除多个文件**

```git obliterate [file1] [file2]```

**将改写限制在某个版本区间内**

```git obliterate [filename] -- [since]..[until]```

# SYNOPSIS

**git** **obliterate** _filename_... [_--_ _rev-list-args_]

# DESCRIPTION

**git obliterate** 彻底地从 Git 历史中移除一个或多个文件。这个 git-extras 命令会对 `--all` 引用（或 `--` 之后给出的版本区间）运行 `git filter-branch --index-filter 'git rm -r --cached <files> --ignore-unmatch' --prune-empty --tag-name-filter cat`，从每个被改写的提交中抹除这些文件，同时让标签继续指向（被改写后的）相应提交。

它适合用来移除误提交的机密、凭证或不该被跟踪的大文件。它在完成后不会对仓库重新打包；旧对象会保留到你执行垃圾回收为止。

# CAVEATS

该操作会改写历史并改变所有提交哈希。在共享分支上使用前请与协作者协调好。之后请运行 `git reflog expire --expire=now --all && git gc --prune=now --aggressive`，才能真正回收磁盘空间并丢弃旧的 blob。

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

[git-filter-branch](/man/git-filter-branch)(1), [git-gc](/man/git-gc)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate)```

<!-- verified: 2026-07-17 -->
