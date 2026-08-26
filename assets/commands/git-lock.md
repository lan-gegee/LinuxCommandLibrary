# TAGLINE

将已跟踪的文件排除在后续本地修改之外

# TLDR

**锁定文件，让 Git 忽略对它的本地编辑**

```git lock [config/database.yml]```

# SYNOPSIS

**git lock** _filename_

# PARAMETERS

_FILENAME_
> 要锁定的已跟踪文件。

# DESCRIPTION

**git lock** 是一个 git-extras 命令，通过 `git update-index --skip-worktree` 为单个已跟踪文件设置 Git 的 skip-worktree 位。文件被锁定后，Git 不再在 `git status`/`git diff` 中报告对该文件的本地修改，因此你做的编辑不会被意外暂存或提交。

它适用于需要机器特定本地修改的文件，例如 `config/database.yml`，而不是用来协调团队成员之间的编辑：它对远程仓库或其他克隆没有影响，也无法阻止其他人向同一文件提交更改。使用 `git locked` 列出当前锁定的文件，使用 `git unlock` 恢复正常跟踪。

# CAVEATS

该命令属于 git-extras（是 `git update-index --skip-worktree` 的薄封装），并非 Git 核心命令。这是一种本地的、仅限单个克隆的设置，不是共享或强制性的锁。若需要真正的跨团队文件锁定，请参阅 `git lfs lock`。

# HISTORY

git lock 是 **git-extras** 的一部分，后者是一套社区维护的 Git 实用脚本合集。它早于 Git LFS 的服务器端强制文件锁定功能，且与后者无关。

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

[git-locked](/man/git-locked)(1), [git-unlock](/man/git-unlock)(1), [git-lfs](/man/git-lfs)(1), [git-update-index](/man/git-update-index)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md)```

<!-- verified: 2026-07-17 -->
