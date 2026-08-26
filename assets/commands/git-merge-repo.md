# TAGLINE

将仓库合并到子目录

# TLDR

**合并另一个仓库**

```git merge-repo [repo-url] [branch] [directory]```

**将仓库合并到子目录**

```git merge-repo [https://github.com/owner/repo.git] main [lib/]```

# SYNOPSIS

**git merge-repo** _url_ _branch_ _directory_

# PARAMETERS

_URL_
> 要合并的仓库 URL。

_BRANCH_
> 从哪个分支合并。

_DIRECTORY_
> 目标子目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git merge-repo** 将另一个仓库合并到子目录中，同时保留其完整提交历史。它是 `git subtree add -P <directory> <repo> <branch>` 的薄封装，因此引入的历史是被嫁接进来的，而不是被压缩掉。

传入 `.` 作为目录是一种特殊情况：仓库先被加入一个临时子目录，然后其中的文件会被上移到仓库根目录（扁平化），而不是保持嵌套。

该命令适用于整合外部库、把多个仓库合并成 monorepo，或吸收此前独立维护的项目。

# CAVEATS

属于 git-extras 软件包。要求 `git subtree` 可用。路径冲突时可能需要手动解决冲突。

# HISTORY

git merge-repo 是 **git-extras** 的一部分，为创建 monorepo 和整合外部库提供仓库合并功能。

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

[git-merge](/man/git-merge)(1), [git-subtree](/man/git-subtree)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-merge-repo)```

<!-- verified: 2026-07-17 -->
